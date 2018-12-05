# Type
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## Cell line
_Information about the cell line or cell culture biomaterial._

Location: type/biomaterial/cell_line.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
supplier | The supplier of the cell line. | string | no |  | Supplier |  | HipSci
catalog_number | The supplier catalogue number for the cell line. | string | no |  | Catalog number |  | 77650057
lot_number | The supplier lot or batch number for the cell line. | string | no |  | Lot/batch number |  | 24.10.14
catalog_url | The supplier catalogue URL for the cell line. | string | no |  | Catalog URL |  | 
cell_cycle | The cell cycle phase if the cell line is synchronized growing cells or the phase is known. | object | no | [See module  cell_cycle_ontology](module.md/#cell_cycle_ontology) | Cell cycle |  | mitotic cell cycle
cell_line_type | The type of cell line. | string | yes |  | Cell line type | primary, immortalized, stem cell-derived, synthetic, induced pluripotent, stem cell | Should be one of: primary, immortalized, stem cell, stem cell-derived, induced pluripotent, or synthetic.
cell_morphology | Features relating to the morphology of the cells. | object | no | [See module  cell_morphology](module.md/#cell_morphology) | Cell morphology |  | 
growth_conditions | Features relating to the growth and/or maintenance of the cell lines. | object | no | [See module  growth_conditions](module.md/#growth_conditions) | Growth conditions |  | 
confluency | The percent a plate surface is covered by cells. | number | no |  | Percent confluency |  | 60
cell_type | The cell type that the cell line represents. | object | no | [See module  cell_type_ontology](module.md/#cell_type_ontology) | Cell type |  | cardiac muscle cell
karyotype | The karyotype of the cell line. | string | no |  | Karyotype |  | 
tissue | The tissue that the cell line was derived from. | object | no | [See module  organ_part_ontology](module.md/#organ_part_ontology) | Tissue |  | bone marrow
date_established | When the cell line was established, in date-time format. yyyy-mm-ddThh:mm:ssZ. | string | no |  | Date established |  | 2017-03-19
disease | Short description of any disease association to the cell type. | object | no | [See module  disease_ontology](module.md/#disease_ontology) | Disease |  | bone squamous cell carcinoma
genus_species | The scientific binomial name for the species of the cell line. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
publication | A publication that cites the cell line creation. | object | no | [See module  publication](module.md/#publication) | Cell line publication |  | 

## Cell suspension
_Information about the suspension of cells or nuclei derived from the collected or cultured specimen._

Location: type/biomaterial/cell_suspension.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
cell_morphology | Features relating to the morphology of cells in a biomaterial. | object | no | [See module  cell_morphology](module.md/#cell_morphology) | Cell morphology |  | 
growth_conditions | Features relating to the growth and/or maintenance of a biomaterial. | object | no | [See module  growth_conditions](module.md/#growth_conditions) | Growth conditions |  | 
genus_species | The scientific binomial name for the species of the suspension. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
selected_cell_type | The cell type(s) selected to be present in the suspension. | array | no | [See module  cell_type_ontology](module.md/#cell_type_ontology) | Selected cell type |  | fetal cardiomyocyte
total_estimated_cells | Total estimated number of cells in the suspension. May be 1 for well-based assays. | integer | no |  | Total estimated cell count |  | 2100
plate_based_sequencing | Fields specific for plate-based sequencing experiments. | object | no | [See module  plate_based_sequencing](module.md/#plate_based_sequencing) | Plate-based sequencing |  | 

## Donor organism
_Information about the donor organism from which a specimen was collected._

Location: type/biomaterial/donor_organism.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
human_specific | Fields specific to human (homo sapiens) organisms. | object | no | [See module  human_specific](module.md/#human_specific) | Human-specific |  | 
mouse_specific | Fields specific to mouse (mus musculus) organisms. | object | no | [See module  mouse_specific](module.md/#mouse_specific) | Mouse-specific |  | 
genus_species | The scientific binomial name for the species of the organism. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
sex | The biological sex of the organism. | string | yes |  | Biological sex | female, male, mixed, unknown | Should be one of: male, female, mixed, or unknown.
is_living | Yes if organism is alive at time of biomaterial collection. No if dead. Unknown if not known. | string | yes |  | Alive at collection? | yes, no, unknown | Should be one of: yes, no, unknown.
organism_age | Age of organism in Organism age unit. Measured since birth. | string | no |  | Organism age |  | 20
organism_age_unit | The unit in which Organism age is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Organism age unit |  | Should be one of: hour, day, week, month, or year.
development_stage | A classification of the developmental stage of the organism. | object | no | [See module  development_stage_ontology](module.md/#development_stage_ontology) | Development stage |  | adult
diseases | Short description of known disease(s) of the organism. Enter 'normal' if no known disease. | array | no | [See module  disease_ontology](module.md/#disease_ontology) | Known disease(s) |  | bone squamous cell carcinoma
death | Information about conditions of death of the organism. | object | no | [See module  death](module.md/#death) | Death conditions |  | 
familial_relationship | Information about other organisms related to this organism. | array | no | [See module  familial_relationship](module.md/#familial_relationship) | Familial relationship |  | 
medical_history | Information about the medical history of the organism. | object | no | [See module  medical_history](module.md/#medical_history) | Medical history |  | 
gestational_age | Gestational age of organism in Gestational age unit. Measured since fertilization. | string | no |  | Gestational age |  | 5-7
gestational_age_unit | The unit in which Gestational age is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Gestational age unit |  | Should be one of: hour, day, week, month, or year.
height | Height of organism in Height unit. | string | no |  | Height |  | 160
height_unit | The unit in which Height is expressed. | object | no | [See module  length_unit_ontology](module.md/#length_unit_ontology) | Height unit |  | centimeter
weight | Weight of organism in Weight unit. | string | no |  | Weight |  | 60
weight_unit | The unit in which Weight is expressed. | object | no | [See module  mass_unit_ontology](module.md/#mass_unit_ontology) | Weight unit |  | kilogram
normothermic_regional_perfusion | Yes if entire body (but not limbs) was perfused with warm oxygenated blood. No otherwise. | string | no |  | Normothermic regional perfusion? | yes, no, unknown | Should be one of: yes, no, or unknown.

## Imaged specimen
_Information about a tissue specimen after it has been sectioned and prepared for imaging._

Location: type/biomaterial/imaged_specimen.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
overview_image | List of filenames of photographs of specimen. Must be of format JPEG, TIFF, or PNG. | array | no |  | Gross image |  | my_mage_file.jpg
imaged_slice_thickness | Thickness of the imaged slice in micrometres. | number | yes |  | Imaged slice thickness |  | 14
internal_anatomical_structures | Internal (landmark) structures visible in the overview image that are informative about the broader anatomical context/location of the sample. | array | no | [See module  organ_part_ontology](module.md/#organ_part_ontology) | Internal tissue structures |  | 

## Organoid
_Information about an organoid biomaterial._

Location: type/biomaterial/organoid.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
genus_species | The scientific binomial name for the species of the organoid. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
model_for_organ | Organ for which this organoid is a model system. | object | yes | [See module  organ_ontology](module.md/#organ_ontology) | Organ model |  | brain
model_organ_part | Organ part for which this organoid is a model system. | object | no | [See module  organ_part_ontology](module.md/#organ_part_ontology) | Organ part model |  | cortex
organoid_age | Age of the organoid in Organoid age unit. Measured from when cell aggregates started differentiating to desired organoid model. | number | no |  | Organoid age |  | 55
organoid_age_unit | The unit in which Organoid age is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Organoid age unit |  | Should be one of: minute, hour, day, week, month, or year.
organoid_size | Size of the organoid in Organoid size unit. | number | no |  | Organoid size |  | 4
organoid_size_unit | The unit in which the Organoid size is expressed. | object | no | [See module  length_unit_ontology](module.md/#length_unit_ontology) | Organoid size unit |  | millimeter
organoid_morphology | General description of the organoid morphology. | string | no |  |  |  | Epithelial monolayer with budding crypt-like domains.
organoid_type | The type of organoid. | string | no |  | Organoid type | primary, immortalized, stem cell-derived, synthetic | Should be one of: primary, immortalized, stem cell-derived, or synthetic.
embedded_in_matrigel | Whether the organoid is embedded in a matrigel. | boolean | no |  | Organoid embeddded in matrigel? |  | Should be one of: yes, no.
organoid_growth_environment | Growth environment in which the organoid is grown. | string | no |  | Organoid growth environment |  | matrigel, liquid suspension, adherent
input_aggregate_cell_count | Estimated number of cells per input cell aggregate. | number | no |  | Input aggregate cell count |  | 10000
organoid_stored_oxygen_levels | Percent oxygen level organoid was stored in prior to sequencing. | number | no |  | Organoid stored oxygen level |  | 75

## Specimen from organism
_Information about the specimen that was collected from the donor organism._

Location: type/biomaterial/specimen_from_organism.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
genus_species | The scientific binomial name for the species of the specimen. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
organ | The organ that the biomaterial came from. Blood and connective tissue are considered organs. | object | yes | [See module  organ_ontology](module.md/#organ_ontology) | Organ |  | blood
organ_part | A term for a specific part of the organ that the biomaterial came from. | object | no | [See module  organ_part_ontology](module.md/#organ_part_ontology) | Organ part |  | umbilical cord blood
diseases | Short description of known disease(s) of the specimen. Enter normal if no known disease. | array | no | [See module  disease_ontology](module.md/#disease_ontology) | Known disease(s) |  | bone squamous cell carcinoma
state_of_specimen | State of the specimen at the time of collection. | object | no | [See module  state_of_specimen](module.md/#state_of_specimen) | State of specimen |  | 
preservation_storage | Information about how a specimen was preserved and/or stored over a period of time. | object | no | [See module  preservation_storage](module.md/#preservation_storage) | Preservation/Storage |  | 
collection_time | When the biomaterial was collected, in date-time format, yyyy-mm-ddThh:mm:ssZ. | string | no |  | Time of collection |  | 2017-03-19T07:22:00Z
purchased_specimen | Information about a purchased specimen. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Purchased specimen |  | 

## Analysis file
_A file analysis results produced by a secondary analysis pipeline._

Location: type/file/analysis_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 

## Image file
_Information about an image file generated by an imaging experiment._

Location: type/file/image_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 

## Reference file
_A reference file used by a secondary reference pipeline._

Location: type/file/reference_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | integer | yes |  | NCBI taxon ID |  | 9606
genus_species | The scientific binomial name for the species of this reference. | object | yes | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
assembly_type | The assembly type of the reference. This applies to reference genome sequences. | string | yes |  | Assembly type | primary assembly, complete assembly, patch assembly | Should be one of: primary assembly, complete assembly, or patch assembly.
reference_type | The type of the genome reference. | string | yes |  | Reference type | genome sequence, transcriptome sequence, annotation reference, transcriptome index, genome sequence index | Should be one of: genome sequence, transcriptome sequence, annotation reference, transcriptome index, or genome sequence index.
reference_version | The genome version of the reference. | string | yes |  | Reference version |  | GencodeV27

