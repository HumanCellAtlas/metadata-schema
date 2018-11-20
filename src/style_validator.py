import unittest
import json
import os


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMAS_SUBDIRS = ["core", "module", "type"]

SCHEMA_BASE_DIR = TESTDATA_FILENAME = os.path.join(THIS_DIR, '../json_schema')
SCHEMAS_DIR_PATHS = list(map(lambda schema_subdir: os.path.join(SCHEMA_BASE_DIR, schema_subdir), SCHEMAS_SUBDIRS))


class SchemaGuideTests(unittest.TestCase):

    # setup

    schemas = []

    @classmethod
    def setUpClass(cls):
        cls.schemas.extend(list(map(lambda schema_filename: cls.get_json_from_file(schema_filename), cls.get_schemas(SCHEMAS_DIR_PATHS))))
        # for schema_json in cls.schemas:
        #     print(json.dumps(schema_json))

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


    def schema_assert(self, assertion):
        schemas_test_results = []

        for schema_json in SchemaGuideTests.schemas:
            schemas_test_results.append({
                "schema": schema_json,
                "result": assertion(schema_json)
            })

        failed_schemas = [schemas_test_result["schema"] for schemas_test_result in schemas_test_results if schemas_test_result["result"] == False]
        failed_schema_names = [schema["name"] for schema in failed_schemas]
        msg = "Failed for schemas " + str(failed_schema_names)
        self.assertTrue(len(failed_schemas) == 0, msg=msg)

    # test methods
    def test_has_a_dollar_schema(self):
        for schema_json in SchemaGuideTests.schemas:
            self.assertTrue("$schema" in schema_json)

    def test_is_version_7(self):
        draft7_assertion = (lambda schema_json: schema_json["$schema"] == 'http://json-schema.org/draft-06/schema#')
        self.schema_assert(draft7_assertion)


if __name__ == '__main__':
    pass

    # unittest.main()
    # SchemaGuideTests.setUpClass()
    # schema_guide_tests = SchemaGuideTests()
    # print(schema_guide_tests.get_schemas())
    #