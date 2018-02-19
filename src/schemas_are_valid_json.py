from schema_test_suite import get_validator
import os

"""
schemas_are_valid_json: 
This code tests whether JSON schemas that are in the json_schema/*
directory are valid JSON schema.
"""

schema_path = '../json_schema'

schemas = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(schema_path)
    for f in files if f.endswith('.json')]

print("Checking %d schemas" % len(schemas))

for s in schemas:
    print('Checking %s' % s)
    get_validator(s)
