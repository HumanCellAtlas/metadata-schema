# The Human Cell Atlas: Metadata Design and Implementation Choices

## Table of Contents
- [Introduction](#introduction)
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
 
## Implementation choices

A detailed specification for the structure of the schema documents can be found in [this document](https://docs.google.com/document/d/1pxQj7BfM8HHgD4ilm4dlvZuZATfJkNC5s_-TUoA4lYA/edit?usp=sharing). It is concerned with the detailed format and syntax of the metadata schema and their instantiation, including schema referencing, manifestation as files, composition, modular design, and other details of the format and syntax. The design principles that this structure follows are:

### Modular schema components

Metadata fields are organized into biologically-meaningful *type* schemas, for example a cell suspension schema or an enrichment protocol schema. Each type schema inherits a  core schema, containing the minimal fields necessary for that type, and any relevant modules that customize the schema for a particular dataset or analysis. Using this modular design, each schema has its own independent version (as described below), and any particular dataset is defined by a collection of appropriate schemas.

The basis for defining a collection of fields and objects in a particular schema can be considered along two axes: 
 1. The fields/objects relate to each other from a scientific point of view. *e.g.* they describe the same assay or sample type like Drop-Seq or a brain section.
 1. The fields/objects have the same stability requirement. *e.g.* adding a new set of fields will not require any DCP software updates. 
 
 Fields which relate scientifically and have similar stability level should be grouped together in a schema.

### Machine readable

All metadata, metadata schema, and metadata conformance are described in machine-readable, well-specified, web-accessible, and versioned file formats.

### Self-describing metadata

All metadata files are self-describing, *i.e.*, explicitly indicate the schema and schema version which they manifest. Ideally, this is done by using a URL so that any metadata consumer can trivially fetch all schema associated with a metadata file.

### Flat metadata instantiation

Metadata files, containing metadata elements from multiple schema, are flattened into single files for storage or transmission (*e.g.*, project.json). The actual contents of a given metadata file are subject to conformance specifications, which indicate the module schema and version that the metadata must conform to.

### Schema language

Schema are a superset of JSON schema and JSON schema validation (json-schema.org) with all extensions declarative in nature (*i.e.*,  no code is required to specify a schema). Extensions to the native JSON schema validation will be needed to support validation of ontology identifiers or other specific HCA requirements. 

## Design choices

The HCA metadata standards are developed and updated in a transparent and open manner to ensure that the whole community can participate in the process. The following principles will be adhered to for the update process.

### Agility

The HCA foresees active development of sample handling, assays, and analyses, and will include both stable and rapidly evolving methods. As such, the metadata schema needs to be able to adapt accordingly, with regular updates (*e.g.*, weekly or monthly), and a process for managing and tracking schema and data versions.

### Modularity

As the metadata evolves, different components will likely evolve at different rates than others. For example, the specification of contact info may never change, whereas entirely new objects will be required when a new experimental technology is invented. A modular design will ensure that different components of the metadata can evolve flexibly and independently. 

### Flexibility

Significant experimental diversity is expected. Our methods for iterating metadata must allow for both the flexible capture of new data variants (*e.g.*, new experimental assays), as well as the subsequent easy adoption of new schema as methods reach common usage. Any data contributor should always be able to add arbitrary additional fields to the metadata objects without causing process failure.

### Separation of (metadata) concerns

It must be possible to separate different concerns related to metadata. For example, the metadata validation process should be driven by the schema, and depend only on having access to the schema, not the particular content of the schema or its semantics. Similarly, it should be possible to store the metadata on disk without understanding its syntax or semantics.
