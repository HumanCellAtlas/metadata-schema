# Changelog

All notable changes to the HCA metadata schema will be documented in this file. Starting with v5.0.0, the schema will be versioned independently. Therefore, this changelog will contain notes for independent updates/releases per schema.

Starting after v5.0.0 release, updates will be declared for schemas independently in the form `[<schema_name>.json vX.Y.Z] - Release-date`. Changes will be organized across six categories: Added, Changed, Removed, Fixed, Deprecated, and Security. The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and (starting with v4.0.0) this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html). Unreleased changes may be indicated under the `Unreleased` heading.

## [Unreleased](https://github.com/HumanCellAtlas/metadata-schema/tree/staging)
## [Released](https://github.com/HumanCellAtlas/metadata-schema/)

### [module/biomaterial/medical_history.json - v9.1.0] - 2026-02-03
### Added
Added household_smoking_exposure, vaping_status and marijuana_inhaled_status

### [type/biomaterial/donor_organism.json - v18.3.0] - 2026-02-03
### Added
Added household_smoking_exposure, vaping_status and marijuana_inhaled_status

### [module/biomaterial/medical_history.json - v9.0.0] - 2025-12-15
### Deprecated
Deprecated alcohol_history

### [type/biomaterial/specimen_from_organism.json - v11.1.0] - 2025-12-15
### Added
Added adjacent_disease_location, indication_for_sampling and radial_tissue_term

### [module/biomaterial/disease_profile.json - v1.1.0] - 2025-12-15
### Added
Added PUCAI_score, PCDAI_score and wPCDAI_score

### [module/biomaterial/medical_history.json - v8.3.0] - 2025-12-15
### Added
Added alcohol_type, alcohol_usage_duration, alcohol_units, defined_diet, diet_specific and previous_surgeries

### [type/protocol/biomaterial_collection/collection_protocol.json - v9.3.0] - 2025-12-15
### Added
Added procedure

### [type/biomaterial/donor_organism.json - v18.2.0] - 2025-12-15
### Added
Added PUCAI_score, PCDAI_score and wPCDAI_score

### [system/file_descriptor.json - v2.2.0] - 2025-11-04
### Added
Added support for compact identifier-based DRS URIs in file descriptors

### [module/biomaterial/human_specific.json - v1.1.0] - 2025-11-12
### Added
Added optional ethnicity_question

### [module/biomaterial/human_specific.json - v1.2.0] - 2025-11-12
### Added
Added optional ethnicity_parents

### [module/biomaterial/human_specific.json - v1.3.0] - 2025-11-12
### Added
Added optional primary_language

### [module/biomaterial/human_specific.json - v1.4.0] - 2025-11-12
### Added
Added optional mother_father_language

### [module/biomaterial/residence.json - v1.0.0] - 2025-11-12
### Added
Added new module for residence information

### [module/biomaterial/human_specific.json - v1.5.0] - 2025-11-12
### Added
Added optional current_residence

### [module/biomaterial/human_specific.json - v1.6.0] - 2025-11-12
### Added
Added optional place_of_birth

### [module/biomaterial/medical_history.json - v8.1.0] - 2025-11-12
### Added
Added optional diet_meat_consumption

### [module/biomaterial/reproductive_history.json - v1.0.0] - 2025-11-12
### Added
Added new reproductive_history module

### [module/biomaterial/medical_history.json - v8.2.0] - 2025-11-12
### Added
Added optional reproductive_history

### [type/biomaterial/donor_organism.json - v18.1.0] - 2025-11-12
### Added
Added optional ethnicity_question

### [type/biomaterial/specimen_from_organism.json - v11.0.0] - 2025-04-29
### Fixed
Fixed typo in specimen_from_organism collection_institute field

### [type/biomaterial/cell_suspension.json - v14.1.0] - 2025-04-08
### Added
Added processing institute in cell_suspension.Issue1608

### [module/biomaterial/collection_institute.json - v1.0.0] - 2025-03-24
### Added
Added collection_institute module.Issue1606

### [type/biomaterial/specimen_from_organism.json - v10.10.0] - 2025-03-24
### Added
Added optional collection_institute module in specimen_from_organism.Issue1606

### [module/ontology/medication_ontology.json - v2.0.0] - 2025-02-28
### Changed
Changed ontology source for the medication_ontology

### [module/biomaterial/medical_history.json - v8.0.0] - 2025-02-28
### Changed
Changed ontology source for the medication_ontology

### [type/biomaterial/donor_organism.json - v18.0.0] - 2025-02-28
### Changed
Changed ontology source for the medication_ontology

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v6.3.0] - 2025-01-21
### Changed
Changed user_friendly name of reagent field

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v6.4.0] - 2025-01-21
### Added
Added optional digestion_time field

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v6.5.0] - 2025-01-21
### Added
Added optional digestion_time_unit field

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v6.6.0] - 2025-01-21
### Added
Added optional digestion_temperature field

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v6.7.0] - 2025-01-21
### Added
Added optional digestion_solution field

### [module/project/hca_bionetwork.json - v2.0.0] - 2025-01-20
### Changed
Changed enum value in hca_bionetwork.name. Fix #1600

### [type/project/project.json - v20.0.0] - 2025-01-20
### Changed
Changed enum value in hca_bionetwork.name. Fix #1600

### [type/biomaterial/donor_organism.json - v17.1.0] - 2024-12-11
### Added
Added non-required gender identity field.

### [module/ontology/gender_identity_ontology.json - v1.0.0] - 2024-12-11
### Added
Added ontology module for gender identity.

### [module/biomaterial/medical_history.json - v7.0.0] - 2024-11-06
### Changed
Changed medication field type Fix#1589

### [module/ontology/medication_ontology.json - v1.0.0] - 2024-11-06
### Added
Added medication ontology module Fix#1589

### [type/biomaterial/donor_organism.json - v17.0.0] - 2024-11-06
### Changed
Changed medication field type Fix#1589

### [type/biomaterial/donor_organism.json - v16.4.0] - 2024-10-21
### Added
Added comorbidities field in the donor_organism Fix#1569

### [module/project/hca_bionetwork.json - v1.0.2] - 2024-10-14
### Added
Added atlas names in hca_bionetwork

### [type/project/project.json - v19.0.1] - 2024-10-14
### Added
Added atlas names in hca_bionetwork

### [module/biomaterial/disease_profile.json - v1.0.0] - 2024-09-30
### Added
Added new disease profile module with COPD fields. Fixes#1572

### [type/biomaterial/donor_organism.json - v16.3.0] - 2024-09-30
### Added
Added an optional disease profile field in the donor_organism. Fixes#1572

### [system/file_descriptor.json - v2.1.0] - 2024-09-24
### Added
Added 'drs_uri' property to file_descriptor

### [module/biomaterial/medical_history.json - v5.3.0] - 2024-09-16
### Added
Added optional smoking related fields in medical_history module. Fix #1565

### [module/biomaterial/medical_history.json - v6.0.0] - 2024-09-16
### Removed
Removed smoking_history in medical_history module. Fix #1565

### [type/biomaterial/donor_organism.json - v16.2.0] - 2024-09-16
### Added
Added optional smoking related fields in medical_history module. Fix #1565

### [module/ontology/file_content_ontology.json - v2.0.0] - 2024-08-28
### Fixed
Fixed class from data:0006 to EDAM:0006. Fixes #1571

### [type/file/analysis_file.json - v8.0.0] - 2024-08-28
### Fixed
Fixed class from data:0006 to EDAM:0006. Fixes #1571

### [type/file/supplementary_file.json - v3.0.0] - 2024-08-28
### Fixed
Fixed class from data:0006 to EDAM:0006. Fixes #1571

### [core/file/file_core.json - v7.0.0] - 2024-08-28
### Fixed
Fixed class from data:0006 to EDAM:0006. Fixes #1571

### [type/file/image_file.json - v3.0.0] - 2024-08-28
### Fixed
Fixed class from data:0006 to EDAM:0006. Fixes #1571

### [type/file/reference_file.json - v4.0.0] - 2024-08-28
### Fixed
Fixed class from data:0006 to EDAM:0006. Fixes #1571

### [type/file/sequence_file.json - v10.0.0] - 2024-08-28
### Fixed
Fixed class from data:0006 to EDAM:0006. Fixes #1571

### [module/biomaterial/medical_tests.json - v1.0.0] - 2024-08-13
### Added
Added medical_tests module

### [type/biomaterial/donor_organism.json - v16.1.0] - 2024-08-13
### Added
Added optional medical_tests module in donor_organism. Fixes #1562

### [type/file/sequence_file.json - v9.6.0] - 2024-07-15
### Added
Added sequencing_run_batch field in the sequencing_file - Fixes#1557

### [type/protocol/analysis/analysis_protocol.json - v10.3.0] - 2024-04-15
### Added
Added intron_inclusion field in analysis_protocol Fixes#1554

### [type/biomaterial/specimen_from_organism.json - v10.9.0] - 2024-03-22
### Added
Added transplant_organ field in specimen_from_organism Fixes#1547"

### [type/project/project.json - v19.0.0] - 2024-03-15
### Added
Added DUOS id field. Fixes #1550

### [type/project/project.json - v18.0.0] - 2024-03-04
### Added
Added data_use_restriction field

### [type/protocol/analysis/analysis_protocol.json - v10.2.0] - 2024-02-05
### Added
Added gene_annotation_version field in analysis_protocol Fixes#1543

### [type/protocol/analysis/analysis_protocol.json - v10.1.0] - 2023-11-07
### Added
Added alignment_software & alignment_software_version field in analysis_protocol Fixes#1533

### [core/biomaterial/biomaterial_core.json - v8.4.0] - 2023-08-22
### Added
Added timecourse module. Fixes #1511

### [type/biomaterial/donor_organism.json - v16.0.0] - 2023-08-22
### Removed
Removed timecourse module.

### [type/biomaterial/cell_suspension.json - v14.0.0] - 2023-08-22
### Removed
Removed timecourse module.

### [type/biomaterial/cell_line.json - v16.0.0] - 2023-08-22
### Removed
Removed timecourse module.

### [type/biomaterial/imaged_specimen.json - v3.5.0] - 2023-08-22
### Added
Added timecourse module. Fixes #1511

### [type/biomaterial/specimen_from_organism.json - v10.8.0] - 2023-08-22
### Added
Added timecourse module. Fixes #1511

### [type/biomaterial/organoid.json - v11.5.0] - 2023-08-22
### Added
Added timecourse module. Fixes #1511

### [module/project/hca_bionetwork.json - v1.0.1] - 2023-05-22
### Added
Added new values to hca_atlas field

### [type/project/project.json - v17.1.1] - 2023-05-22
### Added
Added new values to hca_atlas field

### [module/project/hca_bionetwork.json - v1.0.0] - 2023-04-20
### Added
Added the hca_bionetwork module with four fields for recording bionetwork and atlas information

### [type/project/project.json - v17.1.0] - 2023-04-20
### Added
Added the hca_bionetwork module to be loaded in project

### [type/biomaterial/specimen_from_organism.json - v10.6.0] - 2023-03-13
### Added
Added new optional field adjacent_diseases. Fixes #1512

### [type/file/analysis_file.json - v7.0.0] - 2023-01-30
### Added
Added genome assembly and patch version. Fixes #1508.

### [module/protocol/matrix.json - v2.0.0] - 2022-10-31
### Fixed
Fixed typo in apostrophe. Fixes #1410

### [type/protocol/analysis/analysis_protocol.json - v10.0.0] - 2022-10-31
### Fixed
Fixed typo in apostrophe. Fixes #1410

### [type/biomaterial/donor_organism.json - v15.6.1] - 2022-10-31
### Fixed
Fixed typo in gestational age description

### [core/file/file_core.json - v6.4.0] - 2022-09-16
### Added
Added value to enum for file source. Fixes #1487.

### [type/file/supplementary_file.json - v2.5.0] - 2022-09-16
### Added
Added value to enum for file source. Fixes #1487.

### [type/file/image_file.json - v2.5.0] - 2022-09-16
### Added
Added value to enum for file source. Fixes #1487.

### [type/file/sequence_file.json - v9.5.0] - 2022-09-16
### Added
Added value to enum for file source. Fixes #1487.

### [type/file/analysis_file.json - v6.5.0] - 2022-09-16
### Added
Added value to enum for file source. Fixes #1487.

### [type/file/reference_file.json - v3.5.0] - 2022-09-16
### Added
Added value to enum for file source. Fixes #1487.

### [system/links.json - v3.1.0] - 2022-09-16
### Added
Added treatment protocol to protocol_type. Fixes #1488.

### [module/ontology/contributor_role_ontology.json - v2.0.0] - 2022-08-23
### Changed
Changed class to BFO:0000023 to match ontology changes.

### [module/project/contact.json - v9.0.0] - 2022-08-23
### Changed
Changed class to BFO:0000023 to match ontology changes.

### [type/project/project.json - v17.0.0] - 2022-08-23
### Changed
Changed class to BFO:0000023 to match ontology changes.

### [type/protocol/imaging/imaging_preparation_protocol.json - v2.3.0] - 2022-08-19
### Added
Added permeabilisation time field with time units. Fixes #1471

### [module/ontology/contributor_role_ontology.json - v2.0.0] - 2022-08-23
### Changed
Changed class to BFO:0000023 to match ontology changes.

### [module/project/contact.json - v9.0.0] - 2022-08-23
### Changed
Changed class to BFO:0000023 to match ontology changes.

### [type/project/project.json - v17.0.0] - 2022-08-23
### Changed
Changed class to BFO:0000023 to match ontology changes.

### [type/protocol/biomaterial_collection/treatment_protocol.json - v1.0.0] - 2022-08-01
### Added
Added Treatment protocol entity. Fixes #1428

### [module/ontology/treatment_method_ontology.json - v1.0.0] - 2022-08-01
### Added
Added Treatment protocol method ontology to be used to annotate the Treatment protocol method. Fixes #1428

### [module/ontology/target_pathway_ontology.json - v1.0.0] - 2022-08-01
### Added
Added Treatment protocol target pathway ontology which will be used to describe the target pathway that is targeted by a treatment method. Fixes #1428

### [module/ontology/disease_ontology.json - v5.4.0] - 2022-05-24
### Added
Added the phenotype branch to graphRestrictions. Fixes #1460

### [type/biomaterial/cell_line.json - v15.1.0] - 2022-05-24
### Added
Added the phenotype branch to graphRestrictions. Fixes #1460

### [type/biomaterial/donor_organism.json - v15.6.0] - 2022-05-24
### Added
Added the phenotype branch to graphRestrictions. Fixes #1460

### [type/biomaterial/specimen_from_organism.json - v10.5.0] - 2022-05-24
### Added
Added the phenotype branch to graphRestrictions. Fixes #1460

### [module/ontology/file_content_ontology.json - v1.1.0] - 2022-03-24
### Added
Added information entity branch to graphRestrictions. Fixes #1450

### [type/protocol/imaging/imaging_protocol.json - v11.4.0] - 2022-03-08
### Changed
Changed overlapping_tiles, numerical_aperture and pixel_size non-required. Fixes #1441

### [type/protocol/imaging/imaging_protocol.json - v11.3.0] - 2021-12-20
### Removed
Removed channel and probe from required fields. #Fixes 1420

### [type/project/project.json - v16.0.0] - 2021-12-20
### Added
Added anchors to ega_accessions and dbgap_accessions. Fixes #1425

### [type/file/sequence_file.json - v9.3.1] - 2021-10-29
### Added
Added read3, read4 to read index enum. Fixes #1401

### [module/process/sequencing/barcode.json - v5.2.7] - 2021-10-29
### Added
Added Read 3, Read 4 to barcode read enum. Fixes #1401

### [type/protocol/sequencing/library_preparation_protocol.json - v6.3.1] - 2021-10-29
### Added
Added Read 3, Read 4 to barcode read enum. Fixes #1401

### [type/protocol/sequencing/library_preparation_protocol.json - v6.3.0] - 2021-10-12
### Added
Added spatial barcode field loading barcodes module

### [module/project/publication.json - v7.0.0] - 2021-08-13
### Added
Added required official_hca_publication field. Fixes #1345

### [type/biomaterial/cell_line.json - v15.0.0] - 2021-08-13
### Added
Added required official_hca_publication field. Fixes #1345

### [type/project/project.json - v15.0.0] - 2021-08-13
### Added
Added required official_hca_publication field. Fixes #1345

### [type/project/project.json - v14.3.0] - 2021-07-26
### Added
Added project-level cell count. Fixes #1337.

### [module/protocol/matrix.json - v1.0.0] - 2021-03-24
### Added
Added matrix module

### [type/protocol/analysis/analysis_protocol.json - v9.2.0] - 2021-03-24
### Changed
Changed 'computational_method' field to optional, added matrix module field

### [type/file/analysis_file.json - v6.3.0] - 2021-03-24
### Added
Added optional 'matrix_cell_count' field.

### [core/file/file_core.json - v6.2.0] - 2021-03-24
### Added
Added optional file_source field.

### [type/file/sequence_file.json - v9.3.0] - 2021-03-24
### Added
Added optional file_source field.

### [type/file/supplementary_file.json - v2.3.0] - 2021-03-24
### Added
Added optional file_source field.

### [type/file/reference_file.json - v3.3.0] - 2021-03-24
### Added
Added optional file_source field.

### [type/file/image_file.json - v2.3.0] - 2021-03-24
### Added
Added optional file_source field.

### [type/project/project.json - v14.2.0] - 2021-03-16
### Added
Added ega_accessions and dbgap_accessions. Fixes #1336.

### [system/links.json - v3.0.0] - 2021-03-04
### Changed
Changed protocol_type from string to enum of strings. Fixes #1333

### [system/file_descriptor.json - v2.0.0] - 2020-06-29
### Removed
Removed schema major minor versions.

### [system/file_descriptor.json - v1.0.0] - 2020-06-25
### Added
Added file_descriptor schema

### [system/links.json - v2.1.1] - 2020-06-19
### Fixed
Fixed incomplete refs urls Fixes#1303

### [type/process/analysis/analysis_process.json - v12.0.0] - 2020-06-05
### Changed
Changed reference_bundle properties to reference_files and removed input_bundles. Fixes #1275

### [system/links.json - v2.1.0] - 2020-06-08
### Added
Added supplementary_links. Fixes #1285.

### [system/links.json - v2.0.0] - 2020-05-20
### Changed
Changed properties for links to capture entire processes. Fixes #1278

### [core/biomaterial/biomaterial_core.json - v8.2.0] - 2019-08-29
### Changed
Changed pattern match in fields 'insdc_sample_accession' and 'schema_version'. Fixes #1090

### [type/biomaterial/specimen_from_organism.json - v10.4.0] - 2019-08-29
### Changed
Changed pattern match in fields 'insdc_sample_accession' and 'schema_version'. Fixes #1090

### [type/biomaterial/cell_suspension.json - v13.3.0] - 2019-08-29
### Changed
Changed pattern match in fields 'insdc_sample_accession' and 'schema_version'. Fixes #1090

### [type/biomaterial/imaged_specimen.json - v3.3.0] - 2019-08-29
### Changed
Changed pattern match in fields 'insdc_sample_accession' and 'schema_version'. Fixes #1090

### [type/biomaterial/cell_line.json - v14.5.0] - 2019-08-29
### Changed
Changed pattern match in fields 'insdc_sample_accession' and 'schema_version'. Fixes #1090

### [type/biomaterial/donor_organism.json - v15.5.0] - 2019-08-29
### Changed
Changed pattern match in fields 'insdc_sample_accession' and 'schema_version'. Fixes #1090

### [type/biomaterial/organoid.json - v11.3.0] - 2019-08-29
### Changed
Changed pattern match in fields 'insdc_sample_accession' and 'schema_version'. Fixes #1090

### [system/provenance.json - v1.1.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/protocol/protocol.json - v7.1.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v2.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/biomaterial/cell_suspension.json - v13.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v6.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/file/reference_file.json - v3.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/biomaterial/organoid.json - v11.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/process/process.json - v9.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/file/analysis_file.json - v6.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v3.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/protocol/analysis/analysis_protocol.json - v9.1.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/file/sequence_file.json - v9.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/protocol/biomaterial_collection/aggregate_generation_protocol.json - v2.1.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v3.1.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/protocol/biomaterial_collection/collection_protocol.json - v9.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/protocol/sequencing/sequencing_protocol.json - v10.1.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/file/supplementary_file.json - v2.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/biomaterial/imaged_specimen.json - v3.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/biomaterial/donor_organism.json - v15.4.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/protocol/imaging/imaging_preparation_protocol.json - v2.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/file/image_file.json - v2.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/project/project.json - v14.1.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/process/analysis/analysis_process.json - v11.1.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/biomaterial/cell_line.json - v14.4.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/protocol/sequencing/library_preparation_protocol.json - v6.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/protocol/imaging/imaging_protocol.json - v11.2.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [type/biomaterial/specimen_from_organism.json - v10.3.0] - 2019-07-25
### Added
Added two optional fields to represent schema major and minor versions. Fixes #1076.

### [module/ontology/biological_macromolecule_ontology.json - v5.3.5] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/cell_cycle_ontology.json - v5.3.6] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/cell_type_ontology.json - v5.3.6] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/cellular_component_ontology.json - v1.0.5] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/development_stage_ontology.json - v5.3.6] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/disease_ontology.json - v5.3.8] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/enrichment_ontology.json - v1.2.6] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/ethnicity_ontology.json - v5.3.9] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/instrument_ontology.json - v5.3.6] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/length_unit_ontology.json - v5.3.5] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/library_amplification_ontology.json - v1.2.5] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/library_construction_ontology.json - v1.2.5] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/mass_unit_ontology.json - v5.3.5] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/microscopy_ontology.json - v1.0.5] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/organ_part_ontology.json - v5.3.5] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/process_type_ontology.json - v5.3.5] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/protocol_type_ontology.json - v5.3.5] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/sequencing_ontology.json - v1.1.5] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/species_ontology.json - v5.3.5] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/strain_ontology.json - v5.3.6] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/time_unit_ontology.json - v5.3.5] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/process/analysis/analysis_process.json - v11.0.3] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/protocol/imaging/imaging_preparation_protocol.json - v2.1.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/protocol/imaging/imaging_protocol.json - v11.1.4] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/protocol/sequencing/library_preparation_protocol.json - v6.1.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/biomaterial/cell_line.json - v14.3.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/biomaterial/cell_suspension.json - v13.1.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/protocol/probe.json - v1.1.1] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/biomaterial/donor_organism.json - v15.3.3] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/biomaterial/specimen_from_organism.json - v10.2.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/biomaterial/human_specific.json - v1.0.11] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/protocol/sequencing/sequencing_protocol.json - v10.0.3] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/biomaterial/organoid.json - v11.1.3] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/biomaterial/cell_morphology.json - v6.1.7] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/biomaterial/imaged_specimen.json - v3.1.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v6.1.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/process/process.json - v9.1.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/protocol/biomaterial_collection/collection_protocol.json - v9.1.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/protocol/analysis/analysis_protocol.json - v9.0.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/protocol/protocol.json - v7.0.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v3.0.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [type/file/reference_file.json - v3.1.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/biomaterial/mouse_specific.json - v1.0.8] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/biomaterial/timecourse.json - v2.0.2] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/biomaterial/preservation_storage.json - v6.1.1] - 2019-07-25
### Fixed
Fixed description of schema. Fixes #1035.

### [module/ontology/file_content_ontology.json - v1.0.1] - 2019-06-28
### Fixed
Fixed identifiers to be lower-cased in ontology classes and example. Fixes #1037

### [type/file/analysis_file.json - v6.1.1] - 2019-06-28
### Fixed
Fixed identifiers to be lower-cased in ontology classes and example. Fixes #1037

### [type/file/image_file.json - v2.1.1] - 2019-06-28
### Fixed
Fixed identifiers to be lower-cased in ontology classes and example. Fixes #1037

### [core/file/file_core.json - v6.1.1] - 2019-06-28
### Fixed
Fixed identifiers to be lower-cased in ontology classes and example. Fixes #1037

### [type/file/supplementary_file.json - v2.1.1] - 2019-06-28
### Fixed
Fixed identifiers to be lower-cased in ontology classes and example. Fixes #1037

### [type/file/reference_file.json - v3.1.1] - 2019-06-28
### Fixed
Fixed identifiers to be lower-cased in ontology classes and example. Fixes #1037

### [type/file/sequence_file.json - v9.1.1] - 2019-06-28
### Fixed
Fixed identifiers to be lower-cased in ontology classes and example. Fixes #1037

### [module/ontology/file_format_ontology.json - v1.0.0] - 2019-06-13
### Added
Added new ontology module. Partially fixes #812

### [core/file/file_core.json - v6.1.0] - 2019-06-10
### Added
Added content_description field. Fixes #542.

### [module/ontology/file_content_ontology.json - v1.0.0] - 2019-06-10
### Added
Added new file_content_ontology schema. Fixes #542.

### [type/file/image_file.json - v2.1.0] - 2019-06-10
### Added
Added content_description field. Fixes #542.

### [type/file/reference_file.json - v3.1.0] - 2019-06-10
### Added
Added content_description field. Fixes #542.

### [type/file/analysis_file.json - v6.1.0] - 2019-06-10
### Added
Added content_description field. Fixes #542.

### [type/file/supplementary_file.json - v2.1.0] - 2019-06-10
### Added
Added content_description field. Fixes #542.

### [type/file/sequence_file.json - v9.1.0] - 2019-06-10
### Added
Added content_description field. Fixes #542.

### [system/provenance.json - v1.0.4] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v3.0.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/file/reference_file.json - v3.0.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/file/sequence_file.json - v9.0.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/process/analysis/analysis_process.json - v11.0.2] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/biomaterial/organoid.json - v11.1.2] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/file/image_file.json - v2.0.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/biomaterial/cell_line.json - v14.3.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v3.1.2] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/protocol/biomaterial_collection/collection_protocol.json - v9.1.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v6.1.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/file/supplementary_file.json - v2.0.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/biomaterial/donor_organism.json - v15.3.2] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/biomaterial/cell_suspension.json - v13.1.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/protocol/analysis/analysis_protocol.json - v9.0.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/biomaterial/specimen_from_organism.json - v10.2.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/process/process.json - v9.1.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/protocol/imaging/imaging_preparation_protocol.json - v2.1.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/project/project.json - v14.0.2] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/protocol/biomaterial_collection/aggregate_generation_protocol.json - v2.0.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/protocol/imaging/imaging_protocol.json - v11.1.3] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/protocol/sequencing/sequencing_protocol.json - v10.0.2] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/protocol/protocol.json - v7.0.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/protocol/sequencing/library_preparation_protocol.json - v6.1.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/biomaterial/imaged_specimen.json - v3.1.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/file/analysis_file.json - v6.0.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v2.1.1] - 2019-06-04
### Added
Added user friendly names to fields submission_date, update_date, accession, submitter_id, document_id, updater_id. Fixes #989

### [module/protocol/channel.json - v2.0.4] - 2019-05-30
### Changed
Changed multiplexed property friendly name. Fixes #963

### [module/project/contact.json - v8.0.1] - 2019-05-30
### Changed
Changed corresponding_contributor property friendly name. Fixes #963

### [module/biomaterial/death.json - v5.5.1] - 2019-05-30
### Changed
Changed normothermic_regional_perfusion and cold_perfused friendly names. Fixes #963

### [type/protocol/sequencing/sequencing_protocol.json - v10.0.1] - 2019-05-30
### Changed
Changed paired_end property friendly name. Fixes #963

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v3.1.1] - 2019-05-30
### Changed
Changed pluripotency_vector_removed property friendly name. Fixes #963

### [type/protocol/imaging/imaging_protocol.json - v11.1.2] - 2019-05-30
### Changed
Changed overlapping_tiles property friendly name. Fixes #963

### [type/biomaterial/donor_organism.json - v15.3.1] - 2019-05-30
### Changed
Changed is_living property friendly name. Fixes #963

### [type/biomaterial/organoid.json - v11.1.1] - 2019-05-30
### Changed
Changed embedded_in_matrigel property friendly name. Fixes #963

### [type/project/project.json - v14.0.1] - 2019-05-30
### Changed
Changed corresponding_contributor property friendly name. Fixes #963

### [type/protocol/imaging/imaging_protocol.json - v11.1.1] - 2019-05-15
### Fixed
Fixed probe field where relevant in the imaging_protocol. Fixes #980.

### [type/process/process.json - v9.1.0] - 2019-05-14
### Added
Added start_time and end_time to process.json. Fixes #742.

### [type/biomaterial/cell_line.json - v14.3.0] - 2019-04-29
### Changed
Changed format for date_established property. Fixes #966

### [module/biomaterial/death.json - v5.5.0] - 2019-04-29
### Changed
Changed format for time_of_death property. Fixes #966

### [type/biomaterial/specimen_from_organism.json - v10.2.0] - 2019-04-29
### Changed
Changed format for collection_time property. Fixes #966

### [module/process/purchased_reagents.json - v6.1.0] - 2019-04-29
### Changed
Changed format for expiry_date property. Fixes #966

### [type/biomaterial/donor_organism.json - v15.3.0] - 2019-04-29
### Changed
Changed format for time_of_death property. Fixes #966

### [type/protocol/biomaterial_collection/collection_protocol.json - v9.1.0] - 2019-04-29
### Changed
Changed format for expiry_date property. Fixes #966

### [module/protocol/probe.json - v1.1.0] - 2019-04-29
### Changed
Changed format for expiry_date property. Fixes #966

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v6.1.0] - 2019-04-29
### Changed
Changed format for expiry_date property. Fixes #966

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v2.1.0] - 2019-04-29
### Changed
Changed format for expiry_date property. Fixes #966

### [type/protocol/sequencing/library_preparation_protocol.json - v6.1.0] - 2019-04-29
### Changed
Changed format for expiry_date property. Fixes #966

### [module/protocol/target.json - v1.1.0] - 2019-04-29
### Changed
Changed format for expiry_date property. Fixes #966

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v3.1.0] - 2019-04-29
### Changed
Changed format for expiry_date property. Fixes #966

### [type/protocol/imaging/imaging_protocol.json - v11.1.0] - 2019-04-29
### Changed
Changed format for expiry_date property. Fixes #966

### [type/process/analysis/analysis_process.json - v11.0.1] - 2019-04-29
### Added
Added description, example, user-friendly name, and guidelines to all definition fields. Fixes #955.

### [type/biomaterial/donor_organism.json - v15.2.0] - 2019-04-26
### Added
Added not applicable to is_living. Fixes #921

### [type/process/analysis/analysis_process.json - v11.0.0] - 2019-04-26
### Changed
Changed process_type to type. Fixes #931

### [type/process/process.json - v9.0.0] - 2019-04-26
### Changed
Changed process_type to type. Fixes #931

### [type/protocol/analysis/analysis_protocol.json - v9.0.0] - 2019-04-26
### Changed
Changed protocol_type to type. Fixes #931

### [type/protocol/protocol.json - v7.0.0] - 2019-04-26
### Changed
Changed protocol_type to type. Fixes #931

### [module/project/contact.json - v8.0.0] - 2019-04-25
### Changed
Changed contact_name to name. Fixes #927.

### [type/project/project.json - v14.0.0] - 2019-04-25
### Changed
Changed contact_name to name. Fixes #927.

### [core/file/file_core.json - v6.0.0] - 2019-04-23
### Changed
Changed file_format to format. Fixes #375.

### [type/file/reference_file.json - v3.0.0] - 2019-04-23
### Changed
Changed file_format to format. Fixes #375.

### [type/file/supplementary_file.json - v2.0.0] - 2019-04-23
### Changed
Changed file_format to format. Fixes #375.

### [type/file/image_file.json - v2.0.0] - 2019-04-23
### Changed
Changed file_format to format. Fixes #375.

### [type/file/analysis_file.json - v6.0.0] - 2019-04-23
### Changed
Changed file_format to format. Fixes #375.

### [type/file/sequence_file.json - v9.0.0] - 2019-04-23
### Changed
Changed file_format to format. Fixes #375.

### [type/biomaterial/donor_organism.json - v15.1.1] - 2019-04-18
### Changed
Changed description, guidelines and example for gestational_age. Fixes #911.

### [core/biomaterial/biomaterial_core.json - v8.1.0] - 2019-04-18
### Added
Added HDBR_accession to biomaterial_core. Fixes #945.

### [type/biomaterial/cell_line.json - v14.2.0] - 2019-04-18
### Added
Added HDBR_accession to biomaterial_core. Fixes #945.

### [type/biomaterial/imaged_specimen.json - v3.1.0] - 2019-04-18
### Added
Added HDBR_accession to biomaterial_core. Fixes #945.

### [type/biomaterial/cell_suspension.json - v13.1.0] - 2019-04-18
### Added
Added HDBR_accession to biomaterial_core. Fixes #945.

### [type/biomaterial/organoid.json - v11.1.0] - 2019-04-18
### Added
Added HDBR_accession to biomaterial_core. Fixes #945.

### [type/biomaterial/donor_organism.json - v15.1.0] - 2019-04-18
### Added
Added HDBR_accession to biomaterial_core. Fixes #945.

### [type/biomaterial/specimen_from_organism.json - v10.1.0] - 2019-04-18
### Added
Added HDBR_accession to biomaterial_core. Fixes #945.

### [type/biomaterial/cell_suspension.json - v13.0.0] - 2019-04-18
### Changed
Changed selected_cell_type to selected_cell_types. Fixes #923.

### [type/biomaterial/cell_line.json - v14.1.0] - 2019-04-18
### Added
Added optional timecourse field. Fixes #917.

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v3.0.0] - 2019-04-16
### Changed
Changed ipsc_induction_method to method, ipsc_induction_factors to reprogramming_factors, protocol_reagents to reagents. Removed ipsc_induction_produced_in_house. Fixes #926.

### [module/protocol/probe.json - v1.0.0] - 2019-04-11
### Added
Added new probe.json module. Fixes #813

### [core/process/process_core.json - v10.0.0] - 2019-04-11
### Changed
Changed process_location to location and operator to operators. Fixes #930.

### [type/process/process.json - v8.0.0] - 2019-04-11
### Changed
Changed process_location to location and operator to operators. Fixes #930.

### [type/process/analysis/analysis_process.json - v10.0.0] - 2019-04-11
### Changed
Changed process_location to location and operator to operators. Fixes #930.

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v3.0.0] - 2019-04-11
### Changed
Changed 'enrichment_method' to 'method', 'min_size_selected' to 'minimum_size' and 'max_size_selected' to 'maximum_size'. Fixes #925.

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v2.0.0] - 2019-04-09
### Changed
Changed differentiation_method to method. Fixes #924.

### [core/biomaterial/biomaterial_core.json - v8.0.0] - 2019-04-09
### Changed
Changed biosd_biomaterial to biosamples_accession and insdc_biomaterial to insdc_sample_accession. Fixes #929

### [type/biomaterial/specimen_from_organism.json - v10.0.0] - 2019-04-09
### Changed
Changed biosd_biomaterial to biosamples_accession and insdc_biomaterial to insdc_sample_accession. Fixes #929

### [type/biomaterial/cell_suspension.json - v12.0.0] - 2019-04-09
### Changed
Changed biosd_biomaterial to biosamples_accession and insdc_biomaterial to insdc_sample_accession. Fixes #929

### [type/biomaterial/organoid.json - v11.0.0] - 2019-04-09
### Changed
Changed biosd_biomaterial to biosamples_accession and insdc_biomaterial to insdc_sample_accession. Fixes #929

### [type/biomaterial/cell_line.json - v14.0.0] - 2019-04-09
### Changed
Changed biosd_biomaterial to biosamples_accession and insdc_biomaterial to insdc_sample_accession. Fixes #929

### [type/biomaterial/donor_organism.json - v15.0.0] - 2019-04-09
### Changed
Changed biosd_biomaterial to biosamples_accession and insdc_biomaterial to insdc_sample_accession. Fixes #929

### [type/biomaterial/imaged_specimen.json - v3.0.0] - 2019-04-09
### Changed
Changed biosd_biomaterial to biosamples_accession and insdc_biomaterial to insdc_sample_accession. Fixes #929

### [module/project/publication.json - v6.0.0] - 2019-04-08
### Changed
Changed publication_title to title and publication_url to url. Fixes #928.

### [type/project/project.json - v13.0.0] - 2019-04-08
### Changed
Changed publication_title to title and publication_url to url. Fixes #928.

### [type/biomaterial/cell_line.json - v13.0.0] - 2019-04-08
### Changed
Changed publication_title to title and publication_url to url. Fixes #928.

### [type/biomaterial/cell_line.json - v12.0.0] - 2019-04-08
### Changed
Changed cell_line_type to type. Fixes #935.

### [module/project/contact.json - v7.0.0] - 2019-04-08
### Changed
Changed project_role from enum to ontology. Fixes #894

### [type/project/project.json - v12.0.0] - 2019-04-08
### Changed
Changed project_role from enum to ontology. Fixes #894

### [module/biomaterial/preservation_storage.json - v6.1.0] - 2019-04-04
### Added
Added 'frozen at -80C' to storage_method field. Fixes #916.

### [type/protocol/imaging/imaging_preparation_protocol.json - v2.1.0] - 2019-04-04
### Added
Added 'frozen at -80C' to storage_method field. Fixes #916.

### [type/biomaterial/specimen_from_organism.json - v9.1.0] - 2019-04-04
### Added
Added 'frozen at -80C' to storage_method field. Fixes #916.

### [module/ontology/contributor_role_ontology.json - v1.0.0] - 2019-04-02
### Added
Added new contributor_role_ontology schema. Fixes #893.

### [module/protocol/channel.json - v2.0.3] - 2019-03-29
### Changed
Changed example and guidelines in filter_range. Fixes#878.

### [type/protocol/imaging/imaging_protocol.json - v11.0.13] - 2019-03-29
### Changed
Changed example and guidelines in filter_range. Fixes#878.

### [type/project/project.json - v11.1.0] - 2019-03-25
### Added
Added optional biostudies_accesssion field. Fixes #852.

### [module/process/sequencing/plate_based_sequencing.json - v3.0.0] - 2019-03-15
### Changed
Changed well and plate ID to label. Fixes #837.

### [type/biomaterial/cell_suspension.json - v11.0.0] - 2019-03-15
### Changed
Changed well and plate ID to label. Fixes #837.

### [module/biomaterial/medical_history.json - v5.2.8] - 2019-03-12
### Added
Added second example to test_results. Fixes #846.

### [type/biomaterial/donor_organism.json - v14.0.7] - 2019-03-12
### Added
Added second example to test_results. Fixes #846.

### [type/biomaterial/specimen_from_organism.json - v9.0.0] - 2019-03-08
### Changed
Changed organ_part to organ_parts since it is an array. Fixes #648.

### [type/protocol/sequencing/library_preparation_protocol.json - v6.0.0] - 2019-03-01
### Changed
Changed nucleic_acid_source field to be required. Fixes #824.

### [type/process/analysis/analysis_process.json - v9.0.0] - 2019-03-01
### Removed
Removed required outputs fields. Fixes #664.

### [module/process/sequencing/insdc_experiment.json - v2.0.0] - 2019-02-28
### Fixed
Fixed insdc_experiment_accession field to adhere to Style Guide. Fixes #809.

### [module/process/sequencing/plate_based_sequencing.json - v2.0.0] - 2019-02-28
### Fixed
Fixed well_quality field. Fixes #809.

### [type/process/process.json - v7.0.0] - 2019-02-28
### Fixed
Fixed insdc_experiment_accession field to adhere to Style Guide. Fixes #809.

### [type/biomaterial/cell_suspension.json - v10.0.0] - 2019-02-28
### Fixed
Fixed well_quality field. Fixes #809.

### [module/project/contact.json - v6.1.5] - 2019-02-28
### Added
Added administrator value to project role enum. Fixes #845.

### [type/project/project.json - v11.0.1] - 2019-02-28
### Added
Added administrator value to project role enum. Fixes #845.

### [module/biomaterial/state_of_specimen.json - v6.0.0] - 2019-02-25
### Fixed
Fixed array field names to be plural to adhere to Style Guide. Fixes #792.

### [type/biomaterial/specimen_from_organism.json - v8.0.0] - 2019-02-25
### Fixed
Fixed array field names to be plural to adhere to Style Guide. Fixes #792.

### [module/protocol/target.json - v1.0.9] - 2019-02-21
### Changed
Changed examples in molecule_id and assay_type. Fixes #830.

### [type/protocol/imaging/imaging_protocol.json - v11.0.12] - 2019-02-21
### Changed
Changed examples in molecule_id and assay_type. Fixes #830.

### [module/biomaterial/preservation_storage.json - v6.0.2] - 2019-02-20
### Added
Added enum value to preservation_storage. Fixes #831.

### [type/biomaterial/specimen_from_organism.json - v7.0.4] - 2019-02-20
### Added
Added enum value to preservation_storage. Fixes #831.

### [type/protocol/imaging/imaging_preparation_protocol.json - v2.0.3] - 2019-02-20
### Added
Added enum value to preservation_storage. Fixes #831.

### [type/file/sequence_file.json - v8.0.0] - 2019-02-13
### Fixed
Fixed array field names to be plural to adhere to Style Guide. Fixes #805.

### [type/biomaterial/cell_line.json - v11.0.0] - 2019-02-13
### Changed
Changed date_established from date-time to date format. Fixes #821.

### [module/protocol/target.json - v1.0.8] - 2019-02-12
### Changed
Changed u-f, examples, and description for some fields. Fixes #816.

### [module/protocol/channel.json - v2.0.2] - 2019-02-12
### Changed
Changed u-f, examples, and description for some fields. Fixes #816.

### [module/biomaterial/medical_history.json - v5.2.6] - 2019-02-12
### Added
Added examples. Fixes #816.

### [type/protocol/imaging/imaging_protocol.json - v11.0.11] - 2019-02-12
### Changed
Changed u-f, examples, and description for some fields. Fixes #816.

### [type/biomaterial/donor_organism.json - v14.0.5] - 2019-02-12
### Added
Added examples. Fixes #816.

### [module/ontology/ethnicity_ontology.json - v5.3.8] - 2019-02-12
### Changed
Changed hancestro example from underscore to colon

### [module/biomaterial/human_specific.json - v1.0.10] - 2019-02-12
### Changed
Changed hancestro example from underscore to colon

### [type/biomaterial/donor_organism.json - v14.0.4] - 2019-02-12
### Changed
Changed hancestro example from underscore to colon

### [type/protocol/imaging/imaging_preparation_protocol.json - v2.0.2] - 2019-02-12
### Changed
Changed guidelines, descriptions, and user-friendly names. Fixes #796.

### [module/protocol/target.json - v1.0.7] - 2019-02-12
### Changed
Changed guidelines, descriptions, and user-friendly names. Fixes #797.

### [type/protocol/imaging/imaging_protocol.json - v11.0.10] - 2019-02-12
### Changed
Changed guidelines, descriptions, and user-friendly names. Fixes #797.

### [type/protocol/biomaterial_collection/collection_protocol.json - v9.0.0] - 2019-02-12
### Fixed
Fixed reagent and method field names to remove redundancy to adhere to Style Guide. Fixes #807.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v6.0.0] - 2019-02-12
### Fixed
Fixed reagent and method field names to remove redundancy to adhere to Style Guide. Fixes #807.

### [type/protocol/sequencing/sequencing_protocol.json - v10.0.0] - 2019-02-12
### Fixed
Fixed method field name to be consistent with other protocols. Fixes #807.

### [type/protocol/sequencing/library_preparation_protocol.json - v5.0.0] - 2019-02-12
### Fixed
Fixed method field name to be consistent with other protocols. Fixes #807.

### [type/file/image_file.json - v1.0.4] - 2019-02-08
### Added
Added user_friendly name to file_core in image_file. Fixes #798

### [type/biomaterial/cell_suspension.json - v9.0.0] - 2019-02-05
### Changed
Changed total_estimated_cells to estimated_cell_count. Fixes #649.

### [module/process/sequencing/plate_based_sequencing.json - v1.0.6] - 2019-02-05
### Fixed
Fixed inconsistencies with Style Guide as caught by linter. Fixes #789

### [module/process/sequencing/barcode.json - v5.2.6] - 2019-02-05
### Fixed
Fixed inconsistencies with Style Guide as caught by linter. Fixes #789

### [system/links.json - v1.1.5] - 2019-02-05
### Fixed
Fixed inconsistencies with Style Guide as caught by linter. Fixes #789

### [core/biomaterial/biomaterial_core.json - v7.0.5] - 2019-02-05
### Fixed
Fixed inconsistencies with Style Guide as caught by linter. Fixes #789

### [module/ontology/disease_ontology.json - v5.3.7] - 2019-02-05
### Fixed
Fixed inconsistencies with Style Guide as caught by linter. Fixes #789

### [type/biomaterial/cell_suspension.json - v8.7.4] - 2019-02-05
### Fixed
Fixed inconsistencies with Style Guide as caught by linter. Fixes #789

### [type/protocol/sequencing/library_preparation_protocol.json - v4.4.6] - 2019-02-05
### Fixed
Fixed inconsistencies with Style Guide as caught by linter. Fixes #789

### [type/biomaterial/imaged_specimen.json - v2.0.7] - 2019-02-05
### Fixed
Fixed inconsistencies with Style Guide as caught by linter. Fixes #789

### [type/biomaterial/specimen_from_organism.json - v7.0.3] - 2019-02-05
### Fixed
Fixed inconsistencies with Style Guide as caught by linter. Fixes #789

### [type/biomaterial/donor_organism.json - v14.0.3] - 2019-02-05
### Fixed
Fixed inconsistencies with Style Guide as caught by linter. Fixes #789

### [type/biomaterial/organoid.json - v10.0.2] - 2019-02-05
### Fixed
Fixed inconsistencies with Style Guide as caught by linter. Fixes #789

### [type/biomaterial/cell_line.json - v10.0.4] - 2019-02-05
### Fixed
Fixed inconsistencies with Style Guide as caught by linter. Fixes #789

### [module/protocol/target.json - v1.0.6] - 2019-02-01
### Fixed
Fixed channel_id field which was declared as an array but missing items{} block Fixes #777

### [type/protocol/imaging/imaging_protocol.json - v11.0.9] - 2019-02-01
### Fixed
Fixed channel_id field which was declared as an array but missing items{} block Fixes #777

### [module/ontology/biological_macromolecule_ontology.json - v5.3.4] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/cell_cycle_ontology.json - v5.3.5] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/cell_type_ontology.json - v5.3.5] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/cellular_component_ontology.json - v1.0.4] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/development_stage_ontology.json - v5.3.5] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/disease_ontology.json - v5.3.6] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/enrichment_ontology.json - v1.2.5] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/ethnicity_ontology.json - v5.3.7] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/instrument_ontology.json - v5.3.5] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/length_unit_ontology.json - v5.3.4] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/library_amplification_ontology.json - v1.2.4] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/library_construction_ontology.json - v1.2.4] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/mass_unit_ontology.json - v5.3.4] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/microscopy_ontology.json - v1.0.4] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/organ_ontology.json - v5.3.7] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/organ_part_ontology.json - v5.3.4] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/process_type_ontology.json - v5.3.4] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/protocol_type_ontology.json - v5.3.4] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/sequencing_ontology.json - v1.1.4] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/species_ontology.json - v5.3.4] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/strain_ontology.json - v5.3.5] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/ontology/time_unit_ontology.json - v5.3.4] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/protocol/sequencing/library_preparation_protocol.json - v4.4.5] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/biomaterial/cell_line.json - v10.0.3] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/biomaterial/cell_suspension.json - v8.7.3] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/protocol/imaging/imaging_protocol.json - v11.0.8] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/protocol/target.json - v1.0.5] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/biomaterial/donor_organism.json - v14.0.2] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/biomaterial/specimen_from_organism.json - v7.0.2] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/biomaterial/human_specific.json - v1.0.9] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/protocol/sequencing/sequencing_protocol.json - v9.0.11] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/biomaterial/cell_morphology.json - v6.1.6] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/biomaterial/organoid.json - v10.0.1] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/biomaterial/imaged_specimen.json - v2.0.6] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v5.0.8] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/protocol/protocol.json - v6.3.9] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/process/analysis/analysis_process.json - v8.0.8] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v2.2.9] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/protocol/biomaterial_collection/collection_protocol.json - v8.2.11] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/protocol/analysis/analysis_protocol.json - v8.0.7] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/process/process.json - v6.0.7] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/file/reference_file.json - v2.2.10] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/biomaterial/mouse_specific.json - v1.0.7] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [type/protocol/imaging/imaging_preparation_protocol.json - v2.0.1] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/biomaterial/timecourse.json - v2.0.1] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/biomaterial/preservation_storage.json - v6.0.1] - 2019-02-01
### Fixed
Fixed descriptions to end in full stops. Fixes #785

### [module/protocol/channel.json - v2.0.1] - 2019-02-01
### Fixed
Fixed examples that were separated by comma instead of semi-colon. Fixes #784

### [module/protocol/target.json - v1.0.4] - 2019-02-01
### Fixed
Fixed examples that were separated by comma instead of semi-colon. Fixes #784

### [type/biomaterial/cell_line.json - v10.0.2] - 2019-02-01
### Fixed
Fixed examples that were separated by comma instead of semi-colon. Fixes #784

### [type/biomaterial/imaged_specimen.json - v2.0.5] - 2019-02-01
### Fixed
Fixed examples that were separated by comma instead of semi-colon. Fixes #784

### [type/file/reference_file.json - v2.2.9] - 2019-02-01
### Fixed
Fixed examples that were separated by comma instead of semi-colon. Fixes #784

### [type/file/supplementary_file.json - v1.1.8] - 2019-02-01
### Fixed
Fixed examples that were separated by comma instead of semi-colon. Fixes #784

### [type/protocol/imaging/imaging_protocol.json - v11.0.7] - 2019-02-01
### Fixed
Fixed examples that were separated by comma instead of semi-colon. Fixes #784

### [type/protocol/sequencing/sequencing_protocol.json - v9.0.10] - 2019-02-01
### Fixed
Fixed examples that were separated by comma instead of semi-colon. Fixes #784

### [type/file/image_file.json - v1.0.3] - 2019-02-01
### Fixed
Fixed incorrect name field value identified by linter. Fixes #776

### [module/process/sequencing/plate_based_sequencing.json - v1.0.5] - 2019-02-01
### Fixed
Fixed incorrect describedBy field pattern identified by linter. Fixes #776

### [type/biomaterial/cell_suspension.json - v8.7.2] - 2019-02-01
### Fixed
Fixed incorrect describedBy field pattern identified by linter. Fixes #776

### [module/ontology/cell_cycle_ontology.json - v5.3.4] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [module/ontology/cell_type_ontology.json - v5.3.4] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [module/ontology/development_stage_ontology.json - v5.3.4] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [module/ontology/disease_ontology.json - v5.3.5] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [module/ontology/ethnicity_ontology.json - v5.3.6] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [module/ontology/instrument_ontology.json - v5.3.4] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [module/ontology/microscopy_ontology.json - v1.0.3] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [type/biomaterial/cell_line.json - v10.0.1] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [type/biomaterial/cell_suspension.json - v8.7.1] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [type/biomaterial/donor_organism.json - v14.0.1] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [type/biomaterial/specimen_from_organism.json - v7.0.1] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [module/biomaterial/human_specific.json - v1.0.8] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [type/protocol/sequencing/sequencing_protocol.json - v9.0.9] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [type/protocol/imaging/imaging_protocol.json - v11.0.6] - 2019-02-01
### Fixed
Fixed missing description field in describedBy property. Fixes #780

### [type/file/analysis_file.json - v5.3.6] - 2019-02-01
### Fixed
Fixed missing user_friendly field in file_core. Fixes #778.

### [type/protocol/protocol.json - v6.3.8] - 2019-02-01
### Fixed
Fixed missing user_friendly field in protocol_core. Fixes 778

### [type/process/analysis/analysis_process.json - v8.0.7] - 2019-02-01
### Fixed
Fixed missing user_friendly field in file_core. Fixes #778.

### [type/biomaterial/cell_suspension.json - v8.7.0] - 2019-02-01
### Added
Added timecourse field to schema. Fixes #755.

### [type/biomaterial/donor_organism.json - v14.0.0] - 2019-01-31
### Changed
Changed familial_relationship to be plural. Fixes #768.

### [type/project/project.json - v11.0.0] - 2019-01-30
### Change
Change accession fields to arrays. Changed field names to adhere to Style Guide. Fixes #324.

### [type/biomaterial/cell_line.json - v10.0.0] - 2019-01-30
### Added
Added required model_organ field to cell line schema. Fixes #606.

### [type/biomaterial/organoid.json - v10.0.0] - 2019-01-30
### Removed
Removed organoid_type field. Fixes #736.

### [type/protocol/biomaterial_collection/aggregate_generation_protocol.json - v2.0.0] - 2019-01-30
### Update
Update field names/descriptions. Fixes #746.

### [module/biomaterial/preservation_storage.json - v6.0.0] - 2019-01-22
### Change
Change enum list to remove commas from values. Fixes #743.

### [type/biomaterial/specimen_from_organism.json - v7.0.0] - 2019-01-22
### Change
Change enum list to remove commas from values. Fixes #743.

### [type/protocol/imaging/imaging_preparation_protocol.json - v2.0.0] - 2019-01-22
### Change
Change enum list to remove commas from values. Fixes #743.

### [module/project/funder.json - v2.0.0] - 2019-01-22
### Changed
Changed grant_id and funder_name to be required. Fixes #731.

### [type/project/project.json - v10.0.0] - 2019-01-22
### Changed
Changed funders to be required. Fixes #731.

### [module/biomaterial/timecourse.json - v2.0.0] - 2019-01-18
### Changed
Changed fields to remove timecourse_. Fixes #745.

### [type/biomaterial/donor_organism.json - v13.0.0] - 2019-01-18
### Changed
Changed fields to remove timecourse_. Fixes #745.

### [type/biomaterial/organoid.json - v9.0.0] - 2019-01-16
### Updated
Updated field names to remove organoid_ prefix. Fixes #480.

### [module/process/sequencing/10x.json - v1.0.5] - 2019-01-15
### Added
Added second example for fastq creation method and fastq creation method version.Fixes #723

### [type/protocol/sequencing/sequencing_protocol.json - v9.0.8] - 2019-01-15
### Added
Added second example for fastq creation method and fastq creation method version.Fixes #723

### [type/biomaterial/donor_organism.json - v12.0.5] - 2019-01-14
### Update
Update examples to be separated by semicolon instead of comma. Fixes #728.

### [core/project/project_core.json - v7.0.5] - 2019-01-14
### Update
Update field examples/descriptions for grammar. Fixes #729.

### [type/project/project.json - v9.0.8] - 2019-01-14
### Update
Update field examples/descriptions for grammar. Fixes #729.

### [type/biomaterial/organoid.json - v8.3.12] - 2019-01-14
### Fixed
Fixed typo in field user_friendly in property organoid_morphology. Fixes #726

### [type/protocol/sequencing/sequencing_protocol.json - v9.0.7] - 2019-01-14
### Fixed
Fixed typo in field user_friendly in property protocol_core. Fixes #726

### [module/biomaterial/cell_morphology.json - v6.1.5] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [module/biomaterial/death.json - v5.4.1] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [module/biomaterial/familial_relationship.json - v6.0.3] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [module/biomaterial/growth_conditions.json - v6.4.2] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [module/biomaterial/human_specific.json - v1.0.7] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [module/biomaterial/medical_history.json - v5.2.5] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [module/biomaterial/mouse_specific.json - v1.0.6] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [module/biomaterial/preservation_storage.json - v5.3.5] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [module/biomaterial/state_of_specimen.json - v5.2.7] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [type/biomaterial/cell_line.json - v9.0.5] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [type/biomaterial/cell_suspension.json - v8.6.6] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [type/biomaterial/donor_organism.json - v12.0.4] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [type/biomaterial/specimen_from_organism.json - v6.3.8] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [type/protocol/imaging/imaging_preparation_protocol.json - v1.0.4] - 2019-01-09
### Update
Update examples, description, user-friendly names, and guideslines. Fixes #690.

### [module/biomaterial/timecourse.json - v1.1.5] - 2019-01-09
### Fixed
Fixed bug in spelling of user_friendly field in timecourse module. Fixes #710

### [type/biomaterial/donor_organism.json - v12.0.3] - 2019-01-09
### Fixed
Fixed bug in spelling of user_friendly field in timecourse module. Fixes #710

### [core/biomaterial/biomaterial_core.json - v7.0.4] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [core/file/file_core.json - v5.2.5] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [core/process/process_core.json - v9.0.3] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [core/project/project_core.json - v7.0.4] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [core/protocol/protocol_core.json - v5.2.5] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/biomaterial/cell_suspension.json - v8.6.5] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/biomaterial/organoid.json - v8.3.11] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/biomaterial/cell_line.json - v9.0.4] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/biomaterial/imaged_specimen.json - v2.0.4] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/biomaterial/donor_organism.json - v12.0.2] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/biomaterial/specimen_from_organism.json - v6.3.7] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/file/supplementary_file.json - v1.1.7] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/file/image_file.json - v1.0.2] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/file/sequence_file.json - v7.0.2] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/process/analysis/analysis_process.json - v8.0.6] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/file/analysis_file.json - v5.3.5] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/file/reference_file.json - v2.2.8] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/process/process.json - v6.0.6] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/project/project.json - v9.0.7] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/protocol/imaging/imaging_protocol.json - v11.0.5] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/protocol/biomaterial_collection/aggregate_generation_protocol.json - v1.1.7] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/protocol/biomaterial_collection/collection_protocol.json - v8.2.10] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v5.0.7] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/protocol/sequencing/library_preparation_protocol.json - v4.4.4] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/protocol/protocol.json - v6.3.7] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v2.2.8] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/protocol/imaging/imaging_preparation_protocol.json - v1.0.3] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v2.0.4] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/protocol/analysis/analysis_protocol.json - v8.0.6] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v1.3.3] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/protocol/sequencing/sequencing_protocol.json - v9.0.6] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #703.

### [type/protocol/sequencing/sequencing_protocol.json - v9.0.5] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #685.

### [module/ontology/biological_macromolecule_ontology.json - v5.3.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/cell_cycle_ontology.json - v5.3.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/cell_type_ontology.json - v5.3.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/cellular_component_ontology.json - v1.0.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/development_stage_ontology.json - v5.3.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/disease_ontology.json - v5.3.4] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/enrichment_ontology.json - v1.2.4] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/ethnicity_ontology.json - v5.3.5] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/instrument_ontology.json - v5.3.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/length_unit_ontology.json - v5.3.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/library_amplification_ontology.json - v1.2.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/library_construction_ontology.json - v1.2.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/mass_unit_ontology.json - v5.3.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/microscopy_ontology.json - v1.0.2] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/organ_ontology.json - v5.3.6] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/organ_part_ontology.json - v5.3.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/process_type_ontology.json - v5.3.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/protocol_type_ontology.json - v5.3.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/sequencing_ontology.json - v1.1.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/species_ontology.json - v5.3.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/strain_ontology.json - v5.3.4] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/ontology/time_unit_ontology.json - v5.3.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/protocol/sequencing/library_preparation_protocol.json - v4.4.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/biomaterial/cell_line.json - v9.0.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/biomaterial/cell_suspension.json - v8.6.4] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/protocol/target.json - v1.0.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/protocol/imaging/imaging_protocol.json - v11.0.4] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/biomaterial/donor_organism.json - v12.0.1] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/biomaterial/specimen_from_organism.json - v6.3.6] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/biomaterial/human_specific.json - v1.0.6] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/protocol/sequencing/sequencing_protocol.json - v9.0.5] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/biomaterial/cell_morphology.json - v6.1.4] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/biomaterial/organoid.json - v8.3.10] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/biomaterial/imaged_specimen.json - v2.0.3] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/protocol/protocol.json - v6.3.6] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v2.2.7] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/protocol/analysis/analysis_protocol.json - v8.0.5] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/process/process.json - v6.0.5] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v5.0.6] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/process/analysis/analysis_process.json - v8.0.5] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/protocol/biomaterial_collection/collection_protocol.json - v8.2.9] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/file/reference_file.json - v2.2.7] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/biomaterial/mouse_specific.json - v1.0.5] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/biomaterial/timecourse.json - v1.1.4] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [module/biomaterial/preservation_storage.json - v5.3.4] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/protocol/imaging/imaging_preparation_protocol.json - v1.0.2] - 2019-01-09
### Add
Add examples and user-friendly names. Fixes #613.

### [type/file/reference_file.json - v2.2.6] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #674.

### [type/process/process.json - v6.0.4] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #697.

### [module/process/purchased_reagents.json - v6.0.4] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [module/process/sequencing/10x.json - v1.0.4] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [module/process/sequencing/barcode.json - v5.2.5] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [module/process/sequencing/insdc_experiment.json - v1.1.5] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [module/process/sequencing/plate_based_sequencing.json - v1.0.4] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [type/protocol/biomaterial_collection/collection_protocol.json - v8.2.8] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [type/biomaterial/specimen_from_organism.json - v6.3.5] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v1.3.2] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [module/protocol/target.json - v1.0.2] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [type/protocol/imaging/imaging_protocol.json - v11.0.3] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [type/protocol/sequencing/library_preparation_protocol.json - v4.4.2] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v5.0.5] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v2.0.3] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [type/protocol/sequencing/sequencing_protocol.json - v9.0.4] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [type/process/process.json - v6.0.3] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [type/biomaterial/cell_suspension.json - v8.6.3] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #699.

### [type/protocol/imaging/imaging_protocol.json - v11.0.2] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #706. 

### [type/process/analysis/analysis_process.json - v8.0.4] - 2019-01-09
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #679.

### [type/file/supplementary_file.json - v1.1.6] - 2019-01-08
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #680.

### [type/protocol/analysis/analysis_protocol.json - v8.0.4] - 2019-01-08
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #678.

### [module/project/funder.json - v1.0.4] - 2019-01-08
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #701.

### [module/project/publication.json - v5.2.5] - 2019-01-08
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #701.

### [type/project/project.json - v9.0.6] - 2019-01-08
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #701.

### [type/biomaterial/cell_line.json - v9.0.2] - 2019-01-08
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #701.

### [type/protocol/sequencing/library_preparation_protocol.json - v4.4.1] - 2019-01-07
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #683.

### [type/project/project.json - v9.0.5] - 2019-01-03
### Added
Added user-friendly name, examples, and guidelines to adhere to Style Guide

### [type/protocol/biomaterial_collection/aggregate_generation_protocol.json - v1.1.6] - 2018-12-18
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #687.

### [type/protocol/biomaterial_collection/collection_protocol.json - v8.2.7] - 2018-12-18
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #687.

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v1.3.1] - 2018-12-18
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #687.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v5.0.4] - 2018-12-18
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #687.

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v2.2.6] - 2018-12-18
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #687.

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v2.0.2] - 2018-12-18
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #687.

### [type/biomaterial/donor_organism.json - v12.0.0] - 2018-12-13
### Changed
Changed donor_organism to make development_stage required. Fixes #607

### [type/biomaterial/donor_organism.json - v11.0.0] - 2018-12-13
### Removed
Removed normothermic_regional_perfusion. Fixes #590.

### [module/biomaterial/death.json - v5.4.0] - 2018-12-13
### Added
Added normothermic_regional_perfusion. Fixes #590.

### [type/file/sequence_file.json - v7.0.1] - 2018-12-13
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #672.

### [system/license.json - v1.0.0] - 2018-12-07
### Added
Added system entity to capture license under which data are released. Fixes #338.

### [module/protocol/target.json - v1.0.1] - 2018-12-07
### Changed
Changed molecule_ID to lower case in target.json Fixes #666

### [type/protocol/imaging/imaging_protocol.json - v11.0.1] - 2018-12-07
### Changed
Changed molecule_ID to lower case in target.json Fixes #666

### [type/biomaterial/imaged_specimen.json - v2.0.2] - 2018-12-07
### Removed
Removed extra example and fixed field name to match Style Guide. Fixes #668

### [type/biomaterial/donor_organism.json - v10.2.1] - 2018-12-07
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #650.

### [module/project/contact.json - v6.1.4] - 2018-12-07
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #662.

### [type/project/project.json - v9.0.4] - 2018-12-07
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #662.

### [type/biomaterial/specimen_from_organism.json - v6.3.4] - 2018-12-07
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #653.

### [type/biomaterial/organoid.json - v8.3.9] - 2018-12-07
### Changed
Changed description, user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #652.

### [type/biomaterial/imaged_specimen.json - v2.0.1] - 2018-12-05
### Added
Added user-friendly name for biomaterial_core. Fixes #656

### [module/protocol/target.json - v1.0.0] - 2018-12-05
### Added
Added new schema target.json to replace deprecated imaging_target.json. Fixes #641

### [type/protocol/imaging/imaging_protocol.json - v11.0.0] - 2018-12-05
### Added
Added new schema target.json to replace deprecated imaging_target.json. Fixes #641

### [type/protocol/sequencing/library_preparation_protocol.json - v4.4.0] - 2018-12-05
### Added
Added new optional fields nominal_length and nominal_sdev. Fixes #594.

### [type/file/sequence_file.json - v7.0.0] - 2018-12-05
### Changed
Changed technical_replicate_group_id to library_preparation_id. Fixes #262.

### [type/biomaterial/cell_suspension.json - v8.6.2] - 2018-12-05
### Changed
Changed user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #620.

### [type/biomaterial/cell_line.json - v9.0.1] - 2018-12-05
### Changed
Changed user-friendly, example, and guidelines attributes to adhere to Style Guide. Fixes #612.

### [type/biomaterial/imaged_specimen.json - v2.0.0] - 2018-12-03
### Changed
Changed field names and updated examples in imaged_specimen to match the Style Guide

### [module/protocol/imaging_target.json - v3.0.0] - 2018-11-28
### Changed
Changed channel_id from string to array

### [type/protocol/imaging/imaging_protocol.json - v10.0.0] - 2018-11-28
### Changed
Changed channel_id from string to array

### [module/protocol/channel.json - v2.0.0] - 2018-11-28
### Changed
Changed name of the required field channel_name to channel_id

### [type/protocol/imaging/imaging_protocol.json - v9.0.0] - 2018-11-28
### Changed
Changed name of the required field channel_name to channel_id

### [type/biomaterial/donor_organism.json - v10.2.0] - 2018-11-28
### Added
Added optional field timecourse.

### [system/links.json - v1.1.4] - 2018-11-27
### Fixed
Fixed a bug in the links schema still referencing core instead of system

### [module/protocol/imaging_target.json - v2.0.0] - 2018-11-21
### Changed
Changed channel field type to array

### [type/protocol/imaging/imaging_protocol.json - v9.0.0] - 2018-11-21
### Changed
Changed channel field type to array

### [module/protocol/imaging_target.json - v1.1.0] - 2018-11-19
### Changed
Changed channel field to optional

### [type/protocol/imaging/imaging_protocol.json - v8.1.0] - 2018-11-19
### Changed
Changed channel field to optional

### [type/protocol/sequencing/sequencing_protocol.json - v9.0.3] - 2018-10-17
### Changed
Changed description for paired_end. Fixes #592.

### [type/protocol/imaging/imaging_protocol.json - v8.0.3] - 2018-10-11
### Removed
Removed required field `protocol_type` from imaging_protocol (not actually in the schema). Fixes #572.

### [module/ontology/organ_ontology.json - v5.3.5] - 2018-09-25
### Fixed
Fixed issue with organ ontology assignment by using less stringent term restriction. Fixes #567.

### [type/biomaterial/specimen_from_organism.json - v6.3.3] - 2018-09-25
### Fixed
Fixed issue with organ ontology assignment by using less stringent term restriction. Fixes #567.

### [type/biomaterial/organoid.json - v8.3.8] - 2018-09-25
### Fixed
Fixed issue with organ ontology assignment by using less stringent term restriction. Fixes #567.

### [type/biomaterial/donor_organism.json - v10.1.2] - 2018-09-24
### Updated
Updated user-friendly term for is_living.

### [type/protocol/sequencing/library_preparation_protocol.json - v4.3.3] - 2018-09-21
### Added
Added 'not provided' to enum for strand field. Fixes #544.

### [type/biomaterial/cell_line.json - v9.0.0] - 2018-09-21
### Made
Made publication a single object instead of an array of objects. Fixes #557

### [type/project/project.json - v9.0.3] - 2018-09-21
### Fixed
Fixed missing required field project_core

### [module/ontology/organ_ontology.json - v5.3.4] - 2018-09-18
### Fixed
Fixed organ validation issue by including embryo and children as allowed values

### [type/biomaterial/organoid.json - v8.3.7] - 2018-09-18
### Fixed
Fixed organ validation issue by including embryo and children as allowed values

### [type/biomaterial/specimen_from_organism.json - v6.3.2] - 2018-09-18
### Fixed
Fixed organ validation issue by including embryo and children as allowed values

### [type/file/supplementary_file.json - v1.1.5] - 2018-09-04
### Added
Added missing provenance field

### [module/ontology/cellular_component_ontology.json - v1.0.2] - 2018-09-04
### Fixed
Fixed name/title mix-up bug

### [module/ontology/microscopy_ontology.json - v1.0.1] - 2018-09-04
### Fixed
Fixed name/title mix-up bug

### [type/file/supplementary_file.json - v1.1.4] - 2018-09-04
### Fixed
Fixed name/title mix-up bug

### [module/protocol/imaging_target.json - v1.0.2] - 2018-09-04
### Fixed
Fixed name/title mix-up bug

### [type/protocol/imaging/imaging_protocol.json - v8.0.2] - 2018-09-04
### Fixed
Fixed name/title mix-up bug

### [module/ontology/cellular_component_ontology.json - v1.0.1] - 2018-08-31
### Updated
Updated schema to json-schema draft-07

### [module/protocol/channel.json - v1.0.1] - 2018-08-31
### Updated
Updated schema to json-schema draft-07

### [module/protocol/imaging_target.json - v1.0.1] - 2018-08-31
### Updated
Updated schema to json-schema draft-07

### [type/biomaterial/imaged_specimen.json - v1.0.1] - 2018-08-31
### Updated
Updated schema to json-schema draft-07

### [type/file/image_file.json - v1.0.1] - 2018-08-31
### Updated
Updated schema to json-schema draft-07

### [type/protocol/imaging/imaging_preparation_protocol.json - v1.0.1] - 2018-08-31
### Updated
Updated schema to json-schema draft-07

### [type/protocol/imaging/imaging_protocol.json - v8.0.1] - 2018-08-31
### Updated
Updated schema to json-schema draft-07

### [module/ontology/cellular_component_ontology.json - v1.0.0] - 2018-08-31
### Added
Added new schema

### [module/ontology/microscopy_ontology.json - v1.0.0] - 2018-08-31
### Added
Added new schema

### [module/protocol/imaging_target.json - v1.0.0] - 2018-08-31
### Added
Added new schema

### [module/protocol/channel.json - v1.0.0] - 2018-08-31
### Added
Added new schema

### [type/biomaterial/imaged_specimen.json - v1.0.0] - 2018-08-31
### Added
Added new schema

### [type/file/image_file.json - v1.0.0] - 2018-08-31
### Added
Added new schema

### [type/protocol/imaging/imaging_preparation_protocol.json - v1.0.0] - 2018-08-31
### Added
Added new schema

### [type/protocol/imaging/imaging_protocol.json - v8.0.0] - 2018-08-31
### Added
Added several new fields including new required fields to address imaging use cases

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v1.3.0] - 2018-08-31
### Removed
Removed differentiation from 7 fields. Fixes #517

### [type/protocol/analysis/analysis_protocol.json - v8.0.3] - 2018-08-31
### Added
Added user-friendly name to some properties

### [type/process/analysis/analysis_process.json - v8.0.3] - 2018-08-31
### Added
Added user-friendly name to some properties

### [core/biomaterial/biomaterial_core.json - v7.0.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [core/file/file_core.json - v5.2.4] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [core/process/process_core.json - v9.0.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [core/project/project_core.json - v7.0.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [core/protocol/protocol_core.json - v5.2.4] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/biomaterial/cell_morphology.json - v6.1.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/biomaterial/death.json - v5.3.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/biomaterial/familial_relationship.json - v6.0.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/biomaterial/growth_conditions.json - v6.4.1] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/biomaterial/human_specific.json - v1.0.5] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/biomaterial/medical_history.json - v5.2.4] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/biomaterial/mouse_specific.json - v1.0.4] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/biomaterial/preservation_storage.json - v5.3.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/biomaterial/state_of_specimen.json - v5.2.6] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/biomaterial/timecourse.json - v1.1.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/biological_macromolecule_ontology.json - v5.3.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/cell_cycle_ontology.json - v5.3.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/cell_type_ontology.json - v5.3.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/development_stage_ontology.json - v5.3.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/disease_ontology.json - v5.3.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/enrichment_ontology.json - v1.2.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/ethnicity_ontology.json - v5.3.4] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/instrument_ontology.json - v5.3.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/length_unit_ontology.json - v5.3.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/library_amplification_ontology.json - v1.2.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/library_construction_ontology.json - v1.2.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/mass_unit_ontology.json - v5.3.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/organ_ontology.json - v5.3.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/organ_part_ontology.json - v5.3.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/process_type_ontology.json - v5.3.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/protocol_type_ontology.json - v5.3.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/sequencing_ontology.json - v1.1.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/species_ontology.json - v5.3.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/strain_ontology.json - v5.3.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/ontology/time_unit_ontology.json - v5.3.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/process/purchased_reagents.json - v6.0.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/process/sequencing/10x.json - v1.0.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/process/sequencing/barcode.json - v5.2.4] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/process/sequencing/insdc_experiment.json - v1.1.4] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/process/sequencing/plate_based_sequencing.json - v1.0.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/project/contact.json - v6.1.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/project/funder.json - v1.0.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [module/project/publication.json - v5.2.4] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [system/links.json - v1.1.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [system/provenance.json - v1.0.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/biomaterial/cell_line.json - v8.6.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/biomaterial/cell_suspension.json - v8.6.1] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/biomaterial/donor_organism.json - v10.1.1] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/biomaterial/organoid.json - v8.3.6] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/biomaterial/specimen_from_organism.json - v6.3.1] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/file/analysis_file.json - v5.3.4] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/file/reference_file.json - v2.2.5] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/file/sequence_file.json - v6.5.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/file/supplementary_file.json - v1.1.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/process/analysis/analysis_process.json - v8.0.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/process/process.json - v6.0.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/project/project.json - v9.0.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/protocol/analysis/analysis_protocol.json - v8.0.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/protocol/biomaterial_collection/aggregate_generation_protocol.json - v1.1.5] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/protocol/biomaterial_collection/collection_protocol.json - v8.2.6] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v1.2.6] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v5.0.3] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v2.2.5] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v2.0.1] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/protocol/imaging/imaging_protocol.json - v7.2.4] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/protocol/protocol.json - v6.3.5] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/protocol/sequencing/library_preparation_protocol.json - v4.3.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/protocol/sequencing/sequencing_protocol.json - v9.0.2] - 2018-08-31
### Added
Added schema name. Updated schema title. Fixes #501

### [type/biomaterial/donor_organism.json - v10.1.0] - 2018-08-28
### Changed
Changed optional field disease to diseases

### [type/biomaterial/specimen_from_organism.json - v6.3.0] - 2018-08-28
### Changed
Changed optional field disease to diseases

### [module/ontology/disease_ontology.json - v5.3.2] - 2018-08-21
### Fixed
Fixed schema validation by setting include_self to true

### [module/ontology/organ_ontology.json - v5.3.2] - 2018-08-21
### Fixed
Fixed schema validation by setting include_self to true

### [module/ontology/strain_ontology.json - v5.3.2] - 2018-08-21
### Fixed
Fixed schema validation by setting include_self to true

### [module/ontology/ethnicity_ontology.json - v5.3.3] - 2018-08-21
### Fixed
Fixed schema validation by correcting a casing issue

### [type/biomaterial/donor_organism.json - v10.0.3] - 2018-08-21
### Fixed
Fixed schema validation by setting include_self to true

### [type/biomaterial/cell_line.json - v8.6.1] - 2018-08-21
### Fixed
Fixed schema validation by setting include_self to true

### [type/biomaterial/specimen_from_organism.json - v6.2.9] - 2018-08-21
### Fixed
Fixed schema validation by setting include_self to true

### [type/biomaterial/organoid.json - v8.3.5] - 2018-08-21
### Fixed
Fixed schema validation by setting include_self to true

### [module/biomaterial/mouse_specific.json - v1.0.3] - 2018-08-21
### Fixed
Fixed schema validation by setting include_self to true

### [module/biomaterial/human_specific.json - v1.0.4] - 2018-08-21
### Fixed
Fixed schema validation by correcting a casing issue

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v2.0.0] - 2018-08-16
### Changed
Changed several field names from induced_pluripotent_cell_* to ipsc_*

### [module/biomaterial/growth_conditions.json - v6.4.0] - 2018-08-15
### Added
Added new culture_environment field. Fixes #234.

### [type/biomaterial/cell_line.json - v8.6.0] - 2018-08-15
### Added
Added new culture_environment field. Fixes #234.

### [type/biomaterial/cell_suspension.json - v8.6.0] - 2018-08-15
### Added
Added new culture_environment field. Fixes #234.

### [type/biomaterial/cell_line.json - v8.4.2] - 2018-08-15
### Added
Added stem cell to cell line type enum. Fixes #498.

### [module/ontology/ethnicity_ontology.json - v5.3.2] - 2018-08-10
### Fixed
Fixed the ontology reference to work with the new hancestro

### [type/biomaterial/donor_organism.json - v10.0.2] - 2018-08-10
### Fixed
Fixed the ontology reference to work with the new hancestro

### [module/biomaterial/human_specific.json - v1.0.3] - 2018-08-10
### Fixed
Fixed the ontology reference to work with the new hancestro

### [core/biomaterial/biomaterial_core.json - v7.0.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [core/file/file_core.json - v5.2.3] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [core/process/process_core.json - v9.0.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [core/project/project_core.json - v7.0.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [core/protocol/protocol_core.json - v5.2.3] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/biomaterial/cell_morphology.json - v6.1.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/biomaterial/death.json - v5.3.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/biomaterial/familial_relationship.json - v6.0.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/biomaterial/growth_conditions.json - v6.2.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/biomaterial/human_specific.json - v1.0.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/biomaterial/medical_history.json - v5.2.3] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/biomaterial/mouse_specific.json - v1.0.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/biomaterial/preservation_storage.json - v5.3.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/biomaterial/state_of_specimen.json - v5.2.5] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/biomaterial/timecourse.json - v1.1.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/biological_macromolecule_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/cell_cycle_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/cell_type_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/development_stage_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/disease_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/enrichment_ontology.json - v1.2.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/ethnicity_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/instrument_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/length_unit_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/library_amplification_ontology.json - v1.2.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/library_construction_ontology.json - v1.2.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/mass_unit_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/organ_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/organ_part_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/process_type_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/protocol_type_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/sequencing_ontology.json - v1.1.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/species_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/strain_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/ontology/time_unit_ontology.json - v5.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/process/sequencing/10x.json - v1.0.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/process/sequencing/barcode.json - v5.2.3] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/process/sequencing/insdc_experiment.json - v1.1.3] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/process/sequencing/plate_based_sequencing.json - v1.0.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/process/purchased_reagents.json - v6.0.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/project/contact.json - v6.1.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/project/funder.json - v1.0.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [module/project/publication.json - v5.2.3] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [system/links.json - v1.1.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [system/provenance.json - v1.0.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/biomaterial/cell_line.json - v8.4.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/biomaterial/cell_suspension.json - v8.4.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/biomaterial/donor_organism.json - v10.0.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/biomaterial/organoid.json - v8.3.4] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/biomaterial/specimen_from_organism.json - v6.2.8] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/file/analysis_file.json - v5.3.3] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/file/reference_file.json - v2.2.4] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/file/sequence_file.json - v6.5.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/file/supplementary_file.json - v1.1.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/process/analysis/analysis_process.json - v8.0.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/process/process.json - v6.0.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/project/project.json - v9.0.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/protocol/protocol.json - v6.3.4] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/protocol/analysis/analysis_protocol.json - v8.0.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/protocol/biomaterial_collection/aggregate_generation_protocol.json - v1.1.4] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/protocol/biomaterial_collection/collection_protocol.json - v8.2.5] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v1.2.5] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v5.0.2] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v2.2.4] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v1.2.5] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/protocol/imaging/imaging_protocol.json - v7.2.3] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/protocol/sequencing/library_preparation_protocol.json - v4.3.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/protocol/sequencing/sequencing_protocol.json - v9.0.1] - 2018-08-10
### Changed
Changed from json-schema draft-4 to draft-07

### [type/project/project.json - v9.0.0] - 2018-08-09
### Changed
Changed supplementary_files to supplementary_links.

### [type/file/sequence_file.json - v6.5.0] - 2018-08-07
### Removed
Removed deprecated smartseq2 field that was accidentally re-added.

### [type/file/sequence_file.json - v6.4.0] - 2018-08-06
### Added
Added optional field `technical_replicate_group` fixes #421

### [type/protocol/sequencing/sequencing_protocol.json - v9.0.0] - 2018-08-03
### Changed
Changed paired_ends to paired_end. Fixes #467.

### [type/protocol/sequencing/sequencing_protocol.json - v8.1.3] - 2018-08-03
### Changed
Changed sequencing_approach friendly name to Sequencing approach. Fixes #469.

### [type/biomaterial/donor_organism.json - v10.0.0] - 2018-08-03
### Changed
Changed biological_sex to sex. Fixes #384.

### [core/process/process_core.json - v9.0.0] - 2018-08-01
### Changed
Changed operator_identity to operator. Fixes #377.

### [type/process/process.json - v6.0.0] - 2018-08-01
### Changed
Changed operator_identity to operator. Fixes #377.

### [type/process/analysis/analysis_process.json - v8.0.0] - 2018-08-01
### Changed
Changed operator_identity to operator. Fixes #377.

### [module/biomaterial/familial_relationship.json - v6.0.0] - 2018-07-31
### Changed
Changed is_parent_of to child, is_child_of to parent, and is_sibling_of to sibling.

### [type/biomaterial/donor_organism.json - v9.0.0] - 2018-07-31
### Changed
Changed is_parent_of to child, is_child_of to parent, and is_sibling_of to sibling.

### [module/process/sequencing/10x.json - v1.0.1] - 2018-07-26
### Fixes
Fixes 10x url bug

### [type/protocol/sequencing/sequencing_protocol.json - v8.1.2] - 2018-07-26
### Fixes
Fixes 10x url bug

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v5.0.1] - 2018-07-26
### Removed
Removed requirement for non-existent field.

### [type/protocol/sequencing/library_preparation_protocol.json - v4.3.0] - 2018-07-26
### Added
Added optional nucleic_acid_source field. Fixes #385.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v5.0.0] - 2018-07-26
### Removed
Removed nucleic_acid_source field. Fixes #385.

### [type/biomaterial/donor_organism.json - v8.2.8] - 2018-07-23
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/biomaterial/state_of_specimen.json - v5.2.4] - 2018-07-23
### Changed
Changed example.

### [type/biomaterial/specimen_from_organism.json - v6.2.7] - 2018-07-23
### Changed
Changed example.

### [module/biomaterial/growth_conditions.json - v6.2.0] - 2018-07-23
### Added
Added a new field - `feeder_layer_type` - to capture the type of feeder layer cells biomaterial is grown on as this may have different effects on biomaterial growth/proliferation.

### [type/biomaterial/cell_line.json - v8.4.0] - 2018-07-23
### Added
Added a new field - `feeder_layer_type` - to capture the type of feeder layer cells biomaterial is grown on as this may have different effects on biomaterial growth/proliferation.

### [type/biomaterial/cell_suspension.json - v8.4.0] - 2018-07-23
### Added
Added a new field - `feeder_layer_type` - to capture the type of feeder layer cells biomaterial is grown on as this may have different effects on biomaterial growth/proliferation.

### [type/process/analysis/analysis_process.json - v6.0.0] - 2018-07-19
### Added
Added schema for analysis_process as required by the analysis team

### [type/protocol/analysis/analysis_protocol.json - v8.0.0] - 2018-07-19
### Removed
Removed a number of fields from analysis protocol as they are more appropriate in analysis_process

### [module/biomaterial/cell_morphology.json - v6.1.1] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/biomaterial/death.json - v5.3.1] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/biomaterial/growth_conditions.json - v6.1.2] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/biomaterial/human_specific.json - v1.0.1] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/biomaterial/medical_history.json - v5.2.2] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/biomaterial/mouse_specific.json - v1.0.1] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/biomaterial/preservation_storage.json - v5.3.1] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/biomaterial/state_of_specimen.json - v5.2.3] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/biomaterial/timecourse.json - v1.1.1] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/process/sequencing/barcode.json - v5.2.2] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/process/sequencing/insdc_experiment.json - v1.1.2] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/process/sequencing/plate_based_sequencing.json - v1.0.1] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/process/purchased_reagents.json - v6.0.1] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/project/contact.json - v6.1.1] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/project/funder.json - v1.0.1] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/project/publication.json - v5.2.2] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [system/provenance.json - v1.0.1] - 2018-07-17
### Changed
Changed descriptions.

### [type/biomaterial/cell_suspension.json - v8.3.3] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/cell_line.json - v8.3.3] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/donor_organism.json - v8.2.3] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/cell_suspension.json - v8.3.4] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/cell_line.json - v8.3.4] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/donor_organism.json - v8.2.4] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/donor_organism.json - v8.2.5] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/donor_organism.json - v8.2.6] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/specimen_from_organism.json - v6.2.3] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/specimen_from_organism.json - v6.2.4] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/sequencing/library_preparation_protocol.json - v4.2.3] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/process/process.json - v4.2.3] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/cell_suspension.json - v8.3.5] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v4.2.3] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/specimen_from_organism.json - v6.2.5] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v1.2.3] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v1.2.3] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/collection_protocol.json - v8.2.3] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/sequencing/library_preparation_protocol.json - v4.2.4] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/project/project.json - v8.2.3] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/project/project.json - v8.2.4] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/cell_line.json - v8.3.5] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/project/project.json - v8.2.5] - 2018-07-17
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/cell_line.json - v8.3.6] - 2018-07-17
### Changed
Changed descriptions.

### [type/protocol/biomaterial_collection/aggregate_generation_protocol.json - v1.1.3] - 2018-07-17
### Changed
Changed descriptions.

### [type/protocol/sequencing/sequencing_protocol.json - v8.1.1] - 2018-07-17
### Changed
Changed descriptions.

### [type/protocol/protocol.json - v6.3.3] - 2018-07-17
### Changed
Changed descriptions.

### [type/biomaterial/donor_organism.json - v8.2.7] - 2018-07-17
### Changed
Changed descriptions.

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v2.2.3] - 2018-07-17
### Changed
Changed descriptions.

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v1.2.4] - 2018-07-17
### Changed
Changed descriptions.

### [type/protocol/analysis/analysis_protocol.json - v7.2.4] - 2018-07-17
### Changed
Changed descriptions.

### [type/project/project.json - v8.2.6] - 2018-07-17
### Changed
Changed descriptions.

### [type/biomaterial/organoid.json - v8.3.3] - 2018-07-17
### Changed
Changed descriptions.

### [type/process/process.json - v4.2.4] - 2018-07-17
### Changed
Changed descriptions.

### [type/protocol/biomaterial_collection/collection_protocol.json - v8.2.4] - 2018-07-17
### Changed
Changed descriptions.

### [type/protocol/imaging/imaging_protocol.json - v7.2.2] - 2018-07-17
### Changed
Changed descriptions.

### [type/protocol/sequencing/library_preparation_protocol.json - v4.2.5] - 2018-07-17
### Changed
Changed descriptions.

### [type/file/reference_file.json - v2.2.3] - 2018-07-17
### Changed
Changed descriptions.

### [type/file/analysis_file.json - v5.3.2] - 2018-07-17
### Changed
Changed descriptions.

### [type/biomaterial/cell_suspension.json - v8.3.6] - 2018-07-17
### Changed
Changed descriptions.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v4.2.4] - 2018-07-17
### Changed
Changed descriptions.

### [type/file/sequence_file.json - v6.3.3] - 2018-07-17
### Changed
Changed descriptions.

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v1.2.4] - 2018-07-17
### Changed
Changed descriptions.

### [type/biomaterial/specimen_from_organism.json - v6.2.6] - 2018-07-17
### Changed
Changed descriptions.

### [module/process/sequencing/10x.json - v1.0.0] - 2018-07-17
### Added
Added module with 10x-specific fields.

### [type/protocol/sequencing/sequencing_protocol.json - v8.1.0] - 2018-07-17
### Added
Added reference to optional 10x module.

### [type/protocol/sequencing/sequencing_protocol.json - v8.0.0] - 2018-07-17
### Added
Added module with 10x-specific fields.

### [core/biomaterial/biomaterial_core.json - v7.0.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [core/file/file_core.json - v5.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [core/process/process_core.json - v7.0.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [core/project/project_core.json - v7.0.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [core/protocol/protocol_core.json - v5.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/cell_line.json - v8.3.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/organoid.json - v8.3.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/cell_suspension.json - v8.3.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/donor_organism.json - v8.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/specimen_from_organism.json - v6.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/file/reference_file.json - v2.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/file/sequence_file.json - v6.3.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/process/process.json - v4.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/project/project.json - v8.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/protocol.json - v6.3.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/analysis/analysis_protocol.json - v7.2.3] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/aggregate_generation_protocol.json - v1.1.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/collection_protocol.json - v8.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v1.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v4.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v2.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v1.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/sequencing/library_preparation_protocol.json - v4.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/sequencing/sequencing_protocol.json - v7.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/donor_organism.json - v8.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/cell_suspension.json - v8.3.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/specimen_from_organism.json - v6.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/organoid.json - v8.3.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/biomaterial/cell_line.json - v8.3.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/analysis/analysis_protocol.json - v7.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/file/analysis_file.json - v5.3.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/file/supplementary_file.json - v1.1.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/file/reference_file.json - v2.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/file/sequence_file.json - v6.3.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/process/process.json - v4.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/project/project.json - v8.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/analysis/analysis_protocol.json - v7.2.2] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v2.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/protocol.json - v6.3.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/collection_protocol.json - v8.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/imaging/imaging_protocol.json - v7.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v1.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/aggregate_generation_protocol.json - v1.1.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v1.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/sequencing/sequencing_protocol.json - v7.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/sequencing/library_preparation_protocol.json - v4.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v4.2.1] - 2018-07-16
### Changed
Changed descriptions, user-friendly names, and examples.

### [module/sequencing/plate_based_sequencing.json - v1.0.0] - 2018-07-16
### Added
Added module plate_based_sequencing. Fixes Issue #397

### [module/sequencing/smartseq2.json - v5.2.1] - 2018-07-16
### Deprecated
Deprecated module smartseq2 in favour of a more generic plate_based_sequncing module. Fixes Issue #397

### [type/biomaterial/cell_suspension.json - v8.3.0] - 2018-07-16
### Added
Added field `plate_based_sequencing` importing the module of the same name. Fixes Issue #397.

### [type/file/sequence_file.json - v6.3.0] - 2018-07-16
### Removed
Removed field `smartseq2` as the module has been deprecated. Fixes Issue #397.

### [module/project/contact.json - v6.1.0] - 2018-07-16
### Added
Added new optional field `corresponding_contributor` to contact schema. Fixes #409.

### [type/project/project.json - v8.2.0] - 2018-07-16
### Added
Added new optional field `corresponding_contributor` to contact schema. Fixes #409.

### [type/protocol/imaging/imaging_protocol.json - v7.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/protocol/protocol.json - v6.3.0] - 2018-07-16
### Added
Added optional provenance field

### [type/biomaterial/cell_line.json - v8.3.0] - 2018-07-16
### Added
Added optional provenance field

### [type/biomaterial/cell_suspension.json - v8.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/biomaterial/donor_organism.json - v8.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/biomaterial/organoid.json - v8.3.0] - 2018-07-16
### Added
Added optional provenance field

### [type/biomaterial/specimen_from_organism.json - v6.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/file/analysis_file.json - v5.3.0] - 2018-07-16
### Added
Added optional provenance field

### [type/file/reference_file.json - v2.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/file/sequence_file.json - v6.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/file/supplemental_file.json - v1.1.0] - 2018-07-16
### Added
Added optional provenance field

### [type/process/process.json - v4.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/project/project.json - v8.1.0] - 2018-07-16
### Added
Added optional provenance field

### [type/protocol/analysis/analysis_protocol.json - v7.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/protocol/biomaterial_collection/aggregate_generation_protocol.json - v1.1.0] - 2018-07-16
### Added
Added optional provenance field

### [type/protocol/biomaterial_collection/collection_protocol.json - v8.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v1.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v4.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v2.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v1.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/protocol/sequencing/library_preparation_protocol.json - v4.2.0] - 2018-07-16
### Added
Added optional provenance field

### [type/protocol/sequencing/sequencing_protocol.json - v7.2.0] - 2018-07-16
### Added
Added optional provenance field

### [module/project/contact.json - v6.0.0] - 2018-07-16
### Changed
Changed email to be optional. Changed institution to be required. Fixes #411.

### [type/project/project.json - v8.0.0] - 2018-07-16
### Changed
Changed email to be optional. Changed institution to be required. Fixes #411.

### [bundle/protocol.json - v10.4.0] - 2018-07-16
### Added
Added optional iPSC induction factors field to iPSC induction protocol.

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v1.1.0] - 2018-07-16
### Added
Added optional iPSC induction factors field to iPSC induction protocol.

### [type/file/supplemental_file.json - v1.0.0] - 2018-07-13
### Added
A new file type entity for supplemental files. Fixes #422.

### [core/project/project_core.json - v7.0.0] - 2018-07-12
### Changed
Changed `project_shortname` to `project_short_name`. Fixes #378.

### [bundle/project.json - v7.0.0] - 2018-07-12
### Changed
Changed `project_shortname` to `project_short_name`. Fixes #378.

### [type/project/project.json - v7.0.0] - 2018-07-12
### Changed
Changed `project_shortname` to `project_short_name`. Fixes #378.

### [module/project/contact.json - v5.3.0] - 2018-07-12
### Added
Added two new optional fields - `project_role` and `orcid_id`. Fixes #352.

### [bundle/project.json - v6.1.0] - 2018-07-12
### Added
Added two new optional fields - `project_role` and `orcid_id`. Fixes #352.

### [type/project/project.json - v6.1.0] - 2018-07-12
### Added
Added two new optional fields - `project_role` and `orcid_id`. Fixes #352.

### [bundle/project.json - v6.0.2] - 2018-07-06
### Changed
Changed descriptions and examples for fields in the project_core and project_type schemas.

### Added
Added some examples to fields in the project_core and project_type schemas.

### [type/project/project.json - v6.0.2] - 2018-07-06
### Changed
Changed descriptions and examples for fields in the project_core and project_type schemas.

### Added
Added some examples to fields in the project_core and project_type schemas.

### [core/project/project_core.json - v6.0.1] - 2018-07-06
### Changed
Changed descriptions and examples for fields in the project_core and project_type schemas.

### Added
Added some examples to fields in the project_core and project_type schemas.

### [bundle/project.json - v6.0.1] - 2018-07-06
### Changed
Changed descriptions, examples, and user friendly names in the contact module.

### [type/project/project.json - v6.0.1] - 2018-07-06
### Changed
Changed descriptions, examples, and user friendly names in the contact module.

### [module/project/contact.json - v5.2.2] - 2018-07-06
### Changed
Changed descriptions, examples, and user friendly names in the contact module.

### [bundle/biomaterial.json - v11.2.0] - 2018-07-06
### Added
Added `model_organ_part`, `organoid_size`, `organoid_size_unit`, `organoid_morphology`, `embedded_in_matrigel`, `organoid_growth_environment`, `input_aggregate_cell_count` and `organoid_stored_oxygen_levels` optional fields. Fixes #344. Fixes #347.

### Changed
Changed `organoid_age` description

### [type/biomaterial/organoid.json - v8.2.0] - 2018-07-06
### Added
Added `model_organ_part`, `organoid_size`, `organoid_size_unit`, `organoid_morphology`, `embedded_in_matrigel`, `organoid_growth_environment`, `input_aggregate_cell_count` and `organoid_stored_oxygen_levels` optional fields. Fixes #344. Fixes #347.

### Changed
Changed `organoid_age` description

### [bundle/biomaterial.json - v11.1.0] - 2018-07-06
### Added
Added optional field `normothermic_regional_perfusion` to donor_organism. Fixes #362.

### [type/biomaterial/donor_organism.json - v8.1.0] - 2018-07-06
### Added
Added optional field `normothermic_regional_perfusion` to donor_organism. Fixes #362.

### [bundle/biomaterial.json - v11.0.0] - 2018-07-06
### Changed
Renamed field `mus_musculus_specific` to `mouse_specific` and updated relevant refs. Fixes #387

### [type/biomaterial/donor_organism.json - v8.0.0] - 2018-07-06
### Changed
Renamed field `mus_musculus_specific` to `mouse_specific` and updated relevant refs. Fixes #387

### [module/biomaterial/human_specific.json - v1.0.0] - 2018-07-06
### Added
Added module `human_specific` to replace deprecated `homo_sapiens_specific`. Fixes #387

### [module/biomaterial/mouse_specific.json - v1.0.0] - 2018-07-06
### Added
Added module `mouse_specific` to replace deprecated `mus_musculus _specific`. Fixes #387

### [module/biomaterial/homo_sapiens_specific.json - v5.3.0] - 2018-07-06
### Deprecated
Deprecated module `homo_sapiens_specific` in favour of common name module `human_specific`. Fixes #387

### [module/biomaterial/mus_musculus_specific.json - v5.3.0] - 2018-07-06
### Deprecated
Deprecated module `mus_musculus_specific` in favour of common name module `mouse_specific`. Fixes #387

### [bundle/process.json - v8.1.0] - 2018-07-06
### Added
Added optional fields `length_of_time` and `length_of_time_unit` to process. Fixes #400

### [type/process/process.json - v4.1.0] - 2018-07-06
### Added
Added optional fields `length_of_time` and `length_of_time_unit` to process. Fixes #400

### [bundle/process.json - v8.0.0] - 2018-07-06
### Removed
Removed `length_of_time` and `length_of_time_unit` from process_core. Fixes #400

### [type/process/process.json - v4.0.0] - 2018-07-06
### Removed
Removed `length_of_time` and `length_of_time_unit` from process_core. Fixes #400

### [core/process/process_core.json - v7.0.0] - 2018-07-06
### Removed
Removed `length_of_time` and `length_of_time_unit` from process_core. Fixes #400

### [module/ontology/enrichment_ontology.json - v1.2.1] - 2018-07-06
### Changed
Fixed a typo in the curie for the enrichment ontology root class.

### [bundle/biomaterial.json - v10.2.1] - 2018-07-04
### Fixed
Fixed typo in `is_living` enum from "unkown" to "unknown"

### [type/biomaterial/donor_organism.json - v7.2.1] - 2018-07-04
### Fixed
Fixed typo in `is_living` enum from "unkown" to "unknown"

### [bundle/biomaterial.json - v10.2.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [bundle/process.json - v7.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [bundle/protocol.json - v10.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [bundle/reference.json - v2.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [core/process/process_core.json - v6.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/biomaterial/cell_morphology.json - v6.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/biomaterial/homo_sapiens_specific.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/biomaterial/mus_musculus_specific.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/biomaterial/preservation_storage.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/biomaterial/timecourse.json - v1.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/biomaterial/cell_line.json - v8.2.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/biomaterial/cell_suspension.json - v8.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/biomaterial/donor_organism.json - v7.2.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/biomaterial/organoid.json - v8.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/biomaterial/specimen_from_organism.json - v6.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/file/reference_file.json - v2.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/process/process.json - v3.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/protocol/analysis/analysis_protocol.json - v7.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/protocol/biomaterial_collection/collection_protocol.json - v8.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v4.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v2.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/protocol/protocol.json - v6.2.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/protocol/sequencing/library_preparation_protocol.json - v4.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [type/protocol/sequencing/sequencing_protocol.json - v7.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/biological_macromolecule_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/cell_cycle_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/cell_type_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/development_stage_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/disease_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/enrichment_ontology.json - v1.2.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/ethnicity_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/instrument_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/length_unit_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/library_amplification_ontology.json - v1.2.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/library_construction_ontology.json - v1.2.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/mass_unit_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/organ_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/organ_part_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/process_type_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/protocol_type_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/sequencing_ontology.json - v1.1.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/species_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/strain_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [module/ontology/time_unit_ontology.json - v5.3.0] - 2018-06-26
### Added
Added optional field `ontology_label` to all ontology modules.
Fixes Issue #383

### [bundle/biomaterial.json - v10.1.0] - 2018-06-25
### Added
Added optional field `organ_donation_death_type` to module death.
Fixes Issue #361.

### [type/biomaterial/donor_organism.json - v7.1.0] - 2018-06-25
### Added
Added optional field `organ_donation_death_type` to module death.
Fixes Issue #361.

### [module/biomaterial/death.json - v5.3.0] - 2018-06-25
### Added
Added optional field `organ_donation_death_type` to module death.
Fixes Issue #361.

### [bundle/biomaterial.json - v10.0.0] - 2018-06-25
### Changed
Changed the type of is_living to a string and added an enum to accommodate "unknown" as well as yes/no.
Fixes Issue #371.

### [type/biomaterial/donor_organism.json - v7.0.0] - 2018-06-25
### Changed
Changed the type of is_living to a string and added an enum to accommodate "unknown" as well as yes/no.
Fixes Issue #371.

### [bundle/protocol.json v10.2.0] - 2018-06-25
### Added
Added new aggregate_generation_protocol.json schema.
Fixes Issue #345.

### [type/protocol/biomaterial_collection/aggregate_generation_protocol.json v1.0.0] - 2018-06-25
### Added
Added new aggregate_generation_protocol.json schema.
Fixes Issue #345.

### [bundle/protocol.json - v10.1.1] - 2018-06-25
### Added
Added optionals small_molecules and differentiation_media fields.

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v1.1.1] - 2018-06-25
### Added
Added optionals small_molecules and differentiation_media fields.

### [bundle/biomaterial.json - v9.1.1] - 2018-06-20
### Changed
Updated the schema URL pattern to cell_line.

### [type/biomaterial/cell_line.json - v8.1.1] - 2018-06-20
### Changed
Updated the schema URL pattern to cell_line.

### [bundle/process.json - v7.0.0] - 2018-06-11
### Changed
Renamed `start_time` to `length_of_time` with updated description and added a number-only patterns.

### Added
Added `length_of_time_unit` referencing the time unit ontology module to provide a time unit for the duration in the `length_of_time` field.

### [type/process/process.json - v3.0.0] - 2018-06-11
### Changed
Renamed `start_time` to `length_of_time` with updated description and added a number-only patterns.

### Added
Added `length_of_time_unit` referencing the time unit ontology module to provide a time unit for the duration in the `length_of_time` field.

### [core/process/process_core.json - v6.0.0] - 2018-06-11
### Changed
Renamed `start_time` to `length_of_time` with updated description and added a number-only patterns.

### Added
Added `length_of_time_unit` referencing the time unit ontology module to provide a time unit for the duration in the `length_of_time` field.

### [bundle/biomaterial.json - v9.1.0] - 2018-06-11
### Added
Added optional field `confluency` to cell_line

### [type/biomaterial/cell_line.json - v8.1.0] - 2018-06-11
### Added
Added optional field `confluency` to cell_line

### [bundle/biomaterial.json - v9.0.0] - 2018-06-11
### Removed
Removed field `karyotype` from biomaterial_core as it does not apply to all biomaterials.

### [type/biomaterial/cell_suspension.json - v8.0.0] - 2018-06-11
### Removed
Removed field `karyotype` from biomaterial_core as it does not apply to all biomaterials.

### [type/biomaterial/donor_organism.json - v6.0.0] - 2018-06-11
### Removed
Removed field `karyotype` from biomaterial_core as it does not apply to all biomaterials.

### [type/biomaterial/organoid.json - v8.0.0] - 2018-06-11
### Removed
Removed field `karyotype` from biomaterial_core as it does not apply to all biomaterials.

### [type/biomaterial/specimen_from_organism.json - v6.0.0] - 2018-06-11
### Removed
Removed field `karyotype` from biomaterial_core as it does not apply to all biomaterials.

### [type/biomaterial/cell_line.json - v8.0.0] - 2018-06-11
### Removed
Removed field `karyotype` from biomaterial_core as it does not apply to all biomaterials.

### Added
Added optional field `karyotype` to cell_line

### [core/biomaterial/biomaterial_core.json - v9.0.0] - 2018-06-11
### Removed
Removed field `karyotype` from biomaterial_core as it does not apply to all biomaterials.

### [bundle/biomaterial.json - v8.0.0] - 2018-06-11
### Removed
Removed fields `growth_conditions` and `cell_morphology` from organoid.

### [type/biomaterial/organoid.json - v7.0.0] - 2018-06-11
### Removed
Removed fields `growth_conditions` and `cell_morphology` from organoid.

### [bundle/biomaterial.json - v7.2.0] - 2018-06-11
### Added
Added the field `purchased_specimen` referencing the purchased_reagents module, to capture purchasing of specimens such as blood samples.

### [type/biomaterial/specimen_from_organism.json - v5.3.0] - 2018-06-11
### Added
Added the field `purchased_specimen` referencing the purchased_reagents module, to capture purchasing of specimens such as blood samples.

### [type/biomaterial/cell_line.json - v7.1.0] - 2018-06-11
### Added
Added the field `tissue` referencing the organ part ontology module, to capture the tissue the cell line was derived from.

### [bundle/biomaterial.json - v7.1.0] - 2018-06-11
### Added
Added the field `tissue` referencing the organ part ontology module, to capture the tissue the cell line was derived from.

### [core/project/project_core.json - v6.0.0] - 2018-06-11
### Changed
Made project_description a required field.

### [type/project/project.json - v6.0.0] - 2018-06-11
### Changed
Made project_description a required field.

### [bundle/project.json - v6.0.0] - 2018-06-11
### Changed
Made project_description a required field.

### [bundle/biomaterial.json - v7.0.1] - 2018-06-07
### Changed
Updated definition of `ischemic_time` to address confusion from users.

### [type/biomaterial/specimen_from_organism.json - v5.2.3] - 2018-06-07
### Changed
Updated definition of `ischemic_time` to address confusion from users.

### [module/biomaterial/state_of_specimen.json - v5.2.2] - 2018-06-07
### Changed
Updated definition of `ischemic_time` to address confusion from users.

### [type/project/project.json - v5.3.0] - 2018-06-06
### Changed
Added a pointer to new module with three optional fields to track project funders.

### [module/project/funder.json - v1.0.0] - 2018-06-06
### Added
A new module with three optional fields to track project funders.

### [core/project/project_core.json - v5.2.2] - 2018-06-06
### Changed
Updated descriptions and examples.

### [bundle/protocol.json - v10.0.1] - 2018-06-05
### Changed
Added new protocol types to the oneOf list for protocol bundle.

### [module/biomaterial/timecourse.json - v1.0.0] - 2018-06-05
### Added
Added new module to capture timecourse information.

### [type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v1.0.0] - 2018-06-05
### Added
Added new protocol for IPSC induction.

### [type/protocol/biomaterial_collection/differentiation_protocol.json - v1.0.0] - 2018-06-05
### Added
Added new protocol for cell differentiation.

### [type/file/reference_file.json - v2.0.0] - 2018-06-04
### Changed
Made fields `ncbi_taxon_id`, `genus_species`, `assembly_type`, `reference_type` and `reference_version` required.

### [type/protocol/imaging/imaging_protocol.json - v7.0.0] - 2018-06-04
### Changed
Made field `protocol_type` required.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v4.0.0] - 2018-06-04
### Changed
Made field `nucleic_acid_source` required.

### [type/protocol/analysis/analysis_protocol.json - v7.0.0] - 2018-06-04
### Changed
Made field `protocol_type` required.

### [type/biomaterial/cell_line.json - v7.0.0] - 2018-06-04
### Changed
Made field `cell_line_type` required.

### [type/biomaterial/cell_line.json - v6.1.1] - 2018-06-04
### Changed
Updated the description for the schema.

### [bundle/biomaterial.json - v5.2.1] - 2018-06-01
### Changed
Dependency update for specimen_from_organism

### [type/biomaterial/specimen_from_organism.json - v5.2.1] - 2018-06-01
### Changed
Dependency update for preserveration_storage

### [module/biomaterial/preservation_storage.json - v5.2.1] - 2018-06-01
### Changed
Fixed (patch) incorrect user-friendly name.

### [bundle/protocol.json - v8.0.0] - 2018-06-01
### Changed
Updated protocol types.

### [type/protocol/sequencing/sequencing_protocol.json - v2.0.0] - 2018-06-01
### Added
Added the field `sequencing_approach` referencing the new sequencing ontology module and made it required.

### Removed
Removed the field `protocol_type` as it duplicates the information in `sequencing_approach`.

### [type/protocol/sequencing/library_preparation_protocol.json - v7.0.0] - 2018-06-01
### Removed
Removed the field `protocol_type` as it duplicates the information in `library_preparation_approach`.

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v2.0.0] - 2018-06-01
### Changed
Changed the type of field `enrichment_method` to use a different ontology module.

### Removed
Removed the field `protocol_type` as it duplicates the information in `enrichment_method`.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v2.0.0] - 2018-06-01
### Changed
Changed the type of field `dissociation_method` from string-enums to ontology object references.

### Removed
Removed the field `protocol_type` as it duplicates the information in `dissociation_method`.

### [type/protocol/biomaterial_collection/collection_protocol.json - v7.0.0] - 2018-06-01
### Changed
Changed the type of field `collection_method` from string-enums to ontology object references and made it required.

### Removed
Removed the field `protocol_type` as it duplicates the information in `collection_method`.

### [module/ontology/sequencing_ontology.json - v1.0.0] - 2018-06-01
### Added
Added a new ontology module for sequencing approach.

### [*.json - various version numbers - patch increment] - 2018-05-31
### Changed
Updated regex for all 66 schemas to match a range of schema.{}.humancellatlas domains and accept both version numbers in standard major.minor.patch format and "latest". Patch version increment to all schema versions.

### [*.json - various version numbers - patch increment] - 2018-05-25
### Changed
Updated regex for all 66 schemas to match http or https and schema.data or schema.dev.data.

### [bundle/protocol.json - v7.1.0] - 2018-05-24
### Changed
Updated enrichment_protocol.

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v1.1.0] - 2018-05-24
### Changed
Changed the type of field `enrichment_approach` from string-enums to ontology object references.

### [module/ontology/enrichment_ontology.json - v1.0.0] - 2018-05-24
### Added
Added a new ontology module for enrichment approach.

### [bundle/protocol.json - v7.0.1] - 2018-05-24
### Changed
Updated all protocol type references.

### [type/protocol/protocol.json - v6.0.1] - 2018-05-24
### Changed
Changed protocol_type ontology reference for all protocol schemas to reference process_type_ontology module for ontology modelling reasons.

### [type/protocol/sequencing/library_preparation_protocol.json - v1.0.1] - 2018-05-24
### Changed
Changed protocol_type ontology reference for all protocol schemas to reference process_type_ontology module for ontology modelling reasons.

### [type/protocol/sequencing/sequencing_protocol.json - v6.0.1] - 2018-05-24
### Changed
Changed protocol_type ontology reference for all protocol schemas to reference process_type_ontology module for ontology modelling reasons.

### [type/protocol/imaging/imaging_protocol.json - v6.0.1] - 2018-05-24
### Changed
Changed protocol_type ontology reference for all protocol schemas to reference process_type_ontology module for ontology modelling reasons.

### [type/protocol/biomaterial_collection/enrichment_protocol.json - v1.0.1] - 2018-05-24
### Changed
Changed protocol_type ontology reference for all protocol schemas to reference process_type_ontology module for ontology modelling reasons.

### [type/protocol/biomaterial_collection/dissociation_protocol.json - v1.0.1] - 2018-05-24
### Changed
Changed protocol_type ontology reference for all protocol schemas to reference process_type_ontology module for ontology modelling reasons.

### [type/protocol/biomaterial_collection/collection_protocol.json - v6.0.1] - 2018-05-24
### Changed
Changed protocol_type ontology reference for all protocol schemas to reference process_type_ontology module for ontology modelling reasons.

### [type/protocol/analysis/analysis_protocol.json - v6.0.1] - 2018-05-24
### Changed
Changed protocol_type ontology reference for all protocol schemas to reference process_type_ontology module for ontology modelling reasons.

### [type/protocol/sequencing/library_preparation_protocol.json - v2.0.0] - 2018-05-24
### Changed
Changed the type of fields `library_construction_approach`, `library_preamplification_method` and `cdna_library_amplification_method` from string-enums to ontology object references.

### [module/ontology/library_amplification_ontology.json - v1.0.0] - 2018-05-24
### Added
Added a new ontology module for library amplification approach.

### [module/ontology/library_construction_ontology.json - v1.0.0] - 2018-05-24
### Added
Added a new ontology module for library construction approach.

### [module/process/purchased_reagents.json - v6.0.0] - 2018-05-24
### Changed
Field batch_number changed to lot_number.

### [core/biomaterial/biomaterial_core.json - v6.0.0] - 2018-05-23
### Removed
Removed the `has_input_biomaterial` property as the purpose is misleading and no longer required by the spreadsheet importer

### [type/biomaterial/cell_line.json - v5.2.1] - 2018-05-21
### Added
Added `supplier` field to capture supplier of purchased cell line.
Added `lot_number` field to capture lot number of purchased cell line.
Added `induced pluripotent` to enum of cell line type.

### [module/biomaterial/cell_morphology.json - v6.0.0] - 2018-05-21
### Changed
Changed name of cell_viability field to percent_cell_viability to accurately reflect the value of this field.
### Added
Added a new field - cell_viability_result - to capture whether the cell_viability_method assay passed or failed.

This update is a major change due to the changing of the cell_viability field name.

### [type/biomaterial/cell_suspension.json - v6.0.0] - 2018-05-21
### Changed
Changed the field `target_cell_type` to `selected_cell_type`.

### [module/process/purchased_reagents.json - v5.2.0] - 2018-05-18
### Added
Added a new field - `kit_titer` - to record the appropriate titer and volume recommendations found in a kit's Certificate of Analysis.

### [module/ontology/species_ontology.json - v5.1.1] - 2018-05-18
### Changed
Bug fix to make ontology validation work - root species ontology node changed from "NCBITaxon:131567" to ["OBI:0100026","NCBITaxon:2759"] to reflect usage in HCAO. Patch update to referencing biomaterials and bundles.

### [module/biomaterial/growth_conditions.json - v6.0.0] - 2018-05-18
### Changed
This change is to make the fields mycoplasma_testing_method and mycoplasma_testing_results enums. This is a major change.

### [bundle/process.json - v5.2.1] - 2018-03-15
### Changed
Bug fix to make reference bundle schema reference its own definition with correct version

### [bundle/reference.json - v1.0.1] - 2018-03-15
### Changed
Bug fix to make reference bundle schema use the correct dependent version numbers

### [type/file/reference_file.json - v1.0.1] - 2018-03-15
### Changed
Bug fix to make reference_file schema use the correct dependent version numbers

### [bundle/reference.json - v1.0.0] - 2018-03-15
### Added
Added reference bundle entity to address the analysis pipeline use case for reference bundles

### [type/file/reference_file.json - v1.0.0] - 2018-03-15
### Added
Added reference_file entity to address the analysis pipeline use case for reference bundles

### [bundle/links.json - v1.0.0] - 2018-03-15
### Added
A links entity was added to allow linking of entites in bundles.

### [bundle/process.json - v5.2.0] - 2018-03-13
### Changed
The new generic process type was added to the list of processes that can be imported into a process bundle

### [tpye/process/process.json - v1.0.0] - 2018-03-13
### Added
A new generic process type was created to allow the creation of processes for which no metadata is available.

### [all modules/* and core/* entities - v5.1.0] - 2018-03-13
### Changed
The field `describedBy` was removed from the list of required fields as it was redundant. Only type entites and bundle entities need to explicitly declare a schema in data instances. As a result, all referencing types and bundles were also updated.

### [type/biomaterial/specimen_from_organism.json - v5.1.0] - 2018-03-13
### Changed
The field `organ_part` was removed from the list of required fields as it was causing issues for datasets where a sub-organ sampling site is not known.

### [module/project/publication.json - v5.0.1] - 2018-02-28
### Fixed
The incorrect field `title` in the list of required field was fixed to be the correct field `publication_title`.

### [type/project/project.json - v5.0.1] - 2018-02-28
### Fixed
Reference to patch version update of `module/project/publication.json` was updated.

### [type/biomaterial/cell_line.json - v5.0.1] - 2018-02-28
### Fixed
Reference to patch version update of `module/project/publication.json` was updated.

### [bundle/project.json - v5.0.1] - 2018-02-28
### Fixed
Reference to patch version update of `type/project/project.json` was updated.

### [bundle/biomaterial.json - v5.0.1] - 2018-02-28
### Fixed
Reference to patch version update of `type/biomaterial/cell_line.json` was updated.

## [5.0.0](https://github.com/HumanCellAtlas/metadata-schema/tree/5.0.0) - 2018-02-19
### Added
- New fields based on feedback from extensive user evaluation sessions
- New modules which now capture domain-specific fields
- New field attributes (e.g. example, user_friendly) to improve schema clarity
- New example v5.0.0 JSON files and template spreadsheets
- New markdown-formatted table of current metadata fields for easy browsing

### Changed
- Structural changes to the hierarchy of schema entities
- Updated field names and descriptions based on user feedback
- Expanded use ontologies to validate relevant fields
- Improved automatic Travis CI testing (new passing and failing example JSON)
- Improved documentation for schema updates (changelog.md, Metadata_schema_lifecycle_doc.md)

### Removed
- Removal of fields that were deemed unnecessary

## [v4.6.1](https://github.com/HumanCellAtlas/metadata-schema/tree/4.6.1) - 2017-12-15
### Removed
- Remove controlled vocabulary for `file.file_format`
- Remove regex for `file.filename`

## [v4.6.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.6.0) - 2017-12-14
### Added
- Add `name` field to `file` definition in `analysis_bundle.json`

### Changed
- Change `checksum` from required to optional in `analysis_bundle.json`

### Removed
- Remove undefined property `log` from `task` definition in `analysis_bundle.json`

## [v4.5.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.5.0) - 2017-12-13
### Added
- Add `analysis_bundle.json` as a core type

### Changed
- Update `assay_bundle.json` to include `has_input` and `has_output` references
- Update `analysis.json` to be fully compliant with JSON schema format
- Update enums on multiple fields to based on example test datasets
- Convert `contact.country` and `contact.country_division` free text string fields

## [v4.4.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.4.0) - 2017-12-08
### Added
- Add `core` field to `assay_bundle.json`, `project_bundle.json`, and `sample_bundle.json`
- Add bundle schemas to list of accepted core types
- Add description to `derived_from` field in `sample_bundle.json`

### Changed
- Made `sample_bundle.json`, `assay_bundle.json`, and `project_bundle.json` objects instead of arrays

## [v4.3.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.3.0) - 2017-12-06
### Added
- Add "10X" and "10x" as options to `seq.library_construction`, `rna.library_construction`, and `single_cell.cell_handling`
- Add "Cambridgeshire" as options to `contact.country_division`

### Changed
- Increase maximum `state_of_specimen.ischemic_time` and `state_of_specimen.postmortem_interval` value to 1000000

### Fixed
- Fix `sample.biosd_sample` regex in `sample.json`

## [v4.2.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.2.0) - 2017-12-05
### Changed
- Change `donor.json`' fields `height`, `weight`, and `age` from number type to string type with a regex to allow entering a number range
- Extend enums for `donor.age_unit` to allow plural forms
- Change `death.time_of_death` from required to optional

## [v4.1.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.1.0) - 2017-12-05
### Changed
- Update ontologies for `body_part_ontology.json` and `cell_type_ontology.json`
- Add ontology restrictions for `disease_ontology.json`
- Update example JSON used for testing for above ontologies

### Fixed
- Fix `sample.biosd_sample` regex in `sample.json`

## [v4.0.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.0.0) - 2017-11-21
### Added
- Schema for entities (cell_suspension, immortalized_cell_line, ingest, organoid, file, primary_cell_line, specimen_from_organism, imaging)
- Schema for ontologies (ontology_meta, body_part_ontology, cell_type_ontology, disease_ontology)
- Schema for bundles (assay_bundle, project_bundle, sample_bundle)
- Fields for all entities (name, description, core, id)
- Specific fields (contact.phone, donor.alcohol_history, donor.nutritional_state, donor.smoking_history, ncbi_taxon_id, genus_species, derived_from, sample_acessions, )

### Changed
- Schema `cell_line` split into `immortalized_cell_line` and `primary_cell_line` schema
- Schema `preservation.json` to `state_of_specimen.json`
- Field `sample.donor` to own `donor.json`
- Field `id` to `<entity>_id`
- Fields moved to core schema (`id`, `species`, `name`, `description`)
- Fields `project.ddjb_trace` and `project.sra_project` to `project.insdc_project`
- Field `project.ncbi_bioproject` to `project.insdc_study`
- Fields `sra_experiment` and `ena_experiment` to `insdc_experiment`
- Fields `ena_run` and `sra_run` to `insdc_run`
- Fields `sample.ena_sample` and `sample.ncbi_biosample` to `sample.insdc_sample`
- Field `organ` from `sample.json` to `specimen_from_organism.json`
- Field `preservation` from `sample.json` to `state_of_specimen.json`
- Fields `enrichment`, `total_estimated_cells`, `well` from `sample.json` to `cell_suspension.json`
- Field `cell_type` from `well.json` to `cell_suspension.json`

### Removed
- Field `core` from non-core entities
- Field `culture_type` from `sample.json`
- Field `sample.geo_sample`
- Field `sample.title`

## [v3.0](https://github.com/HumanCellAtlas/metadata-schema/tree/3.0) - 2017-09-19
### Added
- First official release.

## Template changelog formatting

### [schema_name.json - vX.Y.Z] - YYYY-MM-DD
### Added
### Changed
### Removed
### Fixed
### Deprecated
### Security
