# Running scripts

## This directory contains some useful scripts related to exploring the HCA metadata schemas.

### json_to_spreadsheet_template.py

This script generates a custom Excel spreadsheet template based on the JSON schemas. Type schemas to include are indicated using `-t` and Module schemas to include are indicated using `-i`. Either user-friendly (`-u`) or schema field names (`-f`) can be used as column headers.

**Requirements**

- python3
- os,optparse,logging,openpyxl,requests,pprint,openpyxl.styles
- schema_test_suite.py

**Example usage**

Generate a spreadsheet for a 10x assay on samples from a live human donor with no medical history or family relationship info:
```
python3 json_to_spreadsheet_template \
-s "https://schema.humancellatlas.org/" \
-t "type/project/5.1.0/project,type/biomaterial/5.1.0/donor_organism,type/biomaterial/5.1.0/specimen_from_organism,type/biomaterial/5.1.0/cell_suspension,type/process/biomaterial_collection/5.1.0/collection_process,type/process/biomaterial_collection/5.1.0/dissociation_process,type/process/biomaterial_collection/5.1.0/enrichment_process,type/process/sequencing/5.1.0/library_preparation_process,type/process/sequencing/5.1.0/sequencing_process,type/file/5.1.0/sequence_file,type/protocol/5.1.0/protocol" \
-i "module/project/5.1.0/contact,module/project/5.1.0/publication,module/biomaterial/5.1.0/cell_morphology,module/biomaterial/5.1.0/homo_sapiens_specific,module/biomaterial/5.1.0/state_of_specimen,module/process/sequencing/5.1.0/barcode,module/process/5.1.0/purchased_reagents" \
-o "spreadsheet_test.xlsx" \
-r  -u
```

### schemas_are_valid_json.py

This script tests whether each JSON schema in `json_schema/` directory is a valid JSON schema. This script is automatically run as part of Travis CI testing.

### json_examples_validate_against_schema.py

This script tests whether each JSON file in `schema_test_files/` directory validates against its corresponding JSON schema. This test includes intended failures and is automatically run as part of Travis CI testing.