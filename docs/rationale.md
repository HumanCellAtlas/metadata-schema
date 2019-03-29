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

### Modular schemas

Metadata fields are organized into biologically-meaningful *type* schemas, for example a cell suspension schema or an enrichment protocol schema. Each type schema inherits a  core schema, containing the minimal fields necessary for that type, and any relevant modules that customize the schema for a particular dataset or analysis. Using this modular design, each schema has its own independent version (as described below), and any particular dataset is defined by a collection of appropriate schemas.

The basis for defining a collection of fields and objects in a particular schema can be considered along two axes: 
 1. The fields/objects relate to each other from a scientific point of view. *e.g.* they describe the same assay or sample type like Drop-Seq or a brain section.
 1. The fields/objects have the same stability requirement. *e.g.* adding a new set of fields will not require any DCP software updates. 
 
 Fields which relate scientifically and have similar stability level should be grouped together in a schema.

### Machine-readable formats

All metadata standards, metadata schema, and metadata conformance are described in machine-readable, well-specified, web-accessible, and versioned file formats.

### Self-describing metadata

All metadata documents are self-describing, *i.e.*, explicitly indicate the schema name and version which they manifest. Currently, the schema name and version is declared in the `describedBy` field using a URL. This approach allows a metadata consumer to fetch the schema associated with a metadata document.

### Flat metadata instantiation

A metadata document, which contains metadata elements from one or more schemas, is flattened into a single file for storage and transmission. The contents of a metadata document are subject to conformance specifications, which indicate the schema name and version to which the metadata must conform.

### Schema language

Schema are a superset of JSON schema and JSON schema validation (json-schema.org) with all extensions declarative in nature (*i.e.* no code is required to specify a schema). Extensions to the native JSON schema validation will be needed to support validation of ontology identifiers or other specific HCA requirements. 

## Design choices

The HCA metadata standard is developed in a transparent and open manner so that the whole HCA community can participate in the process. The following design principles serve as a foundation for the metadata standard in order to ensure it meets the needs of HCA data contributors and consumers.

### Agile

The HCA foresees active development of sample handling techniques, new experimental assays, and new data processing and analysis approaches in the field of cellular resolution biology. As such, the metadata standard needs to be able to adapt accordingly, with regular updates and a process for managing and tracking schema versions. By designing with this principle in mind, data requiring updates to the metadata standard can quickly be submitted to the HCA and made available to consumers.

### Flexible

Significant experimental diversity among HCA datasets is expected. The metadata standard must be flexible to support current as well as future predicted and unknown data types. This means that the same metadata standard should be able to describe data from plate-based single cell sequencing of organoids as well as RNAScope in situ hybridization experiments of preserved primary tissue samples. We anticipate that the HCA will expand to support other data modalities including controlled access data, model organism data, data from disease cohorts, proteomic, metabolomics, genomic, and metagenomic data, and possibly data from genetically engineered biological samples. By designing with the principle of flexibility in mind, the HCA metadata standard will be prepared to support all future data.

### Self-describing

To ensure those relying on the metadata standard are able to keep up with potentially rapid changes, the metadata standard is designed to be self-describing. The standard is stored as a series of individual JSON schemas which represent the entities and fields associated with them. These schemas contain all the information required to understand and interpret the metadata. Including field attributes such as a description and a user-facing, friendly term means one needs only to inspect the schema to be able to produce a variety of projections based on user requirements. The specifications for what metadata schemas must contain are fully described in the [HCA Metadata Schema Style and Formatting Guide](schema_style_guide.md).

Some fields in the metadata standard accept a controlled set of vocabulary terms organized and structured in an ontology. For such fields, the metadata standard explicitly identifies the relevant ontology or a subset of the ontology that expresses valid values for that field. Metadata schemas also contain the requirements for validation of metadata documents against the standard. Each schema explicitly states which metadata fields are required, the JSON specification the schema adheres to, and that no custom or additional properties are allowed.
