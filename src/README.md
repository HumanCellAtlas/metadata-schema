# The Human Cell Atlas Metadata Standards: Scripts

This directory contains useful scripts related to exploring the HCA metadata schemas.

### schemas_are_valid_json.py

This script tests whether each JSON schema in `json_schema/` directory is a valid JSON schema. This script is automatically run as part of Travis CI testing.

Please note that until jsonschema v3 goes into proper release, you will need to run `pip install jsonschema==3.0.0a5` for this script to work

### human_readable_json.py

This script goes through all the core, module and type schemas in the `json_schema` directory and converts the properties into markdown tables for easier readability. The markdown documents are stored under `docs/jsonBrowser`.

This script runs automatically at every commit.


### release_prepare.py

This script prepares the metadata schema repo for a release by incrementing version numbers (via the `version_update.py` script), updating the change log file and inserting the appropriate version numbers for any new migrations into the `property_migrations.json` file.

This script should be run manually before every release.


### schema_linter.py

This script inspects every schema in the metadata repo and checks all schemas and properties to ensure that they conform to a set of rules defined in the [schema style guide](docs/schema_style_guide.md). Check failures are reported as either warnings or errors, depending on the severity of the mistake.

This script can be run as a standalone (and it should be considered good practice to do so!) but it is also integrated into the automatic Travis build.



### version_update.py

This script increments the version numbers of any schemas listed in the update_log.csv file by the increment type supplied with the schema. It also finds any schemas that reference the updated schemas and increments their version numbers appropriately.

This script can be run as a stand-alone but is normally run automatically as part of the release prep process.