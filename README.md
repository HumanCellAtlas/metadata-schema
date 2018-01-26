[![Build Status](https://travis-ci.org/HumanCellAtlas/metadata-schema.svg)](https://travis-ci.org/HumanCellAtlas/metadata-schema)


# The Human Cell Atlas Metadata Schema

This repo contains the HCA metadata JSON schemas, example JSON files, and template metadata spreadsheets.

The **design-principles** can be read in the [linked Google Doc](https://docs.google.com/document/d/1eUVpYDLu2AxmxRw2ZUMM-jpKNxQudJbznNyNRp35nLc/edit?usp=sharing)

How to contribute is described in [contributing.md](https://github.com/HumanCellAtlas/metadata-schema/blob/master/contributing.md)


### HCA v4.6.1-to-v5.0.0 metadata schema changes overview

#### Primary goals of changes

1. Move to process-based schema for handling transitions between core biomaterial and file entities
1. Move to a module-based schema to support independent versioning and user-/domain-specific metadata fields
1. Move to a more flexible, reusable metadata structure

#### Proposed organisational structure 

* *Core* = Very stable, high-level entities that are referenced by a respective *Type*. These entities contain core fields that apply to and are inherited by corresponding *Type* entities.
* *Type* = An entity that is a specific instance of *Core* entity type. These entities contain fields specific to that *Type* and inherit core fields from the corresponding *Core* entity.
* *Module* = Small, evolvable entities that are extensions of an existing *Type* entity. These entities contain extra fields specific to a *Type* but are domain- or user-specific.

#### Suggested directory structure of schemas

```
core/
    biomaterial/biomaterial_core.json	
    file/file_core.json
    process/process_core.json
    project/project_core.json
    protocol/protocol_core.json
 
type/
    process/    
        analysis/   analysis_process.json
        biomaterial_collection/ enrichment_process.json
                                collection_process.json
                                dissociation_process.json
        imaging/    imaging_process.json
        sequencing/	library_preparation_process.json
                    sequencing_process.json
    protocol/  
        analysis/    analysis_protocol.json
        biomaterial/ biomaterial_collection_protocol.json
        imaging/     imaging_protocol.json
        sequencing/  sequencing_protocol.json
                  
    biomaterial/
        cell_line.json
        cell_suspension.json
        organism.json
        organoid.json
        specimen_from_organism.json
    file/		
        sequence_file.json
    project/	
        project.json
 
module/
    biomaterial/
        death.json
        ...
    ontology/
        body_part_ontology.json
        ...
    process/
        sequencing/
            barcode.json
            ...
        imaging/
            ...
    project/
        contact.json
        publication.json
        ...

```

#### Specifying version info

Each schema should be self describing using `id` field with a URL to the location of the version of the current document. 

Version indicated in schema URL: `http://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core.json`

As we are requiring instance data to also be self describing, all *types* will require a property called `$schema`. 

e.g. For `organism.json` schema, these fields will look like: 

``` 
"$schema": "http://json-schema.org/draft-04/schema#"
"id": "http://schema.humancellatlas.org/type/biomaterial/4.0.0/organism.json"
"additionalProperties": false,
"properties" : {
    "$schema": {
        "description": "The URL reference to the schema.",
        "type": "string",
        "pattern": "http://schema.humancellatlas.org/type/biomaterial/[0-9]{1,}.[0-9]{1,}.[0-9]{1,}/organism.json"
    },
    ...
}
```

