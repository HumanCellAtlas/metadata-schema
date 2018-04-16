# HCA metadata ontology fields

The following fields in the HCA metadata schema can currently be annotated with ontology terms. The relevant ontology module is provided:


Metadata entity | Field | Ontology module
--- | --- | ---
protocol | protocol_type | protocol_type_ontology
sequencing_protocol | protocol_type | protocol_type_ontology
analysis_protocol | protocol_type | protocol_type_ontology
imaging_protocol | protocol_type | protocol_type_ontology
biomaterial_protocol | protocol_type | protocol_type_ontology
specimen_from_organism | genus_species | species_ontology
specimen_from_organism | organ | organ_ontology
specimen_from_organism | organ_part | organ_part_ontology
specimen_from_organism | disease | disease_ontology
cell_suspension | genus_species | species_ontology
cell_suspension | target_cell_type | cell_type_ontology
cell_line | genus_species | species_ontology
cell_line | disease | disease_ontology
cell_line | cell_cycle | cell_cycle_ontology
cell_line | cell_type | cell_type_ontology
donor_organism | genus_species | species_ontology
donor_organism | disease | disease_ontology
donor_organism | organism_age_unit | time_unit_ontology
donor_organism | development_stage | development_stage_ontology
donor_organism | gestational_age_unit | time_unit_ontology
donor_organism | height_unit | length_unit_ontology
donor_organism | weight_unit | mass_unit_ontology
organoid | genus_species | species_ontology
organoid | model_for_organ | organ_ontology
organoid | organoid_age_unit | time_unit_ontology
process | process_type | process_type_ontology
library_preparation_process | process_type | process_type_ontology
library_preparation_process | input_nucleic_acid_molecule | biological_macromolecule_ontology
sequencing_process | process_type | process_type_ontology
sequencing_process | instrument_manufacturer_model | instrument_ontology
analysis_process | process_type | process_type_ontology
collection_process | process_type | process_type_ontology
enrichment_process | process_type | process_type_ontology
dissociation_process | process_type | process_type_ontology
imaging_process | process_type | process_type_ontology
preservation_storage | storage_time_unit | time_unit_ontology
homo_sapiens_specific | ethnicity | ethnicity_ontology
cell_pathology | cell_size_unit | length_unit_ontology
mus_musculus_specific | strain | strain_ontology


## To do

The following fields in the HCA metadata schema might be converted to ontology fields in the future. In some cases, the conversion is already planned subject to a sufficient level of ontology coverage being reached. The ultimate goal is to eliminate all except a few essential defined lists (enums) from the metadata schema as it is easier to add new terms to or update terms in an ontology than to make changes to the metadata schema directly.


Metadata entity | Field | Comment
--- | --- | ---
library_preparation_process | library_construction_approach | Conversion planned, currently enum
enrichment_process | enrichment_method | Conversion planned, currently enum
cell_line | cell_line_type | Currently enum
donor_organism | biological_sex | Currently enum
organoid | organoid_type | Currently enum
library_preparation_process | end_bias | Currently enum
library_preparation_process | primer | Currently enum
library_preparation_process | strand | Currently enum
collection_process | collection_method | Currently enum
dissociation_process | dissociation_method | Currently enum
dissociation_process | nucleic_acid_source | Currently enum
contact | country |
growth_conditions | growth_medium |
growth_conditions | mycoplasma_testing_method |
preservation_storage | storage_method | Currently enum
preservation_storage | preservation_method | Currently enum
death | cause_of_death |
cell_pathology | cell_viability_method |


