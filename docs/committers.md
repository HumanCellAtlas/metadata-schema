# The Human Cell Atlas: Metadata Update Process for Committers

## Table of Contents
- [Introduction](#introduction)
- [General steps of the update process](#general-steps-of-the-update-process)
- [Specific how-to for making changes](#specific-how-to-for-making-changes)
- [Schema update review process](#schema-update-review-process)
- [Committer guidelines](#committer-guidelines)
- [Adding new committers](#adding-new-committers)
- [Glossary of roles](#glossary-of-roles)

## Introduction

This document serves as an SOP for committers who are ultimately responsible for changes to the metadata standards.

**What is in this document?**
 - Directions for how to incorporate feedback into the metadata standards
 - Expectations for contributions to be accepted or rejected

**Who should be reading this document?**
 - HCA DCP internal developers
 - HCA DCP wranglers

**What *isn't* in this document?**
- Description of what defines [major, minor, and patch changes](evolution.md#schema-versioning) to the metadata schema
- Directions for [reporting bugs](contributing.md#reporting-bugs) in the metadata schema
- Directions for the [review process](https://github.com/HumanCellAtlas/dcp2/blob/main/docs/dcp2_operating_procedures.rst#15review-process-overview) of the metadata schema changes
- Directions for the [release process](https://github.com/HumanCellAtlas/metadata-schema/blob/master/docs/release_process.md) of metadata schema PRs

## General steps of the update process

1. **Receive request for update to the metadata standard.** A person (the "Contributor") can suggest changes to the metadata standards via three main routes:
    1. Create a GitHub issue on the metadata-schema repo for either [updates](https://github.com/HumanCellAtlas/metadata-schema/issues/new?template=schema_update.md) or [new schemas](https://github.com/HumanCellAtlas/metadata-schema/issues/new?template=new_schema.md)
    1. Email the HCA DCP helpdesk at [data-help@humancellaltas.org](mailto:data-help@humancellaltas.org)
    1. Make a pull request against the staging branch of the metadata-schema GitHub repo

    There are two main types of suggestions: (1) **updates** to existing schemas and (2) addition of **new** schema(s).

    1. To request an **update** to an existing schema, the following pieces of information are required:

        1. For which schema is a change/update being suggested?
        1. What should the change/update be?
        1. What new field(s) need to be added?
            - Details for requesting **new field(s)** outlined below
        1. Why is the change requested?

    1. To request a **new** schema, the following pieces of information are required:

        1. What is the proposed name of the new schema?
        1. What field(s) should the new schema contain?
            - Details for requesting **new field(s)** outlined below
        1. Why is the new schema needed? Specifically, why does the current metadata standard not meet your need?
    
    For **each new field** requested, the following pieces of information are required:
    
    1. Field name
    1. Field description
    1. Whether the field should be optional or required
    1. An example valid value for this field
    1. If this field needs a controlled vocabulary or ontology. If yes, what those values should be or which ontology should be followed.
    
    If the suggested update comes in the form of a pull request, the above information should be self-evident between the JSON schema itself and the pull request message. If this isn’t clear either from the pull request or the message sent through email or git, then the assigned committer will seek clarification before continuing to step 3.

1. **Assign Committer to review the suggestion.** A person (the "Committer") with commit rights on the metadata-schema repo will be assigned to each suggestion (issue/email/PR). The Committer will be responsible for reviewing the suggestion, noting any consequences of the suggestion, contacting appropriate HCA teams for feedback, and making announcements to ensure the whole community has an opportunity to provide input. 

1. **Make pull request if one does not exist.** If the suggestion came in the form of a GitHub issue or email, then the Committer needs to make the suggested update and a pull request against staging. If the Contributor has a GitHub account, they should be encouraged to make the suggested update and a pull request. When a pull request is made, a test suite of tools will automatically run that validates the updates. 

    **NB** Currently this test suite of tools is not complete, and the tools that do exist must be run manually by the Reviewer.

1. **Annotate the pull request (version) and run unit tests.** The Committer should classify the suggested update by the type of version change (major, minor, patch) in the pull request. The version change classification will be indicated in the `update_log.csv` file. The Committer should also ensure the metadata-schema repo unit tests have been run and pass. Example spreadsheets and JSON documents will potentially need to be updated.

1. **Notify downstream components about the update request.** The Committer should announce the suggested update/PR on the #dcp-2 channel so all the DCP2 components can review and comment on the PR, making sure the list of reviewers specified in the [DCP2 specs document](https://github.com/HumanCellAtlas/dcp2/blob/main/docs/dcp2_system_design.rst#id9) is 

1. **Pre-release the update.** Once the review period is over, if the update is accepted then the Committer merges the pull request into staging following the [release process](release_process.md). The update is now considered "pre-released".

## Before making changes

1. **Clone** the metadata-schema repository into your local environment (should only need to do this once).

        git clone git@github.com:HumanCellAtlas/metadata-schema

1. **Install** the following requirements:
   1. [Python 3](https://www.python.org/downloads/)
   2. [pre-commit](https://pre-commit.com/#quick-start): install then run `pre-commit install` to set up the git hook scripts present in the metadata repo

## Specific how-to for making changes

This section outlines steps for Committers to make suggested changes to the metadata schema via pull requests.

1. **Navigate** to the metadata-schema repo.

        cd metadata-schema
    
2. **Switch** to the staging branch. All suggested changes should be based on the current staging branch.

        git checkout staging

3. **Make** and **switch** to a new working branch from staging. Name the branch following the convention: `initials-brief-desc-of-branch-scope`. Optionally, you can tag a GitHub issue (e.g. `Issue222`) in the branch name.

        git checkout -b mf-new-mouse-module-Issue222

4. **Make** changes locally to the new working branch. After making changes, it is important to run the `src/schemas_are_valid_json.py` script locally. The script checks whether each .json file in the `json_schema/` folder is valid JSON format. 
If a file is not valid the script will output an error message to aid the debugging. Address the errors and only commit changes when the script runs without raising errors.

5. **Document** the changes in the `json_schema/update_log.csv` file. This file is used by the automated release scripts to build the release changelog and increment the version number for the correct metadata schema. Unlike the changelog file, which is a running log of all metadata schema changes, the update_log file should only contain the documented changes for this branch, so the file should be empty apart from the header row when you first check out a new branch. An entry into `update_log.csv` should contain the path to the schema that was changed, the type of change (major, minor, or patch) and the description of the change that should go into the changelog, for example:

    `module/ontology/disease_ontology,patch,Fixed a typo in description of text field in disease_ontology. Fixes #000,,`

    Only list one schema per line and only list schemas that you have actually changed as the release script will automatically identify dependent schemas. If multiple schemas are being updated in a single PR, order the lines in the `update_log.csv` file with patch changes first, then minor, then major. Each line should end in a double comma, signifying the empty columns for version number and release date, which will be filled in by the release script. Not including the commas will cause the release script to fail. If there is a comma in the change message, the message needs to be quoted:

    `type/biomaterial/organoid,patch,"Added user friendly names for fields a, b, c and d",,`

    The change message should start with one of: *Added, Changed, Removed, Fixed, Deprecated, or Security*. These keywords are used in the changelog to classify types of changes.  

    ***New schemas only***

    1. If you added a new schema, **add** the name of the new schema in `json_schema/versions.json` in the correct location and with version number 0.0.0. For example, if you added a new biomaterial module `my_new_module`, your addition to the `versions.json` file would be:

           [...]
            "module": {
            "biomaterial": {
                [...],
                "my_new_module": 0.0.0
            },
            [...]

    1. The corresponding entry in the `update_log.csv` file should be marked a major version update so that the release script sets the version number of the new schema to `1.0.0`.

    ***Breaking changes only***

    1. If you made a breaking (major) change to a property, including adding a new required property, renaming a property, removing a property or moving a property to a different schema, please fill in the `property_migrations.json` file following the correct pattern. Example migrations can be found in `examples/sample_property_migrations.json`.
    
    1. Do **NOT** fill in a value for the `effective_from/_source/_target` property, just insert blank quotes. This will be completed by the release script.

    1. If you are unsure how to fill in the `property_migrations.json` file, contact a wrangler for help.

    ***Note:*** *We currently don't have a process for capturing breaking changes not included in the above categories, such as changing the type of a field from a string to a number or from free text to ontology. Therefore such changes don't need to be captured in `property_migrations.json` for now.*

6. **Stage** and **commit** your changes to the working branch often. We recommend committing after making a few logically grouped changes to help track changes and to increase granularity for rollbacks (if needed). Use helpful/short messages in commit statements. If the commit specifically fixes/addresses a current GitHub issue, add the phrase "Fixes #000" to the commit statement, replacing "000" with the number of the issue. This phrase is handy because when the changes are merged into the master branch, it automatically closes the issue indicated.

        git add <changed files>
        git commit -m "Helpful commit message here. Fixes #000."
    
    Example commit message: "Created new mouse module with mouse-specific fields. Fixes #142."

7. **Push** the committed changes to the working branch.

        git push origin mf-new-mouse-module-Issue222

8. **Continue** to make, stage, and commit changes to the working branch until you have completed and pushed all the changes within the scope of your new branch. In GitHub, **create** a pull request against the staging branch and add the `content` label. In the comment section of the PR, fill out "Release notes" and "Reviews requested" sections as directed by the PR template. 

9. **Request** additional Reviewer(s) in GitHub to signal that a PR needs to be reviewed. The list of reviewers can be found in the [DCP2 specs document](https://github.com/HumanCellAtlas/dcp2/blob/main/docs/dcp2_system_design.rst#id9). If the changes are ultimately approved by all indicated Reviewer(s) and no objections are raised, the PR owner should run the pre-release process and merge the PR. **If not part of the Metadata Schema Team, the Committer should not merge their own PR.** The Reviewer who merges the PR should then delete the branch unless otherwise specified by the Committer.

## Schema update review process

The up-to-date guidelines on the review process are found in the [DCP2 operating procedures](https://github.com/HumanCellAtlas/dcp2/blob/main/docs/dcp2_operating_procedures.rst#15review-process-overview)

## Committer guidelines

1. *Be clear and descriptive in PR comments/commits.* 
    1. Refer to GitHub issues that the PR addresses by adding `Fixes #000` to at least 1 commit statement in the PR (where 000 is replaced by the actual GitHub issue number). 
    1. Tag a specific person if the PR addresses their issue or if the change affects their work.
    1. Include reasoning behind changes that could be controversial (e.g. reason why a field name changes, but no reason needed to fix a typo in a field description).
1. *Group commits by functional changes*
    1. In order to have a clear history, group changes in the least amount of commits possible. When needed, use `git rebase` to squash commits.

## Adding new committers

A nominated group of metadata working group members will have commit access to the metadata-schema repo.  Committers are members of the working group who have permission to merge and accept pull requests to the metadata-schema repo.

Committers are not allowed to skip the review process. Any person including the committers who wish to make a change to a metadata schema module this process must be followed.

Anyone can request to join the committer team. When a request is received, the existing committers will discuss the request and vote on the addition of the new member. This process should be rapid and the requestor should hear the outcome within 72 hours.


## Glossary of roles

**Contributor**

- Does not have commit/merge privileges to metadata-schema repo
- Suggests changes to the metadata standard (email/GitHub issue/PR)
- Reviews PRs

**Committer**

- Has commit/merge privileges to the metadata-schema repo
- Turns update requests into GitHub issues
- Is assigned to GitHub issues by himself/herself or another Committer
- Makes changes/PRs
- Announces PRs to community (Slack/mailing list)
- Reviews PRs
- Merges PRs

**Reviewer**

- Is assigned to review PRs by Committer
- Reviews PRs
- If also a Committer:
    - Has commit/merge privileges to the metadata-schema repo
    - Merges PRs
