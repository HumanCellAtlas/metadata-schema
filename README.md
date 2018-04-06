[![Build Status](https://travis-ci.org/HumanCellAtlas/metadata-schema.svg)](https://travis-ci.org/HumanCellAtlas/metadata-schema)

# The Human Cell Atlas Metadata Standards and Schema

The Human Cell Atlas metadata-schema repo contains documentation, schemas, and examples related to the HCA metadata standard.

# Table of Contents
- [Documentation](#documentation)
- [Metadata schemas and examples](#metadata-schemas-and-examples)
- [Scripts](#scripts)
- [Terminology](#terminology)
- [Community feedback](#community-feedback)

## Documentation

Most documentation is available in the `docs/` directory, including the following:

- High-level overview of the [structure](docs/structure.md) of the HCA metadata standards.
- Rationale for the [design and implementation choices](docs/rationale.md) of the HCA metadata standards.
- [Evolution principles and update process](docs/evolution.md) for the HCA metadata standards.
- Information for [how to contribute](docs/contributing.md) to the HCA metadata standards.

## Metadata schemas and examples

All metadata JSON schemas are available for browsing in the `json_schema/` directory. Schemas are also hosted at [schema.humancellatlas.org](https://schema.humancellatlas.org/a).

When required, extensions to base JSON schemas have been developed and are located in the `json_schema_extensions/` directory.

The `examples/` directory contains a number of example JSON files and spreadsheets (both filled and empty) to illustrate how the HCA metadata standards are implemented.

## Scripts

Any scripts - *e.g.* those required for automatic testing, derivation of template spreadsheets - are located in the `src/` directory.

## Terminology

**Metadata** are the collections of descriptive information needed to understand the data supported by the HCA. Metadata is collected for entities such as, but not limited to, assay content (*e.g.* fastq and tif files), analysis results (*e.g.* expression matrices), and biological samples (*e.g.* biopsy or autopsy samples). This descriptive information will be provided to the community in a structured format defined by the HCA metadata schemas.

**Schemas** are file-based specification for the metadata. The specification defines the metadata structure and fields, including field name, description, format, and cardinality. This specification is likely to have a hierarchical structure (e.g. objects and subobjects containing fields). In principle we could have either a single schema document or individual schema documents per module. In practice, we are mostly like to use individual schema documents. 

**Modules** are schema objects that contains a specific subset of metadata fields associated with an isolated aspect of the metadata. A module schema would be one that is needed for some, but not all, data sets. Examples where this is appropriate include fields specific to a human donor, a particular single cell RNA-Seq platform like SmartSeq2, or a particular imaging experiment like MERFISH. We acknowledge the design must balance the flexibility offered by these modules with the overhead of maintaining a large number modules. We should only seek additional modules where there is a true requirement for them due experimental specialisation and not for convenience sake.

**Contributors** are any members of the HCA or scientific community who suggest, contribute, or review updates to the metadata schemas.

**MWG members** are any persons who are a member of the Metadata Working Group.

**Committers** are any persons with commit privileges to the metadata-schema GitHub repo. All committers are also members of the MWG.

**Submitters** are any persons who submit data or metadata to the HCA.

## Community feedback

Follow our community discussion of HCA metadata by joining the #hca-metadata channel on the [HCA Slack group](http://join-slack.humancellatlas.org/).

If you have any questions or concerns, you are welcome to create GitHub issues or email our helpdesk at data-help@humancellatlas.org. 
 