from schema_test_suite import get_validator
import glob

# Simple first test - are json files in json_schema folder
# valid json schema docs?

schemas = glob.glob('../json_schema/' +"[b-z]*.json")
for s in schemas:
    print("Checking whether %s is a valid json schema" % s) 
    get_validator(s)
    
# Specific schema tests to follow .