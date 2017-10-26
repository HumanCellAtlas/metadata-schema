import json
from jsonschema import Draft4Validator, RefResolver, SchemaError
import warnings
import subprocess
import os


def get_json_from_file(filename):
    f = open(filename, 'r')
    return json.loads(f.read())

def get_validator(filename, base_uri = ''):
    """Load schema from JSON file;
    Check whether it's a valid schema;
    Return a Draft4Validator object.
    Optionally specify a base URI for relative path
    resolution of JSON pointers. This is especially useful
    for local resolution via base_uri of form file://{some_path}/
    """
    schema = get_json_from_file(filename)
    try:
        # Check schema via class method call.
        Draft4Validator.check_schema(schema)  # IDE complaining but seems to work.
        print("Schema %s is valid" % filename)
    except SchemaError: 
        raise    
    if base_uri:
        resolver = RefResolver(base_uri = base_uri, 
                                  referrer = filename)
    else:
        resolver = None
    return Draft4Validator(schema = schema, 
                            resolver = resolver)

def validate(validator, instance):
    """Validate an instance of a schema and report errors."""
    if validator.is_valid(instance):
        print("Passes")
        return True
    else:
        es = validator.iter_errors(instance)
        recurse_through_errors(es)
        return False

def recurse_through_errors(es, level = 0):
    """Recurse through errors posting message 
    and schema path until context is empty"""
    # Assuming blank context is a sufficient escape clause here.
    for e in es:
        warnings.warn("***"*level + "subschema level " + str(level) + "\t".join([e.message, 
                                     "Path to error:" +  str(e.absolute_schema_path)]) + "\n")
        if e.context:
            level += 1
            recurse_through_errors(e.context, level = level)
            

def test_local(path_to_schema_dir, schema_file, instance_file):
    """Tests a single instance against a single schema.
    Assumes all schema files in single dir.
    path_to_schema_dir may be relative.
    schema_file and instance_file may be local to schema dir or full path."""
    os.chdir(path_to_schema_dir)
    pwd = subprocess.check_output('pwd').decode("utf-8").rstrip()
    base_uri = "file://" + pwd + "/"
    sv = get_validator(schema_file, base_uri)
    i = get_json_from_file(instance_file)
    print("Testing: %s" % instance_file)
    validate(sv, i)
    
