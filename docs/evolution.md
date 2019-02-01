# The Human Cell Atlas: Metadata Evolution and Update Principles

## Table of Contents
- [Introduction](#introduction)
- [Schema versioning](#schema-versioning)
- [Schema stability](#schema-stability)
- [Governance of schema updates](#governance-of-schema-updates)

## Introduction

This document describes the principles and standards by which the HCA metadata schema will evolve as well as the semantics for versioning and updating the schema. The HCA is collecting data from complex biological samples and assays with rich metadata. We expect over the lifetime of the project that the schemas that capture these metadata will need to change. These changes will always be to support the main goal of the HCA Data Coordination Platform (DCP): enabling downstream use and interpretation of the data. As our understanding of the data changes, the metadata we need may also change. The schemas, therefore, will also need to evolve to support new assays and changing practices in the contributing labs as the precise steps conducted for a particular assay are improved.

**What is in this document?**
 - How versioning of metadata schemas is defined
 - Definitions of the stability of metadata schemas
 - How schema updates are governed

**Who should be reading this document?**
 - Members of external projects seeking alignment with HCA metadata standards
 - Internal HCA DCP developers, especially those who depend on schema versions

**What *isn't* in this document?**
 - Mechanism by which [approved committers implement the update process](committers.md#specific-how-to-for-making-changes)

## Schema versioning

All metadata schemas will be versioned using [semantic versioning](http://semver.org/) which gives each schema version a specific number in the form `vX.Y.Z` where `X` is the major version number, `Y` is the minor version number, and `Z` is the patch version number.

Schema version numbers change when a schema update is made. The principles used to decide which version number to update primarily consider **backwards compatibility** with metadata created using a previous version. In other words, backwards compatibility is broken if a metadata JSON document generated for and valid against a previous schema version is now invalid against the updated schema version. Understanding backwards compatibility is especially important for HCA data generators and submitters. The three categories of version changes are outlined below along with examples of HCA metadata schema changes for each category:

**Major (increment to X)**: Any schema change that breaks backwards compatibility with metadata created using the previous version.
- Adding a required field
- Removing a required or optional field
- Moving a required field from one schema to another (increment both schemas)
- Changing the unqualified name of a required or optional field
- Making an optional field required
- Changing the type of a field (e.g. number to string, string to ontology/enum)
- Changing the ontology source for an ontologized field
- Removing a value from a controlled vocabulary
- Adding a regular expression to a field

**Minor (increment to Y)**: Any schema change that ensures backwards compatibility with metadata created using the previous version.
- Adding an optional field
- Making a required field optional
- Changing a field from a controlled vocabulary to free text without changing the field type
- Removing a regular expression from a field

**Patch (increment to Z)**: Any change to auxiliary information that does not affect the structure or semantics of the schema itself. Also, any bug fixes to the schema.
- Adding or updating the field description to improve readability
- Adding or updating the field example, comment, or user-friendly name
- Extending a controlled vocabulary enumeration
- Fixing an incorrect regular expression
- Fixing an incorrect ontology source

## Schema stability

The modular design of the HCA metadata standard allows for different rates of change for different schemas. In order to understand the downstream consequences of a suggested update, each schema is annotated with a stability level (high, medium, or low) indicating the expected rate of change. High stability schemas are expected to rarely change while low stability schemas are expected to rapidly change.

Assigning stability to schemas also enables distinct governance rules for each stability level. For example, an update to a high stability schema requires more rigorous review and a wider acceptance than an update to a low stability schema.

It is important to note that the stability of a schema is not the same as the schema version, although the two ideas are related. There are no restrictions on the type of update (major, minor, patch) that can happen to a schema based on its stability; however, the consequences of a major update on a high stability schema are much more severe than a major update to a low stability schema, for example. Both schema stability and update type should be considered when proposing a schema update.

### High Stability

A high stability schema is a schema which is expected to rarely change. Updating high stability schemas would require one or more major updates to DCP component software. The process for requesting updates to high stability schemas requires consultation with appropriate metadata users and DCP software developers and a reasonable timeframe to update the software and educate users about the change before it enters production. The `biomaterial_core.json` and `provenance.json` schemas are examples of high stability schemas.

### Medium Stability

A medium stability schema is a schema which is expected to change periodically in response to scientific advancement or exposure to different types of data. Updating medium stability schemas should not require major updates to DCP component software but may affect how data consumers interpret data. Because updates may have significant downstream consequences, agreement among appropriate metadata users and DCP software developers is strongly recommended. The process for requesting updates to medium stability schemas needs to be agile and able to react to scientific changes, as well. The `cell_suspension.json` and `enrichment_protocol.json` schemas are examples of medium stability schemas.

### Low Stability

A low stability schema is a schema which is associated with rapidly evolving sample types or experimental techniques. DCP component software developers should avoid depending on fields in these schemas given that they are prone to rapid updates. The process for requesting updates to low stability schemas should be rapid and require minimal approval among appropriate metadata users. The `10x.json` and `imaging_target.json` schemas are examples of low stability schemas.

### Reviewing Stability levels

The metadata team should review the stability level of schemas on a quarterly or bi-annual basis to decide if changes are needed. For example, a new, low stability schema might become standard over time and be promoted to medium or even high stability once it has been reviewed and agreed upon by the HCA community.

## Governance of schema updates

The metadata team will review the update process on a yearly basis and ensure it is meeting the needs of the group. If the process becomes problematic, changes will be made to ensure metadata updates are not a blocker for the consortium as a whole. The metadata team will provide updates on the following matters at regular DCP-wide meetings:

- Changes to the metadata standard and specification
  - Updates to existing schemas
  - Addition of new schemas
- New members of the metadata team
- New committers to the metadata-schema GitHub repo

The reporting frequency and process will be reviewed on a yearly basis and modifications made as required.
