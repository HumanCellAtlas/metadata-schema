# Changelog
All notable changes to the HCA metadata schema will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [5.0.0] - 2018-02-14
### Added
- New visual identity by @tylerfortune8.
- Version navigation.

### Changed
- Start using "changelog" over "change log" since it's the common usage.
- Start versioning based on the current English version at 0.3.0 to help
translation authors keep things up-to-date.

### Removed
- Section about "changelog" vs "CHANGELOG".

### Fixed
- Fix typos in recent README changes.
- Update outdated unreleased diff link.

## [Released](https://github.com/HumanCellAtlas/metadata-schema/)

## [4.6.1](https://github.com/HumanCellAtlas/metadata-schema/tree/4.6.1) - 2017-12-15
### Removed
- Remove controlled vocabulary for `file.file_format`
- Remove regex for `file.filename`

## [4.6.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.6.0) - 2017-12-14
### Added
- Add `name` field to `file` definition in `analysis_bundle.json`

### Changed
- Change `checksum` from required to optional in `analysis_bundle.json`

### Removed
- Remove undefined property `log` from `task` definition in `analysis_bundle.json`

## [4.5.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.5.0) - 2017-12-13
### Added
- Add `analysis_bundle.json` as a core type

### Changed
- Update `assay_bundle.json` to include `has_input` and `has_output` references
- Update `analysis.json` to be fully compliant with JSON schema format
- Update enums on multiple fields to based on example test datasets
- Convert `contact.country` and `contact.country_division` free text string fields

## [4.4.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.4.0) - 2017-12-08
### Added
- Add `core` field to `assay_bundle.json`, `project_bundle.json`, and `sample_bundle.json`
- Add bundle schemas to list of accepted core types
- Add description to `derived_from` field in `sample_bundle.json`

### Changed
- Made `sample_bundle.json`, `assay_bundle.json`, and `project_bundle.json` objects instead of arrays

## [4.3.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.3.0) - 2017-12-06
### Added
- Add "10X" and "10x" as options to `seq.library_construction`, `rna.library_construction`, and `single_cell.cell_handling`
- Add "Cambridgeshire" as options to `contact.country_division`

### Changed
- Increase maximum `state_of_specimen.ischemic_time` and `state_of_specimen.postmortem_interval` value to 1000000

### Fixed
- Fix `sample.biosd_sample` regex in `sample.json`

## [4.2.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.2.0) - 2017-12-05
### Changed
- Change `donor.json`' fields `height`, `weight`, and `age` from number type to string type with a regex to allow entering a number range
- Extend enums for `donor.age_unit` to allow plural forms
- Change `death.time_of_death` from required to optional

## [4.1.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.1.0) - 2017-12-05
### Changed
- Update ontologies for `body_part_ontology.json` and `cell_type_ontology.json`
- Add ontology restrictions for `disease_ontology.json`
- Update example JSON used for testing for above ontologies

### Fixed
- Fix `sample.biosd_sample` regex in `sample.json`

## [4.0.0](https://github.com/HumanCellAtlas/metadata-schema/tree/4.0.0) - 2017-11-21
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

## [3.0.0](https://github.com/HumanCellAtlas/metadata-schema/tree/3.0) - 2017-09-19
### Added
- First official release.
