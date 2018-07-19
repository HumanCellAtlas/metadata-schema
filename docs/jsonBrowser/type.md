# Type
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## project
_A project entity contains information about the overall project._

Location: type/project/project.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
project_core | Core project-level information. | object | no | [See core  project_core](core.md/#project_core) |  |  | 
insdc_study | An INSDC (International Nucleotide Sequence Database Collaboration) study accession if study has been submitted. Can be from the DDBJ, EMBL-EBI, or NCBI. Accession must start with PRJE, PRJN, or PRJD. | string | no |  | INSDC study accession |  | PRJNA000000
contributors | List of people contributing to any aspect of the project. | array | no | [See module  contact](module.md/#contact) | Contributors |  | 
publications | A list of publications resulting from this project. | array | no | [See module  publication](module.md/#publication) | Publications |  | 
geo_series | GEO accession number, if data has been submitted. Accession must start with GSE. | string | no |  | GEO series accession |  | GSE00000
insdc_project | An INSDC (International Nucleotide Sequence Database Collaboration) project accession, if project has been submitted. Can be from the DDBJ, NCBI, or EMBL-EBI. Accession must start with DRP, SRP, or ERP. | string | no |  | INSDC project accession |  | SRP000000
funders | A list of funding source(s) supporting the project. | array | no | [See module  funder](module.md/#funder) | Project funding source(s) |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | project | 
array_express_investigation | EBI ArrayExpress accession number, if data has been submitted. | string | no |  | ArrayExpress accession |  | E-AAAA-00
supplementary_files | Project-level supplementary files. | array | no |  | Project supplementary files |  | For example, experimental documents, photos, etc. Please list the file names, separated by double pipes. You will be asked to upload these files separately.

## cell_suspension
_Information about the suspension of cells or nuclei derived from the collected or cultured specimen._

Location: type/biomaterial/cell_suspension.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
cell_morphology | Features relating to the morphology of cells in a biomaterial. | object | no | [See module  cell_morphology](module.md/#cell_morphology) | Cell morphology |  | 
plate_based_sequencing | Fields specific for plate-based sequencing experiments. | object | no | [See module  plate_based_sequencing](module.md/#plate_based_sequencing) | Plate-based sequencing |  | 
genus_species | The scientific binomial name for the species of the suspension. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
selected_cell_type | The cell type(s) selected to be present in the suspension. | array | no | [See module  cell_type_ontology](module.md/#cell_type_ontology) | Selected cell type |  | fetal cardiomyocyte
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
growth_conditions | Features relating to the growth and/or maintenance of a biomaterial. | object | no | [See module  growth_conditions](module.md/#growth_conditions) | Growth conditions |  | 
total_estimated_cells | Total estimated number of cells in the suspension. May be 1 for well-based assays. | integer | no |  | Total estimated cell count |  | 2100

## cell_line
_Information about the cell line or cell culture biomaterial._

Location: type/biomaterial/cell_line.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
cell_morphology | Features relating to the morphology of the cells. | object | no | [See module  cell_morphology](module.md/#cell_morphology) | Cell morphology |  | 
supplier | The supplier of the cell line. | string | no |  | Supplier |  | HipSci
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
genus_species | The scientific binomial name for the species of the cell line. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
date_established | When the cell line was established, in date-time format. yyyy-mm-ddThh:mm:ssZ. | string | no |  | Date established |  | 2017-03-19
cell_type | The cell type that the cell line represents. | object | no | [See module  cell_type_ontology](module.md/#cell_type_ontology) | Cell type |  | cardiac muscle cell
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
tissue | The tissue that the cell line was derived from. | object | no | [See module  organ_part_ontology](module.md/#organ_part_ontology) | Tissue |  | bone marrow
catalog_number | The supplier catalogue number for the cell line. | string | no |  | Catalog number |  | 77650057
confluency | The percent a plate surface is covered by cells. | number | no |  | Percent confluency |  | 60
disease | Short description of any disease association to the cell type. | object | no | [See module  disease_ontology](module.md/#disease_ontology) | Disease |  | bone squamous cell carcinoma
cell_line_type | The type of cell line. | string | yes |  | Cell line type | primary, immortalized, stem cell-derived, synthetic, induced pluripotent | Should be one of: primary, immortalized, stem cell-derived, induced pluripotent, or synthetic.
catalog_url | The supplier catalogue URL for the cell line. | string | no |  | Catalog URL |  | 
karyotype | The karyotype of the cell line. | string | no |  | Karyotype |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
cell_cycle | The cell cycle phase if the cell line is synchronized growing cells or the phase is known. | object | no | [See module  cell_cycle_ontology](module.md/#cell_cycle_ontology) | Cell cycle |  | mitotic cell cycle
growth_conditions | Features relating to the growth and/or maintenance of the cell lines. | object | no | [See module  growth_conditions](module.md/#growth_conditions) | Growth conditions |  | 
lot_number | The supplier lot or batch number for the cell line. | string | no |  | Lot/batch number |  | 24.10.14
publications | One or more publications in which the cell line creation was cited. | array | no | [See module  publication](module.md/#publication) | Cell line publications |  | 

## organoid
_Information about an organoid biomaterial._

Location: type/biomaterial/organoid.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
embedded_in_matrigel | Whether the organoid is embedded in a matrigel. | boolean | no |  | Organoid embeddded in matrigel? |  | Should be one of: yes, no.
organoid_size | Size of the organoid in Organoid size unit. | number | no |  | Organoid size |  | 4
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
genus_species | The scientific binomial name for the species of the organoid. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
model_for_organ | Organ for which this organoid is a model system. | object | yes | [See module  organ_ontology](module.md/#organ_ontology) | Organ model |  | brain
model_organ_part | Organ part for which this organoid is a model system. | object | no | [See module  organ_part_ontology](module.md/#organ_part_ontology) | Organ part model |  | cortex
organoid_size_unit | The unit in which the Organoid size is expressed. | object | no | [See module  length_unit_ontology](module.md/#length_unit_ontology) | Organoid size unit |  | millimeter
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
input_aggregate_cell_count | Estimated number of cells per input cell aggregate. | number | no |  | Input aggregate cell count |  | 10000
organoid_age | Age of the organoid in Organoid age unit. Measured from when cell aggregates started differentiating to desired organoid model. | number | no |  | Organoid age |  | 55
organoid_age_unit | The unit in which Organoid age is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Organoid age unit |  | Should be one of: minute, hour, day, week, month, or year.
organoid_stored_oxygen_levels | Percent oxygen level organoid was stored in prior to sequencing. | number | no |  | Organoid stored oxygen level |  | 75
organoid_growth_environment | Growth environment in which the organoid is grown. | string | no |  | Organoid growth environment |  | matrigel, liquid suspension, adherent
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
organoid_morphology | General description of the organoid morphology. | string | no |  |  |  | Epithelial monolayer with budding crypt-like domains.
organoid_type | The type of organoid. | string | no |  | Organoid type | primary, immortalized, stem cell-derived, synthetic | Should be one of: primary, immortalized, stem cell-derived, or synthetic.

## donor_organism
_Information about the donor organism from which a specimen was collected._

Location: type/biomaterial/donor_organism.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
organism_age | Age in Organism age unit. Measured since birth. | string | no |  | Organism age |  | 20
normothermic_regional_perfusion | Yes if body (but not limbs) was perfused with warm oxygenated blood. No otherwise. | string | no |  | Normothermic regional perfusion | yes, no, unknown | Should be one of: yes, no, unknown.
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
genus_species | The scientific binomial name for the species of the donor. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
familial_relationship | Information about other organisms related to this organism. | array | no | [See module  familial_relationship](module.md/#familial_relationship) | Familial relationship |  | 
gestational_age | Gestational age in Gestational age unit. Measured since fertilization. | string | no |  | Gestational age |  | 5-7
mouse_specific | Fields specific to mouse (mus musculus) organisms. | object | no | [See module  mouse_specific](module.md/#mouse_specific) | Mouse-specific |  | 
biological_sex | The biological sex of the organism. | string | yes |  | Biological sex | female, male, mixed, unknown | Should be one of: male, female, mixed, or unknown.
organism_age_unit | The unit in which Organism age is expressed. Must be one of hour, day, week, month, or year. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Organism age unit |  | year
disease | Short description of known disease(s) of the organism. Enter normal if no known disease. | array | no | [See module  disease_ontology](module.md/#disease_ontology) | Known disease(s) |  | bone squamous cell carcinoma
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
development_stage | A classification of the developmental stage of the organism. | object | no | [See module  development_stage_ontology](module.md/#development_stage_ontology) | Development stage |  | adult
weight | Weight of organism in Weight unit. | string | no |  | Weight |  | 60
medical_history | Information about the medical history of an organism. | object | no | [See module  medical_history](module.md/#medical_history) | Medical history |  | 
gestational_age_unit | The unit in which Gestational age is expressed. Must be one of hour, day, week, month, or year. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Gestational age unit |  | week
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
height_unit | The unit in which height is expressed. | object | no | [See module  length_unit_ontology](module.md/#length_unit_ontology) | Height unit |  | centimeter
is_living | Yes if organism is alive at time of biomaterial collection. No if dead. Unknown if not known. | string | yes |  | Is living? | yes, no, unknown | Should be one of: yes, no, unknown.
weight_unit | The unit in which weight is expressed. | object | no | [See module  mass_unit_ontology](module.md/#mass_unit_ontology) | Weight unit |  | kilogram
death | Information about conditions of death of an organism. | object | no | [See module  death](module.md/#death) | Death conditions |  | 
human_specific | Fields specific to human (homo sapiens) organisms. | object | no | [See module  human_specific](module.md/#human_specific) | Human-specific |  | 
height | Height of organism in Height unit. | string | no |  | Height |  | 160

## specimen_from_organism
_Information about the specimen that was collected from the donor organism._

Location: type/biomaterial/specimen_from_organism.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
organ_part | A term for a specific part of the organ that the biomaterial came from. | object | no | [See module  organ_part_ontology](module.md/#organ_part_ontology) | Organ part |  | umbilical cord blood
purchased_specimen | Information about a purchased specimen. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Purchased specimen |  | 
collection_time | When the biomaterial was collected, in date-time format, yyyy-mm-ddThh:mm:ssZ. | string | no |  | Time of collection |  | 2017-03-19T07:22:00Z
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
genus_species | The scientific binomial name for the species of the specimen. | array | no | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
biomaterial_core | Core biomaterial-level information. | object | yes | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
disease | Short description of known disease(s) of the specimen. Enter normal if no known disease. | array | no | [See module  disease_ontology](module.md/#disease_ontology) | Known disease(s) |  | bone squamous cell carcinoma
organ | The organ that the biomaterial came from. Blood and connective tissue are considered organs. | object | yes | [See module  organ_ontology](module.md/#organ_ontology) | Organ |  | blood
preservation_storage | Information about how a specimen was preserved and/or stored over a period of time. | object | no | [See module  preservation_storage](module.md/#preservation_storage) | Preservation/Storage |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial | 
state_of_specimen | State of the specimen at the time of collection. | object | no | [See module  state_of_specimen](module.md/#state_of_specimen) | State of specimen |  | 

## process
_Information about the process_

Location: type/process/process.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
process_core | Core process-level information. | object | yes | [See core  process_core](core.md/#process_core) |  |  | 
length_of_time | Length of time the process took to execute, from start to finish, in Length of time unit. | string | no |  | Length of time |  | 10
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
process_type | The type of process. | object | no | [See module  process_type_ontology](module.md/#process_type_ontology) | Process type |  | sample enrichment
schema_type | The type of the metadata schema entity. | string | yes |  |  | process | 
length_of_time_unit | The unit in which Length of time is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Length of time unit |  | Should be one of: microsecond, second, minute, hour, day, week, month, or year.
insdc_experiment | An INSDC (International Nucleotide Sequence Database Collaboration) experiment accession. | object | no | [See module  insdc_experiment](module.md/#insdc_experiment) | INSDC experiment |  | 
deviation_from_protocol | Any deviation from the protocol provided. | string | no |  | Deviation from protocol |  | 

## analysis_process
_Information about the analysis process_

Location: type/process/analysis/analysis_process.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
outputs | Output generated by the pipeline run. | array | yes | [See   analysis_file](.md/#analysis_file) |  |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
process_type | The type of process. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Process type |  | 
process_core | Core process-level information. | object | yes | [See core  process_core](core.md/#process_core) |  |  | 
analysis_run_type | Indicator of whether the analysis actually ran or was just copied forward as an optimization. | string | yes |  |  | run, copy-forward | 
tasks | Descriptions of tasks in the workflow. | array | yes |  |  |  | 
input_bundles | The input bundles used in this analysis run. | array | yes |  |  |  | 
timestamp_start_utc | Initial start time of the full pipeline. | string | yes |  |  |  | 
inputs | Input parameters used in the pipeline run, these can be files or string values (settings). | array | yes |  |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | process | 
reference_bundle | Bundle containing the reference used in running the pipeline. | string | yes |  |  |  | 
timestamp_stop_utc | Terminal stop time of the full pipeline. | string | yes |  |  |  | 

## protocol
_Information about the protocol._

Location: type/protocol/protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
protocol_type | The type of protocol. | object | no | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | sample enrichment

## imaging_protocol
_Information about the imaging protocol_

Location: type/protocol/imaging/imaging_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
field_counts | Number of fields in x and y dimensions. | array | no |  | Field count |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
field_resolution | x, y, and z (number of focal planes) resolution of an individual field. | array | no |  | Field resolution |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
embedding | Description of embedding conditions. | string | no |  | Embedding conditions |  | 
protocol_type | The type of protocol. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | 
exposure_time | Exposure time - as a floating point number - in seconds. | number | no |  | Exposure time |  | 
field_microns | Microns covered by a field in x, y, and z. Z includes all focal planes in a single file. | array | no |  | Field microns |  | 
microscope | Microscope used for imaging. |  | no |  | Microscope | generic confocal, generic two photon | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
probes | A file containing information on probe sequence, genes they cover, and colors. | string | no |  | Probes |  | 
fixation | Description of fixation conditions. | string | no |  | Fixation |  | 

## sequencing_protocol
_Information about the sequencing protocol_

Location: type/protocol/sequencing/sequencing_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
local_machine_name | Local name for the particular machine on which the biomaterial was sequenced. | string | no |  | Local machine name |  | Machine1
paired_ends | Was a paired-end sequencing strategy used? | boolean | yes |  | Paired ends? |  | Should be one of: yes, no.
instrument_manufacturer_model | The manufacturer and model of the sequencer used. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0000548. | object | yes | [See module  instrument_ontology](module.md/#instrument_ontology) | Instrument manufacturer and model |  | Illumina HiSeq 4000
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
10x | Fields specific for 10x experiments. | object | no | [See module  10x](module.md/#10x) | 10x-specific |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
sequencing_approach | The general approach for sequencing. | object | yes | [See module  sequencing_ontology](module.md/#sequencing_ontology) | Protocol type |  | full length single cell RNA sequencing

## library_preparation_protocol
_Information about how a sequencing library was created._

Location: type/protocol/sequencing/library_preparation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
library_construction_kit | Name of kit used to construct the sequencing library. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Library construction kit |  | 
library_preamplification_method | The method used to amplify RNA prior to adaptor ligation. | object | no | [See module  library_amplification_ontology](module.md/#library_amplification_ontology) | Library pre-amplification method |  | PCR
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
end_bias | The type of tag or end bias the library has. | string | yes |  | End bias | 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, full length | Should be one of: 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, or full length.
nucleic_acid_conversion_kit | Name of kit used to convert RNA to DNA for sequencing. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Nucleic acid conversion kit |  | 
primer | Primer used for cDNA synthesis from RNA. | string | no |  | Primer | poly-dT, random | Should be one of: poly-dT, or random.
spike_in_dilution | Dilution of spike-in, if used. | integer | no |  | Spike-in dilution |  | 100
umi_barcode | Information about unique molecular identifier (UMI) barcodes. | object | no | [See module  barcode](module.md/#barcode) | UMI barcode |  | 
input_nucleic_acid_molecule | Starting nucleic acid molecule isolated for sequencing. | object | yes | [See module  biological_macromolecule_ontology](module.md/#biological_macromolecule_ontology) | Input nucleic acid molecule |  | polyA RNA
strand | Library strandedness. | string | yes |  | Strand | first, second, unstranded | Should be one of: first, second, or unstranded.
cdna_library_amplification_method | The method used to amplify a cDNA library prior to sequencing. | object | no | [See module  library_amplification_ontology](module.md/#library_amplification_ontology) | cDNA library amplification method |  | PCR
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
cell_barcode | Information about cell identifier barcodes. | object | no | [See module  barcode](module.md/#barcode) | Cell barcode |  | 
library_construction_approach | The general approach for sequencing library construction. | object | yes | [See module  library_construction_ontology](module.md/#library_construction_ontology) | Library construction approach |  | Smart-seq2
spike_in_kit | Information about a spike-in kit, if used. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Spike-in kit |  | 

## enrichment_protocol
_protocol by which one biomaterial was produced from another biomaterial to favor a feature or characteristic of interest._

Location: type/protocol/biomaterial_collection/enrichment_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
markers | A space-delimited list of markers with +/-. | string | no |  | Markers |  | CD4+ CD8-
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
enrichment_method | The method by which enrichment was achieved. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Enrichment method |  | fluorescence-activated cell sorting
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
min_size_selected | Minimum cell or organelle size passing selection, in microns. | number | no |  | Minimum size selected |  | 70
max_size_selected | Maximum cell or organelle size passing selection, in microns. | number | no |  | Maximum size selected |  | 90

## aggregate_generation_protocol
_Information on how cultured cells are developed into cell aggregates._

Location: type/protocol/biomaterial_collection/aggregate_generation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
aggregate_formation_method | Method used to form cell aggreagtes. | string | yes |  | Aggregate formation method |  | rocking, suspension cultures, hanging drops, spinner flasks
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
aggregate_cell_uniformity | Description of uniformity of the cell aggregates after they are formed. | string | no |  | Aggregate cell uniformity |  | Mostly homogenous EBs of variable cell numbers

## ipsc_induction_protocol
_Contains information on how a sample was treated to become an induced pluripotent stem cell._

Location: type/protocol/biomaterial_collection/ipsc_induction_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
ipsc_induction_factors | Induction factors added to primary cell culture to induce pluripotency. | string | no |  | Induction factors |  | POU5F1, SOX2, KLF4, c-MYC
protocol_reagents | A list of additional purchased reagents used in this protocol. | array | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Additional protocol reagents |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
pluripotency_test | Description of how pluripotency was tested in induced pluripotent stem cells. | string | no |  | Pluripotency test |  | teratoma assay
induced_pluripotent_cell_induction_kit | Kit used to induce pluripotent stem cell generation. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Induction kit |  | 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
induced_pluripotent_cell_induction_method | Induction method applied to primary cell culture to induce pluripotent stem cell generation. | string | yes |  | Induction method | lentivirus, sendai virus, Gun particle, piggyBac transposon, miRNA viral, adenovirus, cre-loxP, plasmid, retroviral | piggyBac transposon
pluripotency_vector_removed | Whether a viral vector was removed after induction. | string | no |  | Pluripotent vector removed? | yes, no, unknown | Should be one of: yes, no, or unknown.
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
induced_pluripotent_cell_induction_produced_in_house | Whether the induced pluripotent stem cell was prepared in-house. | boolean | no |  | iPSC prepared in-house? |  | Should be one of: yes, no.
percent_pluripotency | Percent of iPSCs that passed the pluripotency test. | number | no |  | Percent pluripotency |  | 97.2

## dissociation_protocol
_Contains information on the dissociation protocol used to separate the cells in a specimen._

Location: type/protocol/biomaterial_collection/dissociation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
protocol_reagents | A list of purchased reagents used in this protocol. | array | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Protocol reagents |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
nucleic_acid_source | Source cells or organelles from which nucleic acid molecules were collected. | string | yes |  | Nucleic acid source | bulk cell, single cell, single nucleus, bulk nuclei, mitochondria | Should be one of: bulk cell, single cell, single nucleus, bulk nuclei, or mitochondria.
dissociation_method | How cells or organelles were dissociated. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Dissociation method |  | enzymatic dissociation

## differentiation_protocol
_Information on how a pluripotent cell is differentiated to a desired cell type or organoid._

Location: type/protocol/biomaterial_collection/differentiation_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
differentiation_method | Differentiation method applied to cell culture to induce a specific differentiation response. | string | yes |  | Differentiation method |  | Embryoid Body, Monolayer, Inductive Co-Culture
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
differentiation_target_pathway | Targeted pathway for specific differentiation response. | string | no |  | Target pathway |  | Wnt Pathway
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
differentiation_reagents | A list of purchased reagents used in the differentiation protocol. | array | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Differentiation reagents |  | 
differentiation_small_molecules | Differentiation small molecules added to stem cell medium to induce a specific differentiation response. | string | no |  | Small molecules |  | Retinoic Acid, CHIR99021 (GSK-inhibitor), Activin A, BMP4
differentiation_target_cell_yield | Percent of target cells obtained after directed differentiation of origin cell. | number | no |  | Percent target cell yield |  | 95
differentiation_media | Culture media used to induce a specific differentiation response. | string | no |  | Differentiation media |  | RPMI 1640 + B27, Neurobasal Media, StemPro-34 Serum-Free Medium
differentiation_validation_results | Results confirming successful differentiation to target cell type. | string | no |  | Validation results |  | CD103 Positive, Nestin Positive, HCN4 Positive, CD11C Negative
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
differentiation_validation_method | Method used to validate origin cell successfully differentiated to target cell. | string | no |  | Differentiation validation method |  | Pancreatic Cell DTZ Detection Assay, qPCR, Flow Cytometry, Immunocytochemistry Staining

## collection_protocol
_Information about the biomaterial collection protocol._

Location: type/protocol/biomaterial_collection/collection_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
protocol_reagents | A list of purchased reagents used in this protocol. | array | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Protocol reagents |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
collection_method | How the biomaterial was collected. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Collection method |  | blood draw

## analysis_protocol
_Information about the analysis protocol._

Location: type/protocol/analysis/analysis_protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | yes | [See core  protocol_core](core.md/#protocol_core) |  |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
computational_method | A URI to a versioned workflow and versioned execution environment in a GA4GH-compliant repository. | string | yes |  |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol | 
protocol_type | The type of protocol. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | 

## reference_file
_A reference file used by a secondary reference pipeline._

Location: type/file/reference_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
assembly_type | The assembly type of the reference. This applies to reference genome sequences. | string | yes |  | Assembly type | primary assembly, complete assembly, patch assembly | Should be one of: primary assembly, complete assembly, or patch assembly.
reference_version | The genome version of the reference. | string | yes |  | Reference version |  | GencodeV27
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 
reference_type | The type of the genome reference. | string | yes |  | Reference type | genome sequence, transcriptome sequence, annotation reference, transcriptome index, genome sequence index | Should be one of: genome sequence, transcriptome sequence, annotation reference, transcriptome index, or genome sequence index.
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | integer | yes |  | NCBI taxon ID |  | 9606
genus_species | The scientific binomial name for the species of this reference. | object | yes | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens

## sequence_file
_A file of read sequences generated by a sequencing experiment._

Location: type/file/sequence_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 
read_length | The length of a sequenced read in this file, in nucleotides. | integer | no |  | Read length |  | 51
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
lane_index | The index of the lane that this file was sequenced from. | integer | no |  | Lane index |  | 1
read_index | Whether the read file contains the read1, read2, index1, or index2 part of the sequencing read or represents a single-end, non-indexed library. | string | yes |  | Read index | read1, read2, index1, index2, single-end, non-indexed | Should be one of: read1, read2, index1, index2, or 'single-end, non-indexed'
insdc_run | An INSDC (International Nucleotide Sequence Database Collaboration) run accession. Can be from the DDBJ, NCBI, or EMBL-EBI. Accession must start with DRR, SRR, or ERR. | array | no |  | INSDC run |  | SRR0000000

## analysis_file
_A file analysis results produced by a secondary analysis pipeline._

Location: type/file/analysis_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 
provenance | Provenance information provided by the system. | object | no | [See   provenance](.md/#provenance) |  |  | 

## supplementary_file
_Supplementary files belonging to a project._

Location: type/file/supplementary_file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | file | 
file_description | A short description of the file content. This could include information about how the file was generated. | string | no |  | File description |  | Enrichment protocol
file_core | Core file-level information. | object | yes | [See core  file_core](core.md/#file_core) |  |  | 

