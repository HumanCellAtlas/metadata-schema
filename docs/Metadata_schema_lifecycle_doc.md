# HCA Metadata schema lifecycle - v2.0

The **metadata design principles** can be read in the [Metadata schema lifecycle doc](docs/Metadata_schema_lifecycle_doc.md).

# Table of Contents
- [Recording the Standards](#recording-the-standards)
- [Specification of schema structure and content](#specification-of-schema-structure-and-content)
- [Schema Versioning](#schema-versioning)
- [Module stability](#module-stability)
- [Adding new committers to metadata working group](#adding-new-committers-to-metadata-working-group)
- [Governance of Schema Updates](#governance-of-schema-updates)
- [Open questions](#open-questions)

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

The schema modules will be versioned using [semantic versioning](http://semver.org/). This gives each version a specific number in the form `vX.Y.Z`. 

The version numbers change when a schema update is made. The principles we follow to decide which of the three numbers to update are described below. These principles primarily consider **backwards compatibility**. This considers if the new schema is compatible with the old schema. This is the view from the producer of metadata. There are three kinds of changes that may or may not affect backwards compatibility: major, minor, and patch.

**Major (increment to X)**: Any change to the schema that breaks compatibility with metadata created using the previous version. Specific examples include:
- Adding a required field.
- Removing a required or optional field.
- Moving a required field from one schema to another (increment both schemas).
- Making an optional field required.
- Changing the type of a field (e.g. number to string, string to ontology/enum).
- Changing the ontology source for an ontologized field.
- Changing the name of a required or optional field.
- Removing a value from a controlled vocabulary.
- Unpacking an overloaded field (a field which serves multiple purposes e.g. complex biomaterial name)

**Minor (increment to Y)**: Any change to the schema that ensures compatibility with metadata created using the previous version. Specific examples include:
- Adding an optional field.
- Making a required field optional.
- Updating the field description in a way that changes the meaning of the field.
- Adding a new module (increment the type schema that references the new module).
- Removing controlled vocabulary from a field (but the field type stays the same).

**Patch (increment to Z)**: A change to auxiliary information that does affect the structure or semantics of the schema itself. Specific examples include:
- Adding or updating the field description to improve readability.
- Adding or updating the field example.
- Adding or updating the field comment.
- Adding or updating the field user-friendly name.
- Extending a controlled vocabulary enumeration.
- Fixing an incorrect regular expression.

**Forwards compatibility** refers to whether data generated with a newer version will be compatible with conformance requirements of an older version. This is the version from the consumer perspective, for example an analysis tool or a conformance requirement. We use a syntax based on a subset of that allowed by npm (a JavaScript package manager), whereby a consumer specifies the version of a schema it needs and whether it will tolerate alternative versions in any of the three fields. As an example, if a conformance requires version 1.0.4 of a package, it can state that requirement as:

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

## Governance of Schema Updates

The metadata working group will report progress to the HCA executive committee. The working group will provide written updates on the following matters at the start of each month:

- Changes to the metadata specification
  - Updates to existing modules
  - Addition of new modules
- New members of the metadata working group
- New committers to the metadata-schema git repo

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
