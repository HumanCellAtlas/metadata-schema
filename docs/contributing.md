# The Human Cell Atlas: Metadata Update Process

## Table of Contents
- [Introduction](#introduction)
- [Requesting or suggesting changes](#requesting-or-suggesting-changes-to-the-metadata-schema)
- [Example request for schema change](#example-request-for-schema-change)
- [Reporting bugs](#reporting-bugs)

## Introduction

This document describes how you can contribute to the development of the HCA metadata standard by suggesting or requesting changes to and reporting bugs in the metadata schema via GitHub or email. This document also covers our rationale for acceptance or rejection of suggestions.

**What is in this document?**
 - Directions for [requesting or suggesting changes](#requesting-or-suggesting-changes-to-the-metadata-schema) to the metadata schema
 - Directions for [reporting bugs](#reporting-bugs) in the metadata schema
 - Expectations for suggestions to be accepted or rejected

**Who should be reading this document?**
 - Data contributors
 - Data consumers
 - Anyone reporting a bug in the schema

**What *isn't* in this document?**
- Information about contributing **data** to the HCA. This information can be found on the HCA DCP website
- Directions for committing changes to this repo, which is currently restricted to a core group of committers for this repo
- Description of what defines [major, minor, and patch changes](metadata-schema/docs/evolution.md#schema-versioning) to the metadata schema
- Directions for [submitting pull requests](metadata-schema/docs/committers.md) for changes

## Requesting or suggesting changes to the metadata schema

As a prerequisite to this section, you may want to look at [how the metadata is structured](metadata-schema/docs/structure.md)

1. **Gather information** requested for submitting feedback. There are two main types of suggestions: (1) **updates** to existing schemas and (2) addition of **new** schema(s).

    1. To request an **update** to an existing schema, please supply the following pieces of information:

        1. Which schema would you like to be changed?
        1. What field(s) in that schema would you like to be changed, and what should the change be?
        1. What new field(s) need to be added?
            - Details for requesting **new field(s)** outlined below
        1. Why is the change needed?

    1. To request a **new** schema, you need to supply the following pieces of information:

        1. What is the proposed name of the new schema?
        1. What field(s) should the new schema contain?
            - Details for requesting **new field(s)** outlined below
        1. Why is the new schema needed? Specifically, why does the current metadata standard not meet your need?
    
    For **each new field** requested, please supply the following pieces of information:
    
    1. Field name (required)
    1. Field description (required)
    1. Whether the field should be optional or required (required)
    1. An example valid value for this field (optional)
    1. If this field needs a controlled vocabulary or ontology. If yes, what those values should be or which ontology should be followed (optional)
    
1. **Submit request on the HCA metadata standard.** Anyone can suggest/request changes to the metadata standards via three main routes:

    1. Create a [GitHub issue](https://github.com/HumanCellAtlas/metadata-schema/issues/new) on the metadata-schema repo
    1. Email the HCA DCP helpdesk at [data-help@humancellaltas.org](data-help@humancellaltas.org)
    1. Make a pull request against the develop branch of the metadata-schema repo (only recommended for users with familiarity with GitHub)
    
    Whichever method is chosen, the information indicated in Step 1 is requested to be submitted.

1. **Track progress of request.** Within 2 working days, your request will be reviewed by an HCA DCP member. You may be asked for clarification on your request, and additional input may be sough from the appropriate HCA communities.

1. **Review and comment on proposed update.** A proposed schema update to address to your request will be developed by an HCA DCP member and then posted to the #hca-metadata Slack channel and on GitHub. Making the proposed update public allows everyone the opportunity to comment or raise concerns. The amount of time an update remains public for comments depends on the severity of the change. These timeframes can be found [here](metadata-schema/docs/committers.md#schema-update-acceptance-process).

1.  **Notification of acceptance.** Once the review period is over and the update is accepted, the changes will be merged into the metadata standard on your behalf. The update will be announced both on #hca-metadata Slack channel and the metadata-wg mailing list. You can join the HCA slack community follow these [instructions.](https://github.com/HumanCellAtlas/wiki/wiki)

## Example request for schema change

Example **update** request for two **new field(s)**:

1. *Which schema needs to be changed?* I would like to request a change to the project_core schema.

1. *What field(s) in that schema would you like to be changed, and what should the change be?* I am not requesting field changes, only new fields.
1. *What new field(s) need to be added?* I would like to request the addition of a 2 new fields to capture information about the funder or grant supporting the project.

    New field 1\
    i. Funder\
    ii. The name of the funding agency that awarded the grant.\
    iii. Not required\
    vi. NSF\
    v. Should be a controlled vocabulary

    New field 2\
    i. Grant ID\
    ii. The identifier of the grant funding the project.\
    iii. Not required\
    vi. 0903629\
    v. Not CV or ontology at this time, free text is fine.

1. *Why is the change needed?* This change is being requested to help HCA funders track and understand specifically what data they have supported. Ideally, a funder would be able to browse or identify exactly which data they have supported and also the specific grant/program that the data came out of. It will be critical to rationalizing funding and also a metric that funders can track to evaluate impact/effectiveness of specific programs.


## Reporting bugs

Report all bugs and issues (schema-related or other) by creating a [new GitHub issue](https://github.com/HumanCellAtlas/metadata-schema/issues/new) in this repo. Please add the "bug" label to the issue and summarize the expected behavior, actual behavior, and steps to reproduce the bug. Specific instructions can be found in GitHub when a new issue is raise, but briefly please report:

1. On which version of the code did the bug occur? (git hash, date, branch, be specific)
1. Expected behavior
1. Actual behavior
1. Steps to reproduce the behavior
