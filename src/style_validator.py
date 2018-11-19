import unittest
import json
import os, sys


class schema_guide_tests(unittest.TestCase):

    @classmethod

    def setUpClass(cls):
        cls.schemas.append(map(lambda schema_filename: cls.get_json_from_file(schema_filename),cls.get_schemas(schema_paths)))

    def get_schema_paths(cls):
        schema_path = '../json_schema'

        schema_paths = [os.path.join(dirpath, f)
                   for dirpath, dirnames, files in os.walk(schema_path)
                   for f in files if f.endswith('.json')]

        print("Checking %d schemas" % len(schema_paths))
        return schema_paths

    schema_paths = get_schema_paths()

    def get_schemas(schema_paths):
        schemas_found = []

        for schema_path in schema_paths:
            found = [os.path.join(dirpath, f)
                   for dirpath, dirnames, files in os.walk(schema_path)
                   for f in files if f.endswith('.json')]

            schemas_found.append(found)

        print("Checking %d schemas" % len(schemas_found))
        return schemas_found

    def is_version_7(self):
        for schema_json in TestStringMethods.schemas:
            self.assertEqual(schema_json['$schema'], 'http://json-schema.org/draft-07/schema#', "Schema with id " + schema_json["$id"] + " does not adhere to draft-07")



if __name__ == '__main__':
    schema_guide_tests = schema_guide_tests()
    print(schema_guide_tests.setUpClass())
    print(schema_guide_tests.schemas)


