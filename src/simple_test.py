from schema_test_suite import get_validator
import glob

"""
Simple test: Are JSON schemas that are in the 
json_schema folder valid JSON schema?
Specific schema tests to follow.
"""

schemas = glob.glob('../json_schema/' +"[a-z]*.json")

for s in schemas:
    print("Checking whether %s is a valid json schema" % s) 
    get_validator(s)
