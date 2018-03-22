[![Build Status](https://travis-ci.org/HumanCellAtlas/metadata-schema.svg)](https://travis-ci.org/HumanCellAtlas/metadata-schema)

# The Human Cell Atlas Metadata Schema

This repo contains the HCA metadata JSON schemas, example JSON files, and template metadata spreadsheets.

The **metadata design principles** can be read in the [Metadata schema lifecycle doc](docs/Metadata_schema_lifecycle_doc.md).

Details on **how to contribute** to the metadata schema standards are described in the [contributing.md](contributing.md) doc.


### HCA v4.6.1-to-v5.0.0 metadata schema changes overview

#### Primary goals of changes

1. Process-based schema for handling transitions between biomaterial and file entities
1. Modular schemas to support independent versioning and domain-specific metadata fields
1. More flexible, reusable metadata structure

#### Field organisational structure 

* *Core* = Very stable, high-level entities that are referenced by a respective *Type*. These entities contain core fields that apply to and are inherited by corresponding *Type* entities.
* *Type* = An entity that is a specific instance of *Core* entity type. These entities contain fields specific to that *Type* and inherit core fields from the corresponding *Core* entity.
* *Module* = Small, evolvable entities that are extensions of an existing *Type* entity. These entities contain extra fields specific to a *Type* but are domain- or user-specific.

#### Specifying version info

Each schema is self-describing using the `id` field with a URL to the location of the version of the current document. 

Version indicated in schema URL: `https://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core`

As we are requiring instance data to also be self describing, all *Type* entities will require a property called `describedBy`. 

e.g. For `donor_organism.json` schema, these fields will look like: 

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

#### Community-driven metadata standards

Follow our community discussion of HCA metadata by joining the #hca-metadata channel on the HCA Slack group here: https://humancellatlas.slack.com/.