# The Human Cell Atlas: Metadata Update Process

## Table of Contents
- [Introduction](#introduction)
- [Requesting or suggesting changes](#requesting-or-suggesting-changes)
- [Submitting pull requests](#submitting-pull-requests) 
- [Reporting bugs](#reporting-bugs)

## Introduction

This **contributing** document provides directions for suggesting or requesting changes, making pull requests, and reporting bugs in the metadata schema via GitHub. This document also outlines what contributors can expect in terms of acceptance or rejection of contributions. 

What is in this document?
 - Directions for [requesting or suggesting changes](#requesting-or-suggesting-changes)
 - Directions for [submitting pull requests](#submitting-pull-requests) for changes
 - Directions for [reporting bugs](#reporting-bugs) in the metadata schema
 - Expectations for contributions to be accepted or rejected

Who should be reading this document?
 - Data contributors
 - Data consumers
 - Anyone reporting a bug in the schema

What *isn't* in this document?
 - Process for committing changes to the schema (HCA committers **only**) can be found [here]()
 - Description of major, minor, and patch changes can be found [here]()

## Requesting or suggesting changes

**NEED TO FLIP PERSPECTIVE TO BE FROM THAT OF THE CONTRIBUTOR**

1. **Submit feedback to the HCA on metadata standard.** Anyone can suggest changes to the metadata standards via three main routes:
    - Create a [GitHub issue](https://github.com/HumanCellAtlas/metadata-schema/issues/new) on the metadata-schema GitHub repo
    - Email the HCA DCP helpdesk at data-help@humancellaltas.org
    - Make a pull request against the develop branch of the metadata-schema GitHub repo

    To request an **update to an existing schema**, you need to supply the following four pieces of information:

    1. Which schema needs to be changed?
    1. What field(s) in that schema need to be changed? What new field(s) need to be added?
    1. What should the change be?
    1. Why is the change requested?

    To request a **new module**, you need to supply the following three pieces of information:

    1. What is the proposed name of the new module?
    1. What fields should the new module contain? (See next paragraph for more details about what information is needed for each new field proposed)
    1. Why is the new module needed? Specifically, why does the current metadata schema not meet your need?
    
    To request **new field(s)**, you need to supply the following pieces of information:
    
    1. Field name (required)
    1. Field description (required)
    1. Whether the field should be optional or required (required)
    1. An example valid value for this field (optional)
    1. If this field needs a controlled vocabulary or ontology, and, if yes, what those values should be (optional)

    If you are suggesting update via a pull request, the required information should be self-evident in the JSON schema itself and the pull request message. If the required information isn't clear, then you will be asked for clarification before moving to step 3.

2. **Suggestion assigned a committer for review.** Within 2 working days, a committer will be assigned to review the suggestion. The committer will be responsible for reviewing the suggestion, seeking clarification from the proposer, and generating the appropriate updates to the metadata standard. If needed, the committer will also contact the appropriate HCA communities for additional input. 

3. **Pull request made by committer (if one doesn’t exist already).** If the feedback didn’t come in the form of the pull request, then one needs to be created. If the contributor has a GitHub account, they should be encouraged to make a pull request for their proposed change. ,If that is not possible, the committer who is handling the feedback should translate it into a JSON schema update and create the pull request. If this happens, another committer should be added to review and merge the pull request.

4. **Annotate the pull request with suitable labels and run integration tests.** The assigned reviewer should classify the suggested change by the type of change it is from a versioning perspective (patch, minor, or major) and the stability category of the module being changed (high, medium, or low). These labels can be setup in the GitHub repo so which pull requests have been flagged with which category are easy to see and filter. 

    The reviewer should also ensure the integration tests have been run. Minor and patch version changes should not cause the tests to fail. A major version change may cause test failures, especially when in a high stability module and this should help the reviewer to select the appropriate people to assist with the review.

    We aim for steps 1 to 4 to be completed less than 48 hours from the initial request being received.

5. **Notify community about the change request.** The pull request should be posted to the #hca-metadata Slack channel and the metadata-wg mailing list so everyone can have an opportunity to comment over the time frame specified by the combination of stability level and version change.

    The committer leading this effort should ensure appropriate developers from any system which could be impacted by the change are watching the thread on the pull request.

6. **Start the update acceptance process.** The assigned committer now starts the clock on the update acceptance process (see below). They should ensure the community is reminded about the proposed change at least once during the review timeframe. They also need to ensure any other assigned reviewer actively accepts the change and/or provides feedback on the change. 

7. **Accept or reject the change.** Once the review period is over, if the change is accepted into the repository, the pull request will be merged. The pull request merge should trigger automated updates to the documentation and propagation of the new schemas through the ingest system. The precise timing of the new schema version into production will depend on any software consequences for the change. Any patch or minor version change should be usable very quickly but major version changes might take longer depending on how long it takes any affected piece of software to be updated to function with the new schema.

8. **Announce accepted change to community**. The change will be announced both on #hca-metadata Slack channel and the metadata-wg mailing list by the committer. 

## Submitting pull requests
