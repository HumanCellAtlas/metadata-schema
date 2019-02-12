# The Human Cell Atlas: Metadata Release Process

## Table of Contents
- [Introduction](#introduction)
- [Preliminaries](#preliminaries)
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
- Description of what defines [major, minor, and patch changes](evolution.md#schema-versioning) to the metadata schema
- Directions for [reporting bugs](contributing.md#reporting-bugs) in the metadata schema
- Directions for [making changes to metadata schemas](committers.md)

## Preliminaries

Committers who regularly interact with the metadata-schema repo and who merge PRs should have the metadata pre-commit githook enabled that rebuilds the markdown docs on each commit. ***This only needs to be done once.***

1. **Check** that you have Git version 2.9 or greater

        git --version

2. In your local metadata schema repo, **redirect** git hooks to the .githooks directory

        git config core.hooksPath .githooks

From now on, every time you commit anything in the metadata schema repo using the `git commit` command, the git hook will be triggered to build the jsonBrowser markdown docs and add them to your commit.

## Steps of the pre-release process

***Condition for pre-release:*** A pull request is ready to be merged into develop when it has been approved by the metadata community in line with the [acceptance process](committers.md#schema-update-acceptance-process). It is the responsibility of the last Reviewer of the PR to merge it into develop.


1. **Check out** the pull request branch and make sure your local copy is up-to-date

        git checkout <name_of_branch>
        git pull

1. **Verify** whether there are any merge conflicts between the PR branch and develop. You can do this in github or on your computer. If merge conflicts exist between the branch and develop:

    1. **Pull** develop into the PR branch locally (on your computer)

            git pull origin develop

        This is equivalent to merging develop into the PR branch and reveals all the conflicts.

    1. **Fix** any merge conflicts

        There are a few different ways to fix merge conflicts. Some approaches are:
        
        1. Open files an environment that is able to help with merge conflicts such as PyCharm. Right-click anywhere in the directory browser on the left and choose Git ->  Resolve conflicts. In the pop-up, click on each file and either choose to keep Yours, Theirs, or Merge (if the conflicts are more complicated).
        
        1. Open files with an in-line text editor or text editing app. Follow directions [here](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/) for how to fix the conflicts.

        **NB**If merge conflicts are limited to files in the `/docs` directory, always keep *Your* changes as they will be the most up-to-date.

    1. **Commit** merge conflict fixes

1. **Check json_schema/update_log.csv** to make sure that all metadata changes in this branch have been documented. There should be two commas at the end of each line in this file.

1. **Run** the release preparation script from the `/src` directory. The script should be run with Python 3 and takes no direct input arguments, but does require `update_log.csv` to be filled in correctly.

        cd src
        python3 release_prepare.py

    The script updates the version numbers of the schemas listed in `update_log.csv` using the indicated increment type (major, minor or patch) in the `json_schema/versions.json` file as well as any dependent schemas. It then builds the `changelog.md` file. Finally, it deletes the content of `update_log.csv` apart from the header row.

1. **Check** that both `json_schema/versions.json` and `changelog.md` were updated.

        git status

    You can review the changes to all files using

        git diff
    
    Or for a specific file
    
        git diff ../json_schema/versions.json
        git diff ../changelog.md

1. **Commit** your changes back to the branch and push to github

        git commit -a -m "Ran release_prepare.py script."
        git push origin <name_of_branch>

1. **Wait** for the Travis build to pass, then **merge** this PR into develop immediately.

1. **Delete** the PR branch, unless otherwise noted by the person who opened the PR.

## Steps of the release process

### Primary release

Anyone on the metadata team can trigger a primary release from develop to integration. Please note that the DCP-wide release from integration to staging happens each Wednesday. It is preferable to do a primary release no later than Monday so that any issues that might arise can be addressed without disrupting the DCP-wide release process.

1. **Check out** develop to your local machine

1. **Verify** that there are no merge conflicts between develop and integration by running

        git pull origin integration

    1. **Fix** any merge conflicts that might arise, giving priority to changes in the develop branch *except* if a hotfix was propagated ahead of develop.

1. **Open** `changelog.md` and move the line

    `## [Released](https://github.com/HumanCellAtlas/metadata-schema/)`

    right below the line

    `## [Unreleased](https://github.com/HumanCellAtlas/metadata-schema/tree/develop)`

1. **Commit** your changes

        git commit -a -m "Release from develop to integration YYYY-MM-DD."
        git push origin develop

1. **Create a pull request** from *develop* to *integration* for easy traceability. The PR should be tagged with the "release" label and should contain **Release notes** split into two sections:
   1. *Versions*: Enter schema names and version numbers for any updated schemas. Enter the current version as shown in versions.json, skipping over intermediate versions.
   1. *Functionality changes*: Describe any changes in how the schema will function in the context of other DCP components. Include all the major and minor schema changes and any code changes, e.g. changes to the schema validation code.
    
   See example of *develop* to *integration* PR [here](https://github.com/HumanCellAtlas/metadata-schema/pull/665) 

1. **Wait** for the Travis build to pass, then **merge** this PR into develop immediately.
 
   ***Merge your own pull request in this particular scenario!***
   
   No additional Reviewers are required for this step, but if you are unsure about anything, do not hesitate to ask for a review from someone.

1. **Trigger** ingest core to redeploy in order to grab the newly released schemas by running:

   `curl -X POST https://api.ingest.integration.data.humancellatlas.org/schemas/update`

1. **Trigger** a DCP-wide integration test to run in the integration environment to confirm that the changes do not break the integration test. If the test passes, nothing further needs to be done. If the test fails, an investigation is needed to determine what steps need to be taken.

### Release propagation

Promotion of changes from integration to staging and staging to production should be done in line with the general [DCP release schedule](https://docs.google.com/spreadsheets/d/1Tqhs20tj_3FqdO_1Cam1iLSaqE-y9Piu8lDJ6KEdP80/edit#gid=1508723546). These release propagations should be straight forward merge operations through the environments, with no manual changes being required.
The designated **release manager** for the week is in charge of the relevant propagation steps. DCP-wide SOP for release operation can be found [here](https://allspark.dev.data.humancellatlas.org/dcp-ops/docs/wikis/SOP:%20Releasing%20new%20Versions%20of%20DCP%20Software). Metadata-specific SOP can be found [here](https://docs.google.com/document/d/1gNq5I42xY5ie8jqENSVEswn3NXHKUYgrfFgwMK_Vh8A/edit). 

