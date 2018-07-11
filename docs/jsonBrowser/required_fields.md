# Required fields
_This document contains a list of all required fields in the HCA metadata schema. For a fulldescription of each schema, please refer to the relevant entity specification document._
## Core
### links<a name='links'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | link_bundle | 
### provenance_core<a name='provenance_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
submission_date | When project was first submitted to database. | string |  |  |  | 
document_id | Identifier for document. | string |  |  |  | 
### biomaterial_core<a name='biomaterial_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. Multiple IDs can be provided for multi-species samples. | array |  | NCBI taxon ID |  | 
biomaterial_id | A unique ID for this biomaterial. | string |  | Biomaterial ID |  | 
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
project_shortname | A unique label for the project. | string |  | Project label |  | my_project
project_description | A longer description of the project which can include research goals and experimental approach. Approximately 300 words. | string |  | Project description |  | An abstract from a publication.
project_title | A summary of the project in one sentence. Approximately 30 words. | string |  | Project title |  | A publication title.
### protocol_core<a name='protocol_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_id | A unique ID for this protocol. | string |  | Protocol ID |  | 
## Type
### cell_line
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
cell_line_type | The type of cell line. Must be one of primary, immortalized, stem cell-derived, or synthetic. | string |  | Cell line type | primary, immortalized, stem cell-derived, synthetic, induced pluripotent | induced pluripotent
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
### cell_suspension
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
### donor_organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
biological_sex | The biological sex of the organism. Should be one of male, female, mixed, or unknown. | string |  | Biological sex | female, male, mixed, unknown | 
is_living | Yes if organism is alive at time of biomaterial collection. No if dead. Unknown if not known. | string |  | Is living? | yes, no, unkown | 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
### organoid
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
model_for_organ | Organ for which this organoid is a model system. | object | [See module  organ_ontology](module.md/#organ_ontology) | Organ model |  | 
### specimen_from_organism
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
organ | The organ that the biomaterial came from. Blood and connective tissue are considered organs. | object | [See module  organ_ontology](module.md/#organ_ontology) | Organ |  | Blood
schema_type | The type of the metadata schema entity. | string |  |  | biomaterial | 
biomaterial_core | Core biomaterial-level information. | object | [See core  biomaterial_core](core.md/#biomaterial_core) |  |  | 
### analysis_file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
### reference_file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
reference_type | The type of the genome reference. | string |  |  | genome sequence, transcriptome sequence, annotation reference, transcriptome index, genome sequence index | 
genus_species | The scientific binomial name for the species of this reference. | object | [See module  species_ontology](module.md/#species_ontology) | Genus species |  | Homo sapiens
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | integer |  | NCBI taxon ID |  | 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
assembly_type | The assembly type of this reference. This applies to reference genome sequences. | string |  |  | primary assembly, complete assembly, patch assembly | 
reference_version | The genome version of the reference. | string |  |  |  | GencodeV27
### sequence_file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
read_index | Whether the read file contains the read1, read2, index1, or index2 part of the sequencing read. If read file represents a single-end, non-indexed library, indicate that here. | string |  | Read index | read1, read2, index1, index2, single-end, non-indexed | read1
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
### process
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
process_core | Core process-level information. | object | [See core  process_core](core.md/#process_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | process | 
### project
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | project | 
### protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
### analysis_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
inputs | Input parameters used in the pipeline run, these can be files or string values (settings). | array |  |  |  | 
reference_bundle | Bundle containing the reference used in running the pipeline. | string |  |  |  | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
analysis_run_type | Indicator of whether the analysis actually ran or was just copied forward as an optimization. | string |  |  | run, copy-forward | 
timestamp_stop_utc | Terminal stop time of the full pipeline. | string |  |  |  | 
input_bundles | The input bundles used in this analysis run. | array |  |  |  | 
outputs | Output generated by the pipeline run. | array | [See   analysis_file](.md/#analysis_file) |  |  | 
timestamp_start_utc | Initial start time of the full pipeline. | string |  |  |  | 
tasks | Descriptions of tasks in the workflow. | array |  |  |  | 
computational_method | A URI to a versioned workflow and versioned execution environment in a GA4GH-compliant repository. | string |  |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_type | The type of protocol. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | 
### aggregate_generation_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
aggregate_formation_method | Method used to form cell aggreagtes. | string |  | Aggregate formation method |  | rocking, suspension cultures, hanging drops, spinner flasks
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
### biomaterial_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
collection_method | How the biomaterial was collected. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Collection method |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
### differentiation_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
differentiation_method | Differentiation method applied to cell culture to induce a specific differentiation response. | string |  | Differentiation method |  | Embryoid Body, Monolayer, Inductive Co-Culture
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
### dissociation_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
nucleic_acid_source | Source cells or organelles from which nucleic acid molecules were collected. | string |  | Nucleic acid source | bulk cell, single cell, single nucleus, bulk nuclei, mitochondria | 
dissociation_method | How cells or organelles were dissociated. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0002694. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Dissociation method |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
### enrichment_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
enrichment_method | The method by which enrichment was achieved. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0002694. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Enrichment method |  | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
### ipsc_induction_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
induced_pluripotent_cell_induction_method | Induction method applied to primary cell culture to induce pluripotent stem cell generation. | string |  | Induction method | lentivirus, sendai virus, Gun particle, piggyBac transposon, miRNA viral, adenovirus, cre-loxP, plasmid, retroviral | piggyBac transposon
### imaging_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
protocol_type | The type of protocol. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000272. | object | [See module  process_type_ontology](module.md/#process_type_ontology) | Protocol type |  | 
### library_preparation_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
input_nucleic_acid_molecule | Starting nucleic acid molecule isolated for sequencing. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0004446. | object | [See module  biological_macromolecule_ontology](module.md/#biological_macromolecule_ontology) | Input nucleic acid molecule |  | 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
strand | Library strandedness. Must be one of first, second, or unstranded. | string |  | Strand | first, second, unstranded | unstranded
library_construction_approach | The general approach for sequencing library construction. Should be a child term of EFO - library preparation | object | [See module  library_construction_ontology](module.md/#library_construction_ontology) | Library construction approach |  | 
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
end_bias | The type of tag or end bias the library has. Must be one of 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, or full length. | string |  | End bias | 3 prime tag, 3 prime end bias, 5 prime tag, 5 prime end bias, full length | 3_prime_tag
### sequencing_protocol
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_core | Core protocol-level information. | object | [See core  protocol_core](core.md/#protocol_core) |  |  | 
instrument_manufacturer_model | The manufacturer and model of the sequencer used. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fwww.ebi.ac.uk%2Fefo%2FEFO_0000548. | object | [See module  instrument_ontology](module.md/#instrument_ontology) | Instrument manufacturer and model |  | Illumina HiSeq 4000
sequencing_approach | The general approach for sequencing. Must be a child term of https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FOBI_0000070. | object | [See module  sequencing_ontology](module.md/#sequencing_ontology) | Protocol type |  | 
paired_ends | Was a paired-end sequencing strategy used? Must be either yes or no. | boolean |  | Paired ends? |  | yes
schema_type | The type of the metadata schema entity. | string |  |  | protocol | 
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
### homo_sapiens_specific<a name='homo_sapiens_specific'></a>
_There are no required properties in schema homo_sapiens_specific_
### medical_history<a name='medical_history'></a>
_There are no required properties in schema medical_history_
### mus_musculus_specific<a name='mus_musculus_specific'></a>
_There are no required properties in schema mus_musculus_specific_
### preservation_storage<a name='preservation_storage'></a>
_There are no required properties in schema preservation_storage_
### state_of_specimen<a name='state_of_specimen'></a>
_There are no required properties in schema state_of_specimen_
### timecourse<a name='timecourse'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
timecourse_unit | The unit in which the timecourse value is expressed. | object | [See module  time_unit_ontology](module.md/#time_unit_ontology) |  |  | day
timecourse_value | The numerical value associated with a time interval used in the experiment. | string |  |  |  | 2
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
barcode_offset | 0-based offset of start of barcode in read. 0 for beginning of read. | integer |  | Barcode offset |  | 
barcode_read | The read that the barcode is found in. Should be one of Read 1, Read 2, i7 Index, or i5 Index. | string |  | Barcode-containing read | Read 1, Read 2, i7 Index, i5 Index | 
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
email | An email address for the contact. | string |  | Email |  | 
contact_name | The contact's name. Should be in the format 'first, middle, last name'. Middle can be initial or left blank. | string |  | Contact name |  | John,D,Doe
### funder<a name='funder'></a>
_There are no required properties in schema funder_
### publication<a name='publication'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
publication_title | The full title of the publication. | string |  | Publication title |  | 
authors | A list of authors associated with the publication in 'surname initials' format. | array |  | Authors |  | Smith JD
## Bundle
