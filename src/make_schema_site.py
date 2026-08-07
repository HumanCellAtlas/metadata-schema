"""
Walk every commit reachable from ``staging``, oldest to newest, and for
each commit that modifies json_schema/versions.json materialise every
(schema, version) pair it declares. Copies land in ``json_schema_site/``
at the repo root, mirroring the subdirectory layout of ``json_schema/``
but with the version inserted as an extra directory level immediately
above the schema, and with the ``.json`` extension dropped.

Example: ``type/file/analysis_file`` at ``6.2.0`` produces
``json_schema_site/type/file/6.2.0/analysis_file``.

The same version was sometimes served with more than one content, because
schemas were edited without a version bump. Visiting oldest-first means
the content as of the version's first appearance wins, which is the state
that was released; later edits under an unchanged version are typically
unreleased work in progress.

Note that pairs are keyed on what versions.json declares, not on version
*transitions*. Copying only on a transition misses two real cases: a
version released from a feature branch and superseded before that branch
merged, and a schema file that was absent at the transition commit and
only appeared later while the version stood still.

The script writes files under the current working tree; it does not stage
or commit them.
"""

import argparse
import json
import re
import stat
import subprocess
import sys
import textwrap
import urllib.request
from pathlib import Path

SEMVER_RE = re.compile(r'^\d+(?:\.\d+)*$')

VERSIONS_FILE = 'json_schema/versions.json'
SCHEMA_ROOT = 'json_schema'
OUTPUT_DIR = 'json_schema_site'
BASE_URL = 'https://schema.humancellatlas.org'
UPLOAD_SCRIPT = 'upload.sh'
CSS_FILE = 'pico.classless.css'
CSS_URL = 'https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.classless.css'
FAVICON_FILE = 'favicon.ico'
FAVICON_URL = 'https://humancellatlas.org/wp-content/uploads/2025/02/cropped-HCA-globe-32x32.png'


def git(*args, check=True):
    result = subprocess.run(
        ['git', *args],
        capture_output=True,
        check=False,
    )
    if check and result.returncode != 0:
        raise RuntimeError(
            f"git {' '.join(args)} failed: {result.stderr.decode(errors='replace')}"
        )
    return result


def repo_root():
    return Path(git('rev-parse', '--show-toplevel').stdout.decode().strip())


BRANCH = 'staging'


def commits_touching_versions():
    """
    Commit SHAs reachable from ``staging`` that modified versions.json, oldest first.

    ``--full-history`` is essential: the default history simplification that
    ``git log <path>`` applies prunes side branches whose changes match one
    parent of a merge, which silently drops versions that were released from
    a branch. ``--follow`` is deliberately absent -- versions.json was never
    renamed, and --follow re-enables that simplification.
    """
    out = git(
        'log',
        BRANCH,
        '--full-history',
        '--reverse',
        '--format=%H',
        '--',
        VERSIONS_FILE,
    ).stdout.decode()
    return out.split()


def blob_at(commit, path):
    """
    Return the file contents at a commit, or None if missing.
    """
    result = git('show', f'{commit}:{path}', check=False)
    if result.returncode != 0:
        return None
    return result.stdout


def leaf_versions(versions_bytes):
    """
    Flatten versions.json into {(path, tuple): version_string}.
    """
    if versions_bytes is None:
        return {}
    try:
        data = json.loads(versions_bytes)
    except json.JSONDecodeError:
        return {}
    root = data.get('version_numbers', {})
    result = {}

    def walk(node, prefix):
        for key, value in node.items():
            if isinstance(value, dict):
                walk(value, prefix + (key,))
            else:
                result[prefix + (key,)] = value

    walk(root, ())
    return result


def schema_path(path_tuple):
    """
    Map a versions.json leaf path to the schema file path in the tree.
    """
    return Path(SCHEMA_ROOT, *path_tuple).with_suffix('.json')


def rewrite_ref(ref, versions, src_for_log):
    """
    Rewrite a ``$ref`` string so it targets the versioned copy.

    Turns e.g. ``module/ontology/cell_type_ontology.json`` into
    ``module/ontology/5.3.6/cell_type_ontology``, using the version
    recorded in ``versions`` (the flattened versions.json for this
    commit). Preserves any ``#fragment`` suffix. If the ref doesn't
    resolve to a known versioned schema, it's returned unchanged.
    """
    path_part, sep, fragment = ref.partition('#')
    if not path_part.endswith('.json'):
        return ref
    parts = tuple(path_part[: -len('.json')].split('/'))
    version = versions.get(parts)
    if version is None:
        print(f'  ORPHAN {src_for_log}: unresolved $ref {ref!r}')
        return ref
    new_path = '/'.join(parts[:-1] + (version, parts[-1]))
    return f'{BASE_URL}/{new_path}' + (sep + fragment if sep else '')


def inject_id(schema, id_url):
    """
    Return a new dict with ``$id`` set to ``id_url``, positioned right
    after ``$schema`` (or at the top if ``$schema`` is absent) to match
    the layout the destroyed site served.
    """
    if not isinstance(schema, dict):
        return schema
    result = {}
    if '$schema' in schema:
        result['$schema'] = schema['$schema']
    result['$id'] = id_url
    for k, v in schema.items():
        if k not in result:
            result[k] = v
    return result


def rewrite_refs(node, versions, src_for_log):
    if isinstance(node, dict):
        for key, value in node.items():
            if key == '$ref' and isinstance(value, str):
                node[key] = rewrite_ref(value, versions, src_for_log)
            else:
                rewrite_refs(value, versions, src_for_log)
    elif isinstance(node, list):
        for item in node:
            rewrite_refs(item, versions, src_for_log)


def process_commit(commit, root, dry_run, written, unresolved):
    """
    Materialise every (schema, version) pair this commit declares that has
    not been written yet.

    Commits are visited oldest-first, so the first commit declaring a pair
    wins: the content as of when that version was minted. Editing often
    continued under an already-bumped version, and those later states are
    work in progress that was never released -- picking the newest declaring
    commit instead resurrects them, recognisable by ``$ref``s pointing at
    ``0.0.0`` placeholder versions.

    Pairs already written are skipped without a blob fetch, which is what
    keeps the full-history walk cheap.
    """
    current = leaf_versions(blob_at(commit, VERSIONS_FILE))
    logged_subject = False
    for path, version in sorted(current.items()):
        src = schema_path(path)
        dst_rel = Path(OUTPUT_DIR, *src.parts[1:-1], version, src.stem)
        if dst_rel in written:
            continue
        dst_abs = root / dst_rel
        if dst_abs.exists():
            written[dst_rel] = True
            continue
        raw = blob_at(commit, str(src))
        if raw is None:
            unresolved.setdefault((path, version), src)
            continue
        if not logged_subject:
            subject = git('log', '-1', '--format=%s', commit).stdout.decode().strip()
            print(f'\n{commit[:8]} {subject}')
            logged_subject = True
        id_path = '/'.join((*src.parts[1:-1], version, src.stem))
        try:
            schema = json.loads(raw)
        except json.JSONDecodeError as e:
            print(f'  BADJSON {src} @ {version}: {e}; writing raw')
            contents = raw
        else:
            rewrite_refs(schema, current, str(src))
            schema = inject_id(schema, f'{BASE_URL}/{id_path}')
            contents = (json.dumps(schema, indent=2) + '\n').encode()
        print(f'  WRITE  {dst_rel}')
        written[dst_rel] = True
        unresolved.pop((path, version), None)
        if not dry_run:
            dst_abs.parent.mkdir(parents=True, exist_ok=True)
            dst_abs.write_bytes(contents)


def write_index(out_root):
    """
    Emit ``index.html`` at ``out_root`` with a nested listing of every
    file underneath. Links use absolute (server-root-relative) paths.
    """
    import html

    def build_tree():
        tree = {}
        for path in sorted(out_root.rglob('*')):
            if path.name in ('index.html', UPLOAD_SCRIPT, CSS_FILE, FAVICON_FILE):
                continue
            rel = path.relative_to(out_root)
            node = tree
            for part in rel.parts[:-1]:
                node = node.setdefault(part, {})
            node[rel.parts[-1]] = None if path.is_file() else {}
        return tree

    def sort_key(item):
        name, child = item
        if SEMVER_RE.match(name):
            return (child is None, 0, tuple(int(p) for p in name.split('.')))
        return (child is None, 1, name)

    def render(node, prefix):
        lines = ['<ul>']
        for name, child in sorted(node.items(), key=sort_key):
            while (
                isinstance(child, dict)
                and len(child) == 1
                and next(iter(child.values())) is None
            ):
                only_name = next(iter(child))
                name = f'{name}/{only_name}'
                child = None
            path = f'{prefix}/{name}' if prefix else name
            if child is None:
                lines.append(
                    f'<li><a href="{html.escape(path)}">{html.escape(name)}</a></li>'
                )
            else:
                lines.append('<li><details>')
                lines.append(f'<summary>{html.escape(name)}/…</summary>')
                lines.append(render(child, path))
                lines.append('</details></li>')
        lines.append('</ul>')
        return '\n'.join(lines)

    body = render(build_tree(), '')
    doc = (
        '<!doctype html>\n'
        '<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        f'<link rel="icon" href="{FAVICON_FILE}">\n'
        f'<link rel="stylesheet" href="{CSS_FILE}">\n'
        '<style>li:has(> a) { margin-bottom: var(--pico-typography-spacing-vertical); }</style>\n'
        '<title>HCA metadata schemas</title>\n'
        '</head>\n<body>\n<main>\n'
        '<h1>HCA metadata schemas</h1>\n'
        f'{body}\n</main>\n</body>\n</html>\n'
    )
    (out_root / 'index.html').write_text(doc)


def write_stylesheet(out_root):
    """
    Download Pico CSS from the CDN and save it as a sibling of index.html.
    """
    with urllib.request.urlopen(CSS_URL, timeout=30) as response:
        css = response.read()
    (out_root / CSS_FILE).write_bytes(css)


def write_favicon(out_root):
    """
    Download the HCA favicon and save it as a sibling of index.html.
    """
    with urllib.request.urlopen(FAVICON_URL, timeout=30) as response:
        icon = response.read()
    (out_root / FAVICON_FILE).write_bytes(icon)


def write_upload_script(out_root):
    """
    Emit a shell script that uploads the site to S3 with correct
    Content-Type / Content-Disposition headers. Takes the bucket name
    as the sole argument. With --force, re-uploads every schema object
    so that Content-Type / Content-Disposition metadata is refreshed
    even when the body is unchanged (s3 sync would otherwise skip), and
    deletes objects in the bucket that no longer exist locally. The
    deletion is listed and confirmed before it happens unless --yes is
    also given.
    """
    script = '#!/bin/sh' + textwrap.dedent(f'''
        # Upload this directory to S3 with correct Content-Type / Content-Disposition
        # headers for extensionless JSON schemas.
        # Usage: ./{UPLOAD_SCRIPT} [--force] [--yes] <bucket>
        # --force: re-upload every schema even if unchanged, to refresh metadata,
        #          and delete bucket objects that no longer exist locally.
        # --yes:   do not prompt before deleting.
        set -eu

        FORCE=0
        ASSUME_YES=0
        while [ $# -gt 0 ]; do
            case "$1" in
                --force) FORCE=1; shift ;;
                --yes) ASSUME_YES=1; shift ;;
                --) shift; break ;;
                -*) echo "unknown option: $1" >&2; exit 1 ;;
                *) break ;;
            esac
        done

        if [ $# -ne 1 ]; then
            echo "usage: $0 [--force] [--yes] <s3-bucket>" >&2
            exit 1
        fi
        BUCKET="$1"

        cd "$(dirname "$0")"

        TMP=$(mktemp -d)
        trap 'rm -rf "$TMP"' EXIT

        # Schema files: extensionless, served as JSON, displayed inline.
        # --force switches from `s3 sync` (skips unchanged) to `s3 cp --recursive`
        # (always PUTs), so Content-Type / Content-Disposition are always refreshed.
        if [ $FORCE -eq 1 ]; then
            SCHEMA_CMD="aws s3 cp . s3://$BUCKET/ --recursive"
        else
            SCHEMA_CMD="aws s3 sync . s3://$BUCKET/"
        fi
        $SCHEMA_CMD \\
            --exclude "index.html" \\
            --exclude "{UPLOAD_SCRIPT}" \\
            --exclude "{CSS_FILE}" \\
            --exclude "{FAVICON_FILE}" \\
            --content-type application/json \\
            --content-disposition inline

        # Index page: HTML. `s3 cp` always PUTs, so metadata is always fresh.
        aws s3 cp index.html "s3://$BUCKET/index.html" \\
            --content-type "text/html; charset=utf-8"

        # Stylesheet: CSS. Same reasoning as index.html.
        aws s3 cp {CSS_FILE} "s3://$BUCKET/{CSS_FILE}" \\
            --content-type "text/css; charset=utf-8"

        # Favicon: PNG bytes served under an .ico name. Modern browsers sniff.
        aws s3 cp {FAVICON_FILE} "s3://$BUCKET/{FAVICON_FILE}" \\
            --content-type "image/x-icon"

        # --force also prunes: delete objects in the bucket that no longer exist
        # locally. Earlier revisions of the generator used different layouts, so
        # the bucket can hold objects from those runs. Pruning runs last, so the
        # site is never missing files partway through.
        if [ $FORCE -eq 1 ]; then
            echo
            echo "Looking for stale objects in s3://$BUCKET/ ..."
            find . -type f | sed 's|^\\./||' | grep -v "^{UPLOAD_SCRIPT}$" | sort > "$TMP/local"
            aws s3api list-objects-v2 --bucket "$BUCKET" \\
                --query "Contents[].Key" --output text \\
                | tr "\\t" "\\n" | grep -v "^None$" | sed "/^$/d" | sort > "$TMP/remote"
            comm -13 "$TMP/local" "$TMP/remote" > "$TMP/stale"
            STALE=$(wc -l < "$TMP/stale" | tr -d " ")
            if [ "$STALE" -eq 0 ]; then
                echo "No stale objects."
            else
                echo "$STALE stale object(s):"
                sed "s/^/  /" "$TMP/stale"
                DELETE=1
                if [ $ASSUME_YES -eq 0 ]; then
                    printf "Delete these %s object(s)? [y/N] " "$STALE"
                    read ANSWER
                    case "$ANSWER" in
                        y|Y|yes|YES) ;;
                        *) DELETE=0; echo "Left in place." ;;
                    esac
                fi
                if [ $DELETE -eq 1 ]; then
                    while IFS= read -r KEY; do
                        aws s3 rm "s3://$BUCKET/$KEY"
                    done < "$TMP/stale"
                fi
            fi
        fi
        ''')
    path = out_root / UPLOAD_SCRIPT
    path.write_text(script)
    path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Report the files that would be written without touching disk.',
    )
    args = parser.parse_args()

    root = repo_root()
    commits = commits_touching_versions()
    print(f'Processing {len(commits)} commits touching {VERSIONS_FILE}')
    print(f'Writing to {root / OUTPUT_DIR}')
    written = {}
    unresolved = {}
    for commit in commits:
        process_commit(commit, root, args.dry_run, written, unresolved)
    print(f'\nResolved {len(written)} (schema, version) pairs')
    if unresolved:
        print(f'{len(unresolved)} pairs declared but never resolvable to a blob:')
        for (path, version), src in sorted(unresolved.items()):
            print(f'  {src} @ {version}')
    if not args.dry_run:
        write_stylesheet(root / OUTPUT_DIR)
        print(f'\nWrote {root / OUTPUT_DIR / CSS_FILE}')
        write_favicon(root / OUTPUT_DIR)
        print(f'Wrote {root / OUTPUT_DIR / FAVICON_FILE}')
        write_index(root / OUTPUT_DIR)
        print(f"Wrote {root / OUTPUT_DIR / 'index.html'}")
        write_upload_script(root / OUTPUT_DIR)
        print(f'Wrote {root / OUTPUT_DIR / UPLOAD_SCRIPT}')


if __name__ == '__main__':
    sys.exit(main())
