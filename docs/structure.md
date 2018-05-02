# The Human Cell Atlas: Overview of Metadata Structure

## Table of Contents
- [Introduction](#introduction)
- [Overview of the metadata structure](#structure-overview)
- [Specifying schema URL](#specifying-schema-url)

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

Below is an example single-cell sequencing experiment modeled using the HCA metadata entity model described here.

![Entities](images/project_scenario.jpg)

### Metadata field organisation 

* *Core fields* = Very stable, high-level entities that are referenced by a respective *Type*. These entities contain core fields that apply to and are inherited by corresponding *Type* entities.
* *Type fields* = An entity that is a specific instance of *Core* entity type. These entities contain fields specific to that *Type* and inherit core fields from the corresponding *Core* entity.
* *Module fields* = Small, evolvable entities that are extensions of an existing *Type* entity. These entities contain extra fields specific to a *Type* but are domain- or user-specific.

## Recording the standards

The schema will be stored as a series of individual documents which are related to entities and modules associated with them *e.g* project.json, biomaterial.json, sequencing_process.json. These documents are stored in a single versioned control GitHub repository alongside documentation about the schema, the meaning of their contents, and the update process. Using GitHub, anyone will be able to propose changes to the schema through pull requests. Only a specified list of committers will be allowed to approve pull requests and issue new versions of the metadata standards.

### Specifying schema URL

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

The HCA metadata lifecycle document defines the requirement for the metadata schema to be self-describing, ie each metadata file needs to explicitly indicate the schema and schema version which it manifests. The proposed structure of the metadata schema URIs is:

http://schema.humancellatlas.org/{primary_directory}/{secondary/directory/structure}/{version}/{filename}
where
{primary_directory} = [core, type, module]
{secondary/directory/structure} eg biomaterial or process/sequencing
{version} = the version number of the schema file eg 5.0.1

Examples
http://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core
http://schema.humancellatlas.org/type/biomaterial/5.0.0/cell_line
http://schema.humancellatlas.org/type/process/sequencing/5.0.0/library_preparation_process
http://schema.humancellatlas.org/module/ontology/5.0.0/cell_type_ontology
http://schema.humancellatlas.org/module/process/sequencing/5.0.0/barcode

