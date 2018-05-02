# The Human Cell Atlas: Metadata Update Process

## Table of Contents
- [Introduction](#introduction)
- [Requesting or suggesting changes](#requesting-or-suggesting-changes)
- [Reporting bugs](#reporting-bugs)

## Introduction

This document will describe how you can contribute by suggesting or requesting changes, making pull requests, and reporting bugs in the metadata schema via GitHub. This document also covers our rationale for acceptance or rejection of your suggestions.

What is in this document?
 - Directions for [requesting or suggesting changes](#requesting-or-suggesting-changes-to-the-metadata-schema)
 - Directions for [submitting pull requests](#submitting-pull-requests) for changes
 - Directions for [reporting bugs](#reporting-bugs) in the metadata schema
 - Expectations for contributions to be accepted or rejected

Who should be reading this document?
 - Data contributors
 - Data consumers
 - Anyone reporting a bug in the schema

What *isn't* in this document?
- Any information about contributing data to the HCA. This document is about contributing to the metadata schema.
- Automated process for committing changes to the schema. Currently this must be done via a HCA wrangler with commit privilages.
- [Description of major, minor, and patch changes.](https://github.com/HumanCellAtlas/metadata-schema/blob/mg-updade-docs/docs/evolution.md#schema-versioning)

## Requesting or suggesting changes to the metadata schema

As a prerequisite to this section you may want to look at [how the metadata is structured](metadata-schema/docs/structure.md)

1. **Submit feedback to the HCA on metadata standard.** Anyone can suggest changes to the metadata standards via three main routes:
    - Create a [GitHub issue](https://github.com/HumanCellAtlas/metadata-schema/issues/new) on the metadata-schema GitHub repo
    - Email the HCA DCP helpdesk at data-help@humancellaltas.org
    - Make a pull request against the develop branch of the metadata-schema GitHub repo (only recommended for users with prior familiarity with GitHub)

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

2. **Review of your suggestion.** Within 2 working days, we will review your suggestion. We may seek clarification from you or the appropriate HCA communities for additional input.

3. **Review and comments from the community** Your metadata request will be posted to the #hca-metadata Slack channel and the metadata-wg mailing list so everyone can have an opportunity to comment over a time frame that matches the severity of the change.

4.  **Implementing the change** Once the review period is over, if the change is accepted into the repository, we will generate appropriate updates to the metadata standard on your behalf. Details about how and when changes are accepted can be found [here](https://github.com/HumanCellAtlas/metadata-schema/blob/mg-updade-docs/docs/committers.md#schema-update-acceptance-process).

5.  **Notification to the community** The change will be announced both on #hca-metadata Slack channel and the metadata-wg mailing list by the committer. You can [join the HCA slack community follow these instructions.](https://github.com/HumanCellAtlas/wiki/wiki)


## Reporting bugs

[Report all bugs and issues by creating a new issue in this repo.](https://github.com/HumanCellAtlas/metadata-schema/issues/new)
