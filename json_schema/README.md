# The Human Cell Atlas Metadata Standards: JSON Schemas

This repo contains the HCA metadata JSON schemas for core, type, and modules entities, as well as bundles.

## JSON Schema File Standards

Below is a quick list of standards we try to adhere to about the structure of the HCA JSON schemas. If you would like to contribute a metadata JSON schema to this repo, please follow these standards and ask if you have any questions.

### Schema structure

Metadata fields are divided into 3 major entities: Core, Type, and Module.

Metadata fields in **Core** entity schemas are those that apply to 100% of all entities and are highly stable. Example Core fields include those for IDs and accessions. Core fields are inherited by Type entities.

Metadata fields in **Type** entity schemas are those that apply to a majority of entities but not all. Example Type fields include height and weight for donors, target_cell_type for cell suspensions. 

Metadata fields in **Module** entity schemas are those that apply to a small number of entities or may be shared across different entities. Example Module fields include time_of_death and cause_of_death for donors and publication information (which can apply to both projects and biomaterials like cell lines).

Individual JSON files that are all part of the same experiment or assay are wrapped together into a **Bundle**. JSON schemas for these bundles are also present in this repo along with schemas for other infrastructure-related information like links between entities and submission information.

### Required standards

1. Core entities can not reference Type or Module subschemas.
1. All Type entities must reference their associated Core entity.
1. Module entities can only reference ontology (Module) subschemas.
1. A set of fields that are logically grouped, and only applicable in certain situations should be put into their own Module.
1. All schemas must implement semantic versioning. Briefly, a schema version is composed of three integers - each a separated by a period - in major.minor.patch format. Each core, type, module, and bundle schema is versioned independently.

### Strongly recommended standards

1. All field names should be lower case.
1. If a field (property) name is made up of more than one word, an underscore "_" should be used to separate the words.
1. All fields and schemas should have a description.
1. All fields should have an accompanying example and user-friendly name for displaying in a UI.
1. Fields should not have duplicate or snynonymous fields in any other schema.

#### Directory structure of schemas

```
bundle/
    <bundle schemas>
 
core/
    biomaterial/biomaterial_core.json	
    file/file_core.json
    process/process_core.json
    project/project_core.json
    protocol/protocol_core.json
 
type/
    biomaterial/
        cell_line.json
        cell_suspension.json
        donor_organism.json
        organoid.json
        specimen_from_organism.json
    file/		
        analysis_file.json
        reference_file.json
        sequence_file.json
    process/    
        analysis/analysis_process.json
        biomaterial_collection/enrichment_process.json
        biomaterial_collection/collection_process.json
        biomaterial_collection/dissociation_process.json
        imaging/imaging_process.json
        sequencing/library_preparation_process.json
        sequencing/sequencing_process.json
        process.json
    protocol/  
        analysis/analysis_protocol.json
        biomaterial/biomaterial_collection_protocol.json
        imaging/imaging_protocol.json
        sequencing/sequencing_protocol.json
        protocol.json        
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
        sequencing/barcode.json
        ...
    project/
        contact.json
        ...

```
