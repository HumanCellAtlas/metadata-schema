# The Human Cell Atlas: Metadata Design and Implementation Choices

## Table of Contents
- [Introduction](#introduction)
- [Definitions](#definitions)
- [Implementation choices](#implementation-choices)
- [Design choices](#design-choices)

## Introduction

This document describes the rationale behind certain implementation and design choices for how the metadata standard is developed and maintained.

**What is in this document?**
- Rationale for how the HCA metadata standard is designed and implemented

**Who should be reading this document?**
 - Data contributors
 - Data consumers
 - Members of external projects seeking alignment with HCA metadata standards

**What *isn't* in this document?**
- The [structure of the metadata standards](structure.md) based on the design and implementation choices
 
## Definitions

**metadata document**  A file containing metadata according to the specification.
**metadata schema**  A file containing the specification for metadata. Currently, this specification is in JSON format.

## Implementation choices

A detailed specification for the structure of the schema documents can be found in [this document](https://docs.google.com/document/d/1pxQj7BfM8HHgD4ilm4dlvZuZATfJkNC5s_-TUoA4lYA/edit?usp=sharing). It is concerned with the detailed format and syntax of the metadata schema and their instantiation, including schema referencing, manifestation as files, composition, modular design, and other details of the format and syntax. The design principles that this structure follows are:

### Modular schema components

Metadata fields are organized into biologically-meaningful *type* schemas, for example a cell suspension schema or an enrichment protocol schema. Each type schema inherits a  core schema, containing the minimal fields necessary for that type, and any relevant modules that customize the schema for a particular dataset or analysis. Using this modular design, each schema has its own independent version (as described below), and any particular dataset is defined by a collection of appropriate schemas.

The basis for defining a collection of fields and objects in a particular schema can be considered along two axes: 
 1. The fields/objects relate to each other from a scientific point of view. *e.g.* they describe the same assay or sample type like Drop-Seq or a brain section.
 1. The fields/objects have the same stability requirement. *e.g.* adding a new set of fields will not require any DCP software updates. 
 
 Fields which relate scientifically and have similar stability level should be grouped together in a schema.

### Machine readable

All metadata standards, metadata schema, and metadata conformance are described in machine-readable, well-specified, web-accessible, and versioned file formats.

### Self-describing metadata

All metadata documents are self-describing, *i.e.*, explicitly indicate the schema name and version which they manifest. Currently, the schema name and version is declared in the `describedBy` field using a URL. This approach allows a metadata consumer to fetch the schema associated with a metadata document.

### Flat metadata instantiation

A metadata document, which contains metadata elements from one or more schemas, is flattened into a single file for storage and transmission. The contents of a metadata document are subject to conformance specifications, which indicate the schema name and version to which the metadata must conform.

### Schema language

Schema are a superset of JSON schema and JSON schema validation (json-schema.org) with all extensions declarative in nature (*i.e.* no code is required to specify a schema). Extensions to the native JSON schema validation will be needed to support validation of ontology identifiers or other specific HCA requirements. 

## Design choices

The HCA metadata standards are developed and updated in a transparent and open manner to ensure that the whole HCA community can participate in the process. The following principles will be adhered to for the update process.

### Agility

The HCA foresees active development of sample handling, assays, and analyses, and will include both stable and rapidly evolving methods. As such, the metadata standard needs to be able to adapt accordingly, with regular updates and a process for managing and tracking schema versions.

### Modularity

As the metadata standard evolves, different schemas will likely evolve at different rates. For example, the specification of contact info may never change, whereas entirely new schemas might be required when a new experimental technology is invented. A modular design will ensure that different components of the metadata standard can evolve independently. 

### Flexibility

Significant experimental diversity among HCA datasets is expected. The metadata evolution process must be flexible to allow for submission of new data types and subsequent easy adoption of new schema/fields as methods reach common usage. Data contributors should be able to request new metadata fields to describe their datasets without causing process failure.

### Separation of (metadata) concerns

It must be possible to separate different concerns related to metadata. For example, the metadata validation process should be driven by the schema, and depend only on having access to the schema, not the particular content of the schema or its semantics. Similarly, it should be possible to store the metadata on disk without understanding its syntax or semantics.
