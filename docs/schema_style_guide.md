# The Human Cell Atlas: Metadata Schema Style Guide

## Table of Contents
- [Introduction](#introduction)
- [Schema formatting](#schema-formatting)
- [Field formatting](#field-formatting)
- [General rules](#general-rules)

## Introduction

This document describes the style and formatting rules followed when evolving the metadata standard.

**What is in this document**
- General style guidelines and formatting for metadata schema and fields

**Who should be reading this document?**
- HCA DCP internal developers
- Anyone reporting a bug in the schema
- Members of external projects seeking alignment with HCA metadata standards

**What *isn't* in this document?**
- Directions for [requesting or suggesting changes](metadata-schema/docs/contributing.md) to the metadata schema
- Directions for [making changes to metadata schemas](metadata-schema/docs/committers.md)

## Schema formatting


## Field formatting

### Required field attributes

The following attributes are required for each field in a metadata schema. 

1. **description:** A clear, concise statement of the what the metadata field is. The *description* value will appear in the metadata spreadsheet and be displayed in the Metadata Dictionary on the Data Portal. 

    Example:

        "email": {
            "description": "Email address for the individual.",
            ...
        },

1. **type:** The JSON type of value required for the metadata field. The *type* value will be displayed in the Metadata Dictionary on the Data Portal.

    Example:
    
        "email": {
            "description": "Email address for the individual.",
            "type": "string",
            ...
        },
        
    Example valid *type* values include: `string`, `number`, `boolean`, `array`, `object`. A more comprehensive list of JSON-valid *type* values can be found here. 

1. **example:** Directions for how to enter a valid value in the metadata field followed by an example valid value, if able. The `example` value will appear in the metadata spreadsheet and be displayed in the Metadata Dictionary on the Data Portal. 

    Example:
    
        "email": {
            "description": "Email address for the individual.",
            "type": "string",
            "example": "Enter a valid email address.",
            ...
        },

    Sometimes including an example value is not necessary. Instances of this include:
    
    - Fields that import core or module schemas (e.g. `donor_organism.medical_history`)
    - Fields for which including an example could bias contributors (e.g. `donor_organism.biomaterial_id`)

1. **user-friendly:** A user-facing, readable term/phrase of what the metadata field is. The `user-friendly` value will appear in the metadata spreadsheet, be displayed in the Data Browser, and be displayed in the Metadata Dictionary on the Data Portal. 

    Unlike the actual metadata field name, the `user-friendly` value can contain punctuation, spaces, capitalization, and other basic formatting to make the interpretation of the field easier to data contributors and consumers.

    Example:
    
        "email": {
            "description": "Email address for the individual.",
            "type": "string",
            "example": "Enter a valid email address.",
            "user_friendly": "Email address",
            ...
        },


### Conditional required field attributes

1. **$ref:** Relative path to schema which is imported by this metadata field. This attribute is required when a field imports a module, core, or ontology schema.

1. **format:** A JSON-defined format that the value supplied to the metadata field should follow.

    Example:
    
        "email": {
            "description": "Email address for the individual.",
            "type": "string",
            "example": "Enter a valid email address.",
            "user_friendly": "Email address",
            "format": "email"
        },


## General rules

### Tone

1. Avoid using "you" phrases (what is the name of this tone??). For example:

    Bad: `"description": "Your email address."`
    
    Good: `"description": "Email address for the individual."`

1. Avoid making demands. For example:

    Bad: `"description": "You need to include the age of the donor."`
    
    Good: `"description": "Age of the donor."`
    
1. Avoid using "please". For example:

    Bad: `"description": "Please include the phone number of the individual or their lab."`
    
    Good: `"description": "Phone number of the individual or their lab."`

### 
