# Required fields
_This document contains a list of all required fields in the HCA metadata schema. For a fulldescription of each schema, please refer to the relevant entity specification document._
## Core
### File core<a name='File core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
file_name | The name of the file. | string |  | File name |  | R1.fastq.gz; codebook.json
file_format | The format of the file. | string |  | File format |  | fastq.gz; tif
### Protocol core<a name='Protocol core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_id | A unique ID for the protocol. | string |  | Protocol ID |  | 
### Project core<a name='Project core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
project_short_name | A short name for the project. | string |  | Project label |  | CoolOrganProject.
project_title | An official title for the project. | string |  | Project title |  | Study of single cells in the human body.
project_description | A longer description of the project which includes research goals and experimental approach. | string |  | Project description |  | 
### Biomaterial core<a name='Biomaterial core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
biomaterial_id | A unique ID for the biomaterial. | string |  | Biomaterial ID |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | array |  | NCBI taxon ID |  | 9606
### Process core<a name='Process core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
process_id | A unique ID for the process. | string |  | Process ID |  | 
## Type
### Sequence file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) | File core |  | 
read_index | The sequencing read this file represents. | string |  | Read index | read1, read2, index1, index2, single-end, non-indexed | Should be one of: read1, read2, index1, index2
### Image file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) | File core |  | 
### Supplementary file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) | File core |  | 
### Analysis file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) | File core |  | 
### Reference file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) | File core |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | integer |  | NCBI taxon ID |  | 9606; 10090
genus_species | The scientific binomial name for the species of this reference. | object | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | 
reference_type | The type of the reference file. | string |  | Reference type | genome sequence, transcriptome sequence, annotation reference, transcriptome index, genome sequence index | Should be one of: genome sequence, transcriptome sequence, annotation reference, transcriptome index, or genome sequence index.
assembly_type | The assembly type of the genome reference file. | string |  | Genome assembly type | primary assembly, complete assembly, patch assembly | Should be one of: primary assembly, complete assembly, or patch assembly.
reference_version | The genome version of the reference file. | string |  | Reference version |  | GencodeV27; Ensembl 87
### Protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
### Sequencing protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
instrument_manufacturer_model | The manufacturer and model of the sequencer. | object | [See module  instrument_ontology](module.md/#instrument_ontology) | Instrument manufacturer and model |  | 
paired_end | Whether the sequenced molecule was sequenced from both ends. | boolean |  | Paired end? |  | Should be one of: yes, or no.
method | The general method for sequencing. | object | [See module  sequencing_ontology](module.md/#sequencing_ontology) | Sequencing method |  | 
### Library preparation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
input_nucleic_acid_molecule | Starting nucleic acid molecule isolated for sequencing. | object | [See module  biological_macromolecule_ontology](module.md/#biological_macromolecule_ontology) | Input nucleic acid molecule |  | 
nucleic_acid_source | Source cells or organelles from which nucleic acid molecules were collected. | string |  | Nucleic acid source | bulk cell, single cell, single nucleus, bulk nuclei, mitochondria | Should be one of: single cell, bulk cell, single nucleus, bulk nuclei, or mitochondria.
library_construction_method | The general method for sequencing library construction. | object | [See module  library_construction_ontology](module.md/#library_construction_ontology) | Library construction method |  | 
end_bias | The type of tag or end bias the library has. | string |  | End bias | 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, full length | Should be one of: 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, or full length.
strand | Library strandedness. | string |  | Strand | first, second, unstranded, not provided | Should be one of: first, second, unstranded, or not provided.
### Analysis protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
protocol_type | The type of protocol. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | 
computational_method | A URI to a versioned workflow and versioned execution environment in a GA4GH-compliant repository. | string |  | Computational method |  | SmartSeq2SingleCell; 10x
### Aggregate generation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
formation_method | Method used to form cell aggregates. | string |  | Aggregate formation method |  | rocking; suspension cultures; hanging drops; spinner flasks
### Enrichment protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
enrichment_method | The method by which enrichment was achieved. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Enrichment method |  | 
### Dissociation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
method | How cells or organelles were dissociated. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Dissociation method |  | 
### iPSC induction protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
ipsc_induction_method | Induction method applied to primary cell culture to induce pluripotent stem cell generation. | string |  | Induction method | lentivirus, sendai virus, Gun particle, piggyBac transposon, miRNA viral, adenovirus, cre-loxP, plasmid, retroviral | Should be one of: lentivirus, sendai virus, Gun particle, piggyBac transposon, miRNA viral, adenovirus, cre-loxP, plasmid, or retroviral.
### Collection protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
method | Method used to collect the biomaterial. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Collection method |  | 
### Differentiation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
method | Method applied to cell culture to induce a specific differentiation response. | string |  | Differentiation method |  | Embryoid Body; Monolayer; Inductive Co-Culture
### Imaging preparation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
### Imaging Protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
microscopy_technique | The type of microscopy. | object | [See module  microscopy_ontology](module.md/#microscopy_ontology) | Microscopy technique |  | 
magnification | Magnification of the objective used for imaging. | string |  | Magnification |  | 60x; 100x
numerical_aperture | Numerical aperture of the objective. | number |  | Numerical aperture |  | 1.3; 0.75
pixel_size | Pixel size in nanometers. | number |  | Pixel size |  | 109
overlapping_tiles | Whether tiles were collected with overlap. | string |  | Overlapping tiles? | yes, no | Should be one of: yes, or no.
channel | Information about each channel used in the imaging protocol. | array | [See module  channel](module.md/#channel) | Channel |  | 
target | Information about each imaging target in the imaging experiment. | array | [See module  target](module.md/#target) | Imaging target |  | 
### Project
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | project | 
project_core | Core project-level information. | object | [See core  project_core](core.md/#project_core) | Project core |  | 
funders | Funding source(s) supporting the project. | array | [See module  funder](module.md/#funder) | Funding source(s) |  | 
### Specimen from organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
organ | The organ that the biomaterial came from. | object | [See module  organ_ontology](module.md/#organ_ontology) | Organ |  | 
### Cell suspension
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
### Cell line
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
type | The type of cell line. | string |  | Cell line type | primary, immortalized, stem cell, stem cell-derived, induced pluripotent, synthetic | Should be one of: primary, immortalized, stem cell, stem cell-derived, induced pluripotent, or synthetic.
model_organ | Organ for which this cell line is a model. | object | [See module  organ_ontology](module.md/#organ_ontology) | Organ model |  | 
### Imaged specimen
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
slice_thickness | Thickness of the imaged slice in micrometres. | number |  | Imaged slice thickness |  | 14
### Donor organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
sex | The biological sex of the organism. | string |  | Biological sex | female, male, mixed, unknown | Should be one of: male, female, mixed, or unknown.
is_living | Whether organism was alive at time of biomaterial collection. | string |  | Alive at collection? | yes, no, unknown | Should be one of: yes, no, or unknown.
development_stage | A classification of the developmental stage of the organism. | object | [See module  development_stage_ontology](module.md/#development_stage_ontology) | Development stage |  | 
### Organoid
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
model_organ | Organ for which this organoid is a model system. | object | [See module  organ_ontology](module.md/#organ_ontology) | Organ model |  | 
### Process
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | process | 
process_core | Core process-level information. | object | [See core  process_core](core.md/#process_core) | Process core |  | 
### Analysis process
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | process | 
process_core | Core process-level information. | object | [See core  process_core](core.md/#process_core) | Process core |  | 
process_type | The type of process. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Process type |  | 
inputs | Input parameters used in the pipeline run. | array |  | Input parameters |  | 
tasks | Information about steps in the workflow. | array |  | Workflow tasks |  | 
input_bundles | UUID(s) of the input bundle(s) used in running the pipeline. | array |  | Input bundles |  | b816d2d6-5f10-4447-4194-3d0a804454d6
timestamp_start_utc | Initial start time of the full pipeline in UTC. | string |  | Start timestamp (UTC) |  | 2018-01-21T09:34:27Z
timestamp_stop_utc | Terminal stop time of the full pipeline in UTC. | string |  | Stop timestamp (UTC) |  | 2018-01-21T11:35:01Z
analysis_run_type | Whether the analysis was run or was copied forward as an optimization. | string |  | Analysis run type | run, copy-forward | Should be one of: run, or copy-forward.
reference_bundle | UUID of the bundle containing the reference used in running the pipeline. | string |  | Reference bundle |  | b816d2d6-5f10-4447-4194-3d0a804454d6
## Module
### Target<a name='Target'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
assay_type | Type of assay used to detect target. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Assay type |  | MERFISH; in situ sequencing
multiplexed | Whether multiple targets were detected simultaneously in this channel. | string |  | Multiplexed experiment? | yes, no | Should be one of: yes, or no.
### Channel<a name='Channel'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
channel_id | User given ID.  If there is an accompanying codebook, this name should correspond to the channel id used in the codebook. | string |  | Channel ID |  | 1; A
excitation_wavelength | Excitation wavelength of the lightsource in nanometers. | number |  | Excitation wavelength |  | 640
filter_range | Emission filter in nanometers. | string |  | Filter range |  | 461/70
multiplexed | Whether multiple targets were detected simultaneously in this channel. | string |  | Multiplexed experiment? | yes, no | Should be one of: yes, or no.
exposure_time | Acquisition time for a single image per channel, in milliseconds. | number |  | Exposure time |  | 400
