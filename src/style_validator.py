import unittest
import json
import os


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMAS_SUBDIRS = ["core", "module", "type"]

SCHEMA_BASE_DIR = TESTDATA_FILENAME = os.path.join(THIS_DIR, '../json_schema')
SCHEMAS_DIR_PATHS = list(map(lambda schema_subdir: os.path.join(SCHEMA_BASE_DIR, schema_subdir), SCHEMAS_SUBDIRS))


class SchemaGuideTests(unittest.TestCase):
    schemas = []

    @classmethod
    def setUpClass(cls):
        cls.schemas.extend(list(map(lambda schema_filename: cls.get_json_from_file(schema_filename), cls.get_schemas(SCHEMAS_DIR_PATHS))))

    @staticmethod
    def get_schemas(schema_paths):
        schemas_found = []

        for schema_path in schema_paths:
            found = [os.path.join(dp, f) for dp, dn, filenames in os.walk(schema_path) for f in filenames if os.path.splitext(f)[1] == '.json']
            schemas_found.extend(found)

        print("Checking %d schemas" % len(schemas_found))
        return schemas_found

    @staticmethod
    def get_json_from_file(filepath):
        with open(filepath, 'rb') as json_file:
            return json.load(json_file)

    def test_is_version_7(self):
        for schema_json in SchemaGuideTests.schemas:
            self.assertEqual(schema_json['$schema'], 'http://json-schema.org/draft-07/schema#', "Schema with id " + schema_json["$id"] + " does not adhere to draft-07")


if __name__ == '__main__':
    schema_guide_tests = SchemaGuideTests()
    print(schema_guide_tests.setUpClass())
    print(schema_guide_tests.schemas)


