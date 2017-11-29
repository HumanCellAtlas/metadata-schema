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
    1. High-level *core* entities are not submittable on their own (e.g. sample.json)
    1. Mid-level *type* entities are submittable on their own (e.g. donor.json)
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
    sample/sample_core.json	
    file/file_core.json
    project/project_core.json
    analysis/analysis_core.json
 
types/
    process/    
        process.json
        sequencing/	rna_process.json
                    seq_process.json
        imaging/    imaging_process.json
        analysis/   analysis_process.json
        sample/	    enrichment.json
                    preservation.json
                    sample_collection.json
                    single_cell.json
                    sorting.json
    protocols/  
        protocols.json
        sequencing/	rna_protocol.json
                    seq_protocol.json
        imaging/	imaging_protocol.json
        analysis/	analysis.json
        sample/	    enrichment.json
                    preservation.json
                    sample_collection.json
                    single_cell.json
                    sorting.json
    sample/
        sample.json
        donor.json
        specimen.json
        cell_suspension.json
        organoid.json
        primary_cell_line.json
    file/		
        file.json
    project/	
        project.json
    analysis/	
        analysis.json
 
common/
    sample/
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

Version indicated in schema URL: `http://schema.humancellatlas.org/core/sample/4.0.0/sample_core.json`

As we are requiring instance data to also be self describing, all *types* will require a property called `$schema`. 

e.g. For `donor.json` schema, `type` field should contain: 

``` 
"$schema": "http://json-schema.org/draft-04/schema#"
"id": "http://schema.hca.org/schema/v1.0.0/types/sample/donor.json"
"additionalProperties": false,
properties : {
    $schema : {
        "pattern" : "http://schema.hca.org/schema/v[0-9]{1,}.[0-9]{1,}.[0-9]{1,}/types/samples/donor.json"
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

sample/specimen_from_sample/state_of_specimen.json
sample/immortalized_cell_line/publication.json
sample/donor/death.json
sample/cell_suspension/well.json
sample/cell_suspension/enrichment.json

process/imaging.json
process/rna.json 
process/seq.json
process/single_cell.json
process/sequencing/barcode.json

project/contact.json
project/publication.json
```

#### Additional tasks to complete v5 (some are content-related)

1. Discuss implementing a "latest" or an alias for current schema version
1. Group the content fields for easily selecting which ones are relevant for different situations (e.g. avoid giving `alcohol_history` field/column to user submitted mouse data)
1. Generate groupings of modules to reflect where we expect them to be
1. Add `tab name` and `name` outside of property to have text that goes in the actual tab name (`description` can go in the README tab next to the tab name)
