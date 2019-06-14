#!/bin/sh
# Generate MarkDown documents and adds them to commit.

python3 src/human_readable_json.py
git add docs/jsonBrowser/*.md