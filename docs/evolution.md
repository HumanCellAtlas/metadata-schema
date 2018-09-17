# The Human Cell Atlas: Metadata Evolution and Update Principles

## Table of Contents
- [Introduction](#introduction)
- [Schema versioning](#schema-versioning)
- [Module stability](#module-stability)
- [Adding new committers to metadata working group](#adding-new-committers-to-metadata-working-group)
- [Governance of schema updates](#governance-of-schema-updates)

## Introduction

This document describes the principles and standards by which the HCA metadata schema will evolve as well as the semantics for versioning and updating the schema. The HCA is collecting data from complex biological samples and assays with rich metadata. We expect over the lifetime of the project that the schemas that captures these metadata will need to change. These changes will always be to support the main goal of the HCA Data Coordination Platform (DCP): enabling downstream use and interpretation of the data. As our understanding of the data changes, the metadata we need may also change. The schemas, therefore, will also need to evolve to support new assays and changing practices in the contributing labs as the precise steps conducted for a particular assay are improved.

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
- Adding a required field.
- Removing a required or optional field.
- Moving a required field from one schema to another (increment both schemas).
- Changing the unqualified name of a required or optional field.
- Making an optional field required.
- Changing the type of a field (e.g. number to string, string to ontology/enum).
- Changing the ontology source for an ontologized field.
- Removing a value from a controlled vocabulary.
- Adding a regular expression to a field.

**Minor (increment to Y)**: Any schema change that ensures backwards compatibility with metadata created using the previous version.
- Adding an optional field.
- Making a required field optional.
- Removing a controlled vocabulary from a field (but the field type stays the same).
- Removing a regular expression from a field.

**Patch (increment to Z)**: Any change to auxiliary information that does not affect the structure or semantics of the schema itself. Also, any bug fixes to the schema.
- Adding or updating the field description to improve readability.
- Adding or updating the field example, comment, or user-friendly name.
- Extending a controlled vocabulary enumeration.
- Correcting a regular expression.
- Correcting an ontology source.

In the context of HCA metadata, **forwards compatibility** refers to when a metadata JSON document generated for and valid against the current schema version is also valid against an older version of that schema. Understanding forwards compatibility is especially important for HCA data consumers, for example for an analysis tool or a tertiary portal developer. We use a syntax based on a subset of that allowed by npm (a JavaScript package manager), whereby a consumer specifies the version of a schema it needs and whether it will tolerate alternative versions in any of the three fields. As an example, if a conformance requires version 1.0.4 of a package, it can state that requirement as:

- 1.0.4 -- requires exactly 1.0.4 and no other version
- ^1.0.4 -- requires exactly 1.0.4 and higher patch versions (e.g. 1.0.6, 1.0.7)
- 1.0.x -- requires exactly 1.0 but accepts any patch versions (e.g. 1.0.2, 1.0.7)
- 1.x -- requires exactly 1 but accepts any minor or patch versions (e.g. 1.1.0, 1.4.2)
- x -- accepts any major, minor, or patch version

## Module stability

This modular schema design allows us to have different rates of change for different schemas. In order to manage this, each different schema needs to be annotated with a stability level so everyone can understand the impact of a suggested change to a particular schema. This design also allows us to define appropriate governance for each stability level. Schemas labeled at a particular stability level are expected to be that stable, so high-stability modules should rarely change but low-stability modules should be free to iterate quickly. This annotation of stability is not the same as versioning, rather, it’s complimentary: it’s a way of indicating whether a schema is undergoing rapid changes to its version (low stability) or if the version hasn’t changed in awhile and is unlikely to change (high stability). 

### High Stability

High stability schemas are those where the DCP infrastructure has specific knowledge about the schema's structure and changing it would require a new DCP component software version. The ingest service is the most likely component to require high stability schemas. Fields in these schemas should be very limited and contain no scientific meaning. They are likely to be fields assigned by the Ingest infrastructure rather than provided by submitters. The process for requesting and getting updates to these fields should require a large scale consultation with the users of and developers of the Ingest service and a reasonable timeframe to update the software and educate users about the change before it enters production. The *core* entity schemas are generally considered high-stability schemas.

### Medium Stability

Medium stability schemas are those which tend to contain scientific fields on which downstream users - such as the pipeline infrastructure or portal developers - have dependencies. Changing fields in these schemas should not require major software updates for the DCP but may alter how the pipelines or portals query for new data. As these fields are likely to have scientific meaning, this increases the likelihood that they might change as our understanding evolves. The schema update process needs to be agile and able to react to changes in the subject. These changes may have significant downstream consequences for the automated processes that run the pipelines or portals, so strong agreement is needed for a change before it happens. The *type* entity schemas are generally considered medium-stability schemas.

### Low Stability

Schemas which are labeled as low stability are those associated with rapidly evolving sample collection or experimental techniques. Developers should avoid depending on the fields in these schemas. The update process should be rapid and use a minimal approval process such as a small number of +1s on a GitHub pull request. The *module* entity schemas are generally considered low-stability schemas.

### Reviewing Stability levels

The metadata working group should review the stability level of different schemas on a quarterly or bi-annual basis to decide if changes are needed.

## Adding new committers to metadata working group

A nominated group of metadata working group members will have commit access to the metadata-schema repo.  Committers are members of the working group who have permission to merge and accept pull requests to the metadata-schema repo.

Committers are not allowed to skip the review process. Any person including the committers who wish to make a change to a metadata schema module this process must be followed.

Anyone can request to join the committer team. When a request is received, the existing committers will discuss the request and vote on the addition of the new member. This process should be rapid and the requestor should hear the outcome within 72 hours.

## Governance of schema updates

The Metadata Working Group will report progress to the HCA executive committee. The Metadata Working Group will review the update process on a yearly basis and ensure it is meeting the needs of the working group. If at any point the process becomes problematic, changes will be made to ensure metadata update is not a blocker for the consortium as a whole. The working group will provide written updates on the following matters at the start of each month:

- Changes to the metadata specification
  - Updates to existing modules
  - Addition of new modules
- New members of the metadata working group
- New committers to the metadata-schema git repo

The reporting frequency and process will be reviewed on a yearly basis and modifications made as required.
