# from schema_test_suite import get_json_from_file
import logging
import os
import re
import json
import sys

# Schema fields

required_schema_fields = ['$schema', 'description', 'additionalProperties', 'title', 'name', 'type', 'properties']

allowed_schema_fields = ['$schema', 'description', 'additionalProperties', 'required', 'title', 'name', 'type', 'properties', 'definitions']

# Properties

required_properties = ['describedBy', 'schema_version']

required_ontology_properties = ['text', 'ontology', 'ontology_label']

system_supplied_properties = ['describedBy', 'schema_version', 'schema_type', 'provenance']

# Exempt from needing examples because an example might bias what value a contributor supplies
example_exempt_properties = ['biomaterial_id', 'biomaterial_name', 'biomaterial_description', 'process_id', 'process_name', 'process_description', 'protocol_id', 'protocol_name', 'protocol_description', 'project_description', 'parent', 'sibling', 'child']

# Property attributes

property_attributes = ['description', 'type', 'pattern', 'example', 'enum', '$ref', 'user_friendly', 'items', 'guidelines', 'format', 'comment', 'maximum', 'minimum', 'oneOf']

ontology_attributes = ['graph_restriction', 'ontologies', 'classes', 'relations', 'direct', 'include_self']

graph_restriction_attributes = ['ontologies', 'classes', 'relations', 'direct', 'include_self']


class SchemaLinter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def lintSchema(self, path):
        schema = self.get_json_from_file(path)
        properties = schema['properties']
        schema_filename = path.split("/")[-1].split(".")[0]

        # SCHEMA-LEVEL CHECKS

        # All schema fields must be part of the list of allowed schema fields
        for key in schema.keys():
            if key not in allowed_schema_fields:
                sys.exit("Schema field `" + key + "` in " + schema_filename + ".json" + " not an allowed schema field.")

        # All required schema fields must be present in the schema
        for prop in required_schema_fields:
            if prop not in schema.keys():
                sys.exit(schema_filename + ".json: Missing required schema field `" + prop + "`.")

        # additionalProperties must be set to false
        if "additionalProperties" in schema and schema['additionalProperties'] == True:
            sys.exit("Schema " + schema_filename + ".json should not allow additional properties.")

        # $schema must be set to draft-07
        if "$schema" in schema and schema['$schema'] != "http://json-schema.org/draft-07/schema#":
            sys.exit(schema_filename + ".json: Must have $schema set to http://json-schema.org/draft-07/schema#.")

        # Schema filename must match name of the schema in the describedBy URL
        if properties['describedBy']['pattern'].split("/")[-1] != schema_filename:
            sys.exit(schema_filename + ".json: End of `describedBy` URL (" + properties['describedBy']['pattern'].split("/")[-1] + ") must match schema filename (" + schema_filename + ").")

        # Schema filename must match schema name field
        if "name" in schema and schema['name'] != schema_filename:
            sys.exit(schema_filename + ".json: The `name` attribute (" + schema[
            'name'] + ") must match the schema filename (" + schema_filename + ").")

        # Schema type must be set to object
        if "type" in schema and schema['type'] != "object":
            sys.exit(schema_filename + ".json: The `type` attribute must be set to \"object\".")

        # All required fields must actually be in the schema
        if "required" in schema:
            for req_prop in schema["required"]:
                if req_prop not in properties:
                    sys.exit("Property `" + req_prop + "` is required in " + schema_filename + ".json but is missing under properties.")

        # Schema titles should be sentence-case (begin with uppercase letter, no underscores)
        if "title" in schema:
            if (not schema['title'][0].isupper()) or ("_" in schema['title']):
                print(schema_filename + ".json: title \"" +schema['title'] + "\" doesn't start with an uppercase char or contains an underscore.")

        # PROPERTY-LEVEL CHECKS

        # Properties `describedBy` and `schema_version` must be present in each schema
        for ep in required_properties:
            if ep not in properties:
                sys.exit(schema_filename + ".json: Missing required property `" + ep + "`.")

        # Properties `text`, `ontology` and `ontology_label` must be present in each ontology schema
        if "ontology" in schema_filename:
            for p in required_ontology_properties:
                if p not in properties:
                    sys.exit(schema_filename + ".json: Missing required property `" + p + "`.")

        # All type schemas must have corresponding _core property

        # PER-PROPERTY CHECKS

        for property in properties:

            # Property name must contain only lowercase letters, numbers, and underscores
            # TODO: Should be sys.exit() but currently HDBR_accession field fails this
            # TODO: Need to fix HDBR_accession field prior to implementing sys.exit()
            if not re.match("^[a-z0-9_]+$", property) and property not in ['describedBy']:
                print(schema_filename + ".json: Property `" + property + "` contains non-lowercase/underscore characters.")

            # Property must contain description attribute
            if 'description' not in properties[property].keys():
                sys.exit(schema_filename + ".json: Keyword `description` missing from property `" + property + "`.")

            # Property must contain user-friendly attribute
            # Currently excludes ingest-supplied fields and links.json
            # TODO: Should be sys.exit() but currently provenance fields fail this
            # TODO: Fix provenance.json fields prior to implementing sys.exit() and removing provenance from list below
            if 'user_friendly' not in properties[property].keys() and property not in ['schema_version', 'schema_type', 'describedBy', 'provenance']:
                if schema_filename not in ['links']:
                    print(schema_filename + ".json: Keyword `user_friendly` missing from property `" + property + "`.")

            # Property must contain type attribute
            if 'type' not in properties[property].keys():
                sys.exit(schema_filename + ".json: Keyword `type` missing from property `" + property + "`.")

            else:
                # type attribute must be set to one of the valid JSON types
                if properties[property]['type'] not in ["string", "number", "boolean", "array", "object", "integer"]:
                    sys.exit(schema_filename + ".json: Type `" + properties[property]['type'] + "` is not a valid JSON type.")

                # Property of type array must contain the attribute items
                if properties[property]['type'] == "array" and 'items' not in properties[property].keys():
                    sys.exit(schema_filename + ".json: Property `" + property + "` is type array but doesn't contain items.")

                # Property of type array must contains the attribute items
                # items must have either type or $ref attribute
                if properties[property]['type'] == "array" and 'items' in properties[property].keys() and '$ref' not in properties[property]['items'].keys() and 'type' not in properties[property]['items'].keys():
                    sys.exit(schema_filename + ".json: Property `" + property + "` is type array but items attribute doesn't contain type or $ref attribute.")

                # Property of type object must contains the attribute $ref
                if properties[property]['type'] == "object" and '$ref' not in properties[property].keys():
                    sys.exit(schema_filename + ".json: Property `" + property + "` is type object but doesn't contain $ref.")

            # format must be a valid JSON format
            if 'format' in properties[property].keys() and properties[property]['format'] not in ["date", "date-time", "email"]:
                sys.exit(schema_filename + ".json: Format `" + properties[property]['format'] + "` is not a valid JSON format).")

            # description should be a sentence - start with capital letter and end with full stop
            if 'description' in properties[property].keys() and not re.match('^[A-Z][^?!]*[.]$', properties[property]['description']):
                print(schema_filename + ".json: The `description` for property `" + property + "` is not a sentence (" + properties[property]['description'] + ").")

            # guidelines should be a sentence
            if 'guidelines' in properties[property].keys() and not re.match('^[A-Z][^?!]*[.]$', properties[property]['guidelines']):
                print(schema_filename + ".json: The `guidelines` for property `" + property + "` is not a sentence (" + properties[property]['guidelines'] + ").")

            # pattern must be a valid regex
            if 'pattern' in properties[property].keys():
                try:
                    re.compile(properties[property]['pattern'])
                    is_valid_regex = True
                except re.error:
                    is_valid_regex = False
                if not is_valid_regex:
                    sys.exit(schema_filename + ".json: The `pattern` for property `" + property + "` (" + properties[property]['pattern'] + ") is not a valid regex pattern.")

            # Property should contain example attribute
            # Except for system-supplied fields, id/name/description fields, and when importing module ($ref)
            if 'example' not in properties[property].keys() and property not in system_supplied_properties and property not in example_exempt_properties and schema_filename not in ['links', 'provenance']:
                if 'items' in properties[property].keys() and '$ref' not in properties[property]['items'].keys():
                    print(schema_filename + ".json: Keyword `example` missing from property `" + property + "`")
                elif 'items' not in properties[property].keys() and '$ref' not in properties[property].keys():
                    print(schema_filename + ".json: Keyword `example` missing from property `" + property + "`")

            # Property should contain 1 or 2 examples separated by semicolon
            # Excludes enums that list all valid values (Should be one of)
            elif 'example' in properties[property].keys() and property not in system_supplied_properties and schema_filename not in ['links', 'provenance']:
                if not re.match("^Should be one of", str(properties[property]['example'])):
                    ex = str(properties[property]['example']).split(";")
                    if len(ex) == 1 and re.search(",", ex[0]):
                        print(schema_filename + ".json: Property `" + property + "` might have multiple examples that aren't separated by a semicolon (" + str(properties[property]['example']) + ")")

            # _unit properties should have matching property w/o _unit
            if re.match("^[a-z_]+_unit$", property):
                if property.split("_unit")[0] not in properties:
                    sys.exit(schema_filename + ".json: Has unit property `" + property + "` but no corresponding `" + property.split("_unit")[0] + "` property")

            # ADDITIONAL PROPERTY CHECKS & SPECIFIC ONTOLOGY CHECKS

            for kw in properties[property].keys():
                # Ontology field must have graph_restriction property that is an object
                if property == 'ontology' and 'graph_restriction' not in properties[property].keys():
                    sys.exit(schema_filename + ".json: Keyword `graph_restriction` missing from property `" + property + "`.")

                if property == 'ontology' and kw == 'graph_restriction':
                    nested_keywords = properties[property][kw]

                    # graph_restriction property must contain all required attributes
                    for gra in graph_restriction_attributes:
                        if gra not in nested_keywords:
                            sys.exit(schema_filename + ".json: `graph_restriction` missing a required attribute `" + gra + "`.")

                    for nkw in nested_keywords.keys():

                        # Attributes for graph_restriction must be one of acceptable values
                        if nkw not in ontology_attributes:
                            sys.exit(schema_filename + ".json: Keyword `" + nkw + "` is not an acceptable graph_restriction keyword property.")

                    # graph_restriction 'direct' attribute must be 'false'
                    if properties['ontology']['graph_restriction']['direct'] is not False:
                        sys.exit(schema_filename + ".json: Keyword 'direct' must be set to 'false', not " + str(properties['ontology']['graph_restriction']['direct']) + ".")

                    # graph_restriction 'include_self' attribute must be 'false' or 'true'
                    if properties['ontology']['graph_restriction']['include_self'] not in [False, True]:
                        sys.exit(schema_filename + ".json: Keyword 'include_self' must be set to 'false' or 'true', not " + str(
                            properties['ontology']['graph_restriction']['include_self']) + ".")

                    # graph_restriction 'relations' attribute must be a list
                    if not isinstance(properties['ontology']['graph_restriction']['relations'], list):
                        sys.exit(schema_filename + ".json: Keyword 'relations' must be a list.")

                    # graph_restriction 'relations' must at least contain item "rdfs:subClassOf"
                    if 'rdfs:subClassOf' not in properties['ontology']['graph_restriction']['relations']:
                        sys.exit(schema_filename + ".json: Keyword 'relations' must contain item 'rdfs:subClassOf'")

                # All property attributes must be in the allowed list of property attributes
                elif kw not in property_attributes:
                    sys.exit(schema_filename + ".json: Keyword `" + kw + "` in property `" + property + "` is not an allowed property.")

                if isinstance(properties[property][kw], dict) and property != 'ontology':
                    for nkw in properties[property][kw].keys():
                        if nkw not in property_attributes:
                            sys.exit(schema_filename + ".json: Keyword `" + nkw + "` in property `" + property + "` is not an allowed property.")

    def get_json_from_file(self, filename, warn = False):
        """Loads json from a file.
        Optionally specify warn = True to warn, rather than
        fail if file not found."""
        f = open(filename, 'r')
        return json.loads(f.read())


if __name__ == '__main__':
    schema_path = '../json_schema'

    linter = SchemaLinter()

    jsons = [os.path.join(dirpath, f)
               for dirpath, dirnames, files in os.walk(schema_path)
               for f in files if f.endswith('.json')]

    # Exclude top-level JSON files like versions.json and property_migrations.json
    # by including JSON file only if the path contains "core", "module", "system", or "type"
    schemas = [j for j in jsons if any(substring in j for substring in ("core", "module", "system", "type"))]

    print("Linting %d schemas" % len(schemas))

    for s in schemas:
        if 'versions.json' not in s:
            # print('Checking %s' % s)
            linter.lintSchema(s)

    print("\nLinter finished with no errors, but may have some warnings.")
