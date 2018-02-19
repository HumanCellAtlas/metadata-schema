# The Human Cell Atlas Metadata Schema

This repo contains the HCA metadata JSON schemas for core, type, and modules entities, as well as bundles.

## JSON Schema File Standards

Below is a quick list of standards we try to adhere to about the structure of the HCA JSON schemas. If you would like to contribute a metadata JSON schema to this repo, please follow these standards and ask if you have any questions.

### Required standards

1. Core entities can not reference Type or Module subschemas.
1. All Type entities must reference their associated Core entity.
1. Module entities can only reference ontology (Module) subschemas.
1. A set of fields that are logically grouped, and only applicable in certain situations should be put into their own Module.
1. All schemas must implement semantic versioning. Briefly, a schema version is composed of three integers - each a separated by a period - in major.minor.patch format. Each core, type, module, and bundle schema is versioned independently.

### Strongly recommended standards

1. All field names should be lower case.
1. If a field (property) name is made up of more than one word, an underscore "_" should be used to separate the words.
1. All fields and schemas should have a description.
1. All fields should have an accompanying example and user-friendly name for displaying in a UI.
1. Fields should not have duplicate or snynonymous fields in any other schema.
