from schema_test_suite import get_json_from_file
import logging
import os


allowed_root_level_keywords = ['$schema', 'description', 'additionalProperties', 'required', 'title', 'name', 'type', 'properties', 'definitions']

required_root_level_keywords = ['$schema', 'description', 'additionalProperties', 'title', 'name', 'type', 'properties']

essential_properties = ['describedBy', 'schema_version']
# , 'schema_type', 'provenance']

property_keywords = ['description', 'type', 'pattern', 'example', 'enum', '$ref', 'user_friendly', 'items', 'guidelines', 'format', 'comment', 'maximum', 'minimum']

ontology_keywords = ['graph_restriction', 'ontologies', 'classes', 'relations', 'direct', 'include_self']


class SchemaLinter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def lintSchema(self, path):
        schema = get_json_from_file(path)
        schema_filename = path.split("/")[-1].split(".")[0]

        # Check that all root level fields in the schema are part of the list of allowed root level fields
        for key in schema.keys():
            if key not in allowed_root_level_keywords:
                print("Root level field `" + key + "` in schema " + path + " not part of allowed root level properties")

        # Check that all required root level fields are present in the schema
        for prop in required_root_level_keywords:
            if prop not in schema.keys():
                print("Schema " + path + " is missing required root level field `" + prop + "`")

        properties = schema['properties']

        # Check that essential properties `describedBy` and `schema_version` are present
        for ep in essential_properties:
            if ep not in properties:
                print("Schema " + path + " is missing required property `" + ep + "`")

        for property in properties:
            for kw in properties[property].keys():
                if property == 'ontology' and kw == 'graph_restriction':
                    nested_keywords = properties[property][kw]
                    for nkw in nested_keywords.keys():
                        if nkw not in ontology_keywords:
                            print("Keyword `" + nkw + "` is not in the list of acceptable ontology keyword properties")
                elif kw not in property_keywords:
                    print("Keyword `" + kw + "` in property `" + property + "` is not in the list of acceptable keyword properties")

                if isinstance(properties[property][kw], dict) and property != 'ontology':
                    for nkw in properties[property][kw].keys():
                        if nkw not in property_keywords:
                            print(
                                "Keyword `" + nkw + "` in property `" + property + "` is not in the list of acceptable keyword properties")

        # Check that additionalProperties is set to false
        if "additionalProperties" in schema and schema['additionalProperties'] == True:
            print("Schema " + path + " should not allow additional properties")

        # Check that $schema is set to draft-07
        if "$schema" in schema and schema['$schema'] != "http://json-schema.org/draft-07/schema#":
            print("Schema " + path + " must have $schema set to http://json-schema.org/draft-07/schema#")

        # Check that the name of the schema in the describedBy URL is set to the schema filename
        if properties['describedBy']['pattern'].split("/")[-1] != schema_filename:
            print("Schema " + path + " the end of the describedBy URL (" + properties['describedBy']['pattern'].split("/")[-1] + ") must match the schema filename (" + schema_filename + ")")

        # Check that the schema name attribute is set to the schema filename
        if "name" in schema and schema['name'] != schema_filename:
            print("Schema " + path + " the schema name attribute (" + schema['name'] + ") must match the schema filename (" + schema_filename + ")")

        # Check that schema type is set to object
        if "type" in schema and schema['type'] != "object":
            print("Schema " + path + " must have type set to object")

        # Check that all required fields are actually in the schema
        if "required" in schema:
            for req_prop in schema["required"]:
                if req_prop not in properties:
                    print("Property `" + req_prop + "` is listed as required in schema " + path + " but is undefined")


if __name__ == '__main__':
    schema_path = '../json_schema'

    linter = SchemaLinter()

    schemas = [os.path.join(dirpath, f)
               for dirpath, dirnames, files in os.walk(schema_path)
               for f in files if f.endswith('.json')]

    print("Checking %d schemas" % len(schemas))

    for s in schemas:
        if 'versions.json' not in s:
            # print('Checking %s' % s)
            linter.lintSchema(s)
