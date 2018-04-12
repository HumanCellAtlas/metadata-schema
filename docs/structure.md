# The Human Cell Atlas: Overview of Metadata Structure

## Table of Contents
- [Introduction](#introduction)
- [Overview of the metadata structure](#structure-overview)
- [Specification of the metadata structure](#specification-of-schema-structure-and-content)
- [Principles](#principles)
- [Recording the standards](#recording-the-standards)

## Introduction

This **structure** document describes the structure of the HCA metadata standards. More detailed specification of the format and syntax of the metadata schemas and their instantiation can be found in the [metadata schema structure specification](https://docs.google.com/document/d/1pxQj7BfM8HHgD4ilm4dlvZuZATfJkNC5s_-TUoA4lYA/edit?ts=59b16455) on Google Drive.

What is in this document?
 - High-level [overview of the schema structure](#structure-overview)
 - More detailed [specification of the schema structure](#specification-of-schema-structure-and-content)
 - The set of [principles](#principles) specifically guiding the schema structure design
 - Description of the [physical instatiation](#recording-the-standards) of the metadata standards

Who should be reading this document?
 - Data contributors
 - Data consumers
 - Members of external projects seeking alignment with HCA metadata standards

What *isn't* in this document?
 - Something blah blah blah
 
## Structure overview

### Motivation

The primary motivations behind the HCA metadata entity model include:

1. Process-based schema for handling transitions between biomaterial and file entities
1. Modular schemas to support independent versioning and domain-specific metadata fields
1. Flexible and reusable metadata structure to enable modeling of future experiment types

### Entities

There are five major entities supported by the HCA metadata standard: Projects, Biomaterials (samples), Protocols, Processes, and Files.

![Entities](images/entities.jpg)

The entities are arranged in units the represent different parts of an experiment. For example, the diagram below is an abstract illustratation of an input *biomaterial* (*e.g.* a tissue sample) undergoing some *process* (*e.g.* dissociation) to produce another *biomaterial* (*e.g.* a sample of dissociated cells). The *process* that was actually executed followed a specific *protocol* - or intended plan - to produce the output *biomaterial*.

![Entities](images/unit_of_hierarcy.jpg)

The metadata entity model supports units that can have either biomaterials or data files as input or output. If the input is a biomaterial and the output is a data file, we typically refer to this as an assay. If both the input and output is a data file, we refer to this as an analysis. This flexible model also allows for the possibility of modeling synthetic biology experiments - for example a data file is used as input to produce a custom biomaterial - in the future.

![Entities](images/unit_scenarios.jpg)

**Describe wrapper processes**

![Entities](images/wrapper_process.jpg)

### Metadata field organisation 

* *Core fields* = Very stable, high-level entities that are referenced by a respective *Type*. These entities contain core fields that apply to and are inherited by corresponding *Type* entities.
* *Type fields* = An entity that is a specific instance of *Core* entity type. These entities contain fields specific to that *Type* and inherit core fields from the corresponding *Core* entity.
* *Module fields* = Small, evolvable entities that are extensions of an existing *Type* entity. These entities contain extra fields specific to a *Type* but are domain- or user-specific.

## Specification of schema structure and content

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

## Principles

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

The schema will be stored as a series of individual documents which are related to entities and modules associated with them e.g project.json, assay.json, sample.json. These documents should be stored in a single versioned control repository alongside any documentation about the schema, the meaning of their contents or the update process.
 
The metadata schemas are maintained in the [metadata-schema repo](https://github.com/HumanCellAtlas/metadata_schema/json_schema) in the Human Cell Atlas GitHub organisation.

 The Metadata Working Group will review this process on a yearly basis and ensure it is meeting the needs of the working group. If at any point the process becomes problematic, changes will be made to ensure metadata update is not a blocker for the consortium as a whole.
 
Using GitHub, anyone will be able to propose changes to the schema through pull requests. Only a specified list of committers will be allowed to approve pull requests and issue new versions of the metadata standards.

