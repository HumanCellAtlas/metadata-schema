# Type
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## Project
_A project entity contains information about the overall project._

Location: type/project/project.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
geo_series | GEO accession number, if data has been submitted. Accession must start with GSE. | string | no |  | GEO series accession |  | GSE00000
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
insdc_project | An INSDC (International Nucleotide Sequence Database Collaboration) project accession, if project has been submitted. Can be from the DDBJ, NCBI, or EMBL-EBI. Accession must start with DRP, SRP, or ERP. | string | no |  | INSDC project accession |  | SRP000000
schema_type | The type of the metadata schema entity. | string | yes |  |  | project | 
insdc_study | An INSDC (International Nucleotide Sequence Database Collaboration) study accession if study has been submitted. Can be from the DDBJ, EMBL-EBI, or NCBI. Accession must start with PRJE, PRJN, or PRJD. | string | no |  | INSDC study accession |  | PRJNA000000
array_express_investigation | EBI ArrayExpress accession number, if data has been submitted. | string | no |  | ArrayExpress accession |  | E-AAAA-00
funders | A list of funding source(s) supporting the project. | array | no | [See module  funder](module.md/#funder) | Project funding source(s) |  | 
project_core | Core project-level information. | object | no | [See core  project_core](core.md/#project_core) |  |  | 
contributors | List of people contributing to any aspect of the project. | array | no | [See module  contact](module.md/#contact) | Contributors |  | 
publications | A list of publications resulting from this project. | array | no | [See module  publication](module.md/#publication) | Publications |  | 
supplementary_links | External link(s) pointing to code, supplementary data files, or analysis files associated with the project which will not be uploaded. | array | no |  | Supplementary link(s) |  | https://github.com/czbiohub/tabula-muris

## Cell suspension
_Information about the suspension of cells or nuclei derived from the collected or cultured specimen._

Location: type/biomaterial/cell_suspension.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
cell_morphology | Features relating to the morphology of cells in a biomaterial. | object | no | [See module  cell_morphology](module.md/#cell_morphology) | Cell morphology |  | 
genus_species | The scientific binomial name for the species of the suspension. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
selected_cell_type | The cell type(s) selected to be present in the suspension. | array | no | [See module  cell_type_ontology](module.md/#cell_type_ontology) | Selected cell type |  | fetal cardiomyocyte
plate_based_sequencing | Fields specific for plate-based sequencing experiments. | object | no | [See module  plate_based_sequencing](module.md/#plate_based_sequencing) | Plate-based sequencing |  | 
growth_conditions | Features relating to the growth and/or maintenance of a biomaterial. | object | no | [See module  growth_conditions](module.md/#growth_conditions) | Growth conditions |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
total_estimated_cells | Total estimated number of cells in the suspension. May be 1 for well-based assays. | integer | no |  | Total estimated cell count |  | 2100
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 

## Cell line
_Information about the cell line or cell culture biomaterial._

Location: type/biomaterial/cell_line.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
publications | One or more publications in which the cell line creation was cited. | array | no | [See module  publication](module.md/#publication) | Cell line publications |  | 
cell_line_type | The type of cell line. | string | yes |  | Cell line type | primary, immortalized, stem cell-derived, synthetic, induced pluripotent, stem cell | Should be one of: primary, immortalized, stem cell, stem cell-derived, induced pluripotent, or synthetic.
tissue | The tissue that the cell line was derived from. | object | no | [See module  organ_part_ontology](module.md/#organ_part_ontology) | Tissue |  | bone marrow
genus_species | The scientific binomial name for the species of the cell line. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
cell_type | The cell type that the cell line represents. | object | no | [See module  cell_type_ontology](module.md/#cell_type_ontology) | Cell type |  | cardiac muscle cell
karyotype | The karyotype of the cell line. | string | no |  | Karyotype |  | 
confluency | The percent a plate surface is covered by cells. | number | no |  | Percent confluency |  | 60
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
catalog_url | The supplier catalogue URL for the cell line. | string | no |  | Catalog URL |  | 
cell_morphology | Features relating to the morphology of the cells. | object | no | [See module  cell_morphology](module.md/#cell_morphology) | Cell morphology |  | 
disease | Short description of any disease association to the cell type. | object | no | [See module  disease_ontology](module.md/#disease_ontology) | Disease |  | bone squamous cell carcinoma
date_established | When the cell line was established, in date-time format. yyyy-mm-ddThh:mm:ssZ. | string | no |  | Date established |  | 2017-03-19
supplier | The supplier of the cell line. | string | no |  | Supplier |  | HipSci
lot_number | The supplier lot or batch number for the cell line. | string | no |  | Lot/batch number |  | 24.10.14
growth_conditions | Features relating to the growth and/or maintenance of the cell lines. | object | no | [See module  growth_conditions](module.md/#growth_conditions) | Growth conditions |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
cell_cycle | The cell cycle phase if the cell line is synchronized growing cells or the phase is known. | object | no | [See module  cell_cycle_ontology](module.md/#cell_cycle_ontology) | Cell cycle |  | mitotic cell cycle
catalog_number | The supplier catalogue number for the cell line. | string | no |  | Catalog number |  | 77650057
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 

## Organoid
_Information about an organoid biomaterial._

Location: type/biomaterial/organoid.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
organoid_age | Age of the organoid in Organoid age unit. Measured from when cell aggregates started differentiating to desired organoid model. | number | no |  | Organoid age |  | 55
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
input_aggregate_cell_count | Estimated number of cells per input cell aggregate. | number | no |  | Input aggregate cell count |  | 10000
organoid_size | Size of the organoid in Organoid size unit. | number | no |  | Organoid size |  | 4
organoid_growth_environment | Growth environment in which the organoid is grown. | string | no |  | Organoid growth environment |  | matrigel, liquid suspension, adherent
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
organoid_age_unit | The unit in which Organoid age is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Organoid age unit |  | Should be one of: minute, hour, day, week, month, or year.
model_for_organ | Organ for which this organoid is a model system. | object | yes | [See module  organ_ontology](module.md/#organ_ontology) | Organ model |  | brain
organoid_size_unit | The unit in which the Organoid size is expressed. | object | no | [See module  length_unit_ontology](module.md/#length_unit_ontology) | Organoid size unit |  | millimeter
model_organ_part | Organ part for which this organoid is a model system. | object | no | [See module  organ_part_ontology](module.md/#organ_part_ontology) | Organ part model |  | cortex
organoid_stored_oxygen_levels | Percent oxygen level organoid was stored in prior to sequencing. | number | no |  | Organoid stored oxygen level |  | 75
organoid_type | The type of organoid. | string | no |  | Organoid type | primary, immortalized, stem cell-derived, synthetic | Should be one of: primary, immortalized, stem cell-derived, or synthetic.
organoid_morphology | General description of the organoid morphology. | string | no |  |  |  | Epithelial monolayer with budding crypt-like domains.
embedded_in_matrigel | Whether the organoid is embedded in a matrigel. | boolean | no |  | Organoid embeddded in matrigel? |  | Should be one of: yes, no.
genus_species | The scientific binomial name for the species of the organoid. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 

## Donor organism
_Information about the donor organism from which a specimen was collected._

Location: type/biomaterial/donor_organism.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
height | Height of organism in Height unit. | string | no |  | Height |  | 160
normothermic_regional_perfusion | Yes if entire body (but not limbs) was perfused with warm oxygenated blood. No otherwise. | string | no |  | Normothermic regional perfusion? | yes, no, unknown | Should be one of: yes, no, or unknown.
weight | Weight of organism in Weight unit. | string | no |  | Weight |  | 60
organism_age_unit | The unit in which Organism age is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Organism age unit |  | Should be one of: hour, day, week, month, or year.
familial_relationship | Information about other organisms related to this organism. | array | no | [See module  familial_relationship](module.md/#familial_relationship) | Familial relationship |  | 
human_specific | Fields specific to human (homo sapiens) organisms. | object | no | [See module  human_specific](module.md/#human_specific) | Human-specific |  | 
gestational_age_unit | The unit in which Gestational age is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Gestational age unit |  | Should be one of: hour, day, week, month, or year.
development_stage | A classification of the developmental stage of the organism. | object | no | [See module  development_stage_ontology](module.md/#development_stage_ontology) | Development stage |  | adult
genus_species | The scientific binomial name for the species of the organism. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
weight_unit | The unit in which Weight is expressed. | object | no | [See module  mass_unit_ontology](module.md/#mass_unit_ontology) | Weight unit |  | kilogram
sex | The biological sex of the organism. | string | yes |  | Biological sex | female, male, mixed, unknown | Should be one of: male, female, mixed, or unknown.
death | Information about conditions of death of the organism. | object | no | [See module  death](module.md/#death) | Death conditions |  | 
mouse_specific | Fields specific to mouse (mus musculus) organisms. | object | no | [See module  mouse_specific](module.md/#mouse_specific) | Mouse-specific |  | 
gestational_age | Gestational age of organism in Gestational age unit. Measured since fertilization. | string | no |  | Gestational age |  | 5-7
is_living | Yes if organism is alive at time of biomaterial collection. No if dead. Unknown if not known. | string | yes |  | Is living? | yes, no, unknown | Should be one of: yes, no, unknown.
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
height_unit | The unit in which Height is expressed. | object | no | [See module  length_unit_ontology](module.md/#length_unit_ontology) | Height unit |  | centimeter
diseases | Short description of known disease(s) of the organism. Enter 'normal' if no known disease. | array | no | [See module  disease_ontology](module.md/#disease_ontology) | Known disease(s) |  | bone squamous cell carcinoma
organism_age | Age of organism in Organism age unit. Measured since birth. | string | no |  | Organism age |  | 20
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
medical_history | Information about the medical history of the organism. | object | no | [See module  medical_history](module.md/#medical_history) | Medical history |  | 
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 

## Imaged specimen
_Information about a tissue specimen after it has been sectioned and prepared for imaging._

Location: type/biomaterial/imaged_specimen.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
internal_anatomical_structures | Internal (landmark) structures visible in the overview image that are informative about the broader anatomical context/location of the sample. | array | no | [See module  organ_part_ontology](module.md/#organ_part_ontology) | Internal tissue structures |  | 
overview_image | List of filenames of photographs of specimen. Must be of format JPEG, TIFF, or PNG. | array | no |  | Gross image |  | my_mage_file.jpg
imaged_slice_thickness | Thickness of the imaged slice in micrometres. | number | yes |  | Imaged slice thickness |  | 14
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 

## Specimen from organism
_Information about the specimen that was collected from the donor organism._

Location: type/biomaterial/specimen_from_organism.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
state_of_specimen | State of the specimen at the time of collection. | object | no | [See module  state_of_specimen](module.md/#state_of_specimen) | State of specimen |  | 
purchased_specimen | Information about a purchased specimen. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Purchased specimen |  | 
organ_part | A term for a specific part of the organ that the biomaterial came from. | object | no | [See module  organ_part_ontology](module.md/#organ_part_ontology) | Organ part |  | umbilical cord blood
organ | The organ that the biomaterial came from. Blood and connective tissue are considered organs. | object | yes | [See module  organ_ontology](module.md/#organ_ontology) | Organ |  | blood
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
collection_time | When the biomaterial was collected, in date-time format, yyyy-mm-ddThh:mm:ssZ. | string | no |  | Time of collection |  | 2017-03-19T07:22:00Z
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
diseases | Short description of known disease(s) of the specimen. Enter normal if no known disease. | array | no | [See module  disease_ontology](module.md/#disease_ontology) | Known disease(s) |  | bone squamous cell carcinoma
genus_species | The scientific binomial name for the species of the specimen. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
preservation_storage | Information about how a specimen was preserved and/or stored over a period of time. | object | no | [See module  preservation_storage](module.md/#preservation_storage) | Preservation/Storage |  | 

## Process
_Information about the process_

Location: type/process/process.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
process_core | Core process-level information. | object | yes | [See core  process_core](core.md/#process_core) |  |  | 
length_of_time | Length of time the process took to execute, from start to finish, in Length of time unit. | string | no |  | Length of time |  | 10
schema_type | The type of the metadata schema entity. | string | yes |  |  | process | 
length_of_time_unit | The unit in which Length of time is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Length of time unit |  | Should be one of: microsecond, second, minute, hour, day, week, month, or year.
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
deviation_from_protocol | Any deviation from the protocol provided. | string | no |  | Deviation from protocol |  | 
process_type | The type of process. | object | no | [See module  process_type_ontology](module.md/#process_type_ontology) | Process type |  | sample enrichment
insdc_experiment | An INSDC (International Nucleotide Sequence Database Collaboration) experiment accession. | object | no | [See module  insdc_experiment](module.md/#insdc_experiment) | INSDC experiment |  | 

## Analysis process
_Information about the analysis process_

Location: type/process/analysis/analysis_process.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
reference_bundle | Bundle containing the reference used in running the pipeline. | string | yes |  | Reference bundle |  | 
timestamp_stop_utc | Terminal stop time of the full pipeline in UTC. | string | yes |  | Stop timestamp (UTC) |  | 
input_bundles | The input bundles used in this analysis run. | array | yes |  | Input bundles |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | process | 
analysis_run_type | Indicator of whether the analysis actually ran or was just copied forward as an optimization. | string | yes |  | Analysis run type | run, copy-forward | 
process_core | Core process-level information. | object | yes | [See core  process_core](core.md/#process_core) |  |  | 
outputs | Output generated by the pipeline run. | array | yes | [See   analysis_file](.md/#analysis_file) | Outputs |  | 
inputs | Input parameters used in the pipeline run, these can be files or string values (settings). | array | yes |  | Input parameters |  | 
process_type | The type of process. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Process type |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
tasks | Descriptions of tasks in the workflow. | array | yes |  | Workflow tasks |  | 
timestamp_start_utc | Initial start time of the full pipeline in UTC. | string | yes |  | Start timestamp (UTC) |  | 

## Protocol
_Information about the protocol._

Location: type/protocol/protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
protocol_type | The type of protocol. | object | no | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | sample enrichment
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 

## Imaging preparation protocol
_Information about the preparation protocol of the imaged specimen used in an imaging experiment_

Location: type/protocol/imaging/imaging_preparation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
imaged_slice_thickness | Thickness of the imaged slice in micrometres. | number | no |  | Imaged slice thickness |  | 10
final_slicing_method | The method by which the final slice was obtained (e.g. cryosectioning). | string | no |  | Final slicing method |  | cryosectioning
post_resection_interval | Length of time between surgical resection and fresh slicing of tissue. | number | no |  | Time between resection and fresh slicing |  | 5
pre_final_slice_preservation_method | Tissue preservation method used prior to final slicing (e.g. freezing). | object | no | [See module  preservation_storage](module.md/#preservation_storage) | Pre-final slice preservation method |  | 
post_final_slicing_interval | Length of time between secondary slicing and hybridization. | number | no |  | Post final slicing interval |  | 7
post_final_slicing_interval_unit | The unit of time in which the post final slicing interval is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Post final slicing interval time unit |  | day
fiducial_marker | Fiducial markers for the alignment of images taken across multiple rounds of imaging. | string | no |  | Fiducial marker |  | beads
fresh_slicing_method | The method by which fresh tissue was sliced (e.g. vibrotome) | string | no |  | Fresh slicing method |  | vibrotome
expansion_factor | Factor by which the imaged tissue was expanded. | number | no |  | Expansion factor |  | 3
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
post_resection_interval_unit | The unit of time in which the post resection interval is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Post resection interval time unit |  | day
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 

## Imaging Protocol
_Information about the imaging protocol_

Location: type/protocol/imaging/imaging_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
microscopy_technique | The type of microscopy. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | yes | [See module  microscopy_ontology](module.md/#microscopy_ontology) | Microscopy technique |  | 
tile_size_x | X size of the tile in micrometres. | number | no |  | Tile size X |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
imaging_target | Information about each imaging target in the imaging experiment. | array | yes | [See module  imaging_target](module.md/#imaging_target) | Imaging target |  | 
immersion_medium_type | Immersion medium used for imaging. | string | no |  | Immersion medium |  | oil
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
magnification | Magnification of the objective used for imaging. | string | yes |  | Magnification |  | 60x
microscope_setup_description | Description of the microscope setup including manufacturer and model information about the stand, camera and objective. | string | no |  | Microscope setup description |  | Motorized stage (SCAN IM 112 × 74, Marzhauser), sCMOS camera (Zyla 4.2; Andor), 60x, Plan-Apo, 1.3 NA, silicone oil objective (UPLSAPO60XS2; Olympus).
immersion_medium_refractive_index | Refractive index of the immersion medium used for imaging. | number | no |  | Refractive index of the immersion medium |  | 1.5
overlapping_tiles | Were tiles collected with overlap? | string | yes |  | Overlapping tiles? | yes, no | no
channel | Information about each channel used in the imaging protocol. | array | yes | [See module  channel](module.md/#channel) | Channel |  | 
z_stack_step_size | Z-stack step size in nanometres. | number | no |  | Z stack step size |  | 200
number_of_tiles | Number of XY tiles in the experiment. | integer | no |  | Number of tiles |  | 2000
number_of_z_steps | Number of steps in a Z stack. | integer | no |  | Number of Z steps |  | 40
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
pixel_size | Pixel size in nanometres (scaling factor). | number | yes |  | Pixel size |  | 109
tile_size_y | Y size of the tile in micrometres. | number | no |  | Tile size Y |  | 
numerical_aperture | Numerical aperture of the objective. | number | yes |  | Numerical aperture |  | 1.3

## Sequencing protocol
_Information about the sequencing protocol._

Location: type/protocol/sequencing/sequencing_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
paired_end | Was a paired-end sequencing strategy used? | boolean | yes |  | Paired end? |  | Should be one of: yes, no.
instrument_manufacturer_model | The manufacturer and model of the sequencer used. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0000548. | object | yes | [See module  instrument_ontology](module.md/#instrument_ontology) | Instrument manufacturer and model |  | Illumina HiSeq 4000
local_machine_name | Local name for the particular machine on which the biomaterial was sequenced. | string | no |  | Local machine name |  | Machine1
10x | Fields specific for 10x experiments. | object | no | [See module  10x](module.md/#10x) | 10x-specific |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
sequencing_approach | The general approach for sequencing. | object | yes | [See module  sequencing_ontology](module.md/#sequencing_ontology) | Sequencing approach |  | full length single cell RNA sequencing
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 

## Library preparation protocol
_Information about how a sequencing library was prepared._

Location: type/protocol/sequencing/library_preparation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
nucleic_acid_source | Source cells or organelles from which nucleic acid molecules were collected. | string | no |  | Nucleic acid source | bulk cell, single cell, single nucleus, bulk nuclei, mitochondria | Should be one of: bulk cell, single cell, single nucleus, bulk nuclei, or mitochondria.
library_preamplification_method | The method used to amplify RNA prior to adaptor ligation. | object | no | [See module  library_amplification_ontology](module.md/#library_amplification_ontology) | Library pre-amplification method |  | PCR
input_nucleic_acid_molecule | Starting nucleic acid molecule isolated for sequencing. | object | yes | [See module  biological_macromolecule_ontology](module.md/#biological_macromolecule_ontology) | Input nucleic acid molecule |  | polyA RNA
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
spike_in_dilution | Dilution of spike-in, if used. | integer | no |  | Spike-in dilution |  | 100
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
library_construction_kit | Name of kit used to construct the sequencing library. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Library construction kit |  | 
end_bias | The type of tag or end bias the library has. | string | yes |  | End bias | 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, full length | Should be one of: 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, or full length.
cdna_library_amplification_method | The method used to amplify a cDNA library prior to sequencing. | object | no | [See module  library_amplification_ontology](module.md/#library_amplification_ontology) | cDNA library amplification method |  | PCR
library_construction_approach | The general approach for sequencing library construction. | object | yes | [See module  library_construction_ontology](module.md/#library_construction_ontology) | Library construction approach |  | Smart-seq2
umi_barcode | Information about unique molecular identifier (UMI) barcodes. | object | no | [See module  barcode](module.md/#barcode) | UMI barcode |  | 
cell_barcode | Information about cell identifier barcodes. | object | no | [See module  barcode](module.md/#barcode) | Cell barcode |  | 
strand | Library strandedness. | string | yes |  | Strand | first, second, unstranded | Should be one of: first, second, or unstranded.
primer | Primer used for cDNA synthesis from RNA. | string | no |  | Primer | poly-dT, random | Should be one of: poly-dT, or random.
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
spike_in_kit | Information about a spike-in kit, if used. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Spike-in kit |  | 
nucleic_acid_conversion_kit | Name of kit used to convert RNA to DNA for sequencing. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Nucleic acid conversion kit |  | 

## Enrichment protocol
_Information about how a biomaterial is enriched for a feature or characteristic of interest._

Location: type/protocol/biomaterial_collection/enrichment_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
min_size_selected | Minimum cell or organelle size passing selection, in microns. | number | no |  | Minimum size selected |  | 70
max_size_selected | Maximum cell or organelle size passing selection, in microns. | number | no |  | Maximum size selected |  | 90
enrichment_method | The method by which enrichment was achieved. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Enrichment method |  | fluorescence-activated cell sorting
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
markers | A space-delimited list of markers with +/-. | string | no |  | Markers |  | CD4+ CD8-
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 

## Aggregate generation protocol
_Information about how cultured cells are developed into cell aggregates._

Location: type/protocol/biomaterial_collection/aggregate_generation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
aggregate_formation_method | Method used to form cell aggreagtes. | string | yes |  | Aggregate formation method |  | rocking, suspension cultures, hanging drops, spinner flasks
aggregate_cell_uniformity | Description of uniformity of the cell aggregates after they are formed. | string | no |  | Aggregate cell uniformity |  | Mostly homogenous EBs of variable cell numbers
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 

## iPCS induction protocol
_Information about how a biomaterial is treated to become an induced pluripotent stem cell._

Location: type/protocol/biomaterial_collection/ipsc_induction_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
ipsc_induction_method | Induction method applied to primary cell culture to induce pluripotent stem cell generation. | string | yes |  | Induction method | lentivirus, sendai virus, Gun particle, piggyBac transposon, miRNA viral, adenovirus, cre-loxP, plasmid, retroviral | piggyBac transposon
ipsc_induction_kit | Kit used to induce pluripotent stem cell generation. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Induction kit |  | 
pluripotency_vector_removed | Whether a viral vector was removed after induction. | string | no |  | Pluripotent vector removed? | yes, no, unknown | Should be one of: yes, no, or unknown.
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
percent_pluripotency | Percent of iPSCs that passed the pluripotency test. | number | no |  | Percent pluripotency |  | 97.2
pluripotency_test | Description of how pluripotency was tested in induced pluripotent stem cells. | string | no |  | Pluripotency test |  | teratoma assay
ipsc_induction_factors | Induction factors added to primary cell culture to induce pluripotency. | string | no |  | Induction factors |  | POU5F1, SOX2, KLF4, c-MYC
ipsc_induction_produced_in_house | Whether the induced pluripotent stem cell was prepared in-house. | boolean | no |  | iPSC prepared in-house? |  | Should be one of: yes, no.
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_reagents | A list of additional purchased reagents used in this protocol. | array | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Additional protocol reagents |  | 

## Dissociation protocol
_Information about the dissociation protocol used to separate individual cells or nuclei._

Location: type/protocol/biomaterial_collection/dissociation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
dissociation_method | How cells or organelles were dissociated. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Dissociation method |  | enzymatic dissociation
protocol_reagents | A list of purchased reagents used in this protocol. | array | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Protocol reagents |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 

## Differentiation protocol
_Information about how a cell is differentiated to a desired cell type or organoid._

Location: type/protocol/biomaterial_collection/differentiation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
media | Culture media used to induce a specific differentiation response. | string | no |  | Differentiation media |  | RPMI 1640 + B27, Neurobasal Media, StemPro-34 Serum-Free Medium
target_cell_yield | Percent of target cells obtained after directed differentiation of origin cell. | number | no |  | Percent target cell yield |  | 95
reagents | A list of purchased reagents used in the differentiation protocol. | array | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Differentiation reagents |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
validation_result | Result confirming successful differentiation to target cell type. | string | no |  | Validation result |  | CD103 Positive, Nestin Positive, HCN4 Positive, CD11C Negative
target_pathway | Targeted pathway for specific differentiation response. | string | no |  | Target pathway |  | Wnt Pathway
small_molecules | Differentiation small molecules added to stem cell medium to induce a specific differentiation response. | string | no |  | Small molecules |  | Retinoic Acid, CHIR99021 (GSK-inhibitor), Activin A, BMP4
validation_method | Method used to validate origin cell successfully differentiated to target cell. | string | no |  | Differentiation validation method |  | Pancreatic Cell DTZ Detection Assay, qPCR, Flow Cytometry, Immunocytochemistry Staining
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
differentiation_method | Differentiation method applied to cell culture to induce a specific differentiation response. | string | yes |  | Differentiation method |  | Embryoid Body, Monolayer, Inductive Co-Culture
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 

## Collection protocol
_Information about the biomaterial collection protocol._

Location: type/protocol/biomaterial_collection/collection_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
protocol_reagents | A list of purchased reagents used in this protocol. | array | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Protocol reagents |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
collection_method | How the biomaterial was collected. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Collection method |  | blood draw
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 

## Analysis protocol
_Information about the analysis protocol._

Location: type/protocol/analysis/analysis_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
computational_method | A URI to a versioned workflow and versioned execution environment in a GA4GH-compliant repository. | string | yes |  | Computational method |  | 
protocol_type | The type of protocol. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 

## Reference file
_A reference file used by a secondary reference pipeline._

Location: type/file/reference_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
genus_species | The scientific binomial name for the species of this reference. | object | yes | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
reference_version | The genome version of the reference. | string | yes |  | Reference version |  | GencodeV27
reference_type | The type of the genome reference. | string | yes |  | Reference type | genome sequence, transcriptome sequence, annotation reference, transcriptome index, genome sequence index | Should be one of: genome sequence, transcriptome sequence, annotation reference, transcriptome index, or genome sequence index.
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | integer | yes |  | NCBI taxon ID |  | 9606
assembly_type | The assembly type of the reference. This applies to reference genome sequences. | string | yes |  | Assembly type | primary assembly, complete assembly, patch assembly | Should be one of: primary assembly, complete assembly, or patch assembly.

## Sequence file
_A file of read sequences generated by a sequencing experiment._

Location: type/file/sequence_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
technical_replicate_group | A project wide unique label to indicate which groups of files are technical replicates. Technical replicates are sequence files generated from the same sequencing library. Leave blank if files are biological replicates. | string | no |  | Technical replicate group |  | tech_rep_group_001
lane_index | The index of the lane that this file was sequenced from. | integer | no |  | Lane index |  | 1
read_index | Whether the read file contains the read1, read2, index1, or index2 part of the sequencing read or represents a single-end, non-indexed library. | string | yes |  | Read index | read1, read2, index1, index2, single-end, non-indexed | Should be one of: read1, read2, index1, index2, or 'single-end, non-indexed'
read_length | The length of a sequenced read in this file, in nucleotides. | integer | no |  | Read length |  | 51
insdc_run | An INSDC (International Nucleotide Sequence Database Collaboration) run accession. Can be from the DDBJ, NCBI, or EMBL-EBI. Accession must start with DRR, SRR, or ERR. | array | no |  | INSDC run |  | SRR0000000
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 

## Analysis file
_A file analysis results produced by a secondary analysis pipeline._

Location: type/file/analysis_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 

## Image file
_Information about an image file generated by an imaging experiment._

Location: type/file/image_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 

## Supplementary file
_Supplementary files belonging to a project._

Location: type/file/supplementary_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
file_description | A short description of the file content. This could include information about how the file was generated. | string | no |  | File description |  | Enrichment protocol

