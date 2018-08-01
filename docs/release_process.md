# The Human Cell Atlas: Metadata Release Process

## Table of Contents
- [Introduction](#introduction)
- [Steps of the pre-release process](#steps-of-the-pre-release-process)
- [Steps of the release process](#steps-of-the-release-process)

## Introduction

This document serves as an SOP for super users who are responsible for merging PRs into develop ("pre-release") and propagate metadata schemas from develop to integration, to staging, to production ("release").

**What is in this document**
- Steps for merging pull requests (PRs) into the develop branch aka "pre-release"
- Steps for merging the develop branch into the integration branch aka "release"
- Steps for propagating from integration to staging and production

 **Who should be reading this document?**
 - HCA DCP internal developers with authorisation to do metadata pre-releases and releases.

 **What *isn't* in this document?**
- Description of what defines [major, minor, and patch changes](metadata-schema/docs/evolution.md#schema-versioning) to the metadata schema
- Directions for [reporting bugs](metadata-schema/docs/contributing.md#reporting-bugs) in the metadata schema
- Directions of [making changes to metadata schemas](metadata-schema/docs/committers.md)


## Preliminaries

Committers who regularly interact with the metadata-schema repo and who merge PRs should have the metadata pre-commit githook enabled that rebuilds the markdown docs on each commit. ***You only need to do this once***

1. **Check** that you have Git version 2.9 or greater

    `git --version`

2. In your local metadata schema repo, **redirect** git hooks to the .githooks directory

    `git config core.hooksPath .githooks`

From now on, every time you commit anything in the metadata schema repo using the `git commit` command, the git hook will be triggered to build the jsonBrowser markdown docs and add them to your commit.


## Steps of the pre-release process

***Condition for pre-release:*** A pull request is ready to be merged into develop when it has been approved by the metadata community in line with the general acceptance process.


1. **Check out** the pull request branch and make sure your local copy is up to date

    `git checkout <name_of_branch>`

    `git pull`

1. **Verify** whether there are any merge conflicts between the PR branch and develop. You can do this in github. If merge conflicts exist between the branch and develop,

    1. **Pull** develop into the PR branch locally (on your computer)

        `git pull origin develop`

        This is equivalent to merging develop into the PR branch and reveals all the conflicts.

    1. **Open** any files with conflicts, ideally in an environment that is able to help with merge conflicts such as PyCharm (but a text editor is also fine)

    1. **Fix** the merge conflicts and commit.

        ***NB*** If merge conflicts are limited to files in the `/docs` directory, you can designate the version in your branch as the correct version over the files in `develop` by using:

        `git merge --strategy-option ours`

1. **Check json_schema/update_log.csv** to make sure that all metadata changes in this branch have been documented. There should be two commas at the end of each line in this file.

1. **Run** the release preparation script from the src directory. The script should be run with Python 3 and takes no direct input arguments, but does require update_log.csv to be filled in correctly.

    `cd src`

    `python3 release_prepare.py`

    The script updates the version numbers of the schemas listed in update_log.csv using the indicated increment type (major, minor or patch) in the json_schema/versions.json file as well as any dependent schemas. It then builds the changelog.md file. Finally, it deletes the content of update_log.csv apart from the header row.

1. **Check** that both json_schema/versions.json and changelog.md were updated.

    `git status`

    You can also review the specific changes to files using

    `git diff`

1. **Commit** your changes back to the branch and push to github

    `git commit -a -m "Ran release_prepare.py script."`

    `git push origin <name_of_branch>`

1. **Wait** for the Travis build to pass, the **merge** then PR into develop.



## Steps of the release process

### Primary release

1. **Check out** develop to your local machine.

1. **Verify** that there are no merge conflicts between develop and integration by running

    `git pull origin integration`

    1. **Fix** any merge conflicts that might arise, giving priority to changes in the develop branch *except* if a hotfix was propagated ahead of develop.

1. **Open** changelog.md and cut/paste the line

    `## [Released](https://github.com/HumanCellAtlas/metadata-schema/)`

    right below the line

    `## [Unreleased](https://github.com/HumanCellAtlas/metadata-schema/tree/develop)`

1. **Commit** your changes back to Github

    `git commit -a -m "Release from develop to integration YYYY-MM-DD"`

    `git push origin develop`

1. **Create a pull request** from *develop* to *integration* for easy tracability but immediately merge this yourself. ***Only merge your own pull requests in this particular scenario!***


### Release propagation

Promotion of changes from integration to staging and staging to production should be done in line with the general DCP release schedule. These release propagations should be straight forward merge operations through the environments, with no manual changes being required.

The designated **release manager** for the week is in charge of the relevant propagation steps.





