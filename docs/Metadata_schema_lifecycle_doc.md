# HCA Metadata schema lifecycle - v2.0

# Table of Contents
- [High level description](#high-level-description)
- [Terminology](#terminology)
- [Principles](#principles)
- [Stakeholders](#stakeholders)
- [Recording the Standards](#recording-the-standards)
- [Specification of schema structure and content](#specification-of-schema-structure-and-content)
- [Schema Versioning](#schema-versioning)
- [Module stability](#module-stability)
- [Adding new committers to metadata working group](#adding-new-committers-to-metadata-working-group)
- [Governance of Schema Updates](#governance-of-schema-updates)
- [Open questions](#open-questions)

Information about the process by which the HCA metadata schema will evolve is outlined here. Version 1.0 of this document can be found in the [HCA metadata lifecycle and versioning](https://docs.google.com/document/d/1eUVpYDLu2AxmxRw2ZUMM-jpKNxQudJbznNyNRp35nLc/edit#heading=h.6p3dwsx7c3hb) document. The v2.0 document here includes HCA schema design principles and standards and the semantics for versioning and updating these schema. More detailed discussion of the format and syntax of the metadata schema and their instantiation can be found in the complementary document [Metadata schema structure specification](https://docs.google.com/document/d/1pxQj7BfM8HHgD4ilm4dlvZuZATfJkNC5s_-TUoA4lYA/edit?ts=59b16455). These documents should be viewable by everyone. Please contact us if you do not have access to view.

## High level description

The Human Cell Atlas (HCA) is collecting complex biological samples and assays with rich descriptions. We expect over the lifetime of the project that the metadata schema that captures these descriptions will need to change. These changes will always be to support the main goal of the HCA Data Coordination Platform (DCP): enabling downstream use and interpretation of the data. As our understanding changes the descriptions we need may also change. The schema will also need to evolve to support new assays and changing practices in the contributing labs as the precise steps conducted for a particular assay are improved.

This document describes the basis for and the process by which the HCA metadata schema will evolve. This document includes our schema design principles and the semantics and process for versioning and updating these schema. For discussion of the detailed format and syntax of the metadata schema and their instantiation, see the complementary doc [Metadata schema structure specification](https://docs.google.com/document/d/1pxQj7BfM8HHgD4ilm4dlvZuZATfJkNC5s_-TUoA4lYA/edit?ts=59b16455#).

The metadata working group should review this process on a yearly basis and ensure it is meeting the needs of the working group. If at any point the process becomes problematic, changes should be made to ensure metadata update is not a blocker for the consortium as a whole.

## Terminology

### Metadata

The descriptive information needed to understand the data produced by the HCA. This includes assay content (e.g. fastq, tif), analysis results (e.g. gene cell table), and biological samples (e.g. biopsy or autopsy samples). This descriptive information will be provided in a structure as defined by the schema.

### Schema

A file-based specification for the metadata. The specification defines the metadata structure and fields, including field name, description, format, and cardinality. This specification is likely to have a hierarchical structure (e.g. objects and subobjects containing fields). In principle we could have either a single schema document or individual schema documents per module. In practice, we are mostly like to use individual schema documents. 

### Module

A specific subset of objects and fields from the schema associated with an isolated aspect of the metadata. These subsets would be needed for some, but not all, data sets. Examples where this is appropriate include field specific to a human donor, a particular single cell RNA-Seq platform like SmartSeq2, or a particular imaging experiment like MERFISH. We acknowledge the design must balance the flexibility offered by these modules with the overhead of maintaining a large number modules. We should only seek additional modules where there is a true requirement for them due experimental specialisation and not for convenience sake.

### Contributor

Any member of the HCA community can review and suggest updates to the schemas. In this document these individuals are referred to as contributors.

### Metadata WG member

Any person who is a member of the metadata working group.

### Committer

Any person with commit access to the metadata-schema git repo. These people should all be members of the metadata working group.

### Submitter

Any person who submits data or metadata to the HCA.

## Principles

The HCA metadata standards must be created and updated in a transparent and open manner ensuring the whole community can participate in the process if they wish. The following principles will be adhered to for the update process.

### Agility

The HCA foresees active development of sample handling, assays, and analyses, and will include both stable and rapidly evolving methods. As such, the metadata schema needs to be able to adapt accordingly, with regular updates (e.g. weekly or monthly), and a process for managing and tracking schema and data versions.

### Modularity

As the metadata evolves, different components will likely evolve at different rates than others -- for example, the specification of contact info may never change, whereas entirely new objects will be required when a new experimental technology is invented. A modular design will ensure that different components of the metadata can flexibly and independently evolve. 

### Flexibility

Significant experimental diversity is expected. Our methods for iterating metadata must allow for both the flexible capture of new data variants (e.g. new experimental assays), as well as the subsequent easy adoption of new schema as methods reach common usage. Any data contributor should always be able to add arbitrary additional fields to the metadata objects without causing process failure.

### Separation of (metadata) Concerns

It must be possible to separate different concerns related to metadata. For example, the metadata validation process should be driven by the schema, and depend only on having access to the schema, not the particular content of the schema or its semantics. Similarly, it should be possible to store the metadata on disk without understanding its syntax or semantics.

## Stakeholders

The HCA community is broad and has many participating groups. The metadata update process needs to be transparent and easy to access for all these groups. One important issue to face is ensuring that anyone who is not comfortable with the git interface is not blocked from making metadata update suggestions. 

### Collectors and users of the data

#### Data Contributing Labs

Data contributing labs are the groups who collect the samples and run the assays that generate the data for the HCA. They will be the individuals who have to record and report the majority of the metadata specified. The update and review process needs to be accessible to these groups and we must strive to ensure that they can easily find and incorporate changes in their own processes.

#### Ingest Brokers

The ingest brokers are the primary DCP contact with the data contributing labs. It is likely that a significant proportion of update requests will come via the ingest broker teams as they interact with the contributing labs and have a strong connection to the biology of the HCA. They should have a keen understanding of the capabilities of the contributing labs they are supporting and be able to comment on the reasonableness of change or addition to the rules with regard to the labs they support.

#### Secondary Analysis Pipelines team (MINT)
The secondary analysis pipelines will use metadata to discover and run their analysis pipelines. The impact of any changes on how pipelines discover data and run must be understood and where appropriate a member of the secondary analysis pipelines team should be involved in the review.

#### HCA data access portal team

The Data Access Portal (DAP) will be a simple file/bundle browser for the Data Storage System (DSS).  The DAP will use the metadata to build one or more indexes used to search for files and data bundles by a variety of configurable “facets”.  Changes to the metadata schema may alter how the indexer(s) are coded and how these search indexes get built.  The release of metadata versions should be coupled to updates of the indexers (and potentially web UI) by the DAP group..

#### Third party portal developers

The portal developers will use the metadata to build views and querying services on the data. Changes to the metadata schema may alter how these services are built. Portal developers must have access to the update and review process to ensure any downstream consequences on their own processes can be assessed and where necessary acted on.

#### Tertiary methods developers and other downstream users of the data

The metadata also needs to facilitate the all users of the data, whether they access it directly from the data store or via services provided by the different portals. This process must be visible and accessible to all our users.

### Software teams

The majority of metadata updates should have no impact on the software teams and should not require any downstream software updates but occasionally such breaking changes will be necessary.

#### Ingest API team

The Ingest API team should only need to be involved in the metadata update process if fields are updated which require changes to the Ingest API. This should be a very rare event and would require a longer consultation before making the change. The other class of change which would need consultation with the Ingest API is anything where semantic validation is required but the current schema validation tools are not able to validate yet. The schema allows for  additional metadata fields to be defined by a submitter beyond the fields already captured by the schema. This means submitters can always provide additional descriptive data to the DCP without it being officially part of the schema. If the suggested change require validation software updates to be scheduled, an individual submitter should be able to move forward with a change before the new validation is possible.

#### DSS team

The Data Storage System includes automated indexing of files marked as “metadata” in data bundles uploaded to the system.  The current primary, “non-transformative” index takes documents as they are and loads them into an Elasticsearch index.  This primary, non-transformative index can then be 1) queried, resulting in paged results pointing to individual bundles and/or 2) queries can be registered ahead of time and new data bundles (data bundle versions) whose metadata matches the queries will trigger notifications to a system associated with that registered query.

This approach is nice in that it is extremely flexible from a project metadata perspective.  Many different projects can be supported in a DSS with a non-transformative indexing strategy.  It does not need to understand the format of the metadata for a project ahead of time.  However, the limitation is related to changes over time.  In particular, the Elasticsearch indexing technology we are currently using is sensitive to changes in metadata key/value types.  For example, when the value of “species” changes from a string “homo sapiens” to a complex type “{ ‘name’ : ‘homo sapiens’, ‘ontology’: 817 }”.  For this reason, we want to use semantic versioning for each metadata document, such that breaking changes like this can be predicted by simply examining the top-level document schema version number.  Elasticsearch can then place conflicting schemas in different indexes (yet dynamically combine their content in searches).  This is the solution, and resulting limitation, we have currently.

## Recording the Standards

The schema will be stored as a series of individual documents which are related to entities and modules associated with them e.g project.json, assay.json, sample.json. These documents should be stored in a single versioned control repository alongside any documentation about the schema, the meaning of their contents or the update process.
 
The schemas and documentation will be stored in [metadata-schema GitHub repo](https://github.com/HumanCellAtlas/metadata_schema) in the HumanCellAtlas GitHub organisation.

Using GitHub, anyone will be able to propose changes to the schema through git pull requests but only a specified list of committers will be allowed to approve the pull requests and issue new versions of the metadata standards.

## Specification of schema structure and content

A detailed specification for the structure of the schema documents can be found in [this document](https://docs.google.com/document/d/1pxQj7BfM8HHgD4ilm4dlvZuZATfJkNC5s_-TUoA4lYA/edit?usp=sharing). The design principles that this structure follows are:

### Modular schema components

Metadata fields should be organized into `modules`, each with a piece of schema, including a `core` schema, containing the minimal schema necessary for all possible data and analyses, and a collection of additional `modules` that can be mixed and matched for each particular dataset or analysis. In this design, each schema module has its own independent version and lifecycle (as described below), and any particular dataset is defined by a collection of the appropriate modules.

It is worth noting the basis for defining a collection of fields and objects in a particular module can be considered along two different axises; do the fields/objects make sense together from a scientific point of view, e.g they are all fields associated with the same assay or sample type like Drop-Seq or a Brain section; and do the fields have the same stability requirement e.g changing a field will result in software update requirements for either ingest or pipelines or not. Fields which belong together scientifically and have broadly the same stability level should be grouped together in a single module.

### Machine readable

All metadata, metadata schema, and metadata conformance are specified in machine-readable, well-specified, web-accessible, and versioned file formats.

### Self-describing metadata

All metadata files are self-describing, ie, explicitly indicate the schema and schema version which they manifest. Ideally, this is done using a URL so that any metadata consumer can trivially fetch all schema associated with a metadata file.

### Flat Metadata Instantiation

Metadata files, containing metadata elements from multiple schema, are flattened into single files for storage or transmission (e.g. project.json). The actual contents of a given metadata file are subject to conformance specifications, which indicate the module schema and version that the metadata must conform to.

### Schema Language

Schema are a superset of JSON schema and JSON schema validation (json-schema.org) with all extensions declarative in nature (i.e. no "code" is required to specify a schema). Extensions to the native JSON schema validation will be needed to support validation of ontology identifiers or other specific HCA requirements. 

## Schema Versioning

The schema modules will be versioned using [semantic versioning](http://semver.org/). This gives each version a specific number in the form `X.Y.Z`. 

The numbers change when a schema update is made. The principles we follow to decide which of the three numbers to update are as follows. These principles primarily consider **Backwards compatibility**. This considers if the new schema is compatible with the old schema. This is the view from the producer of metadata. There are three kinds of changes that may or may not affect backwards compatibility: major, minor, and patch.

**Major (increment to X)**: Any change to the schema that breaks compatibility with metadata created using the previous version. Specific examples include:
- Removing a required field.
- Making a required field optional.
- Making a field use a controlled vocabulary or ontology.
- Renaming a field.
- Making a field into an array from a single value.
- Changing the type of a field.
- Unpacking an overloaded field (a field which serves multiple purposes, complex sample name for example)

**Minor (increment to Y)**: Any change to the schema that ensures compatibility with metadata created using the previous version. Specific examples include:
- Adding a field.
- Removing controlled vocabulary from a field.
- Making an optional field required.
- Adding controlled vocabulary from a field.

**Patch (increment to Z)**: A change to auxiliary information that does affect the structure or semantics of the schema itself. Specific examples include:
- Changing a description.
- Changing an example.
- Extending a controlled vocabulary enumeration

**Forwards compatibility** refers to whether data generated with a newer version will be compatible with a conformance requirements of an older version. This is the version from the consumer perspective -- e.g. an analysis tool or a conformance requirement. Here, we use a syntax based on a subset of that allowed by npm (a JavaScript package manager), whereby a consumer, e.g. in a conformance requirement, specifies the version of a module it needs and whether it will tolerate alternative version levels in any of the three fields. As an example, if a conformance requirements version 1.0.4 of a package, it can state that requirement as

- 1.0.4 -- requires exactly 1.0.4 and no other version
- ^1.0.4 -- requires exactly 1.0.4 and higher patch versions (e.g. 1.0.6, 1.0.7)
- 1.0.x -- requires exactly 1.0 but accepts any patch versions (e.g. 1.0.2, 1.0.7)
- 1.x -- requires exactly 1 but accepts any minor or patch versions (e.g. 1.1.0, 1.4.2)
- x -- accepts any major, minor, or patch version

## Module stability

This modular schema design allows us to have different rates of change for different modules. In order to manage this, each different module needs to be annotated with a stability level so everyone can understand the impact of a suggested change to a particular module. This also allows us to define appropriate governance for each stability level. Modules labeled at a particular stability level are expected to be that stable, so high stability modules should rarely change but low stability modules should be free to iterate quickly. This annotation of stability is not the same as versioning, rather, it’s complimentary: it’s a way of indicating whether a module is undergoing rapid changes to its version (low stability), or if the version hasn’t changed in awhile and is unlikely to change (high stability). 

### High Stability

High stability modules are those where the DCP infrastructure has specific knowledge about the module’s structure and changing it would require a new DCP component software version. The ingest service is the most likely component to require high stability modules. Fields in these modules should be very limited and contain no scientific meaning. They are likely to be fields assigned by the Ingest infrastructure rather than provided by submitters. The process for requesting and getting updates to these fields should require a large scale consultation with the users of and developers of the Ingest service and a reasonable timeframe to update the software and educate users about the change before it enters production.

### Medium Stability

Medium stability modules are those which tend to contain scientific fields which downstream users such as the pipeline infrastructure or portal developers have dependencies. Changing these fields should not require major software updates for the DCP but may alter how the pipelines or portals query for new data. As these fields are likely to have scientific meaning; this increases the likelihood that they might change as our understanding evolves. This means the update process needs to be agile and able to react to changes in the subject. That said, these changes may have significant downstream consequences for the automated processes that run the pipelines or portals, strong agreement is needed for a change before it happens. 

### Low Stability

Modules which are labeled as low stability are those associated with rapidly evolving sample collection or experimental techniques. Developers should avoid depending on the fields in these modules. The update process should be rapid and use a minimal approval process such as a small number of +1s on a git pull request.

### Reviewing Stability levels

The metadata working group should review the stability level of different modules on a quarterly or bi-annual basis to decide if changes are needed.

Submitters should always be able to define additional fields which are not part of the schema specification and have them pass through the system without error.

## Adding new committers to metadata working group

A nominated group of metadata working group members will have commit access to the metadata-schema repo.  Committers are members of the working group who have permission to merge and accept pull requests to the metadata-schema repo.

Committers are not allowed to skip the review process. Any person including the committers who wish to make a change to a metadata schema module this process must be followed.

Anyone can request to join the committer team. When a request is received, the existing committers will discuss the request and vote on the addition of the new member. This process should be rapid and the requestor should hear the outcome within 72 hours.

## Governance of Schema Updates

The metadata working group will report progress to the HCA executive committee.

The working group will provide written updates on the following matters at the start of each month:

- Changes to the metadata specification.
  - Updates to existing modules
  - Addition of new modules
- New members of the metadata working group.
- New committers to the metadata-schema git repo.

The reporting frequency and process will be reviewed on a yearly basis and modifications made as required.

## Open questions

This section lists open questions about this process which are not yet covered by the process description 

#### Handling submissions in prep

Do we have a strategy for submissions in preparation while the update gets put in?

#### What is the testing process for changes to the metadata-schema?

When a new pull request is made, what integration tests need to be run to reduce the likelihood of something breaking

#### How are update requests assigned to committers?

How do we ensure that all update requests are assigned to a committer and there is a reasonable feedback timeframe.

#### What labels do we need in the github repo to label issues and PRs?

Github has a label system and we need to define the correct labels to annotate issues and PRs to enable more rapid assessment

#### Which developers/teams should be notified for which modules?

We need a process so the committers reviewing a change know which teams need to be reached out to for different suggested changes or to figure out how best to enable people to watch given modules in a git repo

#### What happens if a suggested change required a new software update to be deployed which can’t be carried out in the given timeframe?

How do we modify the process to handle this?

#### Are readmes/other docs in metadata-schema subject to the same review process?

Can the readmes or other documentation which is not contained inside a schema be edited by committers without PR review?

#### What is the formal process of tagging and making a new release in git?

Are there any existing HCA DCP processes we can adopt here

#### How long is reasonable between approval and merge of new schema and it being in production?

Presumably in almost all cases this needs to be instant (or near as damn it) but it would be good to understand if there are occasions where it can’t be if the change happening requires an update to the ingest or any other DCP software. We should discuss this with the engineering teams?
