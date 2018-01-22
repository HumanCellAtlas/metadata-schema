[![Build Status](https://travis-ci.org/HumanCellAtlas/metadata-schema.svg)](https://travis-ci.org/HumanCellAtlas/metadata-schema)


# The Human Cell Atlas Metadata Schema

This repo contains the HCA metadata JSON schemas.

The **design-principles** can be read in the [linked Google Doc](https://docs.google.com/document/d/1eUVpYDLu2AxmxRw2ZUMM-jpKNxQudJbznNyNRp35nLc/edit?usp=sharing)

How to contribute is described in [contributing.md](https://github.com/HumanCellAtlas/metadata-schema/blob/master/contributing.md)


### HCA v4-to-v5 metadata schema overview

#### Primary goals of changes

1. Move to process-based schema for handling transitions between core entities
1. Move to a component-based schema to support independent versioning of submittable types
1. Define hierarchy (directory structure) for core entities and modules
    1. High-level *core* entities are not submittable on their own (e.g. biomaterial.json)
    1. Mid-level *type* entities are submittable on their own (e.g. organism.json)
    1. Low-level *common* modules are not submittable on their own (e.g. death.json)

#### Proposed organisational structure 

* *Core* = Very stable, high-level entities that are referenced by a Type
* *Type* = Any entity that is submittable directly to ingest 
* *Common* = Small, potentially quickly evolving modules that can be referenced by a Type

#### Suggested directory structure of schemas

```
core/
    process/process_core.json
    protocol/protocol_core.json
    biomaterial/biomaterial_core.json	
    file/file_core.json
    project/project_core.json
 
type/
    process/    
        sequencing/	library_preparation_process.json
                    sequencing_process.json
        imaging/    imaging_process.json
        analysis/   analysis_process.json
        biomaterial_collection/enrichment_process.json
                               collection_process.json
                               dissociation_process.json
    protocol/  
        sequencing/ sequencing_protocol.json
        imaging/	imaging_protocol.json
        analysis/	analysis_protocol.json
        biomaterial/biomaterial_collection_protocol.json
        ...
                  
    biomaterial/
        organism.json
        specimen_from_organism.json
        cell_suspension.json
        organoid.json
        cell_line.json
    file/		
        sequence_file.json
    project/	
        project.json

 
module/
    biomaterial/
        death.json
        ...
    process/
        sequencing/
            barcode.json
            ...
        imaging/
            ...
    ontology/
        body_part_ontology.json
        ...
    project/
        contact.json
        submitter.json
        publication.json
        ...
    ...

bundle/

```

#### Specifying version info

Each schema should be self describing using `id` field with a URL to the location of the version of the current document. 

Version indicated in schema URL: `http://schema.humancellatlas.org/core/biomaterial/4.0.0/biomaterial_core.json`

As we are requiring instance data to also be self describing, all *types* will require a property called `$schema`. 

e.g. For `organism.json` schema, `type` field should contain: 

``` 
"$schema": "http://json-schema.org/draft-04/schema#"
"id": "http://schema.humancellatlas.org/type/biomaterial/4.0.0/organism.json"
"additionalProperties": false,
properties : {
    $schema : {
        "pattern" : "http://schema.humancellatlas.org/type/biomaterial/organism/[0-9]{1,}.[0-9]{1,}.[0-9]{1,}/organism.json"
        "type" : "string",
    }
}
```

#### Scope of changes

1. No content changes - fields untouched unless they really need to be moved to restructure, and in which case will be carefully documented
1. Define protocol/process model

#### List of common modules based on v4 $ref:

```
ontology/cell_type_ontology.json
ontology/disease_ontology.json
ontology/ontology.json
ontology/body_part_ontology.json
ontology/…

biomaterial/state_of_specimen.json
biomaterial/death.json
biomaterial/…

process/sequencing/well.json 
process/sequencing/barcode.json

project/contact.json
project/publication.json
```

#### Additional tasks to complete v5 (some are content-related)

1. Discuss implementing a "latest" or an alias for current schema version
1. Group the content fields for easily selecting which ones are relevant for different situations (e.g. avoid giving `alcohol_history` field/column to user submitted mouse data)
1. Generate groupings of modules to reflect where we expect them to be
1. Add `tab name` and `name` outside of property to have text that goes in the actual tab name (`description` can go in the README tab next to the tab name)
