# Required fields
_This document contains a list of all required fields in the HCA metadata schema. For a fulldescription of each schema, please refer to the relevant entity specification document._
## Core
### Biomaterial core<a name='Biomaterial core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
biomaterial_id | A unique ID for the biomaterial. | string |  | Biomaterial ID |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | array |  | NCBI taxon ID |  | 9606
### File core<a name='File core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
file_name | The name of the file. | string |  | File name |  | R1.fastq.gz; codebook.json
file_format | The format of the file. | string |  | File format |  | fastq.gz; tif
content_description | General description of the contents of the file. | string |  | Content description | protocol, expression matrix, count matrix, quality control metrics, log, gene list | protocol; expression matrix
### Process core<a name='Process core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
process_id | A unique ID for the process. | string |  | Process ID |  | 
### Project core<a name='Project core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
project_short_name | A short name for the project. | string |  | Project label |  | CoolOrganProject.
project_title | An official title for the project. | string |  | Project title |  | Study of single cells in the human body.
project_description | A longer description of the project which includes research goals and experimental approach. | string |  | Project description |  | 
### Protocol core<a name='Protocol core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_id | A unique ID for the protocol. | string |  | Protocol ID |  | 
## Type
### Cell line
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
cell_line_type | The type of cell line. | string |  | Cell line type | primary, immortalized, stem cell-derived, synthetic, induced pluripotent, stem cell | Should be one of: primary, immortalized, stem cell, stem cell-derived, induced pluripotent, or synthetic.
### Cell suspension
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
### Donor organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
sex | The biological sex of the organism. | string |  | Biological sex | female, male, mixed, unknown | Should be one of: male, female, mixed, or unknown.
is_living | Whether organism was alive at time of biomaterial collection. | string |  | Alive at collection? | yes, no, unknown | Should be one of: yes, no, or unknown.
development_stage | A classification of the developmental stage of the organism. | object | [See module  development_stage_ontology](module.md/#development_stage_ontology) | Development stage |  | 
### Imaged specimen
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
slice_thickness | Thickness of the imaged slice in micrometres. | number |  | Imaged slice thickness |  | 14
### Organoid
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
### Specimen from organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) | Biomaterial core |  | 
organ | The organ that the biomaterial came from. | object | [See module  organ_ontology](module.md/#organ_ontology) | Organ |  | 
### Analysis file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
### Image file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
### Reference file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) | File core |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | integer |  | NCBI taxon ID |  | 9606, 10090
genus_species | The scientific binomial name for the species of this reference. | object | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | 
reference_type | The type of the reference file. | string |  | Reference type | genome sequence, transcriptome sequence, annotation reference, transcriptome index, genome sequence index | Should be one of: genome sequence, transcriptome sequence, annotation reference, transcriptome index, or genome sequence index.
assembly_type | The assembly type of the genome reference file. | string |  | Genome assembly type | primary assembly, complete assembly, patch assembly | Should be one of: primary assembly, complete assembly, or patch assembly.
reference_version | The genome version of the reference file. | string |  | Reference version |  | GencodeV27; Ensembl 87
### Sequence file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) | File core |  | 
read_index | The sequencing read this file represents. | string |  | Read index | read1, read2, index1, index2, single-end, non-indexed | Should be one of: read1, read2, index1, index2
### Supplementary file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) | File core |  | 
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
outputs | Output files generated by the pipeline run. | array | [See   analysis_file](.md/#analysis_file) | Output files |  | 
timestamp_start_utc | Initial start time of the full pipeline in UTC. | string |  | Start timestamp (UTC) |  | 2018-01-21T09:34:27Z
timestamp_stop_utc | Terminal stop time of the full pipeline in UTC. | string |  | Stop timestamp (UTC) |  | 2018-01-21T11:35:01Z
analysis_run_type | Whether the analysis was run or was copied forward as an optimization. | string |  | Analysis run type | run, copy-forward | Should be one of: run, or copy-forward.
reference_bundle | UUID of the bundle containing the reference used in running the pipeline. | string |  | Reference bundle |  | b816d2d6-5f10-4447-4194-3d0a804454d6
### Project
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | project | 
project_core | Core project-level information. | object | [See core  project_core](core.md/#project_core) | Project core |  | 
### Protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
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
aggregate_formation_method | Method used to form cell aggregates. | string |  | Aggregate formation method |  | rocking; suspension cultures; hanging drops; spinner flasks
### Collection protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
collection_method | Method used to collect the biomaterial. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Collection method |  | 
### Differentiation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
differentiation_method | Method applied to cell culture to induce a specific differentiation response. | string |  | Differentiation method |  | Embryoid Body; Monolayer; Inductive Co-Culture
### Dissociation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
dissociation_method | How cells or organelles were dissociated. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Dissociation method |  | 
### Enrichment protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
enrichment_method | The method by which enrichment was achieved. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Enrichment method |  | 
### iPSC induction protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
ipsc_induction_method | Induction method applied to primary cell culture to induce pluripotent stem cell generation. | string |  | Induction method | lentivirus, sendai virus, Gun particle, piggyBac transposon, miRNA viral, adenovirus, cre-loxP, plasmid, retroviral | Should be one of: lentivirus, sendai virus, Gun particle, piggyBac transposon, miRNA viral, adenovirus, cre-loxP, plasmid, or retroviral.
### Imaging preparation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
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
### Library preparation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
input_nucleic_acid_molecule | Starting nucleic acid molecule isolated for sequencing. | object | [See module  biological_macromolecule_ontology](module.md/#biological_macromolecule_ontology) | Input nucleic acid molecule |  | 
library_construction_approach | The general method for sequencing library construction. | object | [See module  library_construction_ontology](module.md/#library_construction_ontology) | Library construction method |  | 
end_bias | The type of tag or end bias the library has. | string |  | End bias | 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, full length | Should be one of: 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, or full length.
strand | Library strandedness. | string |  | Strand | first, second, unstranded, not provided | Should be one of: first, second, unstranded, or not provided.
### Sequencing protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) | Protocol core |  | 
instrument_manufacturer_model | The manufacturer and model of the sequencer. | object | [See module  instrument_ontology](module.md/#instrument_ontology) | Instrument manufacturer and model |  | 
paired_end | Whether the sequenced molecule was sequenced from both ends. | boolean |  | Paired end? |  | Should be one of: yes, or no.
sequencing_approach | The general method for sequencing. | object | [See module  sequencing_ontology](module.md/#sequencing_ontology) | Sequencing method |  | 
## Module
### Cell morphology<a name='Cell morphology'></a>
_There are no required properties in schema Cell morphology_
### Death<a name='Death'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
cause_of_death | Conditions resulting in death. | string |  | Cause of death |  | Hypoxic brain damage; Sudden cardiac arrest
### Familial relationship<a name='Familial relationship'></a>
_There are no required properties in schema Familial relationship_
### Growth conditions<a name='Growth conditions'></a>
_There are no required properties in schema Growth conditions_
### Human-specific<a name='Human-specific'></a>
_There are no required properties in schema Human-specific_
### Medical history<a name='Medical history'></a>
_There are no required properties in schema Medical history_
### Mouse-specific<a name='Mouse-specific'></a>
_There are no required properties in schema Mouse-specific_
### Preservation and storage<a name='Preservation and storage'></a>
_There are no required properties in schema Preservation and storage_
### State of specimen<a name='State of specimen'></a>
_There are no required properties in schema State of specimen_
### Timecourse<a name='Timecourse'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
timecourse_value | The numerical value in Timecourse unit associated with a time interval used in the experiment. | string |  | Timecourse value |  | 2
timecourse_unit | The unit in which the Timecourse value is expressed. | object | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Timecourse unit |  | day
### Biological macromolecule ontology<a name='Biological macromolecule ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the biological macromolecule being used. | string |  | Biological macromolecule |  | polyA RNA; mRNA
### Cell cycle ontology<a name='Cell cycle ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a cell cycle of the cells in the specimen. | string |  | Cell cycle |  | meiotic cell cycle; mitotic G1 phase
### Cell type ontology<a name='Cell type ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a cell type supplied by a user. | string |  | Cell type |  | bone marrow hematopoietic cell; cardiac muscle cell
### Cellular component ontology<a name='Cellular component ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a subcellular structure. | string |  | Subcellular structure |  | cytoplasm; nucleus
### Development stage ontology<a name='Development stage ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the development stage of the organism. | string |  | Development stage |  | human adult stage; Theiler stage 28
### Disease ontology<a name='Disease ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  | Disease |  | type 2 diabetes mellitus; normal
### Enrichment ontology<a name='Enrichment ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of an enrichment approach being used. | string |  | Enrichment |  | fluorescence-activated cell sorting; Ficoll-Hypaque method
### Ethnicity ontology<a name='Ethnicity ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The ethnicity of the human donor. | string |  | Ethnicity |  | European; Hispanic or Latin American
### Instrument ontology<a name='Instrument ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The full name of the instrument used. | string |  | Instrument |  | Illumina HiSeq 2500; ONT MinION
### Length unit ontology<a name='Length unit ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a length unit being used. | string |  | Length unit |  | micrometer; meter
### Library amplification ontology<a name='Library amplification ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a library amplification approach being used. | string |  | Library amplification |  | PCR; in vitro transcription
### Library construction ontology<a name='Library construction ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a library construction approach being used. | string |  | Library construction |  | 10X v2 sequencing; Smart-seq2
### Mass unit ontology<a name='Mass unit ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a mass unit being used. | string |  | Mass unit |  | kilogram; microgram
### Microscopy ontology<a name='Microscopy ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the type of microscopy used in an imaging experiment. | string |  | Microscopy |  | confocal microscopy; fluorescence microscopy
### Organ ontology<a name='Organ ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  | Organ |  | heart; immune system
### Organ part ontology<a name='Organ part ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  | Organ part |  | bone marrow; islet of Langerhans
### Process type ontology<a name='Process type ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a process type being used. | string |  | Process type |  | enzymatic dissociation; blood draw
### Protocol type ontology<a name='Protocol type ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a protocol type used. | string |  | Protocol type |  | dissociation protocol; enrichment protocol
### Sequencing ontology<a name='Sequencing ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a sequencing approach being used. | string |  | Sequencing approach |  | tag based single cell RNA sequencing; full length single cell RNA sequencing
### Species ontology<a name='Species ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the species to which the organism belongs. | string |  | Species |  | Homo sapiens; Mus musculus
### Strain ontology<a name='Strain ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the strain to which the organism belongs (mouse-specific). | string |  | Strain |  | C57BL/6; BALB/c
### Time unit ontology<a name='Time unit ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a time unit being used. | string |  | Time unit |  | second; week
### Purchased reagents<a name='Purchased reagents'></a>
_There are no required properties in schema Purchased reagents_
### 10x-specific<a name='10x-specific'></a>
_There are no required properties in schema 10x-specific_
### Barcode<a name='Barcode'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
barcode_read | The read in which the barcode is found. | string |  | Barcode-containing read | Read 1, Read 2, i7 Index, i5 Index | Should be one of: Read 1, Read 2, i7 Index, or i5 Index.
barcode_offset | 0-based offset of start of barcode in read. | integer |  | Barcode offset |  | 0
barcode_length | Length of barcode in nucleotides. | integer |  | Barcode length |  | 28
### INSDC experiment<a name='INSDC experiment'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
insdc_experiment | An International Nucleotide Sequence Database Collaboration (INSDC) experiment accession. | string |  | INSDC experiment accession |  | SRX0000000
### Plate-based sequencing<a name='Plate-based sequencing'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
plate_id | An ID for the plate that the well is located on. | string |  | Plate ID |  | 2217
### Contact<a name='Contact'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
contact_name | Name of individual who has contributed to the project. | string |  | Contact name |  | John,D,Doe; Jane,,Smith
institution | Name of primary institute where the individual works. | string |  | Institute |  | EMBL-EBI; University of Washington
### Funder<a name='Funder'></a>
_There are no required properties in schema Funder_
### Publication<a name='Publication'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
authors | A list of authors associated with the publication. | array |  | Authors |  | Doe JD
publication_title | The title of the publication. | string |  | Publication title |  | Study of single cells in the human body.
### Channel<a name='Channel'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
channel_id | User given ID.  If there is an accompanying codebook, this name should correspond to the channel id used in the codebook. | string |  | Channel ID |  | 1, A
excitation_wavelength | Excitation wavelength of the lightsource in nanometers. | number |  | Excitation wavelength |  | 640
filter_range | Wavelength range of the emission filter in nanometers. | string |  | Filter range |  | 665 - 705
multiplexed | Were multiple targets detected simultaneously in this channel? Should be yes or no. | string |  | Is this a multiplexed experiment? | yes, no | yes
exposure_time | Acquisition time for a single image per channel in miliseconds | number |  | Exposure time |  | 400
### Target<a name='Target'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
assay_type | Type of assay used to detect target. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Assay type |  | MERFISH, smFISH, immunofluorescence, fluorescent cell stain
multiplexed | Were multiple targets detected simultaneously in one channel? Should be yes or no. | string |  | Is this a multiplexed experiment? | yes, no | yes
