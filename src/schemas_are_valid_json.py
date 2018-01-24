from schema_test_suite import get_validator
import glob

"""
schemas_are_valid_json: 
This code tests whether JSON schemas that are in the json_schema/* folders
are valid JSON schema.
"""

schemas = glob.glob('../json_schema/*/' + "*.json")
schemas.extend(glob.glob('../json_schema/*/*/' + "*.json"))
schemas.extend(glob.glob('../json_schema/*/*/*/' + "*.json"))
# print(len(schemas))

for s in schemas:
    print("Checking whether %s is a valid json schema" % s)
    get_validator(s)

