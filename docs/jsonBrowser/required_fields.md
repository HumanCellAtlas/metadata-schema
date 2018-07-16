# Required fields
_This document contains a list of all required fields in the HCA metadata schema. For a fulldescription of each schema, please refer to the relevant entity specification document._
## Core
### biomaterial_core<a name='biomaterial_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
biomaterial_id | A unique ID for this biomaterial. | string |  | Biomaterial ID |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. Multiple IDs can be provided for multi-species samples. | array |  | NCBI taxon ID |  | 
### file_core<a name='file_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
file_name | The filename of the data file. | string |  | File name |  | 
file_format | The format of the data file. | string |  | File format |  | 
### process_core<a name='process_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
process_id | A unique ID for this process. | string |  | Process ID |  | 
### project_core<a name='project_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
project_short_name | A short name for the project. | string |  | Project label |  | For example, a short label by which you refer to the project. This will be used for quick orientation and reference.
project_title | An official title for your project. | string |  | Project title |  | For example, the title of a grant proposal or a publication, approximately 30 words. This is how the project title will appear on the Human Cell Atlas data portal.
project_description | A longer description of the project which includes research goals and experimental approach. | string |  | Project description |  | For example, an abstract from a grant application or publication. Approximately 300 words.
### protocol_core<a name='protocol_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_id | A unique ID for this protocol. | string |  | Protocol ID |  | 
## Type
### cell_line
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
cell_line_type | The type of cell line. Must be one of primary, immortalized, stem cell-derived, or synthetic. | string |  | Cell line type | primary, immortalized, stem cell-derived, synthetic, induced pluripotent | induced pluripotent
### cell_suspension
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
### donor_organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
is_living | Yes if organism is alive at time of biomaterial collection. No if dead. Unknown if not known. | string |  | Is living? | yes, no, unknown | 
biological_sex | The biological sex of the organism. Should be one of male, female, mixed, or unknown. | string |  | Biological sex | female, male, mixed, unknown | 
### organoid
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
model_for_organ | Organ for which this organoid is a model system. | object | [See module  organ_ontology](module.md/#organ_ontology) | Organ model |  | brain
### specimen_from_organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
organ | The organ that the biomaterial came from. Blood and connective tissue are considered organs. | object | [See module  organ_ontology](module.md/#organ_ontology) | Organ |  | Blood
### analysis_file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
### reference_file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | integer |  | NCBI taxon ID |  | 
genus_species | The scientific binomial name for the species of this reference. | object | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
assembly_type | The assembly type of this reference. This applies to reference genome sequences. | string |  |  | primary assembly, complete assembly, patch assembly | 
reference_type | The type of the genome reference. | string |  |  | genome sequence, transcriptome sequence, annotation reference, transcriptome index, genome sequence index | 
reference_version | The genome version of the reference. | string |  |  |  | GencodeV27
### sequence_file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
read_index | Whether the read file contains the read1, read2, index1, or index2 part of the sequencing read. If read file represents a single-end, non-indexed library, indicate that here. | string |  | Read index | read1, read2, index1, index2, single-end, non-indexed | read1
### supplementary_file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
### process
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | process | 
process_core | Core process-level information. | object | [See core  process_core](core.md/#process_core) |  |  | 
### project
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | project | 
### protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
### analysis_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
protocol_type | The type of protocol. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | 
inputs | Input parameters used in the pipeline run, these can be files or string values (settings). | array |  |  |  | 
reference_bundle | Bundle containing the reference used in running the pipeline. | string |  |  |  | 
tasks | Descriptions of tasks in the workflow. | array |  |  |  | 
timestamp_stop_utc | Terminal stop time of the full pipeline. | string |  |  |  | 
input_bundles | The input bundles used in this analysis run. | array |  |  |  | 
outputs | Output generated by the pipeline run. | array | [See   analysis_file](.md/#analysis_file) |  |  | 
computational_method | A URI to a versioned workflow and versioned execution environment in a GA4GH-compliant repository. | string |  |  |  | 
timestamp_start_utc | Initial start time of the full pipeline. | string |  |  |  | 
analysis_run_type | Indicator of whether the analysis actually ran or was just copied forward as an optimization. | string |  |  | run, copy-forward | 
### aggregate_generation_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
aggregate_formation_method | Method used to form cell aggreagtes. | string |  | Aggregate formation method |  | rocking, suspension cultures, hanging drops, spinner flasks
### biomaterial_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
collection_method | How the biomaterial was collected. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Collection method |  | 
### differentiation_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
differentiation_method | Differentiation method applied to cell culture to induce a specific differentiation response. | string |  | Differentiation method |  | Embryoid Body, Monolayer, Inductive Co-Culture
### dissociation_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
dissociation_method | How cells or organelles were dissociated. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0002694. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Dissociation method |  | 
nucleic_acid_source | Source cells or organelles from which nucleic acid molecules were collected. | string |  | Nucleic acid source | bulk cell, single cell, single nucleus, bulk nuclei, mitochondria | 
### enrichment_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
enrichment_method | The method by which enrichment was achieved. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0002694. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Enrichment method |  | 
### ipsc_induction_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
induced_pluripotent_cell_induction_method | Induction method applied to primary cell culture to induce pluripotent stem cell generation. | string |  | Induction method | lentivirus, sendai virus, Gun particle, piggyBac transposon, miRNA viral, adenovirus, cre-loxP, plasmid, retroviral | piggyBac transposon
### imaging_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
protocol_type | The type of protocol. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | 
### library_preparation_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
input_nucleic_acid_molecule | Starting nucleic acid molecule isolated for sequencing. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0004446. | object | [See module  biological_macromolecule_ontology](module.md/#biological_macromolecule_ontology) | Input nucleic acid molecule |  | 
library_construction_approach | The general approach for sequencing library construction. Should be a child term of EFO - library preparation | object | [See module  library_construction_ontology](module.md/#library_construction_ontology) | Library construction approach |  | 
end_bias | The type of tag or end bias the library has. Must be one of 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, or full length. | string |  | End bias | 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, full length | 3_prime_tag
strand | Library strandedness. Must be one of first, second, or unstranded. | string |  | Strand | first, second, unstranded | unstranded
### sequencing_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
instrument_manufacturer_model | The manufacturer and model of the sequencer used. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0000548. | object | [See module  instrument_ontology](module.md/#instrument_ontology) | Instrument manufacturer and model |  | Illumina HiSeq 4000
paired_ends | Was a paired-end sequencing strategy used? Must be either yes or no. | boolean |  | Paired ends? |  | yes
sequencing_approach | The general approach for sequencing. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000070. | object | [See module  sequencing_ontology](module.md/#sequencing_ontology) | Protocol type |  | 
## Module
### cell_morphology<a name='cell_morphology'></a>
_There are no required properties in schema cell_morphology_
### death<a name='death'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
cause_of_death | Cause of death from death report for human donor, from research lab for mouse. | string |  | Cause of death |  | 
### familial_relationship<a name='familial_relationship'></a>
_There are no required properties in schema familial_relationship_
### growth_conditions<a name='growth_conditions'></a>
_There are no required properties in schema growth_conditions_
### human_specific<a name='human_specific'></a>
_There are no required properties in schema human_specific_
### medical_history<a name='medical_history'></a>
_There are no required properties in schema medical_history_
### mouse_specific<a name='mouse_specific'></a>
_There are no required properties in schema mouse_specific_
### preservation_storage<a name='preservation_storage'></a>
_There are no required properties in schema preservation_storage_
### state_of_specimen<a name='state_of_specimen'></a>
_There are no required properties in schema state_of_specimen_
### timecourse<a name='timecourse'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
timecourse_value | The numerical value associated with a time interval used in the experiment. | string |  |  |  | 2
timecourse_unit | The unit in which the timecourse value is expressed. | object | [See module  time_unit_ontology](module.md/#time_unit_ontology) |  |  | day
### biological_macromolecule_ontology<a name='biological_macromolecule_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the biological macromolecule being used. | string |  |  |  | 
### cell_cycle_ontology<a name='cell_cycle_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a cell cycle of the cells in the specimen. | string |  |  |  | 
### cell_type_ontology<a name='cell_type_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a cell type supplied by a user. | string |  |  |  | 
### development_stage_ontology<a name='development_stage_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the development stage of the organism. | string |  |  |  | 
### disease_ontology<a name='disease_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  |  |  | 
### enrichment_ontology<a name='enrichment_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of an enrichment approach being used. | string |  |  |  | 
### ethnicity_ontology<a name='ethnicity_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The ethnicity of the human donor. | string |  |  |  | 
### instrument_ontology<a name='instrument_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The full name of the instrument used. | string |  |  |  | 
### length_unit_ontology<a name='length_unit_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a length unit being used. | string |  |  |  | 
### library_amplification_ontology<a name='library_amplification_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a library amplification approach being used. | string |  |  |  | 
### library_construction_ontology<a name='library_construction_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a library construction approach being used. | string |  |  |  | 
### mass_unit_ontology<a name='mass_unit_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a mass unit being used. | string |  |  |  | 
### organ_ontology<a name='organ_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  |  |  | 
### organ_part_ontology<a name='organ_part_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string |  |  |  | 
### process_type_ontology<a name='process_type_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a process type being used. | string |  |  |  | 
### protocol_type_ontology<a name='protocol_type_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a protocol type used. | string |  |  |  | 
### sequencing_ontology<a name='sequencing_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a sequencing approach being used. | string |  |  |  | 
### species_ontology<a name='species_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the species to which the organism belongs. | string |  |  |  | 
### strain_ontology<a name='strain_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of the strain to which the organism belongs (mouse-specific). | string |  |  |  | 
### time_unit_ontology<a name='time_unit_ontology'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
text | The name of a time unit being used. | string |  |  |  | 
### purchased_reagents<a name='purchased_reagents'></a>
_There are no required properties in schema purchased_reagents_
### barcode<a name='barcode'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
barcode_read | The read that the barcode is found in. Should be one of Read 1, Read 2, i7 Index, or i5 Index. | string |  | Barcode-containing read | Read 1, Read 2, i7 Index, i5 Index | 
barcode_offset | 0-based offset of start of barcode in read. 0 for beginning of read. | integer |  | Barcode offset |  | 
barcode_length | Length of barcode in nucleotides. | integer |  | Barcode length |  | 
### insdc_experiment<a name='insdc_experiment'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
insdc_experiment | An INSDC (International Nucleotide Sequence Database Collaboration) experiment accession. Accession must start with DRX, ERX, or SRX. | string |  | INSDC experiment |  | 
### smartseq2<a name='smartseq2'></a>
_There are no required properties in schema smartseq2_
### contact<a name='contact'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
contact_name | Name of any individual who has contributed to this project. | string |  | Contact name |  | Format: 'first, middle, last name', middle can be initial or left blank. Example: John,D,Smith.
institution | Name of primary institute where the individual works. | string |  | Institute |  | 
### funder<a name='funder'></a>
_There are no required properties in schema funder_
### publication<a name='publication'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
authors | A list of authors associated with the publication in 'surname initials' format. | array |  | Authors |  | Smith JD
publication_title | The full title of the publication. | string |  | Publication title |  | 
## Bundle
### biomaterial
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial_bundle | 
### file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file_bundle | 
### ingest
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
submissionDate | When project was first submitted to database. | string |  |  |  | 
document_id | Identifier for document. | string |  |  |  | 
### links
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | link_bundle | 
### process
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | process_bundle | 
### project
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | project_bundle | 
hca_ingest | Core fields added by HCA ingest service | object | [See   ingest_audit](.md/#ingest_audit) |  |  | 
content | Content for a project type entity. | object | [See   project](.md/#project) |  |  | 
### protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | protocol_bundle | 
### reference
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | reference_bundle | 
### submission
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
transfer_service_version |  |  |  |  |  | 
submitted_files |  |  |  |  |  | 
