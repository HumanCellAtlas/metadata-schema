# The Human Cell Atlas: Metadata Design and Implementation Choices

# This doc is high priority and needs work!!

This document outlines rationales for the design and implementation choices for the HCA metadata standards.

## Table of Contents
- [Design choices](#design-choices)
- [Implementation choices](#dimplementation-choices)

What is in this document?

Who should be reading this document?

What *isn't* in this document?
- [Hierarchy of entities (core, type, module)]()


 
## Implementation choices

A detailed specification for the structure of the schema documents can be found in [this document](https://docs.google.com/document/d/1pxQj7BfM8HHgD4ilm4dlvZuZATfJkNC5s_-TUoA4lYA/edit?usp=sharing). The design principles that this structure follows are:

### Modular schema components

Metadata fields should be organized into `modules`, each with a piece of schema, including a `core` schema, containing the minimal schema necessary for all possible data and analyses, and a collection of additional `modules` that can be mixed and matched for each particular dataset or analysis. In this design, each schema module has its own independent version and lifecycle (as described below), and any particular dataset is defined by a collection of the appropriate modules.

It is worth noting the basis for defining a collection of fields and objects in a particular module can be considered along two different axises; do the fields/objects make sense together from a scientific point of view, e.g they are all fields associated with the same assay or sample type like Drop-Seq or a Brain section; and do the fields have the same stability requirement e.g changing a field will result in software update requirements for either ingest or pipelines or not. Fields which belong together scientifically and have broadly the same stability level should be grouped together in a single module.

### Machine readable

All metadata, metadata schema, and metadata conformance are specified in machine-readable, well-specified, web-accessible, and versioned file formats.

### Self-describing metadata

All metadata files are self-describing, ie, explicitly indicate the schema and schema version which they manifest. Ideally, this is done using a URL so that any metadata consumer can trivially fetch all schema associated with a metadata file.

### Flat metadata instantiation

Metadata files, containing metadata elements from multiple schema, are flattened into single files for storage or transmission (*e.g.* project.json). The actual contents of a given metadata file are subject to conformance specifications, which indicate the module schema and version that the metadata must conform to.

### Schema language

Schema are a superset of JSON schema and JSON schema validation (json-schema.org) with all extensions declarative in nature (*i.e.* no code is required to specify a schema). Extensions to the native JSON schema validation will be needed to support validation of ontology identifiers or other specific HCA requirements. 

## Design choices

The HCA metadata standards are developed and updated in a transparent and open manner to ensure that the whole community can participate in the process. The following principles will be adhered to for the update process.

### Agility

The HCA foresees active development of sample handling, assays, and analyses, and will include both stable and rapidly evolving methods. As such, the metadata schema needs to be able to adapt accordingly, with regular updates (*e.g.* weekly or monthly), and a process for managing and tracking schema and data versions.

### Modularity

As the metadata evolves, different components will likely evolve at different rates than others. For example, the specification of contact info may never change, whereas entirely new objects will be required when a new experimental technology is invented. A modular design will ensure that different components of the metadata can flexibly and independently evolve. 

### Flexibility

Significant experimental diversity is expected. Our methods for iterating metadata must allow for both the flexible capture of new data variants (e.g. new experimental assays), as well as the subsequent easy adoption of new schema as methods reach common usage. Any data contributor should always be able to add arbitrary additional fields to the metadata objects without causing process failure.

### Separation of (metadata) concerns

It must be possible to separate different concerns related to metadata. For example, the metadata validation process should be driven by the schema, and depend only on having access to the schema, not the particular content of the schema or its semantics. Similarly, it should be possible to store the metadata on disk without understanding its syntax or semantics.

## Recording the standards

The schema will be stored as a series of individual documents which are related to entities and modules associated with them *e.g* project.json, biomaterial.json, sequencing_process.json. These documents are stored in a single versioned control GitHub repository alongside documentation about the schema, the meaning of their contents, and the update process. Using GitHub, anyone will be able to propose changes to the schema through pull requests. Only a specified list of committers will be allowed to approve pull requests and issue new versions of the metadata standards.

### Specifying version info

Each schema is self-describing using the `id` field with a URL to the location of the version of the current document. 

Version indicated in schema URL: `https://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core`

As we are requiring instance data to also be self describing, all *Type* entities will require a property called `describedBy`. 

For `donor_organism.json` schema, these fields will look like: 

``` 
"$schema": "http://json-schema.org/draft-04/schema#"
"id": "https://schema.humancellatlas.org/type/biomaterial/5.0.0/donor_organism"
"additionalProperties": false,
"properties" : {
    "describedBy": {
        "description": "The URL reference to the schema.",
        "type": "string",
        "pattern": "https://schema.humancellatlas.org/type/biomaterial/[0-9]{1,}.[0-9]{1,}.[0-9]{1,}/donor_organism"
    },
    ...
}
```
