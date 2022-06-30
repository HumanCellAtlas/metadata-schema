# The Human Cell Atlas: Metadata Release Process

## Table of Contents
- [Introduction](#introduction)
- [Preliminaries](#preliminaries)
- [Steps of the pre-release process](#steps-of-the-pre-release-process)
- [Steps of the release process](#steps-of-the-release-process)
- [Check deployment status](#check-deployment-status)
- [Steps of the hotfix process](#steps-of-hotfix-processdocumentation-updates)

## Introduction

This document is an SOP for super users who are responsible for merging PRs into `staging` ("pre-release") and propagate metadata schemas from staging to production (`master`).

**What is in this document**
- Steps for merging pull requests (PRs) into the staging branch aka "pre-release"
- Steps for merging the staging branch into the master branch aka "release"

 **Who should be reading this document?**
 - HCA DCP internal developers with authorisation to do metadata pre-releases and releases.
 - HCA DCP wranglers responsible for metadata schema updates

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

***Condition for pre-release:*** A pull request is ready to be merged into staging when it has been approved by the DCP2 components in line with the [acceptance process](https://github.com/HumanCellAtlas/dcp2/blob/main/docs/dcp2_operating_procedures.rst#review-process-overview). It is the responsibility of the PR author to merge the PR into staging.

1. **Check out** the `staging` branch and pull any changes to make sure it is up-to-date

        git checkout staging
        git pull

1. **Check out** the pull request branch and make sure your local copy is up-to-date

        git checkout <name_of_pull_request_branch>
        git pull

1. **Verify** whether there are any merge conflicts between the PR branch and staging. You can do this in GitHub or on your computer.

    1. **Pull** `staging` into the pull request branch locally (on your computer)

            git pull origin staging

        This is equivalent to merging staging into the PR branch and reveals all the conflicts.

    1. **Fix** any merge conflicts

        There are a few different ways to fix merge conflicts. Some approaches are:
        
        1. Open files in an environment that is able to help with merge conflicts such as PyCharm. Right-click anywhere in the directory browser on the left and choose Git ->  Resolve Conflicts. In the pop-up, click on each file and either choose to keep Yours, Theirs, or Merge (if the conflicts are more complicated).
        
        1. Open files with an in-line text editor or text editing app. Follow directions [here](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/) for how to fix the conflicts.

        **NB** If merge conflicts are limited to files in the `/docs` directory, always keep *Your* changes as they will be the most up-to-date.

    1. **Commit** merge conflict fixes

1. **Check** json_schema/update_log.csv to make sure that all metadata changes in this branch have been documented. There should be two commas at the end of each line in this file.

1. **Run** the release preparation script from the `/src` directory. The script should be run with Python 3 and takes no direct input arguments, but does require `update_log.csv` to be filled in correctly.

        cd src
        python3 release_prepare.py

    The script updates the version numbers of the schemas listed in `update_log.csv` using the indicated increment type (major, minor or patch) in the `json_schema/versions.json` file as well as any dependent schemas. It then builds the `changelog.md` file. Finally, it deletes the content of `update_log.csv` apart from the header row.
    
    > If the release_prepare.py script fails for any reason, run `git checkout -- <file>` replacing <file> with the name of each file that was changed (you can check this by running `git status`). This command with discard any changes that might have been made before the release prepare script failed. Once all the changes have been discarded, determine the cause of the error, make any adjustments to avoid the error, and repeat from Step 4.

1. **Check** that both `json_schema/versions.json` and `changelog.md` were updated.

        git status

    You can review the changes to all files using

        git diff
    
    Or for a specific file
    
        git diff ../json_schema/versions.json
        git diff ../changelog.md
        
     > If `json_schema/versions.json` and `changelog.md` do not appear to have been updated correctly, you can try running release_prepare.py again after discarding all the current changes (`git checkout -- <file>`).

1. **Commit** your changes back to the branch and push to GitHub

        git commit -a -m "Ran release_prepare.py script."
        git push origin <name_of_pull_request_branch>

1. **Merge** the PR into `staging` immediately.

1. **Delete** the PR branch, unless otherwise noted by the person who opened the PR.

1. **Mark** any linked GitHub issues with the "done" label, and then **close** the issue.

1. **Check** the changes in versions have been picked up by checking the #hca-schema-pub-announce slack channel

## Steps of the release process

### Primary release

Anyone on the metadata team can trigger a primary release from staging to master.

1. **Check out** the master branch and pull any changes to make sure it is up-to-date

        git checkout master
        git pull

1. **Check out** the staging branch to your local machine

        git checkout staging
        git pull

1. **Verify** that there are no merge conflicts between staging and master by running

        git pull origin master

    1. **Fix** any merge conflicts that might arise, giving priority to changes in the staging branch *except* if a hotfix was propagated ahead of staging.

1. **Open** `changelog.md` and move the line

    `## [Released](https://github.com/HumanCellAtlas/metadata-schema/)`

    right below the line

    `## [Unreleased](https://github.com/HumanCellAtlas/metadata-schema/tree/staging)`

1. **Commit** your changes

        git commit -a -m "Release from staging to master YYYY-MM-DD."
        git push origin staging

1. **Create a pull request** from *staging* to *master* for easy traceability. The PR should be tagged with the "release" label and should contain **Release notes** split into two sections:
   1. *Versions*: Enter schema names and version numbers for any updated schemas. Enter the current version as shown in versions.json, skipping over intermediate versions.
   1. *Functionality changes*: Describe any changes in how the schema will function in the context of other DCP components. Include all the major and minor schema changes and any code changes, e.g. changes to the schema validation code.
    
   [**WARNING**:Environments outdated] See example of *develop* to *integration* release PR [here](https://github.com/HumanCellAtlas/metadata-schema/pull/665) 

1. **Merge** this PR into master immediately.
 
   ***Merge your own pull request in this particular scenario!***
   
   No additional Reviewers are required for this step, but if you are unsure about anything, do not hesitate to ask for a review from someone.

1. **Check** the changes in versions have been picked up by checking the #hca-schema-pub-announce slack channel

1. In the [geo_to_hca ](https://github.com/ebi-ait/geo_to_hca/tree/master/docs) repository, download the latest version of the hca_template, and edit to add the new metadata schema changes. 

1. Move the now outdated template to the [outdated templates](https://github.com/ebi-ait/geo_to_hca/tree/master/docs/Outdated%20Templates) folder, and upload the new up-to-date template following DDMMYYhca_template.xlsx to the repo. 

1. Notify the other wranglers to download the new version of the spreadsheet template.

## Steps of hotfix process/documentation updates
***Condition for hotfix***: A pull request is ready to be merged into master when it has been approved by the metadata community. Specifics for acceptance may vary between each PR depending on the request. Hotfixes are a special case of PR and do not follow the normal release process.
***Condition for documentation update***: A pull request that only contains documentation (markdown files) updates is ready to be merged.


1. Run `release_prepare.py` as indicated in step 5 the pre-release process
   ```
   cd src/
   python release_prepare.py
   ```
 
 1. **Check** that both `json_schema/versions.json` and `changelog.md` were updated. (Same as step 6 of pre-release process)

        git status

    You can review the changes to all files using

        git diff
    
    Or for a specific file
    
        git diff ../json_schema/versions.json
        git diff ../changelog.md
        
     > If `json_schema/versions.json` and `changelog.md` do not appear to have been updated correctly, you can try running release_prepare.py again after discarding all the current changes (`git checkout -- <file>`).
   
1. **Open** `changelog.md` and move the line 

    `## [Released](https://github.com/HumanCellAtlas/metadata-schema/)`

    right below the line

    `## [Unreleased](https://github.com/HumanCellAtlas/metadata-schema/tree/staging)`
    
    (step 4 of the release process)

1. **Commit and push** your changes
   ```
   git commit -a -m "Ran release_prepare.py script."
   git push origin <PR_branch>
   ```

1. **Merge** the branch to master by clicking on the "merge" button at the end of the PR. **DO NOT DELETE THE BRANCH**. 

After merging to master, carry out the next 5 steps for staging

1. **Check out** the `<release_branch>` you are hotfixing and pull to make sure you have the latest changes locally
   ```
   git checkout <release_branch>
   git pull
   ```

1. **Check out** the `hotfix_branch` again, pull the `<release_branch>` and resolve merge conflicts
   ```
   git checkout <hotfix_branch>
   git pull origin <release_branch>
   ```
   Please do not overwrite changes inside the release branch. There might be changes to:
      - **Metadata Schemas**: Keep all the changes that do not affect the hotfix.
      - **Changelog.md**: Keep specific changes (if any) of the environment.
      - **Versions.json**: Make sure new versions do not conflict.
   > PyCharm provides a handy user interface that makes resolving merge conflicts easier than github.
      
1. **Create** a PR against the release branch. Tag it with the labels `content` (If schema changes) and `hotfix`.

1. **Review all files** to ensure environment-specific updates are not being overwritten.

1. Wait for travis tests to pass and **merge the PR**.

1. **Repeat** for the next branch until it is hotfixed to `master` and `staging` environments.

1. After merging the hotfix to all release branches, **Delete the branch**.

