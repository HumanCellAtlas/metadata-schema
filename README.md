[![Build Status](https://travis-ci.org/HumanCellAtlas/metadata-schema.svg)](https://travis-ci.org/HumanCellAtlas/metadata-schema)

# The Human Cell Atlas Metadata Standards

The Human Cell Atlas metadata-schema repo contains the schema specifications and supporting documentation for the HCA metadata standards.

## Table of Contents
- [Documentation](#documentation)
- [Metadata schemas and examples](#metadata-schemas-and-examples)
- [Terminology](#terminology)
- [Scripts](#scripts)
- [Community feedback](#community-feedback)

## Documentation

Documentation supporting the metadata standard is available in the `docs/` directory. Specific topics covered include:

- High-level overview of the [structure](docs/structure.md) of the HCA metadata standards.
- Rationale for the [design and implementation choices](docs/rationale.md) for the HCA metadata standards.
- [Evolution and update principles](docs/evolution.md) for the HCA metadata standards.
- Information for [how to contribute](docs/contributing.md) to the HCA metadata standards.

## Metadata schemas and examples

Metadata JSON schemas are located in the `json_schema/` directory. Schemas are also hosted at [schema.humancellatlas.org](https://schema.humancellatlas.org/a).

When required, extensions to base JSON schemas have been developed and are located in the `json_schema_extensions/` directory.

The `examples/` directory contains example JSON files and spreadsheets to illustrate how the HCA metadata standards are implemented.

## Terminology

**Metadata** are the collections of descriptive information needed to understand the data supported by the HCA. Metadata is collected for entities such as, but not limited to, assays (*e.g.* fastq and tif files), analysis results (*e.g.* expression matrices), and biological samples (*e.g.* biopsy or autopsy samples). This descriptive information will be provided to the community in a structured format defined by the HCA metadata schemas.

**Schemas** are file-based specifications for the HCA metadata. The specification defines the metadata structure and fields, including field name, description, format, and ontology (where appropriate). This specification is likely to have a hierarchical structure (*e.g.* objects and sub-objects containing fields). In practice, individual JSON schemas are defined for specific entities. More details on the hierarchy of HCA metadata schemas can be found in the [structure](docs/structure.md) document. 

**Modules** are schema objects that contains a specific subset of metadata fields associated with an isolated aspect of the metadata. A module schema would be one that is needed for some, but not all, data sets. Examples where this is appropriate include fields specific to a human donor, a particular single cell RNA-Seq platform like SmartSeq2, or a particular imaging experiment like MERFISH. We acknowledge the design must balance the flexibility offered by these modules with the overhead of maintaining a large number modules. We aim to only include additional modules where there is a true requirement for them due to experimental specialisation and not for convenience's sake.

**Contributors** are any members of the HCA or scientific community who suggest, contribute, or review updates to the metadata schemas.

**Submitters** are any members of the HCA or scientific community who submit data or metadata to the HCA.

**Committers** are any members of the HCA Data Coordination Platform (DCP) with commit privileges to the metadata-schema GitHub repo. All committers are also members of the MWG.

**MWG members** are any persons who are a member of the Metadata Working Group.

## Scripts

Any scripts - *e.g.* those required for automatic testing, generation of template spreadsheets - are located in the `src/` directory.

## Community feedback

Follow our community discussion of HCA metadata by joining the #hca-metadata channel on the [HCA Slack group](http://join-slack.humancellatlas.org/).

If you have any questions or concerns, please create GitHub issues or email our helpdesk at data-help@humancellatlas.org. 
 