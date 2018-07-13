# The Human Cell Atlas: Metadata Schema Style and Formatting Guide

## Table of Contents
- [Introduction](#introduction)
- [Schema formatting](#schema-formatting)
- [Field formatting](#field-formatting)
- [General rules](#general-rules)

## Introduction

>**DISCLAIMER:** At this time, the HCA Metadata Standard development team is actively working towards adhering to this style and formatting guide. In some cases, the Standard might not yet follow all the guidelines outlined in this document.

This document describes the style and formatting rules followed by the HCA Metadata Standard.

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

TBD

## Field formatting

### Required field attributes

The following attributes are required for each metadata field in an HCA metadata schema. 

1. **description:** A clear, concise statement of the what the metadata field is. The *description* value will appear in the metadata spreadsheet and be displayed in the Metadata Dictionary on the Data Portal. 

    Example:

        "email": {
            "description": "Email address for the individual.",
            ...
        }

    Each *description* should be one or more phrases or sentences and end in a full stop (period).

1. **type:** The JSON type of value required for the metadata field. The *type* value will be displayed in the Metadata Dictionary on the Data Portal.

    Example:
    
        "email": {
            "description": "Email address for the individual.",
            "type": "string",
            ...
        }
        
    Example valid *type* values include: string, number, boolean, array (when a field is an array of values), and object (when a field references another schema). The specification of valid JSON *type* values can be found [here](http://json-schema.org/latest/json-schema-validation.html#rfc.section.6.1.1). 

1. **example:** Directions for how to enter a valid value in the metadata field and/or an example valid value. The *example* value will appear in the metadata spreadsheet and be displayed in the Metadata Dictionary on the Data Portal. 

    Examples:
    
        "email": {
            "description": "Email address for the individual.",
            "type": "string",
            "example": "Enter a valid email address.",
            ...
        },

        "project_role": {
            "description": "Primary role of the individual in the project.",
            "type": "string",
            "example": "principal investigator",
            ...
        }

    Sometimes including an *example* value is not necessary, including:
    
    - When a field imports a core or module schema (*e.g.* `donor_organism.medical_history`) because the core and module schema fields will have their own examples
    - When including an example for the field could bias data contributors (*e.g.* `donor_organism.biomaterial_id`) 

1. **user-friendly:** A user-facing, readable term/phrase of what the metadata field is. The *user-friendly* value will appear in the metadata spreadsheet, be displayed in the Data Browser, and be displayed in the Metadata Dictionary on the Data Portal. 

    Example:
    
        "email": {
            "description": "Email address for the individual.",
            "type": "string",
            "example": "Enter a valid email address.",
            "user_friendly": "Email address",
            ...
        }

    Including *user-friendly* values for metadata fields has many advantages, including: 
    
    1. Unlike the actual metadata field name, the *user-friendly* value can contain punctuation, spaces, capitalization, and other basic formatting to make the interpretation of the field easier for data contributors and consumers.
    1. Changing a *user-friendly* value is considered a patch change to the schema version and is thus easier and simpler to implement than changing a metadata field name (which is a major change to the schema version).
    1. The *user-friendly* values can be templated to allow concatenation of the schema name to the field name for improved clarity. For example, if the *user-friendly* value of the `biomaterial_id` field is set to "${schema} ID", then `donor_organism.biomaterial_id` will render as "Donor organism ID" while `cell_line.biomaterial_id` will render as "Cell line ID".

### Conditional required field attributes

1. **$ref:** The relative path to a core, module, or ontology schema which is imported by the metadata field. This attribute is required when a field imports a module, core, or ontology schema. The *$ref* value is not displayed to users outside of the JSON schema itself and should always be used with `"type": "object"`.

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
            "description": "The unit in which age is expressed.",
            "type": "object",
            "$ref": "module/ontology/time_unit_ontology.json",
            ...
        }

1. **format:** A JSON-defined format that the value supplied to the metadata field should follow. This attribute is required when a field should follow and validate against a standard JSON format. The *format* value is not displayed to users outside of the JSON schema itself.

    Example:
    
        "email": {
            "description": "Email address for the individual.",
            "type": "string",
            "example": "Enter a valid email address.",
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
            "example": "Should be one of male, female, mixed, or unknown."
            "enum": [
                "female", 
                "male", 
                "mixed", 
                "unknown"
            ],
            "user_friendly": "Biological sex",
            ...
        },
        "project_role": {
            "description": "Primary role of the individual in the project.",
            "type": "string",
            "example": "principal investigator",
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
            "user_friendly": "Project role",
            ...
        }

    If the *enum* list is short enough (5 or fewer values), the list of valid values can be included in the *example* attribute (*e.g.* the `biological_sex` enum). If the *enum* list is too long to comfortably fit in the *example* attribute, a single valid value can be listed instead (*e.g.* the `project_role` enum).
    
    Creating an ontology module for a metadata field is preferred over maintaining an *enum* list.

### Optional field attributes

1. **pattern:** A regular expression that the metadata field value must follow. The *pattern* value is not displayed to users outside of the JSON schema itself, but the *example* attribute can describe what pattern the value should follow.

    Example:
    
        "insdc_project": {
            "description": "An INSDC (International Nucleotide Sequence Database Collaboration) project accession, if data has already been submitted to the DDBJ, EMBL-EBI, or NCBI.",
            "type": "string",
            "example": "Must start with DRP, ERP, or SRP.",
            "pattern": "^[D|E|S]RP[0-9]+$",
            "user_friendly": "INSDC project accession"
        }

## General rules

### Field naming conventions

1. Field names should be all lower case and snake_case.

        example_field_name

1. Short, meaningful field names are preferred over longer, vaguer field names. 

1. The same field name should not appear within the same or across multiple schemas.

1. If similar field names are needed, prepend the field names with context to differentiate them.

        umi_barcode and cell_barcode

1. If a number field requires a corresponding unit, append `_unit` to the number field name for the unit field name.

        organism_age and organism_age_unit

### Tone and voice

1. Make a statement, not a demand. For example:

    Use

        "description": "Age of the donor."
    
    not
    
        "description": "Enter the age of the donor."
    
1. Be concise instead of verbose. For example:

    Use
    
        "description": "Phone number of the individual or their lab."
    
    not
    
        "description": "Please include the phone number of the individual or the phone number of the individual's lab."

1. Use a formal writing voice. Avoid first-person pronouns, using "you", contractions, and slang. For example:

    Use

        "description": "Email address for the individual."

    not 
    
        "description": "Your email address."   

### 
