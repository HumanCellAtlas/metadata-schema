# The Human Cell Atlas Metadata Structure Overview - v3.0

**Rationale for the [design and implementation choices](docs/rationale.md) for the HCA metadata standards.**

## Table of Contents
- [Design choices](#design-choices)
- [Implementation choices](#dimplementation-choices)

## Design choices

## Implementation choices

### Hierarchy of entities (core, type, module)

### Specifying version info

Each schema is self-describing using the `id` field with a URL to the location of the version of the current document. 

Version indicated in schema URL: `https://schema.humancellatlas.org/core/biomaterial/5.0.0/biomaterial_core`

As we are requiring instance data to also be self describing, all *Type* entities will require a property called `describedBy`. 

e.g. For `donor_organism.json` schema, these fields will look like: 

``` 
"$schema": "http://json-schema.org/draft-04/schema#"
"id": "https://schema.humancellatlas.org/type/biomaterial/5.0.0/donor_organism"
"additionalProperties": false,
"properties" : {
    "describedBy": {
        "description": "The URL reference to the schema.",
        "type": "string",
        "pattern": "https://schema.humancellatlas.org/type/biomaterial/[0-9]{1,}.[0-9]{1,}.[0-9]{1,}/donor_organism"
    },
    ...
}
```