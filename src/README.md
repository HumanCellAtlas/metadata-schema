# The Human Cell Atlas Metadata Standards: Scripts

This directory contains useful scripts related to exploring the HCA metadata schemas.

### schemas_are_valid_json.py

This script tests whether each JSON schema in `json_schema/` directory is a valid JSON schema. This script is automatically run as part of Travis CI testing.

Please note that until jsonschema v3 goes into proper release, you will need to run `pip install jsonschema==3.0.0a5` for this script to work

