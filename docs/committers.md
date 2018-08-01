# The Human Cell Atlas: Metadata Update Process for Committers

## Table of Contents
- [Introduction](#introduction)
- [Steps of the update process](#steps-of-the-update-process)
- [Schema update acceptance process](#schema-update-acceptance-process)
- [Specific steps for making changes](#specific-steps-for-making-changes)
- [Observed guidelines](#observed-guidelines)

## Introduction

This document serves as an SOP for committers who are ultimately responsible for changes to the metadata standards.

**What is in this document?**
 - Directions for [how to incorporate feedback](#steps-of-the-update-process) into the metadata standards
 - Expectations for contributions to be accepted or rejected

**Who should be reading this document?**
 - HCA DCP internal developers

**What *isn't* in this document?**
- Description of what defines [major, minor, and patch changes](evolution.md#schema-versioning) to the metadata schema
- Directions for [reporting bugs](contributing.md#reporting-bugs) in the metadata schema

## Steps of the update process

1. **Receive request for update to the metadata standard.** Any person (a "Contributor") can suggest changes to the metadata standards via three main routes:
    1. Create a [GitHub issue](https://github.com/HumanCellAtlas/metadata-schema/issues/new) on the metadata-schema GitHub repo
    1. Email the HCA DCP helpdesk at [data-help@humancellaltas.org](mailto:data-help@humancellaltas.org)
    1. Make a pull request against the develop branch of the metadata-schema GitHub repo

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

2. **Assign committer to review the suggestion.** A person (the "Reviewer") with commit rights on the metadata-standards repo will be assigned to each suggestion (issue/email/PR). The Reviewer will be responsible for reviewing the suggestion, noting any consequences of the suggestion, contacting appropriate HCA teams for feedback, and making announcements to ensure the whole community has an opportunity to provide input. 

3. **Make pull request if one does not exist.** If the suggestion came in the form of a GitHub issue or email, then the Reviewer needs to make the suggested update and a pull request. If the Contributor has a GitHub account, s/he should be encouraged to make the suggested update and a pull request. If this happens, another committer should be added to review and merge the pull request.

4. **Annotate the pull request with suitable labels and run unit tests.** The assigned reviewer should classify the suggested change by the type of change it is from a versioning perspective (patch, minor, or major) and the stability category of the module being changed (high, medium, or low). These labels can be setup in the GitHub repo so which pull requests have been flagged with which category are easy to see and filter. 

    The reviewer should also ensure the integration tests have been run. Minor and patch version changes should not cause the tests to fail. A major version change may cause test failures, especially when in a high stability module and this should help the reviewer to select the appropriate people to assist with the review.

    We aim for steps 1 to 4 to be completed less than 48 hours from the initial request being received.

5. **Notify community about the change request.** The pull request should be posted to the #hca-metadata Slack channel and the metadata-wg mailing list so everyone can have an opportunity to comment over the time frame specified by the combination of stability level and version change.

    The committer leading this effort should ensure appropriate developers from any system which could be impacted by the change are watching the thread on the pull request.

6. **Start the update acceptance process.** The assigned committer now starts the clock on the update acceptance process (see below). They should ensure the community is reminded about the proposed change at least once during the review timeframe. They also need to ensure any other assigned reviewer actively accepts the change and/or provides feedback on the change. 

7. **Accept or reject the change.** Once the review period is over, if the change is accepted into the repository, the pull request will be merged. The pull request merge should trigger automated updates to the documentation and propagation of the new schemas through the ingest system. The precise timing of the new schema version into production will depend on any software consequences for the change. Any patch or minor version change should be usable very quickly but major version changes might take longer depending on how long it takes any affected piece of software to be updated to function with the new schema.

8. **Announce accepted change to community**. The change will be announced both on #hca-metadata Slack channel and the metadata-wg mailing list by the committer. 

## Schema update acceptance process

There are three types of update acceptance verification: full, medium, and light. These three levels aim to facilitate agility for simple changes with few downstream dependencies but ensure that appropriate consideration is required for changes which are likely to trigger software updates. All reviews should consider what need is met by the requested change and what the impact of the change is on the existing systems, ensuring that updates which require major version changes also bring value to the DCP as a whole.

The *review timeframe* should start when the committer responsible for the suggestion has notified the #hca-metadata slack channel and the metadata-wg email list about the pull request. Weekend days do not count for the review timeframe.

The *minimum reviewer number* is the minimum number of people who need to have seen and agreed to the change before the pull request can be accepted. This agreement must be active and result in at least +1 on the pull request thread. If a DCP team member or metadata-schema repo committer are the person to suggest a change, they should not be counted as one of the reviewers needed for agreement.

Any *negative marks* (-1) against a proposal that can not be resolved in the allotted timeframe will need to extend the review process. The full details of this are described below. 

If during this process there is any disagreement about the best approach, the assigned committer should work with the contributor and other concerned third parties to find an acceptable solution for all concerned. If consensus still cannot be reached, a vote between the committers for the metadata schema repo should decide the right solution.

### Full acceptance

**Review timeframe**: 10 working days

**Minimum reviewer number**: 3 (a committer, and two relevant third parties)

Full acceptance is used when making major version changes to high stability modules. This means the module being changed is likely to trigger a new software release for a DCP service. The DCP service which is most likely to be affected by any metadata update would be the Ingest Infrastructure. This should be a rare occurrence. The DCP metadata and code should have a clear separation of concerns and the dependencies between the two should be minimal. That being said, the ingest infrastructure, in particular, needs some knowledge of the metadata structure in order to enable ID fields to be assigned and to allow the system to know the relationships between the submitted entities. Any module which contains these fields must be considered high stability.

This process should take 10 working days. The assigned committer should identify at least two developers from the DCP team to review the change and comment as well as themselves. If the contributor making the suggestion was a developer from a DCP team, the two reviewers should be other DCP developers. 

### Medium acceptance

**Review timeframe**: 120 hours (5 working days)

**Minimum reviewer number**: 2 (a committer and one relevant third party)

Medium acceptance is the process used for major version changes to medium stability modules and minor version changes to both high and medium stability modules. 

Generally this is a suitable acceptance process for changes which don’t require DCP software updates but are likely to affect how the metadata can be queried from a scientific perspective. It is expected for these types of updates to happen more frequently than those which require full acceptance as they will concerns fields with scientific meaning. New experiments and changes in technology may require new fields or changes to existing fields.

The process should take 5 working days. The assigned committer should identify at least one interested third party from the secondary and tertiary analysis groups to provide review. As before if it the contributor is a member of the secondary or tertiary analysis group, another person should be selected as the reviewer.

### Light acceptance

**Review timeframe**: 72 hours (3 working days)

**Minimum reviewer number**: 1 (a committer)

Light acceptance is the process used for all patch versions, regardless of stability and for all changes to low stability modules.

Light acceptance is lightweight process which allows rapid iteration for new technologies where the requirements are not precisely defined and the processes are changing quickly.  Downstream users of this data should be aware that the metadata is changing rapidly and understand any dependencies they create on specific structures will be broken in future.

The process should take 3 working days. The assigned committer does not need to recruit an additional reviewer though should ensure that as many people as possible have seen the suggestion via slack messages or email.

| | Major version | Minor Version  | Patch version |
|:-|:-|:-|:-|
| High Stability | Full acceptance | Medium acceptance | Light acceptance |
| Medium Stability | Medium acceptance | Medium acceptance | Light acceptance |
| Low Stability | Light acceptance | Light acceptance | Light acceptance |

> Table 1: Which update acceptance process to use for which category of suggested change.

### How to manage negative marks against a suggested change.
Hopefully negative marks or a lack of consensus will be very rare occurrence but this process does contain the possibility of disagreement on the best solution. 

For proposed changes where consensus looks unlikely, as the review deadline looms (~ 1 day before if possible), the assigned committer should schedule a phone call to discuss the issue with the interested parties. If no consensus can be reached, the process should be extended by 5 working days for more interaction. At the end of these 5 days, if no consensus has been reached, the two possible solutions should be presented to the committers and a vote should be called with the committers to the metadata-schemas repo, the solution with most votes being taken forward.

## Specific steps for making changes

This section outlines steps for contributors to suggest changes to the metadata schema via pull requests.

1. **Clone** the metadata-schema repository into your local environment.

    `git clone git@github.com:HumanCellAtlas/metadata-schema`

1. **Navigate** to the metadata-schema repo.

    `cd metadata-schema`
    
1. **Switch** to the develop branch. All suggested changes should be based on the current develop branch.

    `git checkout develop`

1. **Make** and **switch** to a new working branch from develop. Name the branch following the convention: `initials-brief_desc_of_branch_scope`. Optionally, you can tag a GitHub issue (e.g. `Issue222`) or JIRA ticket (e.g. `HCA-123`) in the branch name.

    `git checkout -b mf-new_mouse_module-Issue222`

1. **Make** changes locally to the new working branch. After making changes, it is important to run the `src/schemas_are_valid_json.py` and `src/json_examples_validate_against_schema.py` scripts (which are run by Travis CI). The first script checks whether each .json file in the `json_schema` folder is valid JSON format. The second script attempts to validate example JSON files in the `schema_test_files` directory against their corresponding schemas. Some of the JSON files are meant to fail (e.g. they are lacking required fields) and as their failure is expected behavior, the script should exit with status 0. Ensure both scripts exit with status 0 (you should see `Process finished with exit code 0` printed to the terminal) before committing changes. If either test fails, you will have to debug and fix the errors in the changes you made.

1. **Document** the changes in the update_log.csv file. This file is used by the automated release scripts to build the release changelog and increment the version number for the correct metadata schema. Unlike the changelog file, which is a running log of all metadata schema changes, the update_log file should only contain the documented changes for this branch, so the file should be empty apart from the header row when you first check out a new branch. An entry into update_log.csv should contain the path to the schema that was changed, the type of change (major, minor or patch) and the description of the change that should go into the changelog, for example:

    `module/ontology/disease_ontology,patch,Fixed a typo in description of text field in disease_ontology. Fixes #000,,`

    Only list one schema per line and only list schemas that you have actually changed as the release script will automatically identify dependent schemas. Each line should end in a double comma, signifying the empty columns for version number and release date, which will be filled in by the release script. Not including the commas will cause the release script to fail. If there is a comma in the change message, the message needs to be quoted:

    `type/biomaterial/organoid,patch,"Added user friendly names for fields a, b, c and d",,`

    The change message should start with one of *Added, Changed, Removed, Fixed, Deprecated or Security*

    ***New schemas only***

    1. If you added a new schema, **add** the name of the new schema in `json_schema/versions.json` in the correct location and with version number 0.0.0. For example, if you added a new biomaterial module `my_new_module`, your addition to the `versions.json` file would be:

           `[...]
            "module": {
            "biomaterial": {
                [...],
                "my_new_module": 0.0.0
            },
            [...]`

    2. The corresponding entry in the `update_log.csv` file should be marked a major version update so that the release script sets the version number of the new schema to `1.0.0`.


1. **Stage** and **commit** your changes to the working branch often. We recommend committing after making a few logically grouped changes to help track changes and to increase granularity for rollbacks (if needed). Use helpful/short messages in commit statements. If the commit specifically fixes/addresses a current GitHub issue, you can add the phrase "Fixes #000" to the commit statement, replacing "000" with the number of the issue. This phrase is handy because when the changes are merged into the master branch, it automatically closes the issue indicated.

    `git add <changed files>`
    
    `git commit -m "Helpful commit message here. Fixes #000."`
    
    Example commit message: "Created new mouse module with mouse-specific fields. Fixes #142."

1. **Push** the committed changes to the working branch.

    `git push origin mf-new_mouse_module-Issue222`

1. **Continue** to make, stage, and commit changes to the working branch - ensuring that the two Travis CI scripts pass - until you have completed and pushed all the changes within the scope of your new branch. In the GitHub UI, **create** a pull request (PR) against the `develop` branch. In the comment section of the PR, write a general description of the changes followed by a bulleted list of the specific changes made in the files. 

1. **Request** a reviewer to send notifications that a PR needs to be reviewed and merged. **Do not merge your own PR.** If the changes are ultimately approved, the old branch will be deleted unless otherwise specified by the contributor.

## Observed guidelines

- *Do not merge your own PR.* This ensures that at least one other person has reviewed the suggested changes and has approved them. The only exception is if another person specifically "approves" your PR, but doesn't actually merge it. In this scenario, because the other person gave approval that they agree with the changes, the original PRer is allowed to merge their own changes.
- *Be clear and descriptive in PR comments.* Include references to current GitHub issues when appropriate. Reference specific people if the PR addresses someones concerns. Include reasoning behind changes that could be controversial (e.g. reason why a field name changes, but no reason needed to fix a typo in a field description).

