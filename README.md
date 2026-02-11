[![Schema Linting and Tests](https://github.com/HumanCellAtlas/metadata-schema/actions/workflows/schema-tests.yml/badge.svg)](https://github.com/HumanCellAtlas/metadata-schema/actions/workflows/schema-tests.yml)

# The Human Cell Atlas: Metadata Standards

The Human Cell Atlas metadata-schema repo contains the schema specifications and supporting documentation for the HCA metadata standards.

## Table of Contents
- [Documentation](#documentation)
- [Metadata schemas and examples](#metadata-schemas-and-examples)
- [Contributing](#contributing)
- [Terminology](#terminology)
- [Scripts](#scripts)

## Documentation

Documentation supporting the metadata standard is available in the `docs/` directory. Specific topics covered include:

- Information on [how to contribute](docs/contributing.md) to the HCA metadata standards.
- Overview of the [structure](docs/structure.md) of the HCA metadata standards.
- [Evolution and update principles](docs/evolution.md) for the HCA metadata standards.
- Rationale for the [design and implementation choices](docs/rationale.md) for the HCA metadata standards.

## Metadata schemas and examples

Metadata JSON schemas are located in the `json_schema/` directory. Schemas are also hosted at [schema.humancellatlas.org](https://schema.humancellatlas.org/a).

When required, extensions to base JSON schemas have been developed and are located in the `json_schema_extensions/` directory.

The `examples/` directory contains example JSON files and spreadsheets to illustrate how the HCA metadata standards are implemented.

## Contributing

The HCA is committed to building and evolving the metadata standards based on the needs of the scientific community. Everyone is welcome to suggest updates or additions to the HCA metadata standards by [creating GitHub issues](https://github.com/HumanCellAtlas/metadata-schema/issues/new) or emailing [data-help@humancellaltas.org](data-help@humancellaltas.org). More details on [how to contribute](docs/contributing.md) to the HCA metadata standards are available. 

Follow our community discussion of HCA metadata by joining the #hca-metadata channel on the [HCA Slack group](http://join-slack.humancellatlas.org/).

## Terminology

**Metadata** are the collections of descriptive information needed to understand the data supported by the HCA. Metadata is collected for entities such as, but not limited to, assays (*e.g.* fastq and tif files), analysis results (*e.g.* expression matrices), and biological samples (*e.g.* biopsy or autopsy samples). This descriptive information will be provided to the community in a structured format defined by the HCA metadata schemas.

**Schemas** are file-based specifications for the HCA metadata. The specification defines the metadata structure and fields, including field name, description, format, and ontology (where appropriate). This specification is likely to have a hierarchical structure (*e.g.* objects and sub-objects containing fields). In practice, individual JSON schemas are defined for specific entities. More details on the hierarchy of HCA metadata schemas can be found in the [structure](docs/structure.md) document. 

**Modules** are schema objects that contains a specific subset of metadata fields associated with an isolated aspect of the metadata. A module schema would be one that is needed for some, but not all, data sets. Examples where this is appropriate include fields specific to a human donor, a particular single cell RNA-Seq platform like SmartSeq2, or a particular imaging experiment like MERFISH. We acknowledge the design must balance the flexibility offered by these modules with the overhead of maintaining a large number modules. We aim to only include additional modules where there is a true requirement for them due to experimental specialisation and not for convenience's sake.

**Contributors** are any members of the HCA or scientific community who suggest, contribute, or review updates to the metadata schemas.

**Submitters** are any members of the HCA or scientific community who submit data or metadata to the HCA.

**Committers** are any members of the HCA Data Coordination Platform (DCP) with commit privileges to the metadata-schema GitHub repo.

## Scripts

Any scripts - *e.g.* those required for automatic testing, generation of template spreadsheets - are located in the `src/` directory.

### Install the pre-commit hook

- Installation: `pip install pre-commit`

- Every time you clone the project: `pre-commit install`