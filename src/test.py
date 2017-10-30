from schema_test_suite import test_local, get_json_from_file

path_to_schemas = '../json_schema'
path_to_test = '../schema_tests/'
schemas_to_test = get_json_from_file(path_to_test + "conf.json")['schemas_to_test']

for s in schemas_to_test:
    test_local(path_to_schema_dir = path_to_schemas , 
               schema_file = s + '.json',
               test_dir = path_to_test + s + '/pass/')