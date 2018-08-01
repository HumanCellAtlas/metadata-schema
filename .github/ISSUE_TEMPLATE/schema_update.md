---
name: Schema update
about: Create a request for an update to the metadata schema.
labels: content
---

**For which schema is a change/update being suggested?**

<!--Please indicate the name of the schema for which a change/update is being requested. If a new schema is being requested, please suggest a name for the schema.-->

*e.g.*: I would like to request an update the the `cell_line.json` schema.

**What should the change/update be?**

<!-- Please describe the change you are requesting. Be as descriptive as possible. Possible requests can include, but aren't limited to:

* Updates to field names
* Updates to field or schema descriptions
* Updates to field examples or user-friendly names
* New schemas or fields
* Updates to repo documentation or examples-->

*e.g.*: The `cell_line.json` schema description needs to be updated to reflect that the cell line schema is for describing both cell lines and cultures, and all of primary, immortalized, etc. of those types.

**What new field(s) need to be changed/added?**

<!-- For each **new** field requested, please provide the following:

* Field name: A suggested name for the new field.
* Field description: A short, but clear, description for the new field.
* Required: Whether the field should be required in the schema (yes, no)
* Example: An example value that would satisfy this field.
* CV or enum: Whether this field should be governed by a CV or an ontology. If yes, what should the CV/ontology be?-->

*e.g.*:
* Field name: random_integer
* Field description: Any random integer.
* Required: yes
* Example: 42
* CV or enum: no

**Why is the change requested?**

<!-- Please provide the motivation for the requested change/update. Please cite user feedback or results of UX sessions if possible.-->

*e.g.*: Some scientists use the language "cell culture" to describe a biomaterial that will be modelled with the cell line schema. The name of the schema (cell_line) is less important than having the description be accurate, as the description will be what is displayed to users via the UI and other guides/documentation.

