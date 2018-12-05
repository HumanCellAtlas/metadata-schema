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
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
supplier | The supplier of the cell line. | string | no |  | Supplier |  | HipSci, ATCC
catalog_number | The supplier catalogue number for the cell line. | string | no |  | Catalog number |  | 77650057
lot_number | The supplier lot or batch number for the cell line. | string | no |  | Lot/batch number |  | 24.10.14
catalog_url | The supplier catalogue URL for the cell line. | string | no |  | Catalog URL |  | www.phe-culturecollections.org.uk/products/celllines/ipsc/detail.jsp?refId=77650057&collection=ecacc_ipsc
cell_cycle | The cell cycle phase if the cell line is synchronized growing cells or the phase is known. | object | no | [See module  cell_cycle_ontology](module.md/#cell_cycle_ontology) | Cell cycle |  | 
cell_line_type | The type of cell line. | string | yes |  | Cell line type | primary, immortalized, stem cell-derived, synthetic, induced pluripotent, stem cell | Should be one of: primary, immortalized, stem cell, stem cell-derived, induced pluripotent, or synthetic.
cell_morphology | Features relating to the morphology of the cells. | object | no | [See module  cell_morphology](module.md/#cell_morphology) | Cell morphology |  | 
growth_conditions | Features relating to the growth and/or maintenance of the cell lines. | object | no | [See module  growth_conditions](module.md/#growth_conditions) | Growth conditions |  | 
confluency | The percent a plate surface is covered by cells. | number | no |  | Percent confluency |  | 60
cell_type | The cell type that the cell line represents. | object | no | [See module  cell_type_ontology](module.md/#cell_type_ontology) | Cell type |  | 
karyotype | The karyotype of the cell line. | string | no |  | Karyotype |  | sex chromosome complement of XY, del(2) (q11)
tissue | The tissue that the cell line was derived from. | object | no | [See module  organ_part_ontology](module.md/#organ_part_ontology) | Tissue |  | 
date_established | When the cell line was established. | string | no |  | Date established |  | 2017-03-19
disease | Short description of any disease association to the cell type. | object | no | [See module  disease_ontology](module.md/#disease_ontology) | Disease |  | 
genus_species | The scientific binomial name for the species of the cell line. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | 
publication | A publication that cites the cell line creation. | object | no | [See module  publication](module.md/#publication) | Publication |  | 

## Cell suspension
_Information about the suspension of cells or nuclei derived from the collected or cultured specimen._

Location: type/biomaterial/cell_suspension.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
cell_morphology | Features relating to the morphology of cells in a biomaterial. | object | no | [See module  cell_morphology](module.md/#cell_morphology) | Cell morphology |  | 
growth_conditions | Features relating to the growth and/or maintenance of a biomaterial. | object | no | [See module  growth_conditions](module.md/#growth_conditions) | Growth conditions |  | 
genus_species | The scientific binomial name for the species of the suspension. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | 
selected_cell_type | The cell type(s) selected to be present in the suspension. | array | no | [See module  cell_type_ontology](module.md/#cell_type_ontology) | Selected cell type |  | 
total_estimated_cells | Total estimated number of cells in the suspension. | integer | no |  | Estimated cell count |  | 2100
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
timecourse | Information relating to a timecourse associated with this biomaterial. | object | no | [See module  timecourse](module.md/#timecourse) | Timecourse |  | 

## Imaged specimen
_Information about a tissue specimen after it has been sectioned and prepared for imaging._

Location: type/biomaterial/imaged_specimen.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
overview_images | List of filenames of photographs of specimen. | array | no |  | Gross image |  | my_image_file.jpg, overview_image.tiff
slice_thickness | Thickness of the imaged slice in micrometres. | number | no |  | Imaged slice thickness |  | 14, 30
internal_anatomical_structures | Internal (landmark) structures visible in the overview image that are informative about the broader anatomical context/location of the sample. | array | no | [See module  organ_part_ontology](module.md/#organ_part_ontology) | Internal tissue structures |  | 

## Organoid
_Information about an organoid biomaterial._

Location: type/biomaterial/organoid.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
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

## Sequence file
_A file of read sequences generated by a sequencing experiment._

Location: type/file/sequence_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 
read_index | Whether the read file contains the read1, read2, index1, or index2 part of the sequencing read or represents a single-end, non-indexed library. | string | yes |  | Read index | read1, read2, index1, index2, single-end, non-indexed | Should be one of: read1, read2, index1, index2, or 'single-end, non-indexed'
lane_index | The index of the lane that this file was sequenced from. | integer | no |  | Lane index |  | 1
read_length | The length of a sequenced read in this file, in nucleotides. | integer | no |  | Read length |  | 51
insdc_run | An INSDC (International Nucleotide Sequence Database Collaboration) run accession. Can be from the DDBJ, NCBI, or EMBL-EBI. Accession must start with DRR, SRR, or ERR. | array | no |  | INSDC run |  | SRR0000000
technical_replicate_group | A project wide unique label to indicate which groups of files are technical replicates. Technical replicates are sequence files generated from the same sequencing library. Leave blank if files are biological replicates. | string | no |  | Technical replicate group |  | tech_rep_group_001

## Supplementary file
_Supplementary files belonging to a project._

Location: type/file/supplementary_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 
file_description | A short description of the file content. This could include information about how the file was generated. | string | no |  | File description |  | Enrichment protocol

## Process
_Information about the process_

Location: type/process/process.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | process | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
process_core | Core process-level information. | object | yes | [See core  process_core](core.md/#process_core) |  |  | 
length_of_time | Length of time the process took to execute, from start to finish, in Length of time unit. | string | no |  | Length of time |  | 10
length_of_time_unit | The unit in which Length of time is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Length of time unit |  | Should be one of: microsecond, second, minute, hour, day, week, month, or year.
process_type | The type of process. | object | no | [See module  process_type_ontology](module.md/#process_type_ontology) | Process type |  | sample enrichment
deviation_from_protocol | Any deviation from the protocol provided. | string | no |  | Deviation from protocol |  | 
insdc_experiment | An INSDC (International Nucleotide Sequence Database Collaboration) experiment accession. | object | no | [See module  insdc_experiment](module.md/#insdc_experiment) | INSDC experiment |  | 

## Analysis process
_Information about the analysis process_

Location: type/process/analysis/analysis_process.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | process | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
process_core | Core process-level information. | object | yes | [See core  process_core](core.md/#process_core) |  |  | 
process_type | The type of process. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Process type |  | 
inputs | Input parameters used in the pipeline run, these can be files or string values (settings). | array | yes |  | Input parameters |  | 
tasks | Descriptions of tasks in the workflow. | array | yes |  | Workflow tasks |  | 
input_bundles | The input bundles used in this analysis run. | array | yes |  | Input bundles |  | 
outputs | Output generated by the pipeline run. | array | yes | [See   analysis_file](.md/#analysis_file) | Outputs |  | 
timestamp_start_utc | Initial start time of the full pipeline in UTC. | string | yes |  | Start timestamp (UTC) |  | 
timestamp_stop_utc | Terminal stop time of the full pipeline in UTC. | string | yes |  | Stop timestamp (UTC) |  | 
analysis_run_type | Indicator of whether the analysis actually ran or was just copied forward as an optimization. | string | yes |  | Analysis run type | run, copy-forward | 
reference_bundle | Bundle containing the reference used in running the pipeline. | string | yes |  | Reference bundle |  | 

## Project
_A project entity contains information about the overall project._

Location: type/project/project.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | project | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
project_core | Core project-level information. | object | yes | [See core  project_core](core.md/#project_core) |  |  | 
contributors | List of people contributing to any aspect of the project. | array | no | [See module  contact](module.md/#contact) | Contributors |  | 
supplementary_links | External link(s) pointing to code, supplementary data files, or analysis files associated with the project which will not be uploaded. | array | no |  | Supplementary link(s) |  | https://github.com/czbiohub/tabula-muris
publications | A list of publications resulting from this project. | array | no | [See module  publication](module.md/#publication) | Publications |  | 
insdc_project | An INSDC (International Nucleotide Sequence Database Collaboration) project accession, if project has been submitted. Can be from the DDBJ, NCBI, or EMBL-EBI. Accession must start with DRP, SRP, or ERP. | string | no |  | INSDC project accession |  | SRP000000
geo_series | GEO accession number, if data has been submitted. Accession must start with GSE. | string | no |  | GEO series accession |  | GSE00000
array_express_investigation | EBI ArrayExpress accession number, if data has been submitted. | string | no |  | ArrayExpress accession |  | E-AAAA-00
insdc_study | An INSDC (International Nucleotide Sequence Database Collaboration) study accession if study has been submitted. Can be from the DDBJ, EMBL-EBI, or NCBI. Accession must start with PRJE, PRJN, or PRJD. | string | no |  | INSDC study accession |  | PRJNA000000
funders | A list of funding source(s) supporting the project. | array | no | [See module  funder](module.md/#funder) | Project funding source(s) |  | 

## Protocol
_Information about the protocol._

Location: type/protocol/protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
protocol_type | The type of protocol. | object | no | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | sample enrichment

## Analysis protocol
_Information about the analysis protocol._

Location: type/protocol/analysis/analysis_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
protocol_type | The type of protocol. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | 
computational_method | A URI to a versioned workflow and versioned execution environment in a GA4GH-compliant repository. | string | yes |  | Computational method |  | 

## Aggregate generation protocol
_Information about how cultured cells are developed into cell aggregates._

Location: type/protocol/biomaterial_collection/aggregate_generation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
aggregate_formation_method | Method used to form cell aggreagtes. | string | yes |  | Aggregate formation method |  | rocking, suspension cultures, hanging drops, spinner flasks
aggregate_cell_uniformity | Description of uniformity of the cell aggregates after they are formed. | string | no |  | Aggregate cell uniformity |  | Mostly homogenous EBs of variable cell numbers

## Collection protocol
_Information about the biomaterial collection protocol._

Location: type/protocol/biomaterial_collection/collection_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
collection_method | How the biomaterial was collected. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Collection method |  | blood draw
protocol_reagents | A list of purchased reagents used in this protocol. | array | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Protocol reagents |  | 

## Differentiation protocol
_Information about how a cell is differentiated to a desired cell type or organoid._

Location: type/protocol/biomaterial_collection/differentiation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
differentiation_method | Differentiation method applied to cell culture to induce a specific differentiation response. | string | yes |  | Differentiation method |  | Embryoid Body, Monolayer, Inductive Co-Culture
media | Culture media used to induce a specific differentiation response. | string | no |  | Differentiation media |  | RPMI 1640 + B27, Neurobasal Media, StemPro-34 Serum-Free Medium
small_molecules | Differentiation small molecules added to stem cell medium to induce a specific differentiation response. | string | no |  | Small molecules |  | Retinoic Acid, CHIR99021 (GSK-inhibitor), Activin A, BMP4
target_cell_yield | Percent of target cells obtained after directed differentiation of origin cell. | number | no |  | Percent target cell yield |  | 95
reagents | A list of purchased reagents used in the differentiation protocol. | array | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Differentiation reagents |  | 
target_pathway | Targeted pathway for specific differentiation response. | string | no |  | Target pathway |  | Wnt Pathway
validation_method | Method used to validate origin cell successfully differentiated to target cell. | string | no |  | Differentiation validation method |  | Pancreatic Cell DTZ Detection Assay, qPCR, Flow Cytometry, Immunocytochemistry Staining
validation_result | Result confirming successful differentiation to target cell type. | string | no |  | Validation result |  | CD103 Positive, Nestin Positive, HCN4 Positive, CD11C Negative

## Dissociation protocol
_Information about the dissociation protocol used to separate individual cells or nuclei._

Location: type/protocol/biomaterial_collection/dissociation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
dissociation_method | How cells or organelles were dissociated. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Dissociation method |  | enzymatic dissociation
protocol_reagents | A list of purchased reagents used in this protocol. | array | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Protocol reagents |  | 

## Enrichment protocol
_Information about how a biomaterial is enriched for a feature or characteristic of interest._

Location: type/protocol/biomaterial_collection/enrichment_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
enrichment_method | The method by which enrichment was achieved. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Enrichment method |  | fluorescence-activated cell sorting
markers | A space-delimited list of markers with +/-. | string | no |  | Markers |  | CD4+ CD8-
min_size_selected | Minimum cell or organelle size passing selection, in microns. | number | no |  | Minimum size selected |  | 70
max_size_selected | Maximum cell or organelle size passing selection, in microns. | number | no |  | Maximum size selected |  | 90

## iPCS induction protocol
_Information about how a biomaterial is treated to become an induced pluripotent stem cell._

Location: type/protocol/biomaterial_collection/ipsc_induction_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
ipsc_induction_method | Induction method applied to primary cell culture to induce pluripotent stem cell generation. | string | yes |  | Induction method | lentivirus, sendai virus, Gun particle, piggyBac transposon, miRNA viral, adenovirus, cre-loxP, plasmid, retroviral | piggyBac transposon
ipsc_induction_factors | Induction factors added to primary cell culture to induce pluripotency. | string | no |  | Induction factors |  | POU5F1, SOX2, KLF4, c-MYC
ipsc_induction_kit | Kit used to induce pluripotent stem cell generation. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Induction kit |  | 
pluripotency_test | Description of how pluripotency was tested in induced pluripotent stem cells. | string | no |  | Pluripotency test |  | teratoma assay
percent_pluripotency | Percent of iPSCs that passed the pluripotency test. | number | no |  | Percent pluripotency |  | 97.2
pluripotency_vector_removed | Whether a viral vector was removed after induction. | string | no |  | Pluripotent vector removed? | yes, no, unknown | Should be one of: yes, no, or unknown.
ipsc_induction_produced_in_house | Whether the induced pluripotent stem cell was prepared in-house. | boolean | no |  | iPSC prepared in-house? |  | Should be one of: yes, no.
protocol_reagents | A list of additional purchased reagents used in this protocol. | array | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Additional protocol reagents |  | 

## Imaging preparation protocol
_Information about the preparation protocol of the imaged specimen used in an imaging experiment_

Location: type/protocol/imaging/imaging_preparation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
fresh_slicing_method | The method by which fresh tissue was sliced (e.g. vibrotome) | string | no |  | Fresh slicing method |  | vibrotome
imaged_slice_thickness | Thickness of the imaged slice in micrometres. | number | no |  | Imaged slice thickness |  | 10
final_slicing_method | The method by which the final slice was obtained (e.g. cryosectioning). | string | no |  | Final slicing method |  | cryosectioning
post_resection_interval | Length of time between surgical resection and fresh slicing of tissue. | number | no |  | Time between resection and fresh slicing |  | 5
post_resection_interval_unit | The unit of time in which the post resection interval is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Post resection interval time unit |  | day
pre_final_slice_preservation_method | Tissue preservation method used prior to final slicing (e.g. freezing). | object | no | [See module  preservation_storage](module.md/#preservation_storage) | Pre-final slice preservation method |  | 
post_final_slicing_interval | Length of time between secondary slicing and hybridization. | number | no |  | Post final slicing interval |  | 7
post_final_slicing_interval_unit | The unit of time in which the post final slicing interval is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Post final slicing interval time unit |  | day
fiducial_marker | Fiducial markers for the alignment of images taken across multiple rounds of imaging. | string | no |  | Fiducial marker |  | beads
expansion_factor | Factor by which the imaged tissue was expanded. | number | no |  | Expansion factor |  | 3

## Imaging Protocol
_Information about the imaging protocol_

Location: type/protocol/imaging/imaging_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
microscope_setup_description | Description of the microscope setup including manufacturer and model information about the stand, camera and objective. | string | no |  | Microscope setup description |  | Motorized stage (SCAN IM 112 × 74, Marzhauser), sCMOS camera (Zyla 4.2; Andor), 60x, Plan-Apo, 1.3 NA, silicone oil objective (UPLSAPO60XS2; Olympus).
microscopy_technique | The type of microscopy. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | yes | [See module  microscopy_ontology](module.md/#microscopy_ontology) | Microscopy technique |  | 
magnification | Magnification of the objective used for imaging. | string | yes |  | Magnification |  | 60x
numerical_aperture | Numerical aperture of the objective. | number | yes |  | Numerical aperture |  | 1.3
immersion_medium_type | Immersion medium used for imaging. | string | no |  | Immersion medium |  | oil
immersion_medium_refractive_index | Refractive index of the immersion medium used for imaging. | number | no |  | Refractive index of the immersion medium |  | 1.5
pixel_size | Pixel size in nanometres (scaling factor). | number | yes |  | Pixel size |  | 109
number_of_tiles | Number of XY tiles in the experiment. | integer | no |  | Number of tiles |  | 2000
tile_size_y | Y size of the tile in micrometres. | number | no |  | Tile size Y |  | 
tile_size_x | X size of the tile in micrometres. | number | no |  | Tile size X |  | 
z_stack_step_size | Z-stack step size in nanometres. | number | no |  | Z stack step size |  | 200
number_of_z_steps | Number of steps in a Z stack. | integer | no |  | Number of Z steps |  | 40
overlapping_tiles | Were tiles collected with overlap? | string | yes |  | Overlapping tiles? | yes, no | no
channel | Information about each channel used in the imaging protocol. | array | yes | [See module  channel](module.md/#channel) | Channel |  | 
imaging_target | Information about each imaging target in the imaging experiment. | array | yes | [See module  imaging_target](module.md/#imaging_target) | Imaging target |  | 

## Library preparation protocol
_Information about how a sequencing library was prepared._

Location: type/protocol/sequencing/library_preparation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
cell_barcode | Information about cell identifier barcodes. | object | no | [See module  barcode](module.md/#barcode) | Cell barcode |  | 
input_nucleic_acid_molecule | Starting nucleic acid molecule isolated for sequencing. | object | yes | [See module  biological_macromolecule_ontology](module.md/#biological_macromolecule_ontology) | Input nucleic acid molecule |  | polyA RNA
nucleic_acid_source | Source cells or organelles from which nucleic acid molecules were collected. | string | no |  | Nucleic acid source | bulk cell, single cell, single nucleus, bulk nuclei, mitochondria | Should be one of: bulk cell, single cell, single nucleus, bulk nuclei, or mitochondria.
library_construction_approach | The general approach for sequencing library construction. | object | yes | [See module  library_construction_ontology](module.md/#library_construction_ontology) | Library construction approach |  | Smart-seq2
library_construction_kit | Name of kit used to construct the sequencing library. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Library construction kit |  | 
nucleic_acid_conversion_kit | Name of kit used to convert RNA to DNA for sequencing. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Nucleic acid conversion kit |  | 
end_bias | The type of tag or end bias the library has. | string | yes |  | End bias | 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, full length | Should be one of: 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, or full length.
primer | Primer used for cDNA synthesis from RNA. | string | no |  | Primer | poly-dT, random | Should be one of: poly-dT, or random.
strand | Library strandedness. | string | yes |  | Strand | first, second, unstranded, not provided | Should be one of: first, second, or unstranded.
spike_in_kit | Information about a spike-in kit, if used. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Spike-in kit |  | 
spike_in_dilution | Dilution of spike-in, if used. | integer | no |  | Spike-in dilution |  | 100
umi_barcode | Information about unique molecular identifier (UMI) barcodes. | object | no | [See module  barcode](module.md/#barcode) | UMI barcode |  | 
library_preamplification_method | The method used to amplify RNA prior to adaptor ligation. | object | no | [See module  library_amplification_ontology](module.md/#library_amplification_ontology) | Library pre-amplification method |  | PCR
cdna_library_amplification_method | The method used to amplify a cDNA library prior to sequencing. | object | no | [See module  library_amplification_ontology](module.md/#library_amplification_ontology) | cDNA library amplification method |  | PCR

## Sequencing protocol
_Information about the sequencing protocol._

Location: type/protocol/sequencing/sequencing_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
instrument_manufacturer_model | The manufacturer and model of the sequencer used. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0000548. | object | yes | [See module  instrument_ontology](module.md/#instrument_ontology) | Instrument manufacturer and model |  | Illumina HiSeq 4000
local_machine_name | Local name for the particular machine on which the biomaterial was sequenced. | string | no |  | Local machine name |  | Machine1
paired_end | Was the sequenced molecule sequenced from both ends? | boolean | yes |  | Paired end? |  | Should be one of: yes, no.
sequencing_approach | The general approach for sequencing. | object | yes | [See module  sequencing_ontology](module.md/#sequencing_ontology) | Sequencing approach |  | full length single cell RNA sequencing
10x | Fields specific for 10x experiments. | object | no | [See module  10x](module.md/#10x) | 10x-specific |  | 

