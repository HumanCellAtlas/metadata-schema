# Changelog

All notable changes to the HCA metadata schema will be documented in this file. Starting with v5.0.0, the schema will be versioned independently. Therefore, this changelog will contain notes for independent updates/releases per schema.

Starting after v5.0.0 release, updates will be declared for schemas independently in the form `[<schema_name>.json vX.Y.Z] - Release-date`. Changes will be organized across six categories: Added, Changed, Removed, Fixed, Deprecated, and Security. The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and (starting with v4.0.0) this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html). Unreleased but planned changes may be indicated under the `Unreleased` heading.

## [Unreleased](https://github.com/HumanCellAtlas/metadata-schema/tree/develop)

### [type/biomaterial/cell_line.json - v5.2.1] - 2018-05-21
### Added
Added `supplier` field to capture supplier of purchased cell line.
Added `lot_number` field to capture lot number of purchased cell line.
Added `induced pluripotent` to enum of cell line type.

### [module/ontology/species_ontology.json - v5.1.1] - 2018-05-18
### Changed
Bug fix to make ontology validation work - root species ontology node changed from "NCBITaxon:131567" to ["OBI:0100026","NCBITaxon:2759"] to reflect usage in HCAO. Patch update to referencing biomaterials and bundles.

## [Released](https://github.com/HumanCellAtlas/metadata-schema/)

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

