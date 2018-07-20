# The Human Cell Atlas: Metadata Schema Style and Formatting Guide

## Table of Contents
- [Introduction](#introduction)
- [Schema formatting](#schema-formatting)
- [Field formatting](#field-formatting)
- [General rules](#general-rules)

## Introduction

>**DISCLAIMER:** At this time, the HCA Metadata Standard development team is actively working towards adhering to this style and formatting guide. In some cases, the Standard might not yet follow all the guidelines outlined in this document.

This document describes the style and formatting rules followed by the HCA Metadata Standard for schemas and fields.

**What is in this document**
- General style guidelines and formatting for metadata schema and fields

**Who should be reading this document?**
- HCA DCP developers
- Anyone reporting a bug in the schema
- Members of external projects seeking alignment with HCA metadata standards

**What *isn't* in this document?**
- Directions for [requesting or suggesting changes](metadata-schema/docs/contributing.md) to the metadata schema
- Directions for [making changes to metadata schemas](metadata-schema/docs/committers.md)

## Schema formatting

The following attributes are required for each metadata schema in the HCA metadata standard. 

1. **$schema:** The JSON draft version being used. **NB:** Migration to draft-07 will occur soon.

    Example:
    
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            ...
        }

1. **description:** A clear, concise description of the schema. 

    Example:
    
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "description": "Information about an organoid biomaterial.",
            ...
        }

1. **additionalProperties:** Whether additional fields not in the schema will be allowed. The *additionalProperties* attribute should always be set to `false`. 

    Example:
    
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "description": "Information about an organoid biomaterial.",
            "additionalProperties": false,
            ...
        }

1. **required:** An array indicating which fields in the schema are required. If no fields are required, omit this attribute.  

    Example:
    
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "description": "Information about an organoid biomaterial.",
            "additionalProperties": false,
            "required": [
                "describedBy",
                "schema_type",
                "biomaterial_core",
                "model_for_organ"
            ],
            ...
        }

1. **title:** A title for the schema. The *title* is the name of the schema which should be in all lowercase and snake_case.  

    Example:
    
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "description": "Information about an organoid biomaterial.",
            "additionalProperties": false,
            "required": [
                "describedBy",
                "schema_type",
                "biomaterial_core",
                "model_for_organ"
            ],
            "title": "organoid",
            ...
        }

1. **type** and **properties:** The *type* of the schema (should always be `object`) followed by the metadata fields (`properties`).  

    Example:
    
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "description": "Information about an organoid biomaterial.",
            "additionalProperties": false,
            "required": [
                "describedBy",
                "schema_type",
                "biomaterial_core",
                "model_for_organ"
            ],
            "title": "organoid",
            "type": "object",
            "properties": {
                ...
            }
        }

**NB:** The `id` attribute is **not** included in JSON schemas in GitHub. Instead, it is inserted automatically at the time schemas are published to the HCA metadata standard on schema.humancellatlas.org.

Example:

    {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "id": "http://schema.humancellatlas.org/type/biomaterial/8.3.3/organoid",
        "description": "Information about an organoid biomaterial.",
        ...
    }

## Field formatting

### Required field attributes

The following attributes are required for each metadata field in an HCA metadata schema. 

1. **description:** A clear, concise statement of the what the metadata field is. The *description* value will appear in the metadata spreadsheet and be displayed in the Metadata Dictionary on the Data Portal. 

    Example:

        "project_role": {
            "description": "Primary role of the individual in the project.",
            ...
        }

    Each *description* should be one or more phrases or sentences and end in a full stop (period).

1. **type:** The JSON type of value required for the metadata field. The *type* value will be displayed in the Metadata Dictionary on the Data Portal.

    Example:
    
        "project_role": {
            "description": "Primary role of the individual in the project.",
            "type": "string",
            ...
        }
        
    Example valid *type* values include: string, number, boolean, array (when a field is an array of values), and object (when a field references another schema). The specification of valid JSON *type* values can be found [here](http://json-schema.org/latest/json-schema-validation.html#rfc.section.6.1.1). 

1. **user-friendly:** A user-facing, readable term or phrase for the metadata field. The *user-friendly* value will appear in the metadata spreadsheet, be displayed in the Data Browser, and be displayed in the Metadata Dictionary on the Data Portal. 

    Example:
    
        "project_role": {
            "description": "Primary role of the individual in the project.",
            "type": "string",
            "example": "principal investigator",
            "user_friendly": "Project role",
            ...
        }

    Each *user-friendly* value should be a short term or phrase written in sentence case (*i.e.* only the first word capitalized). Exceptions can be made for acronyms or other special capitalization schemes.
    
    Examples:
    
        Programmatic: min_size_selected
        User-friendly: Minimum size selected
        
        Programmatic: ncbi_taxon_id
        User-friendly: NCBI Taxonomy ID
        
        Programmatic: paired_ends
        User-friendly: Paired ends?
        
    Having *user-friendly* values for metadata fields has many advantages, including: 
    
    1. Unlike the programmatic metadata field name, the *user-friendly* value can contain punctuation, spaces, capitalization, and other basic formatting to make the interpretation of the field easier for data contributors and consumers.
    1. Changing a *user-friendly* value is considered a patch change to the schema version and is thus easier and simpler to implement than changing a metadata field name (which is a major change to the schema version).
    1. A *user-friendly* value can be templated to allow for custom displays. For example, appending a schema name to a *user-friendly* name can improve clarity: if the *user-friendly* value of the `biomaterial_id` field is set to `"${schema} ID"`, then `donor_organism.biomaterial_id` will render as "Donor organism ID" while `cell_line.biomaterial_id` will render as "Cell line ID".
    
### Conditional required field attributes

1. **example:** An example valid value for the metadata field. This attribute is required for all fields except those that reference a core, module, or ontology schema and those for which providing an example might bias data contributors. The *example* value will appear in the metadata spreadsheet and be displayed in the Metadata Dictionary on the Data Portal. 

    Example:
    
        "project_role": {
            "description": "Primary role of the individual in the project.",
            "type": "string",
            "example": "principal investigator",
            ...
        }

    An *example* value can be supplied for fields that are governed by an ontology, but the value should be the ontology term (text) not the ontology curie.
    
    Example:
    
        "organ": {
            "description": "The organ that the biomaterial came from. Blood and connective tissue are considered organs.",
            "type": "object",
            "example": "blood",
            "$ref": "module/ontology/organ_ontology.json",
            ...
        }

    An *example* should **not** be provided when:
    
    - A field imports a core or module schema, *e.g.* `donor_organism.medical_history`, because the fields in the imported schema will have their own example valid values.
    - A field uses an ontology, *e.g.* `genus_species`, because the fields in the imported ontology schema will have their own example valid values.
    - An example for a field could bias data contributors, *e.g.* providing an example ID for a biomaterial in the `biomaterial_id` field. 

1. **$ref:** The relative path to a core, module, or ontology schema which is imported by the metadata field. This attribute is required when a field imports a module, core, or ontology schema. The *$ref* value is not displayed to users outside of the JSON schema itself, and it should always be used with `"type": "object"`.

    Examples:

        "project_core" : {
            "description": "Core project-level information.",
            "type": "object",
            "$ref": "core/project/project_core.json",
            ...
        },
        "umi_barcode": {
            "description": "Information about unique molecular identifier (UMI) barcode sequences.",
            "type": "object",
            "$ref": "module/process/sequencing/barcode.json",
            ...
        },
        "organism_age_unit": {
            "description": "The unit in which Organism age is expressed.",
            "type": "object",
            "$ref": "module/ontology/time_unit_ontology.json",
            ...
        }

1. **format:** A JSON-defined format that the value supplied to the metadata field should follow. This attribute is required when a field should follow and validate against a standard JSON format. The *format* value is not displayed to users outside of the JSON schema itself.

    Example:
    
        "email": {
            "description": "Email address for the individual.",
            "type": "string",
            "user_friendly": "Email address",
            "format": "email",
            ...
        }

    Example valid *format* values include: date-time, email. The specification of valid JSON *format* values can be found [here](http://json-schema.org/latest/json-schema-validation.html#rfc.section.7.3). 


1. **enum:** A defined list of valid values for the metadata field. This attribute is required when a field should only be given a limited set of values, and an appropriate ontology is not available. The *enum* values currently are not displayed to users outside of the JSON schema itself, but in the future will be shown in the metadata spreadsheet.

    Example:
    
        "biological_sex": {
            "description": "The biological sex of the organism.",
            "type": "string",
            "example": "Should be one of: male, female, mixed, or unknown."
            "user_friendly": "Biological sex",
            "enum": [
                "female", 
                "male", 
                "mixed", 
                "unknown"
            ],
            ...
        },
        "project_role": {
            "description": "Primary role of the individual in the project.",
            "type": "string",
            "example": "principal investigator",
            "user_friendly": "Project role",
            "enum": [
                "principal investigator",
                "co investigator",
                "experimental scientist",
                "computational scientist",
                "clinician",
                "pathologist",
                "technician",
                "external curator",
                "Human Cell Atlas wrangler",
                "other"
            ],
            ...
        }

    If the *enum* list is short enough (5 or fewer values), the list of valid values should be included in the *example* attribute (*e.g.* the `biological_sex` enum) starting with the phrase "Should be one of:". If the *enum* list is too long to reasonably fit in the *example* attribute, a single valid value should be listed (*e.g.* the `project_role` enum).
    
    Creating an ontology module for a metadata field is preferred over maintaining an *enum* list.

### Optional field attributes

1. **pattern:** A regular expression that the metadata field value must follow. The *pattern* value is not displayed to users outside of the JSON schema itself, but the *example* attribute can describe what pattern the value should follow.

    Example:
    
        "insdc_project": {
            "description": "An INSDC (International Nucleotide Sequence Database Collaboration) project accession, if data has already been submitted to the DDBJ, ENA, or SRA.",
            "type": "string",
            "example": "SRP0000000.",
            "pattern": "^[D|E|S]RP[0-9]+$",
            "user_friendly": "INSDC project accession",
            ...
        }

1. **guidelines:** Instructions for how to fill in a valid value for the metadata field. This attribute is can be included on an as-needed basis when further clarification for how to fill in a metadata field would be helpful to data contributors. The *guidelines* value will appear in the metadata spreadsheet. 

    Example:
    
        "address": {
            "description": "Street address where the individual works.",
            "type": "string",
            "example": "0000 Main Street, Nowheretown, MA, 12091",
            "guidelines": "Include street name and number, city, country division, and postal code.",
            "user_friendly": "Street address"
        }

## General rules

### Field name conventions

The following conventions should be followed when deciding on a new metadata field name or suggesting changes to a current metadata field name.

1. Field names should be all lower case and snake_case.

    Example:

    `biomaterial_id`

1. Field names should be kept as short as possible while still conveying meaningful context. 

    Examples:
    
    `biomaterial_id` is preferred over `id` as it limits the field context to biomaterials.
    
    `paired_ends` is preferred over `does_sequencing_use_paired_ends` because it is shorter but still conveys full context.

1. The same field name should not appear within the same or across multiple schemas. If two fields require the same name, include context to differentiate them.

    Example:
    
    `umi_barcode` and `cell_barcode` differentiate between barcodes used to identify unique molecules and barcodes used to identify unique cells.

1. If a number field requires a corresponding unit field, append `_unit` to the number field name to generate the unit field name.

    Example:

    `organism_age` and `organism_age_unit`

### Field description tone and voice

1. Make a statement instead of a demand in the field description. For example:

    Use

        "description": "Age of the donor."
    
    not
    
        "description": "Enter the age of the donor."
    
1. Be concise instead of verbose in the field description. For example:

    Use
    
        "description": "Phone number of the individual or their lab."
    
    not
    
        "description": "Please include the phone number of the individual or the phone number of the individual's lab."

1. Use a formal writing voice. Avoid first-person pronouns, using "you", contractions, and slang. For example:

    Use

        "description": "Email address for the individual."

    not 
    
        "description": "Your email address."

### Ontology or enum?

Using an ontology to define valid values for a metadata field is preferred over using a JSON *enum* in most cases, provided that an appropriate ontology with good or full coverage is available.

The advantages of using an HCA ontology over an *enum* include:

1. Ontology can be adapted to changing needs without requiring the metadata schema to change.
1. Displaying, filtering, and sorting in the HCA Data Portal becomes easier.
1. Annotating HCA metadata with ontology terms improves the semantic interoperability of the data.

Instances when an *enum* are preferred over an ontology include:

1. The list of valid values is short and unlikely to change. For example, the valid values for the `donor_organism.is_living` field will always be "yes", "no", or "unknown".
1. The list of valid values has to include options such as "unknown", "other" or "NR".
1. The list of valid values is too diverse to be organized into a meaningful ontology or while awaiting the development of an appropriate ontology or ontology branch. If in doubt, check with one of the HCA ontologists!
