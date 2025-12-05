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
