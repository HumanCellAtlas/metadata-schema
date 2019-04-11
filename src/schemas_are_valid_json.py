import os
import json
from jsonschema import Draft4Validator
from jsonschema import RefResolver, SchemaError

"""
schemas_are_valid_json: 
This code tests whether JSON schemas that are in the json_schema/*
directory are valid JSON schema.

NOTE: until jsonschema v3 goes into proper release, do `pip install jsonschema==3.0.0a5`

"""

def get_validator(filename, base_uri=''):
    """Load schema from JSON file;
    Check whether it's a valid schema;
    Return a Draft4Validator object.
    Optionally specify a base URI for relative path
    resolution of JSON pointers (This is especially useful
    for local resolution via base_uri of form file://{some_path}/)
    """

    schema = get_json_from_file(filename)
    try:
        # Check schema via class method call. Works, despite IDE complaining
        Draft4Validator.check_schema(schema)
        print("Schema %s is valid JSON" % filename)
    except SchemaError:
        raise
    if base_uri:
        resolver = RefResolver(base_uri=base_uri,
                               referrer=filename)
    else:
        resolver = None
    return Draft4Validator(schema=schema,
                           resolver=resolver)

def get_json_from_file(filename, warn = False):
    """Loads json from a file.
    Optionally specify warn = True to warn, rather than
    fail if file not found."""
    f = open(filename, 'r')
    return json.loads(f.read())


if __name__ == '__main__':
    schema_path = '../json_schema'

    schemas = [os.path.join(dirpath, f)
               for dirpath, dirnames, files in os.walk(schema_path)
               for f in files if f.endswith('.json')]

    print("Checking %d schemas" % len(schemas))

    for s in schemas:
        print('Checking %s' % s)
        get_validator(s)
