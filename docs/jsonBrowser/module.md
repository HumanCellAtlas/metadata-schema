# Module
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## Channel<a name='Channel'></a>
_Information about a single microscope channel._

Location: module/protocol/channel.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
channel_id | User given ID.  If there is an accompanying codebook, this name should correspond to the channel id used in the codebook. | string | yes |  | Channel ID |  | 1; A
excitation_wavelength | Excitation wavelength of the lightsource in nanometers. | number | yes |  | Excitation wavelength |  | 640
filter_range | Emission filter in nanometers. | string | yes |  | Filter range |  | 461/70
multiplexed | Whether multiple targets were detected simultaneously in this channel. | string | yes |  | Multiplexed experiment | yes, no | Should be one of: yes, or no.
target_fluorophore | The name of the fluorophore this channel is designed to assay. | string | no |  | Target fluorophore |  | Alexa 647
exposure_time | Acquisition time for a single image per channel, in milliseconds. | number | yes |  | Exposure time |  | 400

## Probe<a name='Probe'></a>
_Information about probes used to detect targets._

Location: module/protocol/probe.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
probe_label | The label of a probe used to detect target in this experiment. | string | yes |  | Probe label |  | ACTA1; cFos
probe_sequence | Sequence of a probe used to detect target. | string | no |  | Probe sequence |  | AGGCTATAGCGGAGCTACG; aggctatagcggagctacg
target_name | The name of the target molecule. | string | no |  | Target name |  | ACTA1_exon1; nuclear cFos
target_codebook_label | A label used in the codebook for the target. | string | no |  | Target label in codebook |  | AKT1; CFOS
target_label | An identifier for the target molecule. | string | yes |  | Target label |  | CHEBI:85345; ENSG00000170345
subcellular_structure | Target subcellular structure. | object | no | [See module  cellular_component_ontology](module.md#cellular-component-ontology) | Target subcellular structure |  | 
probe_reagents | Name of reagents used to construct the probe. | object | no | [See module  purchased_reagents](module.md#purchased-reagents) | Probe construction reagents |  | 
assay_type | Type of assay used to detect target. | object | yes | [See module  process_type_ontology](module.md#process-type-ontology) | Assay type |  | MERFISH; in situ sequencing
fluorophore | Fluorophore used to detect target. | array | no |  | Fluorophore |  | Cy5; Alexa 488
channel_label | Channel label used to assay signal. | array | no |  | Channel |  | 1; A

## Matrix<a name='Matrix'></a>
_Information relating to generation of matrices_

Location: module/protocol/matrix.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
data_normalization_methods | Method(s) used to normalize data in the matrix | array | no |  | Data normalization method(s) | CPM (counts per million), TPM (transcripts per kilobase million), RPKM (reads per kilobase of exon per million reads mapped), FPKM (fragments per kilobase of exon per million fragments mapped), DESeq2's median of ratios, TMM (EdgeR's trimmed mean of M values), SF (size factor), UQ (Upper quartile), Downsampling, other, unknown | 
derivation_process | Type of computational tool used in generating the matrix object. | array | no |  | Derivation process | alignment, quantification, peak calling, peak annotation, gene filtering, cell filtering, merging, cell calling, ambient RNA correction, doublet removal, batch correction, depth normalization, other | 

## File content ontology<a name='File content ontology'></a>
_A term that describes the contents of a file._

Location: module/ontology/file_content_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | General description of the contents of the file. | string | yes |  | Content description |  | DNA sequence (raw); Sequence alignment
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Content description ontology ID |  | EDAM:3494; EDAM:0863
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Content description ontology label |  | DNA sequence; Sequence alignment

## Length unit ontology<a name='Length unit ontology'></a>
_A term that may be associated with a cell type-related ontology term._

Location: module/ontology/length_unit_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a length unit being used. | string | yes |  | Length unit |  | micrometer; meter
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Length unit ontology ID |  | UO:0000017; UO:0000008
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Length unit ontology label |  | micrometer; meter

## Cell cycle ontology<a name='Cell cycle ontology'></a>
_A term that may be associated with a cell cycle-related ontology term._

Location: module/ontology/cell_cycle_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a cell cycle of the cells in the specimen. | string | yes |  | Cell cycle |  | meiotic cell cycle; mitotic G1 phase
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Cell cycle ontology ID |  | GO:0051321; GO:0000080
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Cell cycle ontology label |  | meiotic cell cycle; mitotic G1 phase

## Library amplification ontology<a name='Library amplification ontology'></a>
_A term that may be associated with a process-related ontology term._

Location: module/ontology/library_amplification_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a library amplification approach being used. | string | yes |  | Library amplification |  | PCR; in vitro transcription
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Library amplification ontology ID |  | OBI:0000415; EFO:0009013
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Library amplification ontology label |  | PCR; in vitro transcription

## Contributor role ontology<a name='Contributor role ontology'></a>
_A term that describes the role of a contributor in the project._

Location: module/ontology/contributor_role_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The primary role of the contributor in the project. | string | yes |  | Contributor role |  | principal investigator; experimental scientist
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Contributor role ontology ID |  | EFO:0009736; EFO:0009741
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Contributor role ontology label |  | principal investigator; experimental scientist

## Ethnicity ontology<a name='Ethnicity ontology'></a>
_A term that may be associated with a ethnicity-related ontology term._

Location: module/ontology/ethnicity_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The ethnicity of the human donor. | string | yes |  | Ethnicity |  | European; Hispanic or Latin American
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Ethnicity ontology ID |  | HANCESTRO:0005; HANCESTRO:0014
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Ethnicity ontology label |  | European; Hispanic or Latin American

## Target pathway ontology<a name='Target pathway ontology'></a>
_A term that may be associated with a process-related ontology term._

Location: module/ontology/target_pathway_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the treatment target pathway. | string | yes |  | Target pathway |  | positive regulation of memory T cell differentiation
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Target pathway ontology ID |  | GO:0043382
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Target pathway ontology label |  | positive regulation of memory T cell differentiation

## Treatment method ontology<a name='Treatment method ontology'></a>
_A term that may be associated with a process-related ontology term._

Location: module/ontology/treatment_method_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a treatment method or approach being used. | string | yes |  | Treatment method |  | T cell activation assay
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Treatment ontology ID |  | EFO:0030037
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Treatment ontology label |  | T cell activation assay

## Cellular component ontology<a name='Cellular component ontology'></a>
_A term that may be associated with an intra-cellular structure ontology term._

Location: module/ontology/cellular_component_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a subcellular structure. | string | yes |  | Subcellular structure |  | cytoplasm; nucleus
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Subcellular structure ontology ID |  | GO:0005737; GO:0005634
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Subcellular structure ontology label |  | cytoplasm; nucleus

## Library construction ontology<a name='Library construction ontology'></a>
_A term that may be associated with a process-related ontology term._

Location: module/ontology/library_construction_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a library construction approach being used. | string | yes |  | Library construction |  | 10X v2 sequencing; Smart-seq2
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Library construction ontology ID |  | EFO:0009310; EFO:0008931
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Library construction ontology label |  | 10X v2 sequencing; Smart-seq2

## Process type ontology<a name='Process type ontology'></a>
_A term that may be associated with a process-related ontology term._

Location: module/ontology/process_type_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a process type being used. | string | yes |  | Process type |  | enzymatic dissociation; blood draw
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Process type ontology ID |  | EFO:0009128; EFO:0009121
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Process type ontology label |  | enzymatic dissociation; blood draw

## Gender identity ontology<a name='Gender identity ontology'></a>
_A term that may be associated with a gender-related ontology term._

Location: module/ontology/gender_identity_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The gender identity of the human donor at the time of the experiment. | string | yes |  | Gender identity |  | Female Gender; Agender; Non-Binary Gender
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Gender identity ontology ID |  | NCIT:C46110; NCIT:C205469; NCIT:C160941
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Gender identity ontology label |  | Female Gender; Agender; Non-Binary Gender

## Sequencing ontology<a name='Sequencing ontology'></a>
_A term that may be associated with a process-related ontology term._

Location: module/ontology/sequencing_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a sequencing approach being used. | string | yes |  | Sequencing approach |  | tag based single cell RNA sequencing; full length single cell RNA sequencing
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Sequencing approach ontology ID |  | EFO:0008440; EFO:0008441
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Sequencing approach ontology label |  | tag based single cell RNA sequencing; full length single cell RNA sequencing

## Species ontology<a name='Species ontology'></a>
_A term that may be associated with a species-related ontology term._

Location: module/ontology/species_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the species to which the organism belongs. | string | yes |  | Species |  | Homo sapiens; Mus musculus
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Species ontology ID |  | NCBITaxon:9606; NCBITaxon:10090
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Species ontology label |  | Homo sapiens; Mus musculus

## Disease ontology<a name='Disease ontology'></a>
_A term that may be associated with a disease-related ontology term._

Location: module/ontology/disease_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string | yes |  | Disease |  | type 2 diabetes mellitus; normal
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Disease ontology ID |  | MONDO:0005148; PATO:0000461; HP:0001397
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Disease ontology label |  | type 2 diabetes mellitus; normal

## Strain ontology<a name='Strain ontology'></a>
_A term that may be associated with a strain-related ontology term._

Location: module/ontology/strain_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the strain to which the organism belongs. | string | yes |  | Strain |  | C57BL/6; BALB/c
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Strain ontology ID |  | EFO:0004472; EFO:0000602
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Strain ontology label |  | C57BL/6; BALB/c

## Medication ontology<a name='Medication ontology'></a>
_A term that may be associated with a medication-related ontology term._

Location: module/ontology/medication_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | Medication(s) the individual was taking at time of biomaterial collection. | string | yes |  | Medication |  | bisoprolol; paracetamol; loratadine
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Medication ontology ID |  | CHEBI:3127; CHEBI:46195; CHEBI:6538
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Medication ontology label |  | bisoprolol; paracetamol; loratadine

## File format ontology<a name='File format ontology'></a>
_A term that may be associated with a file format-related ontology term._

Location: module/ontology/file_format_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the file format. | string | yes |  | File format |  | FASTQ; JSON
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | File format ontology ID |  | format:1930; format:3464
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | File format ontology label |  | FASTQ; JSON

## Enrichment ontology<a name='Enrichment ontology'></a>
_A term that may be associated with a process-related ontology term._

Location: module/ontology/enrichment_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of an enrichment approach being used. | string | yes |  | Enrichment |  | fluorescence-activated cell sorting; Ficoll-Hypaque method
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Enrichment ontology ID |  | EFO:0009108; EFO:0009110
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Enrichment ontology label |  | fluorescence-activated cell sorting; Ficoll-Hypaque method

## Organ part ontology<a name='Organ part ontology'></a>
_A term that may be associated with an anatomy-related ontology term._

Location: module/ontology/organ_part_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string | yes |  | Organ part |  | bone marrow; islet of Langerhans
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Organ part ontology ID |  | UBERON:0002371; UBERON:0000006
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Organ part ontology label |  | bone marrow; islet of Langerhans

## Microscopy ontology<a name='Microscopy ontology'></a>
_A term that may be associated with a microscopy-related ontology term._

Location: module/ontology/microscopy_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the type of microscopy used in an imaging experiment. | string | yes |  | Microscopy |  | confocal microscopy; fluorescence microscopy
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Microscopy ontology ID |  | FBbi:00000251; FBbi:00000246
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Microscopy ontology label |  | confocal microscopy; fluorescence microscopy

## Time unit ontology<a name='Time unit ontology'></a>
_A term that may be associated with a time unit-related ontology term._

Location: module/ontology/time_unit_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a time unit being used. | string | yes |  | Time unit |  | second; week
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Time unit ontology ID |  | UO:0000010; UO:0000034
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Time unit ontology label |  | second; week

## Protocol type ontology<a name='Protocol type ontology'></a>
_A term that may be associated with a protocol-related ontology term._

Location: module/ontology/protocol_type_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a protocol type used. | string | yes |  | Protocol type |  | dissociation protocol; enrichment protocol
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Protocol type ontology ID |  | EFO:0009088; EFO:0009089
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Protocol type ontology label |  | dissociation protocol; enrichment protocol

## Development stage ontology<a name='Development stage ontology'></a>
_A term that may be associated with a development stage-related ontology term._

Location: module/ontology/development_stage_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the development stage of the organism. | string | yes |  | Development stage |  | human adult stage; Theiler stage 28
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Development stage ontology ID |  | HsapDv:0000087; EFO:0002588
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Development stage ontology label |  | human adult stage; Theiler stage 28

## Instrument ontology<a name='Instrument ontology'></a>
_A term that may be associated with a instrument-related ontology term._

Location: module/ontology/instrument_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The full name of the instrument used. | string | yes |  | Instrument |  | Illumina HiSeq 2500; ONT MinION
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Instrument ontology ID |  | EFO:0008565; EFO:0008632
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Instrument ontology label |  | Illumina HiSeq 2500; ONT MinION

## Mass unit ontology<a name='Mass unit ontology'></a>
_A term that may be associated with a cell type-related ontology term._

Location: module/ontology/mass_unit_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a mass unit being used. | string | yes |  | Mass unit |  | kilogram; microgram
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Mass unit ontology ID |  | UO:0000009; UO:0000023
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Mass unit ontology label |  | kilogram; microgram

## Biological macromolecule ontology<a name='Biological macromolecule ontology'></a>
_A term that may be associated with a biological macromolecule-related ontology term._

Location: module/ontology/biological_macromolecule_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the biological macromolecule being used. | string | yes |  | Biological macromolecule |  | polyA RNA; mRNA
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Biological macromolecule ontology ID |  | OBI:0000869; CHEBI:33699
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Biological macromolecule ontology label |  | polyA RNA; messenger RNA

## Cell type ontology<a name='Cell type ontology'></a>
_A term that may be associated with a cell type-related ontology term._

Location: module/ontology/cell_type_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a cell type supplied by a user. | string | yes |  | Cell type |  | bone marrow hematopoietic cell; cardiac muscle cell
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Cell type ontology ID |  | CL:1001610; CL:0000746
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Cell type ontology label |  | bone marrow hematopoietic cell; cardiac muscle cell

## Organ ontology<a name='Organ ontology'></a>
_A term that may be associated with an anatomy-related ontology term._

Location: module/ontology/organ_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string | yes |  | Organ |  | heart; immune system
ontology | An ontology term identifier in the form prefix:accession. | string | no |  | Organ ontology ID |  | UBERON:0000948; UBERON:0002405
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field. | string | no |  | Organ ontology label |  | heart; immune system

## Funder<a name='Funder'></a>
_Information about the project funding source._

Location: module/project/funder.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
grant_title | The name of the grant funding the project. | string | no |  | Grant title |  | Study of single cells in the human body.
grant_id | The unique grant identifier or reference. | string | yes |  | Grant ID |  | BB/P0000001/1
organization | The name of the funding organization. | string | yes |  | Funding organization |  | Biotechnology and Biological Sciences Research Council (BBSRC); California Institute of Regenerative Medicine (CIRM)

## HCA Bionetwork<a name='HCA Bionetwork'></a>
_Information about whether the project is part of a HCA Bionetwork or HCA Atlas._

Location: module/project/hca_bionetwork.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
name | HCA Bionetwork the project is a part of (e.g. Kidney).  | string | no |  | Official HCA Bionetwork | Adipose, Breast, Development, Eye, Genetic Diversity, Gut, Heart, Immune, Kidney, Liver, Lung, Musculoskeletal, Nervous System, Oral & Craniofacial, Organoid, Pancreas, Reproduction, Skin | Kidney; Lung
hca_tissue_atlas | A field describing if the project is part of a HCA Tissue Atlas (e.g. Brain Alzheimer Atlas).  | string | no |  | HCA Tissue Atlas | Adipose, Blood, Brain, Breast, Development, Eye, GDN, Gut, Heart, Immune, Kidney, Liver, Lung, MSK, ORCF, Organoid-Endoderm, Organoid-Neural, Pancreas, Retina, Reproduction, Skin | Retina
hca_tissue_atlas_version | A field describing which version of the HCA Tissue Atlas is associated with the project (e.g. v1.0; v2.0) | string | no |  | Official HCA Tissue Atlas Version |  | v1.0; v2.0
atlas_project | A field describing if this project is the HCA Tissue Atlas project which integrates data from other datasets. | boolean | no |  | Project Tissue Atlas Status |  | Yes; No

## Contact<a name='Contact'></a>
_Information about an individual who submitted or contributed to a project._

Location: module/project/contact.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
name | Name of individual who has contributed to the project. | string | yes |  | Contact name |  | John,D,Doe; Jane,,Smith
email | Email address for the individual. | string | no |  | Email address |  | dummy@email.com
phone | Phone number of the individual or their lab. | string | no |  | Phone number |  | (+1) 234-555-6789
institution | Name of primary institute where the individual works. | string | yes |  | Institute |  | EMBL-EBI; University of Washington
laboratory | Name of lab or department within the institute where the individual works. | string | no |  | Laboratory/Department |  | Division of Vaccine Discovery; Department of Biology
address | Street address where the individual works. | string | no |  | Street address |  | 0000 Main Street, Nowheretown, MA, 12091
country | Country where the individual works. | string | no |  | Country |  | USA
corresponding_contributor | Whether the individual is a primary point of contact for the project. | boolean | no |  | Corresponding contributor |  | Should be one of: yes, or no.
project_role | Primary role of the individual in the project. | object | no | [See module  contributor_role_ontology](module.md#contributor-role-ontology) | Project role |  | principal investigator; computational scientist
orcid_id | The individual's ORCID ID linked to previous work. | string | no |  | ORCID ID |  | 0000-1111-2222-3333

## Publication<a name='Publication'></a>
_Information about a journal article, book, web page, or other external available documentation for a project._

Location: module/project/publication.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
authors | A list of authors associated with the publication. | array | yes |  | Authors |  | Doe JD
title | The title of the publication. | string | yes |  | Publication title |  | Study of single cells in the human body.
doi | The publication digital object identifier (doi) of the publication. | string | no |  | Publication DOI |  | 10.1016/j.cell.2016.07.054
pmid | The PubMed ID of the publication. | integer | no |  | Publication PMID |  | 27565351
url | A URL for the publication. | string | no |  | Publication URL |  | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5667944/
official_hca_publication | Has the publication been accepted as an official HCA publication, according to the process described in https://www.humancellatlas.org/publications/ ? | boolean | yes |  | Official HCA Publication |  | yes; no

## Human-specific<a name='Human-specific'></a>
_Information specific to a donor that is a human (Homo sapiens)._

Location: module/biomaterial/human_specific.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
body_mass_index | The body mass index of the donor. | number | no |  | Body mass index |  | 36.4
ethnicity | Ethnicity of the donor. | array | no | [See module  ethnicity_ontology](module.md#ethnicity-ontology) | Ethnicity |  | 

## Growth conditions<a name='Growth conditions'></a>
_Information relating to how a biomaterial was grown and/or maintained in a laboratory setting._

Location: module/biomaterial/growth_conditions.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
passage_number | The number of passages that the biomaterial has been through. | integer | no |  | Passage number |  | 22
growth_medium | The solid, liquid, or semi-solid medium used to support growth. | string | no |  | Growth medium |  | human placental cord serum; RPMI 1640 + 2mM Glutamine + 10-20% FBS
culture_environment | Cell culture environment in which cells are grown. | string | no |  | Culture environment |  | Adherent cell culture; Suspension cell culture
mycoplasma_testing_method | The method by which the biomaterial was tested for mycoplasma contamination. | string | no |  | Mycoplasma testing method | Direct DNA stain, Indirect DNA stain, Broth and agar culture, PCR, Nested PCR, ELISA, Autoradiography, Immunostaining, Cell-based assay, Microbiological assay | Should be one of: Direct DNA stain, Indirect DNA stain, Broth and agar culture, PCR, Nested PCR, ELISA, Autoradiography, Immunostaining, Cell-based assay, or Microbiological assay.
mycoplasma_testing_results | Whether the biomaterial passed or failed the mycoplasma test. | string | no |  | Mycoplasma testing results | pass, fail | Should be one of: pass, or fail.
drug_treatment | Description of drugs added to the growth medium. | string | no |  | Drug treatment |  | 100 ug/mL ampicillin; 15 ug/mL tetracycline
feeder_layer_type | Type of feeder layer cells on which biomaterial was grown. | string | no |  | Feeder layer type | feeder-free, feeder-dependent, JK1 feeder cells, feeder-dependent, SNL 76/7 feeder cells, feeder-dependent, human marrow stromal cells, feeder-dependent, bovine embryonic fibroblast cells, feeder-dependent, mouse embryonic fibroblast cells, feeder-dependent, mouse fibroblast STO cells, feeder-dependent, mouse bone marrow stromal cells, feeder-dependent, mouse yolk sac-derived endothelial cells, feeder-dependent, human foreskin fibroblast cells, feeder-dependent, human newborn fibroblast cells, feeder-dependent, human fetal lung fibroblast cells, feeder-dependent, human uterine endometrial cells, feeder-dependent, human breast parenchymal cells, feeder-dependent, human embryonic fibroblast cells, feeder-dependent, human adipose stromal cells, feeder-dependent, human amniotic epithelial cells, feeder-dependent, human placental fibroblast cells, feeder-dependent, human umbilical cord stromal cells, feeder-dependent, human fetal muscle cells, feeder-dependent, human fetal skin cells, feeder-dependent, human fetal liver stromal cells, feeder-dependent, human fallopian tubal epithelial cells, feeder-dependent, human amniotic mesenchymal cells | feeder-free; feeder-dependent, mouse embryonic fibroblast cells

## Medical tests<a name='Medical tests'></a>
_Information about the medical tests performed on the individual._

Location: module/biomaterial/medical_tests.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
pft_method | Indicate which Pulmonary Function Testings (PFTs) methods were performed. Please indicate all tests performed. | array | no |  | Pulmonary Function Testing method | spirometry, plethysmography, DLCO_KCO_test | spirometry; plethysmography; DLCO_KCO_test
pft_age | Indicate the age of the subject at the time point of Pulmonary Function Testing (PFT) in years, if known. | number | no |  | Age at Pulmonary Function Test |  | 10; 34; 68
pft_time_point | Indicate at which date the Pulmonary Function Testing (PFT) were recorded as YYYY-MM-DD if available. If this information is not shareable, please indicate 'not_shareable'. | string | no |  | Date at Pulmonary Function Test |  | 2024-11-14; 2019-01-31; not_shareable
pft_relative_time_point | If timepoint of sample collection (time of collection) and/or timepoint of PFT recording (pft_time_point) is not available, indicate how many days prior or after sample collection the pulmonary function parameters were assessed if available. | integer | no |  | Days between collection and Pulmonary Function Test |  | -5; 2; 0
fev1_predicted | Indicate the predicted Forced Expiratory Volume in 1 second (FEV1) in milliliters, based on patient age, sex, height, and ethnicity, if available. | number | no |  | FEV1 predicted |  | 3500; 4200; 2800
fev1_prebd | Indicate the measured FEV1 in milliliters before the administration of a bronchodilator if available. | number | no |  | FEV1 before bronchodilator |  | 3000; 3800; 2600
fev1_postbd | Indicate the measured FEV1 in milliliters after the administration of a bronchodilator if available. | number | no |  | FEV1 after bronchodilator |  | 3200; 4000; 2700
fev1_prebd_predicted_percent | Indicate the percentage of the predicted FEV1 achieved before bronchodilator administration if available. | number | no |  | FEV1 before bronchodilator percent of predicted |  | 86; 90; 78
fev1_postbd_predicted_percent | Indicate the percentage of the predicted FEV1 achieved after bronchodilator administration if available. | number | no |  | FEV1 after bronchodilator percent of predicted |  | 91; 95; 82
fvc_predicted | Indicate the predicted Forced Vital Capacity (FVC) in milliliters, based on patient age, sex, height, and ethnicity, if available. | number | no |  | FVC predicted |  | 4500; 5000; 3800
fvc_prebd | Indicate the measured FVC in milliliters before bronchodilator administration if available. | number | no |  | FVC before bronchodilator |  | 4000; 4800; 3600
fvc_postbd | Indicate the measured FVC in milliliters after bronchodilator administration if available. | number | no |  | FVC after bronchodilator |  | 4200; 5000; 3700
fvc_prebd_predicted_percent | Indicate the percentage of the predicted FVC achieved before bronchodilator administration if available. | number | no |  | FVC before bronchodilator percent of predicted |  | 89; 96; 95
fvc_postbd_predicted_percent | Indicate the percentage of the predicted FVC achieved after bronchodilator administration if available. | number | no |  | FVC after bronchodilator percent of predicted |  | 93; 100; 97
fev1_fvc_ratio_prebd | Indicate the ratio of FEV1 to FVC before bronchodilator administration if available. | number | no |  | FEV1 to FVC ratio before bronchodilator |  | 0.75; 0.79; 0.72
fev1_fvc_ratio_postbd | Indicate the ratio of FEV1 to FVC after bronchodilator administration if available. | number | no |  | FEV1 to FVC ratio after bronchodilator |  | 0.76; 0.80; 0.73
frc_abs | Indicate the Functional Residual Capacity (FRC) in absolute milliliters if available. | number | no |  | FRC absolute |  | 3000; 3500; 2700
frc_predicted_percent | Indicate the percentage of the predicted FRC, based on patient demographics, if available. | number | no |  | FRC percent of predicted |  | 95; 88; 102
rv | Indicate the Residual Volume (RV) in milliliters if available. | number | no |  | RV |  | 1500; 1800; 1400
rv_predicted_percent | Indicate the percentage of the predicted RV, based on patient demographics, if available. | number | no |  | RV percent of predicted |  | 80; 90; 85
ic | Indicate the Inspiratory Capacity (IC) in milliliters if available. | number | no |  | IC |  | 3500; 4000; 3200
ic_predicted_percent | Indicate the percentage of the predicted IC, based on patient demographics, if available. | number | no |  | IC percent of predicted |  | 92; 85; 97
dlco | Indicate the Diffusing Capacity of the Lung for Carbon Monoxide (DLCO) in milliliters if available. | number | no |  | DLCO |  | 25; 30; 22
dlco_predicted_percent | Indicate the percentage of the predicted DLCO, based on patient demographics, if available. | number | no |  | DLCO percent of predicted |  | 88; 95; 82
kco | Indicate the transfer coefficient of the lung for carbon monoxide (KCO) in mmol/min/kPa/L if available. | number | no |  | KCO |  | 5; 6; 4.5
kco_predicted_percent | Indicate the percentage of the predicted KCO, based on patient demographics, if available. | number | no |  | KCO percent of predicted |  | 90; 98; 85

## Disease profile<a name='Disease profile'></a>
_Information about specific diseases profile of the individual._

Location: module/biomaterial/disease_profile.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
