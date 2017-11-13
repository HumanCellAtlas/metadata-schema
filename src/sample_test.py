from schema_test_suite import get_validator, get_json_from_file, validate
import os
import sys
import subprocess

"""
Sample test: Are JSON files that are in the 
schema_test* folders valid JSON schema?
"""

# Flag for tracking the exit status of validate() calls
status_flag = True

os.chdir('../json_schema')
pwd = subprocess.check_output('pwd').decode("utf-8").rstrip()
base_uri = "file://" + pwd + "/"
print(base_uri)

print('\nValidating sample_core.json')
sv = get_validator('sample_core.json', base_uri)

# Specific schema tests follow

print('\nValidating schema_test_files/10x_pbmc8k_donor_0.json')
dt1 = get_json_from_file('../schema_test_files/10x_pbmc8k_donor_0.json')
if not validate(sv, dt1): # will return False if fails (show return value)
    status_flag = False

print('\nValidating schema_test_files/10x_pbmc8k_sample_0.json')
sfo1 = get_json_from_file('../schema_test_files/10x_pbmc8k_sample_0.json')
if not validate(sv, sfo1):
    status_flag = False

print('\nValidating schema_tests/sample/fail/sample-test-current.json\n(This should fail)')
sf1 = get_json_from_file('../schema_tests/sample/fail/sample-test-current.json')
# This should fail. If it fails, keep status_flag = True
if validate(sv, sf1):
    status_flag = False

# Specific bundle tests follow

print('\nValidating sample_bundle.json')
sample_bundle_validator = get_validator('sample_bundle.json', base_uri)

print('\nValidating schema_test_files/10x_pbmc8k_sample_bundle.json')
sample_bundle_file = get_json_from_file('../schema_test_files/10x_pbmc8k_sample_bundle.json')
if not validate(sample_bundle_validator, sample_bundle_file):
    status_flag = False

# If any of the validate() calls fail, set exit status to 1.
# Failed validate() calls on things that are supposed to fail will not affect exit status.
# Without the following line, failed validate() will result in exit status 0, which is not desirable.
if not status_flag:
    sys.exit(1)
