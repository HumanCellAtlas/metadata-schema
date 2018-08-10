# Required fields
_This document contains a list of all required fields in the HCA metadata schema. For a fulldescription of each schema, please refer to the relevant entity specification document._
## Core
### project_core<a name='project_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
project_short_name | A short name for the project. | string |  | Project label |  | For example, a short label by which you refer to the project. This label will be used for quick reference.
project_description | A longer description of the project which includes research goals and experimental approach. | string |  | Project description |  | For example, an abstract from a grant application or publication. Approximately 300 words.
project_title | An official title for the project. | string |  | Project title |  | For example, the title of a grant proposal or a publication. Approximately 30 words. This title will appear on the Human Cell Atlas data portal.
### biomaterial_core<a name='biomaterial_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | array |  | NCBI taxon ID |  | 9606
biomaterial_id | A unique ID for the biomaterial. | string |  | Biomaterial ID |  | 
### process_core<a name='process_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
process_id | A unique ID for the process. | string |  | Process ID |  | 
### protocol_core<a name='protocol_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_id | A unique ID for the protocol. | string |  | Protocol ID |  | 
### file_core<a name='file_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
file_name | The filename of the file. | string |  | File name |  | 
file_format | The format of the file. | string |  | File format |  | fastq.gz
## Type
### project
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | project | 
### cell_suspension
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
### cell_line
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
cell_line_type | The type of cell line. | string |  | Cell line type | primary, immortalized, stem cell-derived, synthetic, induced pluripotent | Should be one of: primary, immortalized, stem cell-derived, induced pluripotent, or synthetic.
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
### organoid
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
model_for_organ | Organ for which this organoid is a model system. | object | [See module  organ_ontology](module.md/#organ_ontology) | Organ model |  | brain
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
### donor_organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
is_living | Yes if organism is alive at time of biomaterial collection. No if dead. Unknown if not known. | string |  | Is living? | yes, no, unknown | Should be one of: yes, no, unknown.
sex | The biological sex of the organism. | string |  | Biological sex | female, male, mixed, unknown | Should be one of: male, female, mixed, or unknown.
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
### specimen_from_organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
organ | The organ that the biomaterial came from. Blood and connective tissue are considered organs. | object | [See module  organ_ontology](module.md/#organ_ontology) | Organ |  | blood
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
### process
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | process | 
process_core | Core process-level information. | object | [See core  process_core](core.md/#process_core) |  |  | 
### analysis_process
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
process_type | The type of process. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Process type |  | 
outputs | Output generated by the pipeline run. | array | [See   analysis_file](.md/#analysis_file) |  |  | 
tasks | Descriptions of tasks in the workflow. | array |  |  |  | 
analysis_run_type | Indicator of whether the analysis actually ran or was just copied forward as an optimization. | string |  |  | run, copy-forward | 
timestamp_start_utc | Initial start time of the full pipeline. | string |  |  |  | 
timestamp_stop_utc | Terminal stop time of the full pipeline. | string |  |  |  | 
process_core | Core process-level information. | object | [See core  process_core](core.md/#process_core) |  |  | 
reference_bundle | Bundle containing the reference used in running the pipeline. | string |  |  |  | 
input_bundles | The input bundles used in this analysis run. | array |  |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | process | 
inputs | Input parameters used in the pipeline run, these can be files or string values (settings). | array |  |  |  | 
### protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
### imaging_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_type | The type of protocol. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | 
### sequencing_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
instrument_manufacturer_model | The manufacturer and model of the sequencer used. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0000548. | object | [See module  instrument_ontology](module.md/#instrument_ontology) | Instrument manufacturer and model |  | Illumina HiSeq 4000
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
sequencing_approach | The general approach for sequencing. | object | [See module  sequencing_ontology](module.md/#sequencing_ontology) | Sequencing approach |  | full length single cell RNA sequencing
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
paired_end | Was a paired-end sequencing strategy used? | boolean |  | Paired end? |  | Should be one of: yes, no.
### library_preparation_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
strand | Library strandedness. | string |  | Strand | first, second, unstranded | Should be one of: first, second, or unstranded.
library_construction_approach | The general approach for sequencing library construction. | object | [See module  library_construction_ontology](module.md/#library_construction_ontology) | Library construction approach |  | Smart-seq2
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
input_nucleic_acid_molecule | Starting nucleic acid molecule isolated for sequencing. | object | [See module  biological_macromolecule_ontology](module.md/#biological_macromolecule_ontology) | Input nucleic acid molecule |  | polyA RNA
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
end_bias | The type of tag or end bias the library has. | string |  | End bias | 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, full length | Should be one of: 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, or full length.
### enrichment_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
enrichment_method | The method by which enrichment was achieved. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Enrichment method |  | fluorescence-activated cell sorting
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
### aggregate_generation_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
aggregate_formation_method | Method used to form cell aggreagtes. | string |  | Aggregate formation method |  | rocking, suspension cultures, hanging drops, spinner flasks
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
### ipsc_induction_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
induced_pluripotent_cell_induction_method | Induction method applied to primary cell culture to induce pluripotent stem cell generation. | string |  | Induction method | lentivirus, sendai virus, Gun particle, piggyBac transposon, miRNA viral, adenovirus, cre-loxP, plasmid, retroviral | piggyBac transposon
### dissociation_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
dissociation_method | How cells or organelles were dissociated. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Dissociation method |  | enzymatic dissociation
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
### differentiation_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
differentiation_method | Differentiation method applied to cell culture to induce a specific differentiation response. | string |  | Differentiation method |  | Embryoid Body, Monolayer, Inductive Co-Culture
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
### collection_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
collection_method | How the biomaterial was collected. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Collection method |  | blood draw
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
### analysis_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
computational_method | A URI to a versioned workflow and versioned execution environment in a GA4GH-compliant repository. | string |  |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_type | The type of protocol. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | 
### reference_file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
genus_species | The scientific binomial name for the species of this reference. | object | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | integer |  | NCBI taxon ID |  | 9606
reference_version | The genome version of the reference. | string |  | Reference version |  | GencodeV27
assembly_type | The assembly type of the reference. This applies to reference genome sequences. | string |  | Assembly type | primary assembly, complete assembly, patch assembly | Should be one of: primary assembly, complete assembly, or patch assembly.
schema_type | The type of the metadata schema entity. | string |  |  | file | 
reference_type | The type of the genome reference. | string |  | Reference type | genome sequence, transcriptome sequence, annotation reference, transcriptome index, genome sequence index | Should be one of: genome sequence, transcriptome sequence, annotation reference, transcriptome index, or genome sequence index.
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
### sequence_file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
read_index | Whether the read file contains the read1, read2, index1, or index2 part of the sequencing read or represents a single-end, non-indexed library. | string |  | Read index | read1, read2, index1, index2, single-end, non-indexed | Should be one of: read1, read2, index1, index2, or 'single-end, non-indexed'
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
### analysis_file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
### supplementary_file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
## Module
### cell_type_ontology<a name='cell_type_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a cell type supplied by a user. | string |  |  |  | 
### ethnicity_ontology<a name='ethnicity_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The ethnicity of the human donor. | string |  |  |  | 
### species_ontology<a name='species_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the species to which the organism belongs. | string |  |  |  | 
### enrichment_ontology<a name='enrichment_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of an enrichment approach being used. | string |  |  |  | 
### disease_ontology<a name='disease_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  |  |  | 
### organ_part_ontology<a name='organ_part_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  |  |  | 
### length_unit_ontology<a name='length_unit_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a length unit being used. | string |  |  |  | 
### library_construction_ontology<a name='library_construction_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a library construction approach being used. | string |  |  |  | 
### time_unit_ontology<a name='time_unit_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a time unit being used. | string |  |  |  | 
### development_stage_ontology<a name='development_stage_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the development stage of the organism. | string |  |  |  | 
### organ_ontology<a name='organ_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  |  |  | 
### mass_unit_ontology<a name='mass_unit_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a mass unit being used. | string |  |  |  | 
### strain_ontology<a name='strain_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the strain to which the organism belongs (mouse-specific). | string |  |  |  | 
### instrument_ontology<a name='instrument_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The full name of the instrument used. | string |  |  |  | 
### cell_cycle_ontology<a name='cell_cycle_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a cell cycle of the cells in the specimen. | string |  |  |  | 
### library_amplification_ontology<a name='library_amplification_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a library amplification approach being used. | string |  |  |  | 
### process_type_ontology<a name='process_type_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a process type being used. | string |  |  |  | 
### sequencing_ontology<a name='sequencing_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a sequencing approach being used. | string |  |  |  | 
### protocol_type_ontology<a name='protocol_type_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a protocol type used. | string |  |  |  | 
### biological_macromolecule_ontology<a name='biological_macromolecule_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the biological macromolecule being used. | string |  |  |  | 
### contact<a name='contact'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
contact_name | Name of individual who has contributed to the project. | string |  | Contact name |  | John,D,Doe. Format: first name, middle name or initial, last name.
institution | Name of primary institute where the individual works. | string |  | Institute |  | EMBL-EBI
### publication<a name='publication'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
publication_title | The title of the publication. | string |  | Publication title |  | Study of single cells in the human body
authors | A list of authors associated with the publication in 'surname initials' format. | array |  | Authors |  | Doe JD
### funder<a name='funder'></a>
_There are no required properties in schema funder_
### medical_history<a name='medical_history'></a>
_There are no required properties in schema medical_history_
### familial_relationship<a name='familial_relationship'></a>
_There are no required properties in schema familial_relationship_
### cell_morphology<a name='cell_morphology'></a>
_There are no required properties in schema cell_morphology_
### timecourse<a name='timecourse'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
timecourse_unit | The unit in which the Timecourse value is expressed. | object | [See module  time_unit_ontology](module.md/#time_unit_ontology) |  |  | day
timecourse_value | The numerical value in Timecourse unit associated with a time interval used in the experiment. | string |  |  |  | 2
### growth_conditions<a name='growth_conditions'></a>
_There are no required properties in schema growth_conditions_
### preservation_storage<a name='preservation_storage'></a>
_There are no required properties in schema preservation_storage_
### mouse_specific<a name='mouse_specific'></a>
_There are no required properties in schema mouse_specific_
### state_of_specimen<a name='state_of_specimen'></a>
_There are no required properties in schema state_of_specimen_
### human_specific<a name='human_specific'></a>
_There are no required properties in schema human_specific_
### death<a name='death'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
cause_of_death | Cause of death from death report for human donor, from research lab for mouse. | string |  | Cause of death |  | 
### purchased_reagents<a name='purchased_reagents'></a>
_There are no required properties in schema purchased_reagents_
### barcode<a name='barcode'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
barcode_read | The read that the barcode is found in. | string |  | Barcode-containing read | Read 1, Read 2, i7 Index, i5 Index | Should be one of: Read 1, Read 2, i7 Index, or i5 Index.
barcode_length | Length of barcode in nucleotides. | integer |  | Barcode length |  | 28
barcode_offset | 0-based offset of start of barcode in read. 0 for beginning of read. | integer |  | Barcode offset |  | 0
### insdc_experiment<a name='insdc_experiment'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
insdc_experiment | An INSDC (International Nucleotide Sequence Database Collaboration) experiment accession if experiment has been submitted. Can be from the DDBJ, EMBL-EBI, or NCBI.  Accession must start with DRX, ERX, or SRX. | string |  | INSDC experiment |  | SRX0000000
### 10x<a name='10x'></a>
_There are no required properties in schema 10x_
### plate_based_sequencing<a name='plate_based_sequencing'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
plate_id | An ID for the plate that the well is located on. | string |  | Well plate ID |  | 2217
