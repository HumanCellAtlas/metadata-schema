# The Human Cell Atlas: Metadata Schema Style and Formatting Guide

## Table of Contents
- [Introduction](#introduction)
- [Schema model](#schema-model)
- [Schema style and formatting](#schema-style-and-formatting)
- [Field style and formatting](#field-style-and-formatting)
- [General rules](#general-rules)
- [The schema linter](#schema-linter)

## Introduction

>**DISCLAIMER:** At this time, the HCA Metadata Standard development team is actively working towards adhering to this style and formatting guide. In some cases, the standard might not yet follow all the guidelines outlined in this document. Your patience is appreciated!

This document describes the style and formatting rules followed by the HCA Metadata Standard for JSON schemas and fields. The goals of the Metadata Standard are to improve the accessibility, (re-)usability, and quality of data submitted to the HCA. In order to develop a high-quality, robust Metadata Standard, we propose the following guidelines and aim to adhere to them as the standard evolves and adapts to changing technologies. 

**What is in this document**
- General style guidelines for naming and formatting for metadata schemas and fields
- Rationale for why the guidelines were chosen

**Who should be reading this document?**
- HCA DCP developers
- Anyone reporting a bug in the schema
- Members of external projects seeking alignment with HCA metadata standards

**What *isn't* in this document?**
- Directions for [requesting or suggesting changes](contributing.md) to the metadata schema
- Explanation of [how fields are determined to be core, type, or module fields](structure.md) (TBD)
- Discussion of [reasons and rationale for implementation and design choices](rationale.md) for the metadata standard

## Schema model

The JSON format that is the canonical representation of the HCA Metadata Standard is a programming language-neutral, persistent method of storing data structures. See [ECMA-404 The JSON Data Interchange Standard](http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf) specification for technical details of the format. JSON objects are analogous to C structs, objects in JAVA and Python, and to an extent, SQL tables. The design of JSON metadata objects follows the common approaches used in designing computational data structures for programmers. The schema is used to describe the contents of the JSON data objects for both programmatic access and human understanding.

The JSON schemas that make up the HCA Metadata Standard are publicly developed and maintained in GitHub [HumanCellAtlas/metadata-schema](https://github.com/HumanCellAtlas/metadata-schema). The official published and released JSON schemas are hosted at [schema.humancellatlas.org](https://schema.humancellatlas.org/).

As implemented for the HCA Metadata Standard, each JSON schema contains a set of related fields (also called properties). For example, the `cell_line.json` schema contains fields specific to describing cell lines. The following sections describe style and formatting rules followed by HCA metadata schemas and fields.

## Schema style and formatting

The following attributes are required for each metadata schema in the HCA metadata standard. 

1. **$schema:** The JSON draft version being used.

    Example:
    
        {
            "$schema": "http://json-schema.org/draft-07/schema#",
            ...
        }

1. **description:** A clear, concise description of the schema. 

    Example:
    
        {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "description": "Information about an organoid biomaterial.",
            ...
        }

1. **additionalProperties:** Whether additional fields not in the schema will be allowed. The *additionalProperties* attribute should always be set to `false`. Currently, user-supplied fields are not accepted without consultation. The metadata team actively encourages data contributors who want new fields to contact them so the new fields can be added to the schema following the process for requesting updates to the Metadata Standard to include new fields is outlined in our contributing documentation [here](contributing.md#requesting-or-suggesting-changes-to-the-metadata-schema).

    Example:
    
        {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "description": "Information about an organoid biomaterial.",
            "additionalProperties": false,
            ...
        }

1. **required:** An array indicating which fields in the schema are required. If no fields are required, omit this attribute. Fields are determined to be required if they are necessary to enable downstream analysis and visualization.

    Example:
    
        {
            "$schema": "http://json-schema.org/draft-07/schema#",
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

1. **title:** A title for the schema. The *title* is the user-friendly name of the schema which should be in sentence case. This attribute is displayed in the metadata spreadsheet and the Data Browser.

    Example:
    
        {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "description": "Information about an organoid biomaterial.",
            "additionalProperties": false,
            "required": [
                "describedBy",
                "schema_type",
                "biomaterial_core",
                "model_for_organ"
            ],
            "title": "Organoid",
            ...
        }

1. **name:** A programmatic, unqualified name for the schema. The *name* is the name of the schema which should be in all lowercase and snake_case. This attribute is used by the DCP software to identify the schema, and the *name* should match the filename of the schema absent the `.json` file extension.

    Example:
    
        {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "description": "Information about an organoid biomaterial.",
            "additionalProperties": false,
            "required": [
                "describedBy",
                "schema_type",
                "biomaterial_core",
                "model_for_organ"
            ],
            "title": "Organoid",
            "name": "organoid",
            ...
        }

1. **type** and **properties:** The *type* of the schema (should always be `object`) followed by the metadata fields (`properties`).  

    Example:
    
        {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "description": "Information about an organoid biomaterial.",
            "additionalProperties": false,
            "required": [
                "describedBy",
                "schema_type",
                "biomaterial_core",
                "model_for_organ"
            ],
            "title": "Organoid",
            "name": "organoid",
            "type": "object",
            "properties": {
                ...
            }
        }

1. **$id:** A persistent URI for the schema. The `$id` attribute is **not** included in JSON schemas in GitHub. Instead, it is inserted automatically at the time schemas are published to the HCA Metadata Standard at [schema.humancellatlas.org](https://schema.humancellatlas.org/).

    Example:
    
    *GitHub*
    
        {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "description": "Information about an organoid biomaterial.",
            ...
        }
    
    *schema.humancellatlas.org*
    
        {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "$id": "http://schema.humancellatlas.org/type/biomaterial/8.3.4/organoid",
            "description": "Information about an organoid biomaterial.",
            ...
        }
        
    The `$id` attribute is a resolvable URL which points to the published schema hosted by the Human Cell Atlas. This attribute is inserted at build time as it must contain the version of the schema which is not defined within the schema document itself on GitHub. The list of latest schema versions is maintained in the `versions.json` file in GitHub, separate from the JSON schema documents themselves, in order to enable unit testing. The specification for using the JSON `$id` keyword can be found [here](http://json-schema.org/latest/json-schema-core.html#rfc.section.8.2)

## Field style and formatting

Naming fields in data structures is challenging because of the desire to optimize both clarity to avoid ambiguity and brevity to avoid cumbersome code. To help chose field names that are both clear and brief, it is vital to consider the context in which field names are referred. In structured programming languages, an *unqualified* field name is a name local to its context (in this case, to its schema). When combined with its context (in this case, with its schema name), an unqualified field name becomes a *qualified* field name, which is usually expressed as a concatenation of the context name and the unqualified field name. For example:
    
> HCA unqualified field name: `diseases`
>
> HCA qualified field name: `donor_organism.diseases`\
> HCA qualified field name: `specimen_from_organism.diseases`

In the HCA, qualified field names are used by the Ingestion Service to convert metadata spreadsheets to JSON, by the Data Store Service (DSS) to index JSON documents, and by the Secondary Analysis Service and Data Browser to query for metadata in the DSS. Unqualified field names are not used in isolation, although corresponding *user-friendly* names (see below) are used in the metadata spreadsheet, the Data Browser, and the Metadata Dictionary on the Data Portal. 

Some principles the HCA Metadata Standard follows regarding field and schema names are:

1. *Field and schema names are programming constructs, not GUI constructs.* Field and schema names are only intended for use by programmers, including those writing textual queries. Attempting to have a field name that is both a good GUI name and a good programmatic name makes the naming problem more difficult. For example, field name changes to make a GUI clearer potentially creates breaking changes for code accessing the data structures. Additionally, GUI implementation from field and schemas names is difficult as different labels for data are often needed depending on how data are being presented. Therefore, field and schemas names should be used as keys to look up natural language terms (*e.g.* to look up schema titles and user-friendly field names).

1. *Unqualified field names need to be unique within a schema, but do not need to be globally unique among all schemas.* Within a single JSON schema, no two field names should be identical. However, the same field name can exist in two different schemas, as their qualified names will be different. For example, the field name `diseases` can exist in both the `donor_organism.json` and `specimen_from_organism.json` schemas because the qualified field names are `donor_organism.diseases` and `specimen_from_organism.diseases`, respectively.

1. *Qualified field names need to be unique among all schemas.* Fully qualified field names need to be globally unique across the HCA Metadata Standard. Qualified field names are used by multiple services, thus they need to be globally unique so that only a single field is accessed/returned for a given qualified field name request.

1. *Unqualified field names should not contain context.* Unqualified field names do not stand alone, meaning they are not accessed or used outside of their context (*i.e.* their schema). Therefore, additional context should be removed from unqualified field names unless there is justification for including it. For example:

    > Unqualified field name for media in a differentiation protocol:\
    > Correct: `media`\
    > Incorrect: `differentiation_media`
    >    
    > Corresponding qualified field name:\
    > Correct: `differentiation_protocol.media`\
    > Incorrect: `differentiation_protocol.differentiation_media`
    
    Potential caveats for including context in an unqualified field name include:
    
    1. There are two or more similar field names in a single schema and including context helps disambiguate between them (*e.g.* `organism_age` and `gestational_age` in the `donor_organism` schema).
    1. The field name is generally ambiguous or overloaded and including context helps reduce confusion about the field's usage (*e.g.* `type` fields in biomaterial schemas or `method` fields in protocol schemas).

1. *Field names should only include `id` if the values are guaranteed to be globally unique.* There are two contexts in which metadata values are guaranteed to be unique: (1) globally and (2) within a submission in the Ingestion Service. For fields whose values are guaranteed to be globally unique for the entity/concept they represent, the field name should contain `_id`. For example, an NCBI Taxon ID (`ncbi_taxon_id`) only represents one species, and an ORCID ID (`orcid_id`) only represents one person. For fields whose values are guaranteed to be unique within a submission in the Ingestion Service but not globally unique, the field name must **not** contain `_id`. Instead, these fields can use `_label` (or another reasonable alternative). For example, a Biomaterial label (`biomaterial_label`) value must be unique within a submission (in order to generate links between the biomaterials), but the same value could exist in another submission resulting in the same value representing two distinct biomaterials. For `_id` and `_label` fields, the scope of the uniqueness should be indicated in the field description or guidelines attribute.

The section [Field name conventions](#field-name-conventions) provides guidelines to use when defining names.

### Required field attributes

The following attributes are required for each metadata field in an HCA metadata schema. 

1. **description:** A clear, concise statement of the what the metadata field is. The *description* value will appear in the metadata spreadsheet and be displayed in the Metadata Dictionary on the Data Portal. 

    Example:

        "project_role": {
            "description": "Primary role of the individual in the project.",
            ...
        }

    Each *description* should be 1 phrase and end in a full stop (period). An additional phrase or sentence is allowed if required for improved clarity of the description.

1. **type:** The JSON type of value required for the metadata field. The *type* value will be displayed in the Metadata Dictionary on the Data Portal.

    Example:
    
        "project_role": {
            "description": "Primary role of the individual in the project.",
            "type": "string",
            ...
        }
        
    Example valid *type* values include: string, number, boolean, array (when a field is an array of values), and object (when a field references another schema). The specification of valid JSON *type* values can be found [here](http://json-schema.org/latest/json-schema-validation.html#rfc.section.6.1.1). 

1. **user-friendly:** A user-facing, readable term or phrase for the metadata field name. The *user-friendly* value will appear in the metadata spreadsheet, be displayed in the Data Browser, and be displayed in the Metadata Dictionary on the Data Portal. 

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
        
        Programmatic: paired_end
        User-friendly: Paired-end
        
    Having *user-friendly* values for metadata fields has many advantages, including: 
    
    1. Unlike the programmatic metadata field name, the *user-friendly* value can contain punctuation, spaces, capitalization, and other basic formatting to make the interpretation of the field easier for data contributors and consumers.
    1. Changing a *user-friendly* value is a patch change to the schema version and is thus easier and simpler to implement than changing a field name (which is a major change to the schema version).
    1. A *user-friendly* value can be templated to allow for custom displays. For example, appending a schema name to a *user-friendly* name can improve clarity: if the *user-friendly* value of the `biomaterial_id` field is set to `"${schema} ID"`, then `donor_organism.biomaterial_id` will render as "Donor organism ID" while `cell_line.biomaterial_id` will render as "Cell line ID".
    
### Conditional required field attributes

1. **example:** 1-2 example valid values for the metadata field, separated by a semicolon. This attribute is required for all fields except those that reference a core, module, or ontology schema and those for which providing an example might bias data contributors. The *example* value will appear in the metadata spreadsheet and be displayed in the Metadata Dictionary on the Data Portal. 

    Example:
    
        "project_role": {
            "description": "Primary role of the individual in the project.",
            "type": "string",
            "example": "principal investigator; clinician",
            ...
        }

    An *example* should **not** be provided when:
    
    - A field references a core or module schema, *e.g.* `donor_organism.medical_history`, because the fields in the imported schema will have their own example valid values.
    - A field references an ontology schema, *e.g.* `genus_species`, because the fields in the imported ontology schema will have their own example valid values.
    - An example for a field could bias data contributors, *e.g.* providing an example ID for a biomaterial in the `biomaterial_id` field.
    
    In general, fields should include two examples to highlight the range of possible valid values. In some cases, however, including two examples does not provide more clarity than including one example. For instance, the `cell_line.catalog_url` field takes a string representing the "supplier catalogue URL for the cell line". Including one example catalog URL for this field is sufficient to demonstrate what a valid value looks like, and including a second example would likely not improve clarity.   

    **Special case: Ontology examples**
    
    *Example* values can be supplied for fields that are governed by an ontology by including them in the ontology schema. The `text`, `ontology`, and `ontology_label` fields can all take *example* valid values.
    
    Example:
    
        module/ontology/species_ontology.json:
        
        "text": {
            "description": "The name of the species to which the organism belongs.",
            "type": "string",
            "example": "Human",
            ...
        },
        "ontology": {
            "description": "An ontology term identifier in the form prefix:accession",
            "type": "string",
            "example": "NCBITaxon:9606",
            ...
        },
        "ontology_label": {
            "description": "The preferred label for the ontology term referred to in the ontology field. This may differ from the user-supplied value in the text field.",
            "type": "string",
            "example": "Homo sapiens",
            ...
        }

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


1. **enum:** A defined list of valid values for the metadata field. This attribute is required when a field should be governed by a controlled vocabulary and an appropriate ontology is not available. The *enum* values currently are not displayed to users outside of the JSON schema, but in the future they will be shown in the metadata spreadsheet.

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
            "example": "principal investigator; clinician",
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

    If the *enum* list is short enough (5 or fewer values), the list of valid values should be included in the *example* attribute (*e.g.* the `biological_sex` enum) starting with the phrase "Should be one of:". If the *enum* list is too long to reasonably fit in the *example* attribute, one or two valid values should be listed separated by a semicolon (*e.g.* the `project_role` enum).
    
    Creating an ontology module for a metadata field is preferred over maintaining an *enum* list. See the [Ontology versus enum for a controlled vocabulary](#ontology-or-enum) section below for more details.

### Optional field attributes

1. **guidelines:** Instructions for how to fill in a valid value for the metadata field. This attribute can be included on an as-needed basis when further clarification for how to fill in a metadata field would be helpful to data contributors. In otherwords, when the description and example attributes are not clear enough. The *guidelines* value will appear in the metadata spreadsheet. 

    Example:
    
        "address": {
            "description": "Street address where the individual works.",
            "type": "string",
            "example": "0000 Main Street, Nowheretown, MA, 12091",
            "guidelines": "Include street name and number, city, country division, and postal code.",
            "user_friendly": "Street address"
        }

1. **pattern:** A regular expression that the metadata field value must follow. The *pattern* value is not displayed to users outside of the JSON schema itself, but the *example* and *guidelines* attributes can demonstrate and describe what pattern the value should follow.

    Example:
    
        "insdc_project": {
            "description": "An International Nucleotide Sequence Database Collaboration (INSDC) project accession.",
            "type": "string",
            "pattern": "^[D|E|S]RP[0-9]+$",
            "example": "SRP000000",
            "guidelines": "Enter accession if project has been archived. Accession can be from the DDBJ, NCBI, or EMBL-EBI and must start with DRP, SRP, or ERP, respectively.",
            ...
        },

## General rules

### Spelling and grammer

1. Use American English spelling of words. *e.g.*: "meter" instead of "metre". This standard is in line with the HCA DCP.
1. Use Oxford comma in lists. Exception is when using a semi-colon to separate multiple example values in the *example* attribute.
1. Use present tense.

### Field name conventions

The following conventions should be followed when defining a new field name or suggesting changes to a current field name.

1. Field names should be all lowercase and snake_case.

    Example:

    `publication_doi`
    
    `plate_based_sequencing`

1. Field names should be as short as possible while still naturally readable, without attempting to be fully grammatically correct. They should be clear within their context and should not contain articles.

    Example:

    `paired_end` is preferred over `was_paired_end_sequencing_done` because it is shorter but still conveys full meaning.

    `funders` is preferred over `the_funders` because the grammatical determiner (`the`) does not improve clarity.
    
1. Field names should be plural if their values are arrays.

    Example:

    `children` is preferred if the field can indicate more than 1 child. 
    
    `child` is preferred if the field can only indicate 1 child.

1. If a number field requires a corresponding unit field, append `_unit` to the number field name to generate the unit field name.

    Example:

    `height` and `height_unit`

### Field description tone and voice

1. Make a statement instead of a demand. For example:

    Use

        "description": "Age of the donor."
    
    not
    
        "description": "Enter the age of the donor."
    
1. Be concise. For example:

    Use
    
        "description": "Phone number of the individual or their lab."
    
    not
    
        "description": "Please include the phone number of the individual or the phone number of the individual's lab."

1. Use a formal writing voice. Avoid first-person pronouns, using "you", contractions, and slang. For example:

    Use

        "description": "Email address for the individual."

    not 
    
        "description": "Your email address."

### Field example conventions

1. Include one or two examples per field, when appropriate ([see above](#conditional-required-field-attributes)). Two examples - separated by a semicolon - should be used when a range of values are valid to illustrate potential breadth of values. A single example should be used otherwise to illustrate general usage of the field. For example:

    Use
    
        "example": "bone squamous cell carcinoma; type 2 diabetes mellitus"
        
    not
    
        "example": "bone squamous cell carcinoma"

    Use
    
        "example": "0000 Main Street, Nowheretown, MA, 12091"
        
    not
    
        "example": "0000 Main Street, Nowheretown, MA, 12091; 9999 Main Avenue, Noplaceville, CA, 91120"

1. Do not include instructions for entering a value. Instructions should be entered in the "guidelines" attribute. For example: 

    Use
    
        "insdc_study": {
            "guidelines": "Accession must start with PRJE, PRJN, or PRJD.",
            "example": "PRJNA000000",
            ...
        },
        
    not
    
        "insdc_study": {
            "example": "Accession must start with PRJE, PRJN, or PRJD. e.g. PRJNA000000",
            ...
        },

### Ontology vs. enum vs. free text

Metadata fields will benefit from using a controlled vocabulary to restrict valid values. Such restrictions enable data consumers to filter, search, or order fields based on values of interest without having to account for different values that mean the same thing. For example, the `genus_species` field benefits from using a controlled vocabulary so that all human data is annotated with `"genus_species": "Homo sapiens"` instead of with other possible values such as "Human" (colloquial term), "homo sapiens" (different case), "Homo sapeins" (misspelling), or "Hs" (shorthand). 

The HCA Metadata Standard is committed to using controlled vocabularies - in the form of externally maintained **ontologies** and JSON **enums** - to standardize valid values for metadata fields. In most cases, using an ontology is preferred over using a JSON *enum* provided that an appropriate ontology with good or full coverage is available. 

The advantages of using an HCA ontology over an *enum* include:

1. Ontology can be adapted to changing needs without requiring the metadata schema to change.
1. Displaying, filtering, and sorting in the HCA Data Portal becomes easier.
1. Annotating HCA metadata with ontology terms improves the semantic interoperability of the data.

Instances when an *enum* is preferred over an ontology include:

1. The list of valid values is short and unlikely to change. For example, the valid values for the `donor_organism.is_living` field will always be "yes", "no", or "unknown".
1. The list of valid values is short but too diverse to be organized into a meaningful ontology, or while awaiting the development of an appropriate ontology or ontology branch. If in doubt, check with an HCA ontologist.

Finally, if the list of valid values for a field is very long - for example more than ten valid values - and does not have an appropriate ontology, a free text field is preferred as it means data submitters will not need to constantly validate against the enum (which can be frustrating).


## Schema linter
The schema linter uses a python script to ensure the rules of the schema style guide are followed. These rules are labeled as `must` (Will produce an error if not followed) or `should` (Will throw a warning if not followed). The script, [`schema_linter.py`](https://github.com/HumanCellAtlas/metadata-schema/blob/master/src/schema_linter.py), that performs these checks is in the [src folder](https://github.com/HumanCellAtlas/metadata-schema/blob/master/src/).

Below is a list of rules that are currently tested:

||**Must**|**Should**|
:------|:------|:------|
**Schema check**|All schema fields must be part of a list of allowed schema fields|Description of schema should be a sentence
 ||All required schema fields must be present in the schema|Schema titles should be sentence-case
 ||Schema must not have additional properties| 
 ||Schema must be set to draft 07| 
 ||Schema filename must match the name of the schema provided in the URL| 
 ||Schema filename must match schema name field| 
 ||Schema type must be set to object| | 
 ||All required fields must actually be in the schema| | 
 ||||
**Property check**|Properties `describedBy` and `schema_version` must be present in each schema|description should be a sentence
 ||Properties `text`,  `ontology` and `ontology_label` must be present in each ontology schema|guidelines should be a sentence
 ||All type schemas must have corresponding `_core` property|Property should contain example attribute| 
 ||Property name must contain only lowercase letters, numbers and underscores|`_unit` properties should have matching property without `_unit`
 ||Property must contain description attribute|
 ||Property must contain user-friendly attribute (Only user-supplied fields)| 
 ||Property must contain type attribute| 
 ||type attribute must be set to one of the valid JSON types| 
 ||Property of type array must contain the attribute items| 
 ||items must have either type or `$ref` attribute| 
 ||Property of type object must contains the attribute $ref| 
 ||format must be a valid JSON format| 
 ||pattern must be a valid regex| 
 ||example values must match regex pattern| 
 ||All `$ref` referenced schemas must exist| 
 ||||
**Ontology check**|Ontology field must have graph\_restriction property that is an object| 
 ||`graph_restriction` property must contain all required attributes| 
 ||Attributes for `graph_restriction` must be one of acceptable values| 
 ||`graph_restriction` 'direct' attribute must be `False`| 
 ||`graph_restriction` 'include\_self' attribute must be `False` or `True`| 
 ||`graph_restriction` 'relations' attribute must be a list| 
 ||`graph_restriction` 'classes' attribute must be a list| 
 ||`graph_restriction` 'ontologies' attribute must be a list| 
 ||`graph_restriction` 'relations' must at least contain item `rdfs:subClassOf`| 
 ||`graph_restriction` 'ontologies' must contain ontologies that are valid within the HCA ontology space| 
 ||`graph_restriction` 'classes' must contain only ontology classes that are valid in the HCA ontology space| 
 ||All property attributes must be in the allowed list of property attributes| 