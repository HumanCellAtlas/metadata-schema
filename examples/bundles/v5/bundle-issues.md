# Errors in Bundles

## Project
    VALID!
    
## Biomaterial Bundle
```
String 'https://schema.humancellatlas.org/type/biomaterial/5.0.0/donor_organism' does not match regex pattern 'https://schema.humancellatlas.org/type/biomaterial/v[0-9]{1,}.[0-9]{1,}.[0-9]{1,}/cell_line'.
Schema path:
https://schema.humancellatlas.org/type/biomaterial/5.0.0/cell_line#/properties/describedBy/pattern
```
The schema: https://schema.humancellatlas.org/type/biomaterial/5.0.0/cell_line

Contains a v in the regex for version number

```
"describedBy":  {
    "description": "The URL reference to the schema.",
    "type": "string",
    "pattern" : "https://schema.humancellatlas.org/type/biomaterial/v[0-9]{1,}.[0-9]{1,}.[0-9]{1,}/cell_line"
}
```

### donor_organism
Schema seems to expect more fields than are in the JSON likely ontology fields

### specimen_from_organism
Ontology fields are not being created correctly

## Protocol Bundle
Content does not seem to be referencing the correct schemas

## Process Bundle
As with protocol the schema types of the content seem unexpected. This may be to incorrect references in the content.

schema_type is wrong in several places referring in the specific type and not the generic type

## File Bundle
Number are being converted to floating point not integers

Link elements added unexpectedly
```
"biomaterial_id": "Q4_DEMO-sample_SAMN02797092",
"sequencing_process_id": "assay_1"
```


