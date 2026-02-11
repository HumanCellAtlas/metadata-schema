# Required fields
_This document contains a list of all required fields in the HCA metadata schema. For a fulldescription of each schema, please refer to the relevant entity specification document._
## Core
### File core<a name='File core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
file_name | The name of the file. | string |  | File name |  | R1.fastq.gz; codebook.json
format | The format of the file. | string |  | File format |  | fastq.gz; tif
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
file_core | Core file-level information. | object | [See core  file_core](core.md#file-core) | File core |  | 
read_index | The sequencing read this file represents. | string |  | Read index | read1, read2, read3, read4, index1, index2, single-end, non-indexed | Should be one of: read1, read2, index1, index2
### Image file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md#file-core) | File core |  | 
### Supplementary file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md#file-core) | File core |  | 
### Analysis file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md#file-core) | File core |  | 
genome_assembly_version | Name of the genome assembly used to generate this file. | string |  | Genome version | GRCh38, GRCh37, GRCm39, GRCm38, GRCm37, Not Applicable | Should be one of: GRCh38, GRCh37, GRCm39, GRCm38, GRCm37, Not Applicable
### Reference file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md#file-core) | File core |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | integer |  | NCBI taxon ID |  | 9606; 10090
genus_species | The scientific binomial name for the species of this reference. | object | [See module  species_ontology](module.md#species-ontology) | Genus species |  | 
reference_type | The type of the reference file. | string |  | Reference type | genome sequence, transcriptome sequence, annotation reference, transcriptome index, genome sequence index | Should be one of: genome sequence, transcriptome sequence, annotation reference, transcriptome index, or genome sequence index.
assembly_type | The assembly type of the genome reference file. | string |  | Genome assembly type | primary assembly, complete assembly, patch assembly | Should be one of: primary assembly, complete assembly, or patch assembly.
reference_version | The genome version of the reference file. | string |  | Reference version |  | GencodeV27; Ensembl 87
### Protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md#protocol-core) | Protocol core |  | 
### Sequencing protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md#protocol-core) | Protocol core |  | 
instrument_manufacturer_model | The manufacturer and model of the sequencer. | object | [See module  instrument_ontology](module.md#instrument-ontology) | Instrument manufacturer and model |  | 
paired_end | Whether the sequenced molecule was sequenced from both ends. | boolean |  | Paired end |  | Should be one of: yes, or no.
method | The general method for sequencing. | object | [See module  sequencing_ontology](module.md#sequencing-ontology) | Sequencing method |  | 
### Library preparation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md#protocol-core) | Protocol core |  | 
input_nucleic_acid_molecule | Starting nucleic acid molecule isolated for sequencing. | object | [See module  biological_macromolecule_ontology](module.md#biological-macromolecule-ontology) | Input nucleic acid molecule |  | 
nucleic_acid_source | Source cells or organelles from which nucleic acid molecules were collected. | string |  | Nucleic acid source | bulk cell, single cell, single nucleus, bulk nuclei, mitochondria | Should be one of: single cell, bulk cell, single nucleus, bulk nuclei, or mitochondria.
library_construction_method | The general method for sequencing library construction. | object | [See module  library_construction_ontology](module.md#library-construction-ontology) | Library construction method |  | 
end_bias | The type of tag or end bias the library has. | string |  | End bias | 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, full length | Should be one of: 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, or full length.
strand | Library strandedness. | string |  | Strand | first, second, unstranded, not provided | Should be one of: first, second, unstranded, or not provided.
### Analysis protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md#protocol-core) | Protocol core |  | 
type | The type of protocol. | object | [See module  process_type_ontology](module.md#process-type-ontology) | Protocol type |  | 
### Aggregate generation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md#protocol-core) | Protocol core |  | 
formation_method | Method used to form cell aggregates. | string |  | Aggregate formation method |  | rocking; suspension cultures; hanging drops; spinner flasks
### Enrichment protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md#protocol-core) | Protocol core |  | 
method | The method by which enrichment was achieved. | object | [See module  process_type_ontology](module.md#process-type-ontology) | Enrichment method |  | 
### Dissociation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md#protocol-core) | Protocol core |  | 
method | How cells or organelles were dissociated. | object | [See module  process_type_ontology](module.md#process-type-ontology) | Dissociation method |  | 
### iPSC induction protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md#protocol-core) | Protocol core |  | 
method | Induction method applied to primary cell culture to induce pluripotent stem cell generation. | string |  | Induction method | lentivirus, sendai virus, Gun particle, piggyBac transposon, miRNA viral, adenovirus, cre-loxP, plasmid, retroviral | Should be one of: lentivirus, sendai virus, Gun particle, piggyBac transposon, miRNA viral, adenovirus, cre-loxP, plasmid, or retroviral.
### Collection protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md#protocol-core) | Protocol core |  | 
method | Method used to collect the biomaterial. | object | [See module  process_type_ontology](module.md#process-type-ontology) | Collection method |  | 
### Differentiation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md#protocol-core) | Protocol core |  | 
method | Method applied to cell culture to induce a specific differentiation response. | string |  | Differentiation method |  | Embryoid Body; Monolayer; Inductive Co-Culture
### Treatment protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md#protocol-core) | Protocol core |  | 
method | Method applied to cell culture to induce a specific treatment response. | array | [See module  treatment_method_ontology](module.md#treatment-method-ontology) | Treatment method |  | 
### Imaging preparation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md#protocol-core) | Protocol core |  | 
### Imaging Protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md#protocol-core) | Protocol core |  | 
microscopy_technique | The type of microscopy. | object | [See module  microscopy_ontology](module.md#microscopy-ontology) | Microscopy technique |  | 
magnification | Magnification of the objective used for imaging. | string |  | Magnification |  | 60x; 100x
### Project
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | project | 
project_core | Core project-level information. | object | [See core  project_core](core.md#project-core) | Project core |  | 
funders | Funding source(s) supporting the project. | array | [See module  funder](module.md#funder) | Funding source(s) |  | 
data_use_restriction | Data use restrictions that apply to the project. | string |  | Data use restriction | NRES, GRU, GRU-NCU | GRU
### Specimen from organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md#biomaterial-core) | Biomaterial core |  | 
organ | The organ that the biomaterial came from. | object | [See module  organ_ontology](module.md#organ-ontology) | Organ |  | 
### Cell suspension
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md#biomaterial-core) | Biomaterial core |  | 
### Cell line
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md#biomaterial-core) | Biomaterial core |  | 
type | The type of cell line. | string |  | Cell line type | primary, immortalized, stem cell, stem cell-derived, induced pluripotent, synthetic | Should be one of: primary, immortalized, stem cell, stem cell-derived, induced pluripotent, or synthetic.
model_organ | Organ for which this cell line is a model. | object | [See module  organ_ontology](module.md#organ-ontology) | Organ model |  | 
### Imaged specimen
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md#biomaterial-core) | Biomaterial core |  | 
slice_thickness | Thickness of the imaged slice in micrometres. | number |  | Imaged slice thickness |  | 14
### Donor organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md#biomaterial-core) | Biomaterial core |  | 
sex | The biological sex of the organism. | string |  | Biological sex | female, male, mixed, unknown | Should be one of: male, female, mixed, or unknown.
is_living | Whether organism was alive at time of biomaterial collection. | string |  | Alive at collection | yes, no, unknown, not applicable | Should be one of: yes, no, not applicable, or unknown.
development_stage | A classification of the developmental stage of the organism. | object | [See module  development_stage_ontology](module.md#development-stage-ontology) | Development stage |  | 
### Organoid
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md#biomaterial-core) | Biomaterial core |  | 
model_organ | Organ for which this organoid is a model system. | object | [See module  organ_ontology](module.md#organ-ontology) | Organ model |  | 
### Process
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | process | 
process_core | Core process-level information. | object | [See core  process_core](core.md#process-core) | Process core |  | 
### Analysis process
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | process | 
process_core | Core process-level information. | object | [See core  process_core](core.md#process-core) | Process core |  | 
type | The type of process. | object | [See module  process_type_ontology](module.md#process-type-ontology) | Process type |  | 
inputs | Input parameters used in the pipeline run. | array |  | Input parameters |  | 
tasks | Information about steps in the workflow. | array |  | Workflow tasks |  | 
timestamp_start_utc | Initial start time of the full pipeline in UTC. | string |  | Start timestamp (UTC) |  | 2018-01-21T09:34:27Z
timestamp_stop_utc | Terminal stop time of the full pipeline in UTC. | string |  | Stop timestamp (UTC) |  | 2018-01-21T11:35:01Z
analysis_run_type | Whether the analysis was run or was copied forward as an optimization. | string |  | Analysis run type | run, copy-forward | Should be one of: run, or copy-forward.
reference_files | UUID of the file entities that contain the reference genome used in running the pipeline. | array |  | Reference files |  | 
## Module
### Channel<a name='Channel'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
channel_id | User given ID.  If there is an accompanying codebook, this name should correspond to the channel id used in the codebook. | string |  | Channel ID |  | 1; A
excitation_wavelength | Excitation wavelength of the lightsource in nanometers. | number |  | Excitation wavelength |  | 640
filter_range | Emission filter in nanometers. | string |  | Filter range |  | 461/70
multiplexed | Whether multiple targets were detected simultaneously in this channel. | string |  | Multiplexed experiment | yes, no | Should be one of: yes, or no.
exposure_time | Acquisition time for a single image per channel, in milliseconds. | number |  | Exposure time |  | 400
### Probe<a name='Probe'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
probe_label | The label of a probe used to detect target in this experiment. | string |  | Probe label |  | ACTA1; cFos
target_label | An identifier for the target molecule. | string |  | Target label |  | CHEBI:85345; ENSG00000170345
assay_type | Type of assay used to detect target. | object | [See module  process_type_ontology](module.md#process-type-ontology) | Assay type |  | MERFISH; in situ sequencing
### Matrix<a name='Matrix'></a>
_There are no required properties in schema Matrix_
### File content ontology<a name='File content ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | General description of the contents of the file. | string |  | Content description |  | DNA sequence (raw); Sequence alignment
### Length unit ontology<a name='Length unit ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a length unit being used. | string |  | Length unit |  | micrometer; meter
### Cell cycle ontology<a name='Cell cycle ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a cell cycle of the cells in the specimen. | string |  | Cell cycle |  | meiotic cell cycle; mitotic G1 phase
### Library amplification ontology<a name='Library amplification ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a library amplification approach being used. | string |  | Library amplification |  | PCR; in vitro transcription
### Contributor role ontology<a name='Contributor role ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The primary role of the contributor in the project. | string |  | Contributor role |  | principal investigator; experimental scientist
### Ethnicity ontology<a name='Ethnicity ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The ethnicity of the human donor. | string |  | Ethnicity |  | European; Hispanic or Latin American
### Target pathway ontology<a name='Target pathway ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the treatment target pathway. | string |  | Target pathway |  | positive regulation of memory T cell differentiation
### Treatment method ontology<a name='Treatment method ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a treatment method or approach being used. | string |  | Treatment method |  | T cell activation assay
### Cellular component ontology<a name='Cellular component ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a subcellular structure. | string |  | Subcellular structure |  | cytoplasm; nucleus
### Library construction ontology<a name='Library construction ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a library construction approach being used. | string |  | Library construction |  | 10X v2 sequencing; Smart-seq2
### Process type ontology<a name='Process type ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a process type being used. | string |  | Process type |  | enzymatic dissociation; blood draw
### Gender identity ontology<a name='Gender identity ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The gender identity of the human donor at the time of the experiment. | string |  | Gender identity |  | Female Gender; Agender; Non-Binary Gender
### Sequencing ontology<a name='Sequencing ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a sequencing approach being used. | string |  | Sequencing approach |  | tag based single cell RNA sequencing; full length single cell RNA sequencing
### Species ontology<a name='Species ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the species to which the organism belongs. | string |  | Species |  | Homo sapiens; Mus musculus
### Disease ontology<a name='Disease ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  | Disease |  | type 2 diabetes mellitus; normal
### Strain ontology<a name='Strain ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the strain to which the organism belongs. | string |  | Strain |  | C57BL/6; BALB/c
### Medication ontology<a name='Medication ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | Medication(s) the individual was taking at time of biomaterial collection. | string |  | Medication |  | Ibuprofen Lysine; Bisoprolol; Ambroxol Hydrochloride
### File format ontology<a name='File format ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the file format. | string |  | File format |  | FASTQ; JSON
### Enrichment ontology<a name='Enrichment ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of an enrichment approach being used. | string |  | Enrichment |  | fluorescence-activated cell sorting; Ficoll-Hypaque method
### Organ part ontology<a name='Organ part ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  | Organ part |  | bone marrow; islet of Langerhans
### Microscopy ontology<a name='Microscopy ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the type of microscopy used in an imaging experiment. | string |  | Microscopy |  | confocal microscopy; fluorescence microscopy
### Time unit ontology<a name='Time unit ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a time unit being used. | string |  | Time unit |  | second; week
### Protocol type ontology<a name='Protocol type ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a protocol type used. | string |  | Protocol type |  | dissociation protocol; enrichment protocol
### Development stage ontology<a name='Development stage ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the development stage of the organism. | string |  | Development stage |  | human adult stage; Theiler stage 28
### Instrument ontology<a name='Instrument ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The full name of the instrument used. | string |  | Instrument |  | Illumina HiSeq 2500; ONT MinION
### Mass unit ontology<a name='Mass unit ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a mass unit being used. | string |  | Mass unit |  | kilogram; microgram
### Biological macromolecule ontology<a name='Biological macromolecule ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the biological macromolecule being used. | string |  | Biological macromolecule |  | polyA RNA; mRNA
### Cell type ontology<a name='Cell type ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a cell type supplied by a user. | string |  | Cell type |  | bone marrow hematopoietic cell; cardiac muscle cell
### Organ ontology<a name='Organ ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  | Organ |  | heart; immune system
### Funder<a name='Funder'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
grant_id | The unique grant identifier or reference. | string |  | Grant ID |  | BB/P0000001/1
organization | The name of the funding organization. | string |  | Funding organization |  | Biotechnology and Biological Sciences Research Council (BBSRC); California Institute of Regenerative Medicine (CIRM)
### HCA Bionetwork<a name='HCA Bionetwork'></a>
_There are no required properties in schema HCA Bionetwork_
### Contact<a name='Contact'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
name | Name of individual who has contributed to the project. | string |  | Contact name |  | John,D,Doe; Jane,,Smith
institution | Name of primary institute where the individual works. | string |  | Institute |  | EMBL-EBI; University of Washington
### Publication<a name='Publication'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
authors | A list of authors associated with the publication. | array |  | Authors |  | Doe JD
title | The title of the publication. | string |  | Publication title |  | Study of single cells in the human body.
official_hca_publication | Has the publication been accepted as an official HCA publication, according to the process described in https://www.humancellatlas.org/publications/ ? | boolean |  | Official HCA Publication |  | yes; no
### Human-specific<a name='Human-specific'></a>
_There are no required properties in schema Human-specific_
### Growth conditions<a name='Growth conditions'></a>
_There are no required properties in schema Growth conditions_
### Medical tests<a name='Medical tests'></a>
_There are no required properties in schema Medical tests_
### Collection institute<a name='Collection institute'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
name | Name of the institute where the biomaterial was collected on. | string |  | Collection institute name |  | institute_1; Addenbrooke's Hospital; University of California, San Francisco
### Disease profile<a name='Disease profile'></a>
_There are no required properties in schema Disease profile_
### Reproductive history<a name='Reproductive history'></a>
_There are no required properties in schema Reproductive history_
### Preservation and storage<a name='Preservation and storage'></a>
_There are no required properties in schema Preservation and storage_
### Death<a name='Death'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
cause_of_death | Conditions resulting in death. | string |  | Cause of death |  | Hypoxic brain damage; Sudden cardiac arrest
### Familial relationship<a name='Familial relationship'></a>
_There are no required properties in schema Familial relationship_
### Medical history<a name='Medical history'></a>
_There are no required properties in schema Medical history_
### Residence<a name='Residence'></a>
_There are no required properties in schema Residence_
### Cell morphology<a name='Cell morphology'></a>
_There are no required properties in schema Cell morphology_
### State of specimen<a name='State of specimen'></a>
_There are no required properties in schema State of specimen_
### Timecourse<a name='Timecourse'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
value | The numerical value in Timecourse unit associated with a time interval used in the experiment. | string |  | Timecourse value |  | 2; 5.5-10.5
unit | The unit in which the Timecourse value is expressed. | object | [See module  time_unit_ontology](module.md#time-unit-ontology) | Timecourse unit |  | 
### Mouse-specific<a name='Mouse-specific'></a>
_There are no required properties in schema Mouse-specific_
### Purchased reagents<a name='Purchased reagents'></a>
_There are no required properties in schema Purchased reagents_
### INSDC experiment<a name='INSDC experiment'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
insdc_experiment_accession | An International Nucleotide Sequence Database Collaboration (INSDC) experiment accession. | string |  | INSDC experiment accession |  | SRX0000000
### Barcode<a name='Barcode'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
barcode_read | The read in which the barcode is found. | string |  | Barcode-containing read | Read 1, Read 2, Read 3, Read 4, i7 Index, i5 Index | Should be one of: Read 1, Read 2, i7 Index, or i5 Index.
barcode_offset | The 0-based offset of start of barcode in read. | integer |  | Barcode offset |  | 0
barcode_length | Length of barcode in nucleotides. | integer |  | Barcode length |  | 28
### 10x-specific<a name='10x-specific'></a>
_There are no required properties in schema 10x-specific_
### Plate-based sequencing<a name='Plate-based sequencing'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
plate_label | A label or name for the plate on which the well is located. | string |  | Plate label |  | 2217
