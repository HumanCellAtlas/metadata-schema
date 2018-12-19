# Module
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## Cell morphology<a name='Cell morphology'></a>
_Information relating to pathological and morphological features of cells._

Location: module/biomaterial/cell_morphology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
cell_morphology | General description of the morphology of cells. | string | no |  | Cell morphology |  | adherent cells, form single layer colonies
cell_size | Size of cells in Cell size unit. Average value is acceptable. | string | no |  | Cell size |  | 20-30
cell_size_unit | The unit in which the Cell size is expressed. | object | no | [See module  length_unit_ontology](module.md/#length_unit_ontology) | Cell size unit |  | micrometer
percent_cell_viability | Percent of cells determined to be viable. Average value is acceptable. | number | no |  | Percent cell viability |  | 98.7
cell_viability_method | The method by which cell viability was determined. | string | no |  | Cell viability method |  | Fluorescein diacetate hydrolysis assay
cell_viability_result | Result of the cell viability test. | string | no |  | Cell viability pass/fail result | pass, fail | Must be one of: pass, fail
percent_necrosis | Percent of cells identified to be necrotic. | number | no |  | Percent necrotic cells |  | 10

## Death<a name='Death'></a>
_Information relating to the death of an organism._

Location: module/biomaterial/death.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
cause_of_death | Cause of death from death report for human donor, from research lab for mouse. | string | yes |  | Cause of death |  | 
cold_perfused | Yes if perfused with cold fluid to help preserve tissues before heart stopped. No otherwise. | boolean | no |  | Cold perfused? |  | Should be one of: yes, no.
days_on_ventilator | Number of days on ventilator before death occurred. | number | no |  | Number of days on ventilator |  | 4
hardy_scale | Value of 4-point Hardy scale cause of death classification: (0) ventilator case, (1) violent and fast death, (2) fast death of natural causes, (3) intermediate death, or (4) slow death. | integer | no |  | Value on Hardy scale |  | 0
time_of_death | Date and time of death of the organism, in format yyyy-mm-ddThh:mm:ssZ. | string | no |  | Time of death |  | 2016-01-21T00:00:00Z
organ_donation_death_type | Type of death preceding organ donation (for organ donors only). | string | no |  | Organ donation death type | Donation after circulatory death (DCD), Donation after brainstem death (DBD) | Should be one of: Donation after circulatory death (DCD), or Donation after brainstem death (DBD).
normothermic_regional_perfusion | Yes if entire body (but not limbs) was perfused with warm oxygenated blood. No otherwise. | string | no |  | Normothermic regional perfusion? | yes, no, unknown | Should be one of: yes, no, or unknown.

## Familial relationship<a name='Familial relationship'></a>
_Information about other organisms that this organism is related to._

Location: module/biomaterial/familial_relationship.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
parent | The individual's parent. | string | no |  | Parent |  | 
child | The individual's child. | string | no |  | Child |  | 
sibling | The individual's sibling. | string | no |  | Sibling |  | 

## Growth conditions<a name='Growth conditions'></a>
_Information relating to how a biomaterial was grown and/or maintained in a laboratory setting._

Location: module/biomaterial/growth_conditions.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
passage_number | The number of passages (as an integer) that the biomaterial has been through. | integer | no |  | Passage number |  | 22
growth_medium | The solid, liquid, or semi-solid medium used to support growth. | string | no |  | Growth medium |  | lysogeny broth (LB) medium
culture_environment | Cell culture environment in which cells are grown. | string | no |  | Culture environment |  | adherent culture
mycoplasma_testing_method | The method by which the biomaterial was tested for mycoplasma contamination. | string | no |  | Mycoplasma testing method | Direct DNA stain, Indirect DNA stain, Broth and agar culture, PCR, Nested PCR, ELISA, Autoradiography, Immunostaining, Cell-based assay, Microbiological assay | Should be one of: Direct DNA stain, Indirect DNA stain, Broth and agar culture, PCR, Nested PCR, ELISA, Autoradiography, Immunostaining, Cell-based assay, or Microbiological assay.
mycoplasma_testing_results | Whether the biomaterial passed or failed the mycoplasma test. | string | no |  | Mycoplasma testing results | pass, fail | Should be one of: pass, or fail.
drug_treatment | Description of drugs added to the growth medium. | string | no |  | Drug treatment |  | 100 ug/mL ampicillin
feeder_layer_type | Type of feeder layer cells biomaterial was grown on. | string | no |  | Feeder layer type | feeder-free, feeder-dependent, JK1 feeder cells, feeder-dependent, SNL 76/7 feeder cells, feeder-dependent, human marrow stromal cells, feeder-dependent, bovine embryonic fibroblast cells, feeder-dependent, mouse embryonic fibroblast cells, feeder-dependent, mouse fibroblast STO cells, feeder-dependent, mouse bone marrow stromal cells, feeder-dependent, mouse yolk sac-derived endothelial cells, feeder-dependent, human foreskin fibroblast cells, feeder-dependent, human newborn fibroblast cells, feeder-dependent, human fetal lung fibroblast cells, feeder-dependent, human uterine endometrial cells, feeder-dependent, human breast parenchymal cells, feeder-dependent, human embryonic fibroblast cells, feeder-dependent, human adipose stromal cells, feeder-dependent, human amniotic epithelial cells, feeder-dependent, human placental fibroblast cells, feeder-dependent, human umbilical cord stromal cells, feeder-dependent, human fetal muscle cells, feeder-dependent, human fetal skin cells, feeder-dependent, human fetal liver stromal cells, feeder-dependent, human fallopian tubal epithelial cells, feeder-dependent, human amniotic mesenchymal cells | feeder-dependent, mouse embryonic fibroblast cells

## Human-specific<a name='Human-specific'></a>
_Information specific to a donor that is a human (Homo sapiens)._

Location: module/biomaterial/human_specific.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
body_mass_index | The body mass index of the donor organism. | number | no |  | Body mass index |  | 36.4
ethnicity | Ethnicity of the donor organism using ontology terms from EMBL-EBI's Ancestry Ontology. | array | no | [See module  ethnicity_ontology](module.md/#ethnicity_ontology) | Ethnicity |  | European, White, British

## Medical history<a name='Medical history'></a>
_Information about the medical history of a donor._

Location: module/biomaterial/medical_history.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
alcohol_history | Estimated number of drink units consumed per day. | string | no |  | Alcohol history |  | 3-6 units/day
medication | List of medications the individual was taking at time of biomaterial collection. | string | no |  | Medications |  | Naproxen 500mg/day, 
nutritional_state | Nutritional state of individual at time of biomaterial collection. | string | no |  | Nutritional state | normal, fasting, feeding tube removed | Should be one of: normal, fasting, or feeding tube removed.
smoking_history | Estimated number of cigarettes smoked per day and for how many years. | string | no |  | Smoking history |  | Smoker, 20/day for 25 years, stopped 2000
test_results | Results from any medical tests performed on the individual. | string | no |  | Test results |  | 
treatment | Description of treatments the individual has undergone prior to biomaterial collection. | string | no |  | Treatments |  | 

## Mouse-specific<a name='Mouse-specific'></a>
_Information specific to an organism that is a mouse (Mus musculus)._

Location: module/biomaterial/mouse_specific.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
strain | The name of the mouse strain. | array | no | [See module  strain_ontology](module.md/#strain_ontology) | Mouse strain |  | C57BL/6

## Preservation and storage<a name='Preservation and storage'></a>
_Information relating to how a biomaterial was preserved and/or stored over a period of time._

Location: module/biomaterial/preservation_storage.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
storage_method | The method by which a biomaterial was stored after preservation or before another protocol was used. | string | no |  | Storage method | ambient temperature, cut slide, fresh, frozen, -70C freezer, frozen, -150C freezer, frozen, liquid nitrogen, frozen, vapor phase, paraffin block, RNAlater, frozen, TRIzol, frozen | frozen, liquid nitrogen
storage_time | Length of time the biomaterial was stored for in Storage time units. | number | no |  | Storage time |  | 5
storage_time_unit | The unit in which Storage time is expressed. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Storage time unit |  | day
preservation_method | The method by which a biomaterial was preserved through the use of chemicals, cold, or other means to prevent or retard biological or physical deterioration. Enter 'fresh' if not preserved. | string | no |  | Preservation method | cryopreservation in liquid nitrogen (dead tissue), cryopreservation in dry ice (dead tissue), cryopreservation of live cells in liquid nitrogen, cryopreservation, other, formalin fixed, unbuffered, formalin fixed, buffered, formalin fixed and paraffin embedded, fresh | cryopreservation in liquid nitrogen (dead tissue)

## State of specimen<a name='State of specimen'></a>
_State of specimen at time of collection._

Location: module/biomaterial/state_of_specimen.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
autolysis_score | State of tissue breakdown due to self-digestion. | string | no |  | Autolysis score | none, mild, moderate | Should be one of: none, mild, or moderate.
gross_description | Color, size, and other aspects of specimen as visible to naked eye. | string | no |  | Gross description |  | 
gross_image | List of filenames of photographs of specimen without magnification. Must be of format JPEG, TIFF, or PNG. | array | no |  | Gross image |  | my_gross_image_file.jpg
ischemic_temperature | Whether specimen experienced warm or cold ischemia. | string | no |  | Ischemic temperature | warm, cold | Should be one of: warm, or cold.
ischemic_time | Duration of time, in seconds, between when the specimen stopped receiving oxygen and when it was preserved or processed. | integer | no |  | Ischemic time |  | 7200
microscopic_description | How the specimen looks under the microscope and how it compares with normal cells. | string | no |  | Microscopic description |  | Mixture of different cell sizes apparent.
microscopic_image | List of filenames of photographs of specimen under microscope. Must be of format JPEG, TIFF, or PNG. | array | no |  | Microscopic image |  | my_microscopic_image_file.jpg
postmortem_interval | Duration of time, in seconds, between when death was declared and when the specimen was preserved or processed. | integer | no |  | Post-mortem interval |  | 2400

## Timecourse<a name='Timecourse'></a>
_Information relating to a timecourse._

Location: module/biomaterial/timecourse.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
timecourse_value | The numerical value in Timecourse unit associated with a time interval used in the experiment. | string | yes |  |  |  | 2
timecourse_unit | The unit in which the Timecourse value is expressed. | object | yes | [See module  time_unit_ontology](module.md/#time_unit_ontology) |  |  | day
timecourse_relevance | Relevance of the Timecourse value/unit to the experiment. | string | no |  |  |  | Collection after tumor cells injected into the mammary gland.

## Biological macromolecule ontology<a name='Biological macromolecule ontology'></a>
_A term that may be associated with a biological macromolecule-related ontology term_

Location: module/ontology/biological_macromolecule_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the biological macromolecule being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Cell cycle ontology<a name='Cell cycle ontology'></a>
_A term that may be associated with a cell cycle-related ontology term_

Location: module/ontology/cell_cycle_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a cell cycle of the cells in the specimen. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Cell type ontology<a name='Cell type ontology'></a>
_A term that may be associated with a cell type-related ontology term_

Location: module/ontology/cell_type_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a cell type supplied by a user. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Cellular component ontology<a name='Cellular component ontology'></a>
_A term that may be associated with an intra-cellular structure ontology term_

Location: module/ontology/cellular_component_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a subcellular structure. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Development stage ontology<a name='Development stage ontology'></a>
_A term that may be associated with a development stage-related ontology term_

Location: module/ontology/development_stage_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the development stage of the organism. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Disease ontology<a name='Disease ontology'></a>
_A term that may be associated with a disease-related ontology term_

Location: module/ontology/disease_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string | yes |  |  |  | 
ontology | An optional ontology reference in format where prefix_ indicates which ontology | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Enrichment ontology<a name='Enrichment ontology'></a>
_A term that may be associated with a process-related ontology term_

Location: module/ontology/enrichment_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of an enrichment approach being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Ethnicity ontology<a name='Ethnicity ontology'></a>
_A term that may be associated with a ethnicity-related ontology term_

Location: module/ontology/ethnicity_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The ethnicity of the human donor. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Instrument ontology<a name='Instrument ontology'></a>
_A term that may be associated with a instrument-related ontology term_

Location: module/ontology/instrument_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The full name of the instrument used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Length unit ontology<a name='Length unit ontology'></a>
_A term that may be associated with a cell type-related ontology term_

Location: module/ontology/length_unit_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a length unit being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Library amplification ontology<a name='Library amplification ontology'></a>
_A term that may be associated with a process-related ontology term_

Location: module/ontology/library_amplification_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a library amplification approach being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Library construction ontology<a name='Library construction ontology'></a>
_A term that may be associated with a process-related ontology term_

Location: module/ontology/library_construction_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a library construction approach being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Mass unit ontology<a name='Mass unit ontology'></a>
_A term that may be associated with a cell type-related ontology term_

Location: module/ontology/mass_unit_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a mass unit being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Microscopy ontology<a name='Microscopy ontology'></a>
_A term that may be associated with a microscopy-related ontology term_

Location: module/ontology/microscopy_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the type of microscopy used in an imaging experiment. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Organ ontology<a name='Organ ontology'></a>
_A term that may be associated with an anatomy-related ontology term._

Location: module/ontology/organ_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string | yes |  |  |  | 
ontology | A term from the ontology [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) for an organ or a cellular bodily fluid such as blood or lymph. | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Organ part ontology<a name='Organ part ontology'></a>
_A term that may be associated with an anatomy-related ontology term_

Location: module/ontology/organ_part_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The text for the term as the user provides it. | string | yes |  |  |  | 
ontology | A term for a specific part of an organ from the ontology [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon). | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Process type ontology<a name='Process type ontology'></a>
_A term that may be associated with a process-related ontology term_

Location: module/ontology/process_type_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a process type being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Protocol type ontology<a name='Protocol type ontology'></a>
_A term that may be associated with a protocol-related ontology term_

Location: module/ontology/protocol_type_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a protocol type used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Sequencing ontology<a name='Sequencing ontology'></a>
_A term that may be associated with a process-related ontology term_

Location: module/ontology/sequencing_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a sequencing approach being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Species ontology<a name='Species ontology'></a>
_A term that may be associated with a species-related ontology term_

Location: module/ontology/species_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the species to which the organism belongs. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Strain ontology<a name='Strain ontology'></a>
_A term that may be associated with a strain-related ontology term_

Location: module/ontology/strain_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of the strain to which the organism belongs (mouse-specific). | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Time unit ontology<a name='Time unit ontology'></a>
_A term that may be associated with a time unit-related ontology term_

Location: module/ontology/time_unit_ontology.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
text | The name of a time unit being used. | string | yes |  |  |  | 
ontology | An ontology term identifier in the form prefix:accession | string | no |  |  |  | 
ontology_label | The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field | string | no |  |  |  | 

## Purchased reagents<a name='Purchased reagents'></a>
_Information describing purchased kits or reagents used in a protocol._

Location: module/process/purchased_reagents.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
retail_name | The retail name of the kit/reagent. | string | no |  | Retail name |  | SureCell WTA 3' Library Prep Kit
catalog_number | The catalog number of the kit/reagent. | string | no |  | Catalog number |  | 20014279
manufacturer | The manufacturer of the kit/reagent. | string | no |  | Manufacturer |  | Illumina
lot_number | The batch or lot number of the kit/reagent. | string | no |  | Batch/lot number |  | 10001A
expiry_date | The date of expiration for the kit/reagent in the format YYYY-MM-DD. | string | no |  | Expiry date |  | 2018-01-31
kit_titer | Appropriate titer and volume recommendations found in kit/reagent Certificate of Analysis. | string | no |  | Kit titer |  | Titer: Specification is 3.0x10^7

## 10x-specific<a name='10x-specific'></a>
_This module describes information specific to 10x experiments._

Location: module/process/sequencing/10x.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
fastq_method | Method used for the generation of fastq files from bcl files. | string | no |  | Fastq creation method |  | Cellranger mkfastq
fastq_method_version | Version of the program used for fastq generation. | string | no |  | Fastq creation method version |  | Cellranger 2.1.1
pooled_channels | The number of channels pooled within a sequencing lane. | number | no |  | Pooled channels |  | 4
drop_uniformity | Whether drop uniformity was achieved as a result of visual inspection of emulsion after a 10x run. | boolean | no |  | Drop uniformity |  | Should be one of: yes, or no.

## Barcode<a name='Barcode'></a>
_Information about barcodes used in a protocol._

Location: module/process/sequencing/barcode.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
barcode_read | The read that the barcode is found in. | string | yes |  | Barcode-containing read | Read 1, Read 2, i7 Index, i5 Index | Should be one of: Read 1, Read 2, i7 Index, or i5 Index.
barcode_offset | 0-based offset of start of barcode in read. 0 for beginning of read. | integer | yes |  | Barcode offset |  | 0
barcode_length | Length of barcode in nucleotides. | integer | yes |  | Barcode length |  | 28
white_list_file | Name of file containing legitimate barcode sequences, if known. | string | no |  | White list barcode file |  | barcode_whitelist_file.txt

## INSDC experiment<a name='INSDC experiment'></a>
_Information relating to an INSDC experiment._

Location: module/process/sequencing/insdc_experiment.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
insdc_experiment | An INSDC (International Nucleotide Sequence Database Collaboration) experiment accession if experiment has been submitted. Can be from the DDBJ, EMBL-EBI, or NCBI.  Accession must start with DRX, ERX, or SRX. | string | yes |  | INSDC experiment |  | SRX0000000

## Plate-based sequencing<a name='Plate-based sequencing'></a>
_Information specific to plate-based sequencing experiments._

Location: module/process/sequencing/plate_based_sequencing.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
plate_id | An ID for the plate that the well is located on. | string | yes |  | Well plate ID |  | 2217
well_id | An ID or name for the well. Should be unique for the plate. | string | no |  | Well ID |  | A1
cell_quality | Note on how good cell looks if imaged in well before sequencing. | string | no |  | Cell quality | OK, control, 2-cell well, control, empty well, low quality cell | Should be one of: 'OK', 'control, 2-cell well', 'control, empty well', or 'low quality cell'.

## Contact<a name='Contact'></a>
_Information about an individual who submitted or contributed to a project._

Location: module/project/contact.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
contact_name | Name of individual who has contributed to the project. | string | yes |  | Contact name |  | John,D,Doe; Jane,,Smith
email | Email address for the individual. | string | no |  | Email address |  | dummy@email.com
phone | Phone number of the individual or their lab. | string | no |  | Phone number |  | (+1) 234-555-6789
institution | Name of primary institute where the individual works. | string | yes |  | Institute |  | EMBL-EBI; University of Washington
laboratory | Name of lab or department within the institute where the individual works. | string | no |  | Laboratory/Department |  | Division of Vaccine Discovery; Department of Biology
address | Street address where the individual works. | string | no |  | Street address |  | 0000 Main Street, Nowheretown, MA, 12091
country | Country where the individual works. | string | no |  | Country |  | USA
corresponding_contributor | Whether the individual is a primary point of contact for the project. | boolean | no |  | Corresponding contributor? |  | Should be one of: yes, or no.
project_role | Primary role of the individual in the project. | string | no |  | Project role | principal investigator, co investigator, experimental scientist, computational scientist, clinician, pathologist, technician, external curator, Human Cell Atlas wrangler, other | principal investigator; computational scientist
orcid_id | The individual's ORCID ID linked to previous work. | string | no |  | ORCID ID |  | 0000-1111-2222-3333

## Funder<a name='Funder'></a>
_Information about the project funding source._

Location: module/project/funder.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
grant_title | The name of the grant funding the project. | string | no |  | Grant title |  | A title of a grant proposal.
grant_id | The unique grant identifier or reference. | string | no |  | Grant ID |  | BB/P0000001/1
funder_name | The name of the funding organization. | string | no |  | Funding organization |  | Biotechnology and Biological Sciences Research Council (BBSRC)

## Publication<a name='Publication'></a>
_Information about a journal article, book, web page, or other external available documentation for a project._

Location: module/project/publication.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
authors | A list of authors associated with the publication in 'surname initials' format. | array | yes |  | Authors |  | Doe JD
publication_title | The title of the publication. | string | yes |  | Publication title |  | Study of single cells in the human body
doi | The publication digital object identifier (doi). | string | no |  | Publication DOI |  | 10.1016/j.cell.2016.07.054
pmid | The PubMed ID of the publication. | integer | no |  | Publication PMID |  | 27565351
publication_url | A URL, preferably not behind a paywall, for the publication. | string | no |  | Publication URL |  | 

## Channel<a name='Channel'></a>
_Information about a single microscope channel._

Location: module/protocol/channel.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
channel_id | User given ID.  If there is an accompanying codebook, this name should correspond to the channel id used in the codebook. | string | yes |  | Channel ID |  | 1, A
excitation_wavelength | Excitation wavelength of the lightsource in nanometers. | number | yes |  | Excitation wavelength |  | 640
filter_range | Wavelength range of the emission filter in nanometers. | string | yes |  | Filter range |  | 665 - 705
multiplexed | Were multiple targets detected simultaneously in this channel? Should be yes or no. | string | yes |  | Is this a multiplexed experiment? | yes, no | yes
target_fluorophore | The name of the fluorophore this channel is designed to assay. | string | no |  | Target fluorophore |  | Alexa 647
exposure_time | Acquisition time for a single image per channel in miliseconds | number | yes |  | Exposure time |  | 400

## Target<a name='Target'></a>
_Information about a single microscope channel._

Location: module/protocol/target.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
molecule_name | The name of a target molecule (small molecule or gene product) whose distribution is assayed by this experiment. If there is an accompanying codebook, this name should correspond to the target name used in the codebook. | string | no |  | Target molecule name |  | ACTA1, cFos
molecule_id | An identifier referring to the the target molecule. For small molecules this should be from the ChEBI ontology. For gene products this should be a standard gene or gene product identifier (e.g. ensembl, uniprot). | string | no |  | Target molecule identifier. |  | CHEBI:85345, ensembl_9606
subcellular_structure | Target subcellular structure. This should be a term from the GO cell component ontology. | object | no | [See module  cellular_component_ontology](module.md/#cellular_component_ontology) | Target subcellular structure |  | 
reagent_name | Name of reagent used to detect target. | string | no |  | Reagent name |  | 
purchased_reagent_details | Information describing purchased reagent used to detect target. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Purchased reagent details |  | 
probe_sequence | Sequence of a probe used to detect target. | string | no |  | Probe sequence |  | 
fluorophore | Fluorophore used to detect target. | string | no |  | Fluorophore |  | FITC
assay_type | Type of assay used to detect target. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Assay type |  | MERFISH, smFISH, immunofluorescence, fluorescent cell stain
multiplexed | Were multiple targets detected simultaneously in one channel? Should be yes or no. | string | yes |  | Is this a multiplexed experiment? | yes, no | yes
channel_id | Channel ID used to assay signal. Should be consistent with the ID in the channel tab. | array | no |  | Channel |  | 1, A

