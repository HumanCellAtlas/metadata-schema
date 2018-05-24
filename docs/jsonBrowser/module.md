# Module
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## cell_type_ontology<a name='cell_type_ontology'></a>
_A term that may be associated with a cell type-related ontology term_

Location: module/ontology/cell_type_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a cell type supplied by a user. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 

## ethnicity_ontology<a name='ethnicity_ontology'></a>
_A term that may be associated with a ethnicity-related ontology term_

Location: module/ontology/ethnicity_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The ethnicity of the human donor. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 

## species_ontology<a name='species_ontology'></a>
_A term that may be associated with a species-related ontology term_

Location: module/ontology/species_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the species to which the organism belongs. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 

## disease_ontology<a name='disease_ontology'></a>
_A term that may be associated with a disease-related ontology term_

Location: module/ontology/disease_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string | yes |  |  |  | 
ontology | An optional ontology reference in format where prefix_ indicates which ontology | string | no |  |  |  | 

## organ_part_ontology<a name='organ_part_ontology'></a>
_A term that may be associated with an anatomy-related ontology term_

Location: module/ontology/organ_part_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string | yes |  |  |  | 
ontology | A term for a specific part of an organ from the ontology [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon). | string | no |  |  |  | 

## length_unit_ontology<a name='length_unit_ontology'></a>
_A term that may be associated with a cell type-related ontology term_

Location: module/ontology/length_unit_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a length unit being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 

## time_unit_ontology<a name='time_unit_ontology'></a>
_A term that may be associated with a time unit-related ontology term_

Location: module/ontology/time_unit_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a time unit being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 

## development_stage_ontology<a name='development_stage_ontology'></a>
_A term that may be associated with a development stage-related ontology term_

Location: module/ontology/development_stage_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the development stage of the organism. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 

## organ_ontology<a name='organ_ontology'></a>
_A term that may be associated with an anatomy-related ontology term._

Location: module/ontology/organ_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string | yes |  |  |  | 
ontology | A term from the ontology [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) for an organ or a cellular bodily fluid such as blood or lymph. | string | no |  |  |  | 

## mass_unit_ontology<a name='mass_unit_ontology'></a>
_A term that may be associated with a cell type-related ontology term_

Location: module/ontology/mass_unit_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a mass unit being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 

## strain_ontology<a name='strain_ontology'></a>
_A term that may be associated with a strain-related ontology term_

Location: module/ontology/strain_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the strain to which the organism belongs (mouse-specific). | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 

## instrument_ontology<a name='instrument_ontology'></a>
_A term that may be associated with a instrument-related ontology term_

Location: module/ontology/instrument_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The full name of the instrument used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 

## cell_cycle_ontology<a name='cell_cycle_ontology'></a>
_A term that may be associated with a cell cycle-related ontology term_

Location: module/ontology/cell_cycle_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a cell cycle of the cells in the specimen. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 

## process_type_ontology<a name='process_type_ontology'></a>
_A term that may be associated with a process-related ontology term_

Location: module/ontology/process_type_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a process type being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 

## protocol_type_ontology<a name='protocol_type_ontology'></a>
_A term that may be associated with a protocol-related ontology term_

Location: module/ontology/protocol_type_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a protocol type used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 

## biological_macromolecule_ontology<a name='biological_macromolecule_ontology'></a>
_A term that may be associated with a biological macromolecule-related ontology term_

Location: module/ontology/biological_macromolecule_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the biological macromolecule being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 

## contact<a name='contact'></a>
_Information about a person who submitted or contributed to a project._

Location: module/project/contact.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
contact_name | The contact's name. Should be in the format 'first, middle, last name'. Middle can be initial or left blank. | string | yes |  | Contact name |  | John,D,Doe
email | An email address for the contact. | string | yes |  | Email |  | 
phone | Phone number (including country code) of contact or contact's lab. | string | no |  | Phone number |  | 
institution | Name of primary institute where contact works. | string | no |  | Institution |  | 
laboratory | Name of lab (often the PI name) within institute where contact works. | string | no |  | Laboratory |  | 
address | Street address where contact works. Should include street name and number, city, country division, postal code. | string | no |  | Address |  | 
country | Country where contact works. | string | no |  | Country |  | 

## publication<a name='publication'></a>
_Information about a journal article, book, web page, or other external available documentation on a project._

Location: module/project/publication.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
authors | A list of authors associated with the publication in 'surname initials' format. | array | yes |  | Authors |  | Smith JD
publication_title | The full title of the publication. | string | yes |  | Publication title |  | 
doi | The publication digital object identifier. | string | no |  | DOI |  | 10.1016/j.cell.2016.07.054
pmid | The PubMed ID of the publication. | integer | no |  | PMID |  | 27565351
publication_url | A URL, preferably not behind a paywall, for the publication. | string | no |  | Publication URL |  | 

## medical_history<a name='medical_history'></a>
_Information about the medical history of an organism._

Location: module/biomaterial/medical_history.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
alcohol_history | Number of drinks consumed on a typical day. | string | no |  | Alcohol history |  | 
medication | List of medications the organism was currently taking at time of biomaterial donation. | string | no |  | Medications |  | 
nutritional_state | Should be one of normal, fasting, or feeding tube removed. | string | no |  | Nutritional state | normal, fasting, feeding tube removed | 
smoking_history | Estimated number of cigarettes smoked per day and for how many years. | string | no |  | Smoking history |  | 
test_results | Results from any medical tests performed on the individual. | string | no |  | Test results |  | 
treatment | Any treatments the individual has undergone. | string | no |  | Treatments |  | 

## familial_relationship<a name='familial_relationship'></a>
_Information about other organisms that this organism is related to._

Location: module/biomaterial/familial_relationship.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
is_child_of | This organism is a child of the indicated organism. | string | no |  | Child of |  | 
is_parent_of | This organism is a parent of the indicated organism. | string | no |  | Parent of |  | 
is_sibling_of | This organism is a sibling of the indicated organism. | string | no |  | Sibling of |  | 

## cell_pathology<a name='cell_pathology'></a>
_Information relating to pathological features of cells._

Location: module/biomaterial/cell_morphology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
cell_morphology | General description of the morphology of the cells in the cell suspension. | string | no |  | Cell morphology |  | 
cell_size | The size of the cells. Average cell size is acceptable. | number | no |  | Cell size number |  | 
cell_size_unit | The unit in which the cell size is expressed. Should be a child term of https://www.ebi.ac.uk/ols/ontologies/uo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUO_0000001. | object | no | [See module  length_unit_ontology](module.md/#length_unit_ontology) | Cell size unit |  | 
cell_viability | Percent of cells determined to be viable. | number | no |  | Percent cell viability |  | 
cell_viability_method | The method by which cell viability was determined. | string | no |  | Cell viability method |  | 
percent_necrosis | Percent of cells identified to be necrotic. | number | no |  | Percent necrosis |  | 

## growth_conditions<a name='growth_conditions'></a>
_Information relating to how a biomaterial was grown and/or maintained in a laboratory setting._

Location: module/biomaterial/growth_conditions.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
passage_number | The number of passages the cell line has been through. | integer | no |  | Passage number |  | 
growth_medium | The solid, liquid, or semi-solid medium used to support the growth of the biomaterial. | string | no |  | Growth medium |  | lysogeny broth (LB) medium
mycoplasma_testing_method | The method used for detecting mycoplasma contamination of a biomaterial culture. | string | no |  | Mycoplasma testing method |  | Indirect DNA stain using Hoechst 33258 with 3T3 indicator cells
mycoplasma_testing_results | Results of mycoplasma testing of a biomaterial culture. | string | no |  | Mycoplasma testing results |  | No spots of bright blue stain observed at high magnification
drug_treatment | Description of drugs added to the growth medium for this biomaterial. | string | no |  | Drug treatment |  | 100 ug/mL ampicillin

## mus_musculus_specific<a name='mus_musculus_specific'></a>
_Information specific to an organism that is a mouse (mus musculus)._

Location: module/biomaterial/mus_musculus_specific.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
strain | The name of the strain. | array | no | [See module  strain_ontology](module.md/#strain_ontology) | Strain |  | C57BL/6.

## preservation_storage<a name='preservation_storage'></a>
_Information relating to how a biomaterial was preserved and/or stored over a period of time._

Location: module/biomaterial/preservation_storage.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
storage_method | The method by which a biomaterial was stored. | string | no |  | Storage method | ambient temperature, cut slide, fresh, frozen, -70C freezer, frozen, -150C freezer, frozen, liquid nitrogen, frozen, vapor phase, paraffin block, RNAlater, frozen, TRIzol, frozen | 
storage_time | Length of time the biomaterial was stored for in Storage time units. | number | no |  | Storage time |  | 5
storage_time_unit | The unit in which Storage time is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Storage time unit |  | days
preservation_method | The method by which a biomaterial was preserved or not. | string | no |  | Storage method | cryopreservation in liquid nitrogen (dead tissue), cryopreservation in dry ice (dead tissue), cryopreservation of live cells in liquid nitrogen, cryopreservation, other, formalin fixed, unbuffered, formalin fixed, buffered, formalin fixed and paraffin embedded, Fresh | 

## homo_sapiens_specific<a name='homo_sapiens_specific'></a>
_Information specific to an organism that is a homo sapiens._

Location: module/biomaterial/homo_sapiens_specific.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
body_mass_index | The body mass index of the organism. | number | no |  | Body mass index |  | 
ethnicity | An array of ontology terms from EMBL-EBI's Ancestry Ontology describing ancestral groups, uncategorised ancestral groups, and population isolates. | array | no | [See module  ethnicity_ontology](module.md/#ethnicity_ontology) | Ethnicity |  | 

## state_of_specimen<a name='state_of_specimen'></a>
_State of body part at collection and how it was preserved after removal and/or cell enrichment_

Location: module/biomaterial/state_of_specimen.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
autolysis_score | State of tissue breakdown due to self-digestion. Must be one of: none, mild, moderate. | string | no |  | Autolysis score | none, mild, moderate | 
gross_description | Color, size, and other aspects of specimen as visible to naked eye. | string | no |  | Gross description |  | 
gross_image | List of filenames of photographs of body part without magnification. Must be of format JPEG, TIFF, or PNG. | array | no |  | Gross image |  | 
ischemic_temperature | Whether warm or cold ischemia. | string | no |  | Ischemic temperature | warm, cold | 
ischemic_time | Duration of time, in seconds, that the body part had insufficient blood supply. | integer | no |  | Ischemic time |  | 
microscopic_description | How the biomaterial looks under the microscope and how it compares with normal cells. | string | no |  | Microscopic description |  | 
microscopic_image | List of filenames of photographs of body part under microscope. Must be of format JPEG, TIFF, or PNG. | array | no |  | Microscopic image |  | 
postmortem_interval | Duration of time, in seconds, between when death is declared and when the tissue is preserved or processed. | integer | no |  | Post-mortem interval |  | 

## death<a name='death'></a>
_Information relating to the death of an organism._

Location: module/biomaterial/death.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
cause_of_death | Cause of death from death report for human donor, from research lab for mouse. | string | yes |  | Cause of death |  | 
cold_perfused | Yes if perfused with cold fluid to help preserve tissues before heart stopped. No otherwise. | boolean | no |  | Cold perfused? |  | 
days_on_ventilator | Days on ventilator before dying. | number | no |  | Number of days on ventilator |  | 
hardy_scale | Should be integer representing: (0) ventilator case, (1) violent and fast death, (2) fast death of natural causes, (3) intermediate death, or (4) slow death. | integer | no |  | Value on Hardy scale |  | 
time_of_death | Date and time of death of the organism, in format yyyy-mm-ddThh:mm:ssZ. | string | no |  | Time of death |  | 

## purchased_reagents<a name='purchased_reagents'></a>
_This module describes purchased kits or reagents used in any process._

Location: module/process/purchased_reagents.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
retail_name | The retail name of the kit/reagent. | string | no |  | Retail name |  | SureCell WTA 3' Library Prep Kit
catalog_number | The catalog number of the kit/reagent. | string | no |  | Catalog number |  | 20014279
manufacturer | The manufacturer of the kit/reagent. | string | no |  | Manufacturer |  | Illumina
batch_number | The batch or lot number of the kit/reagent. | string | no |  | Batch/lot number |  | 10001A
expiry_date | The date of expiration for the kit/reagent. | string | no |  | Expiry date |  | 2018-01-31

## barcode<a name='barcode'></a>
_This module describes barcodes used in a library preparation process._

Location: module/process/sequencing/barcode.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
barcode_read | The read that the barcode is found in. Should be one of Read 1, Read 2, i7 Index, or i5 Index. | string | yes |  | Barcode-containing read | Read 1, Read 2, i7 Index, i5 Index | 
barcode_offset | 0-based offset of start of barcode in read. 0 for beginning of read. | integer | yes |  | Barcode offset |  | 
barcode_length | Length of barcode in nucleotides. | integer | yes |  | Barcode length |  | 
white_list_file | Name of file containing legitimate barcode sequences. | string | no |  | White list barcode file |  | 

## smartseq2<a name='smartseq2'></a>
_This module describes information specific to SmartSeq2 experiments._

Location: module/process/sequencing/smartseq2.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
plate_id | An ID for the plate that the well is located on. | string | no |  | Well plate ID |  | 
well_name | A name for the well. Should be unique for the plate | string | no |  | Well name |  | 
well_row | Well row in plate. | string | no |  | Well row |  | 
well_column | Well column in plate. | string | no |  | Well column |  | 
cell_quality | Note on how good cell looks if imaged in well before sequencing. | string | no |  | Cell quality | OK, control, 2-cell well, control, empty well, low quality cell | 

