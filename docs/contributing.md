# The Human Cell Atlas: Metadata Update Process

## Table of Contents
- [Introduction](#introduction)
- [Requesting or suggesting changes](#requesting-or-suggesting-changes-to-the-metadata-schema)
- [Example request for update to schema](#example-request-for-update-to-schema)
- [Reporting bugs](#reporting-bugs)

## Introduction

This document describes how you can contribute to the development of the HCA metadata standard by suggesting or requesting changes to and reporting bugs in the metadata schema via GitHub or email. This document also covers our rationale for acceptance or rejection of suggestions.

**What is in this document?**
 - Directions for requesting or suggesting changes to the metadata schema
 - Directions for reporting bugs in the metadata schema

**Who should be reading this document?**
 - Data contributors
 - Data consumers
 - Anyone reporting a bug in the schema

**What *isn't* in this document?**
- Information about contributing **data** to the HCA. This information can be found on the HCA Data Portal
- Directions for committing changes to this repo, which is currently restricted to a core group of Committers
- Description of what defines [major, minor, and patch changes](evolution.md#schema-versioning) to the metadata schema
- Directions for submitting pull requests for changes

## Requesting or suggesting changes to the metadata schema

As a prerequisite to this section, you may want to look at [how the metadata is structured](structure.md).

1. **Gather information** requested for submitting feedback. There are two main types of suggestions: (1) **updates** to existing schemas and (2) addition of **new** schema(s).

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
    
1. **Submit request** for update to the HCA metadata standard. Anyone can suggest/request changes to the metadata standards via three main routes:

    1. Create a GitHub issue on the metadata-schema repo for either [updates](https://github.com/HumanCellAtlas/metadata-schema/issues/new?template=schema_update.md) or [new schemas](https://github.com/HumanCellAtlas/metadata-schema/issues/new?template=new_schema.md). Please add the "content" label to the issue.
    1. Email the HCA DCP helpdesk at [data-help@humancellaltas.org](mailto:data-help@humancellaltas.org)
    1. Make a pull request against the develop branch of the metadata-schema repo (recommended for users familiar with GitHub)
    
    Whichever method is chosen, the information indicated in Step 1 is requested to be submitted.

1. **Track progress of request.** Within 2 working days, your request will be reviewed by an HCA DCP member. You may be asked for clarification on your request, and additional input may be sought from the appropriate HCA communities.

1. **Review and comment on proposed update.** A proposed schema update to address to your request will be made by an HCA DCP member and then posted to the #hca-metadata and #dcp Slack channels and on GitHub. Making the proposed update public allows everyone the opportunity to comment or raise concerns. The amount of time an update remains public for comments depends on the severity of the change and can be found [here](committers.md#schema-update-acceptance-process).

1.  **Notification of acceptance.** Once the review period is over and the update is accepted, the changes will be merged into the metadata standard on your behalf. You can join the HCA Slack community by following these [instructions.](https://github.com/HumanCellAtlas/wiki/wiki)

## Example request for update to schema

**For which schema is a change/update being suggested?**

I would like to request an update the the `cell_line.json` schema.

**What should the change/update be?**

I would like to add a new field - `random_integer` - to this schema to allow data contributors to assign a random integer to the cell line.

**What new field(s) need to be changed/added?**

* Field name: random_integer
* Field description: Any random integer.
* Required: no
* Example: 42
* CV or enum: no

**Why is the change requested?**

Some scientists need to be able to assign a random integer to a cell line in order to keep track of it.

## Reporting bugs

Report any bugs (schema-related or other) by creating a [GitHub issue](https://github.com/HumanCellAtlas/metadata-schema/issues/new?template=bug_report.md) using the provided template. Please add the "bug" label to the issue. Briefly, the following information should be reported for all bugs:

**Give the bug a title**

*Please give the bug a title that includes a short description.*

Typo in description for `publication.title` field.

**To reproduce**

*Please explain as much as you can about what you were doing when the bug was observed (to help us reproduce the error for testing).*

Steps to reproduce the behavior:
1. Go to `publication.json` schema on develop branch
1. Observe typo in description for `title` field

**Schema version(s)**

*Please list any schema versions related to this bug.*
 
`publication.json`: 6.0.1

**Observed behavior**

*Please explain what you observed.*

The description says "Title of *publicatoin*".

**Expected behavior**

*Please explain what you expect to happen.*
 
I expect the description to say "Title of publication".

**Screenshots or Messages**

*If applicable, add screenshots to help explain your problem or the text of any error messages.*
