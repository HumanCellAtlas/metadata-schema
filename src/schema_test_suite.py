import json
from jsonschema import Draft4Validator, RefResolver, SchemaError
import warnings

def get_json_from_file(filename):
    f = open(filename, 'r')
    return json.loads(f.read())

def get_validator(filename, base_uri = ''):
    schema = get_json_from_file(filename)
    try:
        Draft4Validator.check_schema(schema)  # Not clear what's wrong here. Works in notebook.
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
    if validator.is_valid(instance):
        print("Passes")
        return True
    else:
        es = validator.iter_errors(instance)
        for e in es:
            warnings.warn(str("\n".join([e.message, str(e.instance)])))
        return False
