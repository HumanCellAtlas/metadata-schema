from schema_test_suite import get_validator, get_json_from_file, validate
import os
import subprocess

# Simple first test - are json files in json_schema folder
# valid json schema docs?

## Flag for tracking the exit status of validate() calls
status_flag = True

os.chdir('../json_schema')
pwd = subprocess.check_output('pwd').decode("utf-8").rstrip()
base_uri = "file://" + pwd + "/"
print(base_uri)

sv = get_validator('sample.json', base_uri)
dt1 = get_json_from_file('../schema_test_files/10x_pbmc8k_donor_0.json')
# Specific schema tests to follow .
if not validate(sv, dt1): ## will return False if fails (show return value)
    status_flag = False

sfo1 = get_json_from_file('../schema_test_files/10x_pbmc8k_sample_0.json')
if not validate(sv, sfo1):
    status_flag = False

sample_bundle_validator = get_validator('sample_bundle.json', base_uri)
sample_bundle_file = get_json_from_file('../schema_test_files/10x_pbmc8k_sample_bundle.json')
if not validate(sample_bundle_validator, sample_bundle_file):
    status_flag = False

if not status_flag:
    print('validate() failed.')