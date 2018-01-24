from schema_test_suite import test_local, get_json_from_file
import re
import os

# Could move these into config
path_to_schemas = '../json_schema'
path_to_test = '../schema_test_files/'

# Assume all dir in test directory not 
# beginning with a '.' are the names of schemas to test.
# (Note - maybe simpler to use glob?)
dtree = list(os.walk(top = path_to_test))
dlist = dtree[0][1]
schemas_to_test = []
for d in dlist:
    if not re.match('\..+', d):
        schemas_to_test.append(d)

valid = True
for s in schemas_to_test:
    print("Checking whether %s.json is a valid json schema" % s)
    test_local(path_to_schema_dir = path_to_schemas ,
               schema_file = s + '.json',
               test_dir = path_to_test + s + '/pass/')