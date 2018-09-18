# Required fields
_This document contains a list of all required fields in the HCA metadata schema. For a fulldescription of each schema, please refer to the relevant entity specification document._
## Core
### Project core<a name='Project core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
project_description | A longer description of the project which includes research goals and experimental approach. | string |  | Project description |  | For example, an abstract from a grant application or publication. Approximately 300 words.
project_title | An official title for the project. | string |  | Project title |  | For example, the title of a grant proposal or a publication. Approximately 30 words. This title will appear on the Human Cell Atlas data portal.
project_short_name | A short name for the project. | string |  | Project label |  | For example, a short label by which you refer to the project. This label will be used for quick reference.
### Biomaterial core<a name='Biomaterial core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
biomaterial_id | A unique ID for the biomaterial. | string |  | Biomaterial ID |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | array |  | NCBI taxon ID |  | 9606
### Process core<a name='Process core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
process_id | A unique ID for the process. | string |  | Process ID |  | 
### Protocol core<a name='Protocol core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_id | A unique ID for the protocol. | string |  | Protocol ID |  | 
### File core<a name='File core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
file_name | The filename of the file. | string |  | File name |  | 
file_format | The format of the file. | string |  | File format |  | fastq.gz
## Type
### Project
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | project | 
### Cell suspension
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
### Cell line
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
cell_line_type | The type of cell line. | string |  | Cell line type | primary, immortalized, stem cell-derived, synthetic, induced pluripotent, stem cell | Should be one of: primary, immortalized, stem cell, stem cell-derived, induced pluripotent, or synthetic.
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
### Organoid
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
model_for_organ | Organ for which this organoid is a model system. | object | [See module  organ_ontology](module.md/#organ_ontology) | Organ model |  | brain
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
### Donor organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
sex | The biological sex of the organism. | string |  | Biological sex | female, male, mixed, unknown | Should be one of: male, female, mixed, or unknown.
is_living | Yes if organism is alive at time of biomaterial collection. No if dead. Unknown if not known. | string |  | Is living? | yes, no, unknown | Should be one of: yes, no, unknown.
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
### Imaged specimen
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
imaged_slice_thickness | Thickness of the imaged slice in micrometres. | number |  | Imaged slice thickness |  | 14
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
### Specimen from organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
organ | The organ that the biomaterial came from. Blood and connective tissue are considered organs. | object | [See module  organ_ontology](module.md/#organ_ontology) | Organ |  | blood
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
### Process
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
process_core | Core process-level information. | object | [See core  process_core](core.md/#process_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | process | 
### Analysis process
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
reference_bundle | Bundle containing the reference used in running the pipeline. | string |  | Reference bundle |  | 
timestamp_stop_utc | Terminal stop time of the full pipeline in UTC. | string |  | Stop timestamp (UTC) |  | 
input_bundles | The input bundles used in this analysis run. | array |  | Input bundles |  | 
schema_type | The type of the metadata schema entity. | string |  |  | process | 
analysis_run_type | Indicator of whether the analysis actually ran or was just copied forward as an optimization. | string |  | Analysis run type | run, copy-forward | 
process_core | Core process-level information. | object | [See core  process_core](core.md/#process_core) |  |  | 
outputs | Output generated by the pipeline run. | array | [See   analysis_file](.md/#analysis_file) | Outputs |  | 
inputs | Input parameters used in the pipeline run, these can be files or string values (settings). | array |  | Input parameters |  | 
process_type | The type of process. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Process type |  | 
tasks | Descriptions of tasks in the workflow. | array |  | Workflow tasks |  | 
timestamp_start_utc | Initial start time of the full pipeline in UTC. | string |  | Start timestamp (UTC) |  | 
### Protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
### Imaging preparation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
### Imaging Protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
microscopy_technique | The type of microscopy. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | [See module  microscopy_ontology](module.md/#microscopy_ontology) | Microscopy technique |  | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
imaging_target | Information about each imaging target in the imaging experiment. | array | [See module  imaging_target](module.md/#imaging_target) | Imaging target |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
magnification | Magnification of the objective used for imaging. | string |  | Magnification |  | 60x
overlapping_tiles | Were tiles collected with overlap? | string |  | Overlapping tiles? | yes, no | no
channel | Information about each channel used in the imaging protocol. | array | [See module  channel](module.md/#channel) | Channel |  | 
pixel_size | Pixel size in nanometres (scaling factor). | number |  | Pixel size |  | 109
numerical_aperture | Numerical aperture of the objective. | number |  | Numerical aperture |  | 1.3
### Sequencing protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
paired_end | Was a paired-end sequencing strategy used? | boolean |  | Paired end? |  | Should be one of: yes, no.
instrument_manufacturer_model | The manufacturer and model of the sequencer used. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0000548. | object | [See module  instrument_ontology](module.md/#instrument_ontology) | Instrument manufacturer and model |  | Illumina HiSeq 4000
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
sequencing_approach | The general approach for sequencing. | object | [See module  sequencing_ontology](module.md/#sequencing_ontology) | Sequencing approach |  | full length single cell RNA sequencing
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
### Library preparation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
input_nucleic_acid_molecule | Starting nucleic acid molecule isolated for sequencing. | object | [See module  biological_macromolecule_ontology](module.md/#biological_macromolecule_ontology) | Input nucleic acid molecule |  | polyA RNA
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
end_bias | The type of tag or end bias the library has. | string |  | End bias | 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, full length | Should be one of: 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, or full length.
library_construction_approach | The general approach for sequencing library construction. | object | [See module  library_construction_ontology](module.md/#library_construction_ontology) | Library construction approach |  | Smart-seq2
strand | Library strandedness. | string |  | Strand | first, second, unstranded | Should be one of: first, second, or unstranded.
### Enrichment protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
enrichment_method | The method by which enrichment was achieved. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Enrichment method |  | fluorescence-activated cell sorting
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
### Aggregate generation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
aggregate_formation_method | Method used to form cell aggreagtes. | string |  | Aggregate formation method |  | rocking, suspension cultures, hanging drops, spinner flasks
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
### iPCS induction protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
ipsc_induction_method | Induction method applied to primary cell culture to induce pluripotent stem cell generation. | string |  | Induction method | lentivirus, sendai virus, Gun particle, piggyBac transposon, miRNA viral, adenovirus, cre-loxP, plasmid, retroviral | piggyBac transposon
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
### Dissociation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
dissociation_method | How cells or organelles were dissociated. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Dissociation method |  | enzymatic dissociation
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
### Differentiation protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
differentiation_method | Differentiation method applied to cell culture to induce a specific differentiation response. | string |  | Differentiation method |  | Embryoid Body, Monolayer, Inductive Co-Culture
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
### Collection protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
collection_method | How the biomaterial was collected. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Collection method |  | blood draw
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
### Analysis protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
computational_method | A URI to a versioned workflow and versioned execution environment in a GA4GH-compliant repository. | string |  | Computational method |  | 
protocol_type | The type of protocol. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
### Reference file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
genus_species | The scientific binomial name for the species of this reference. | object | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
reference_version | The genome version of the reference. | string |  | Reference version |  | GencodeV27
reference_type | The type of the genome reference. | string |  | Reference type | genome sequence, transcriptome sequence, annotation reference, transcriptome index, genome sequence index | Should be one of: genome sequence, transcriptome sequence, annotation reference, transcriptome index, or genome sequence index.
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | integer |  | NCBI taxon ID |  | 9606
assembly_type | The assembly type of the reference. This applies to reference genome sequences. | string |  | Assembly type | primary assembly, complete assembly, patch assembly | Should be one of: primary assembly, complete assembly, or patch assembly.
### Sequence file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
read_index | Whether the read file contains the read1, read2, index1, or index2 part of the sequencing read or represents a single-end, non-indexed library. | string |  | Read index | read1, read2, index1, index2, single-end, non-indexed | Should be one of: read1, read2, index1, index2, or 'single-end, non-indexed'
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
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
### Supplementary file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
## Module
### Cell type ontology<a name='Cell type ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a cell type supplied by a user. | string |  |  |  | 
### Ethnicity ontology<a name='Ethnicity ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The ethnicity of the human donor. | string |  |  |  | 
### Species ontology<a name='Species ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the species to which the organism belongs. | string |  |  |  | 
### Enrichment ontology<a name='Enrichment ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of an enrichment approach being used. | string |  |  |  | 
### Disease ontology<a name='Disease ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  |  |  | 
### Organ part ontology<a name='Organ part ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  |  |  | 
### Length unit ontology<a name='Length unit ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a length unit being used. | string |  |  |  | 
### Cellular component ontology<a name='Cellular component ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a subcellular structure. | string |  |  |  | 
### Library construction ontology<a name='Library construction ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a library construction approach being used. | string |  |  |  | 
### Time unit ontology<a name='Time unit ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a time unit being used. | string |  |  |  | 
### Development stage ontology<a name='Development stage ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the development stage of the organism. | string |  |  |  | 
### Microscopy ontology<a name='Microscopy ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the type of microscopy used in an imaging experiment. | string |  |  |  | 
### Organ ontology<a name='Organ ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  |  |  | 
### Mass unit ontology<a name='Mass unit ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a mass unit being used. | string |  |  |  | 
### Strain ontology<a name='Strain ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the strain to which the organism belongs (mouse-specific). | string |  |  |  | 
### Instrument ontology<a name='Instrument ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The full name of the instrument used. | string |  |  |  | 
### Cell cycle ontology<a name='Cell cycle ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a cell cycle of the cells in the specimen. | string |  |  |  | 
### Library amplification ontology<a name='Library amplification ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a library amplification approach being used. | string |  |  |  | 
### Process type ontology<a name='Process type ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a process type being used. | string |  |  |  | 
### Sequencing ontology<a name='Sequencing ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a sequencing approach being used. | string |  |  |  | 
### Protocol type ontology<a name='Protocol type ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a protocol type used. | string |  |  |  | 
### Biological macromolecule ontology<a name='Biological macromolecule ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the biological macromolecule being used. | string |  |  |  | 
### Contact<a name='Contact'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
institution | Name of primary institute where the individual works. | string |  | Institute |  | EMBL-EBI
contact_name | Name of individual who has contributed to the project. | string |  | Contact name |  | John,D,Doe. Format: first name, middle name or initial, last name.
### Publication<a name='Publication'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
publication_title | The title of the publication. | string |  | Publication title |  | Study of single cells in the human body
authors | A list of authors associated with the publication in 'surname initials' format. | array |  | Authors |  | Doe JD
### Funder<a name='Funder'></a>
_There are no required properties in schema Funder_
### Medical history<a name='Medical history'></a>
_There are no required properties in schema Medical history_
### Familial relationship<a name='Familial relationship'></a>
_There are no required properties in schema Familial relationship_
### Cell morphology<a name='Cell morphology'></a>
_There are no required properties in schema Cell morphology_
### Timecourse<a name='Timecourse'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
timecourse_value | The numerical value in Timecourse unit associated with a time interval used in the experiment. | string |  |  |  | 2
timecourse_unit | The unit in which the Timecourse value is expressed. | object | [See module  time_unit_ontology](module.md/#time_unit_ontology) |  |  | day
### Growth conditions<a name='Growth conditions'></a>
_There are no required properties in schema Growth conditions_
### Preservation and storage<a name='Preservation and storage'></a>
_There are no required properties in schema Preservation and storage_
### Mouse-specific<a name='Mouse-specific'></a>
_There are no required properties in schema Mouse-specific_
### State of specimen<a name='State of specimen'></a>
_There are no required properties in schema State of specimen_
### Human-specific<a name='Human-specific'></a>
_There are no required properties in schema Human-specific_
### Death<a name='Death'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
cause_of_death | Cause of death from death report for human donor, from research lab for mouse. | string |  | Cause of death |  | 
### Purchased reagents<a name='Purchased reagents'></a>
_There are no required properties in schema Purchased reagents_
### Barcode<a name='Barcode'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
barcode_length | Length of barcode in nucleotides. | integer |  | Barcode length |  | 28
barcode_read | The read that the barcode is found in. | string |  | Barcode-containing read | Read 1, Read 2, i7 Index, i5 Index | Should be one of: Read 1, Read 2, i7 Index, or i5 Index.
barcode_offset | 0-based offset of start of barcode in read. 0 for beginning of read. | integer |  | Barcode offset |  | 0
### INSDC experiment<a name='INSDC experiment'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
insdc_experiment | An INSDC (International Nucleotide Sequence Database Collaboration) experiment accession if experiment has been submitted. Can be from the DDBJ, EMBL-EBI, or NCBI.  Accession must start with DRX, ERX, or SRX. | string |  | INSDC experiment |  | SRX0000000
### 10x-specific<a name='10x-specific'></a>
_There are no required properties in schema 10x-specific_
### Plate-based sequencing<a name='Plate-based sequencing'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
plate_id | An ID for the plate that the well is located on. | string |  | Well plate ID |  | 2217
### Channel<a name='Channel'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
exposure_time | Acquisition time for a single image per channel in miliseconds | number |  | Exposure time |  | 400
channel_name | User given name.  If there is an accompanying codebook, this name should correspond to a channel name used in the codebook. | string |  | Channel name |  | far red
multiplexed | Were multiple targets detected simultaneously in this channel? Should be yes or no. | string |  | Is this a multiplexed experiment? | yes, no | yes
excitation_wavelength | Excitation wavelength of the lightsource in nanometers. | number |  | Excitation wavelength |  | 640
filter_range | Wavelength range of the emission filter in nanometers. | string |  | Filter range |  | 665 - 705
### Imaging target<a name='Imaging target'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
assay_type | Type of assay used to detect target. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Assay type |  | MERFISH, smFISH, immunofluorescence, fluorescent cell stain
multiplexed | Were multiple targets detected simultaneously in one channel? Should be yes or no. | string |  | Is this a multiplexed experiment? | yes, no | yes
channel | Channel name used to assay signal in non-multiplexed experiments. Should be consistent with the name in channel tab. | string |  | Channel |  | far red
