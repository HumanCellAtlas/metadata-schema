from schema_test_suite import get_validator, get_json_from_file, validate
import os
import subprocess

# Simple first test - are json files in json_schema folder
# valid json schema docs?

os.chdir('../json_schema')
pwd = subprocess.check_output('pwd').decode("utf-8").rstrip()
base_uri = "file://" + pwd + "/"
print(base_uri)
sv = get_validator('sample.json', base_uri)
dt1 = get_json_from_file('../schema_test_files/10x_pbmc8k_donor_0.json')
# Specific schema tests to follow .
validate(sv, dt1)

sfo1 = get_json_from_file('../schema_test_files/10x_pbmc8k_sample_0.json')
validate(sv, sfo1)
#
sample_ingest_validator = get_validator('sample_ingest.json', base_uri)
sample_ingest_file = get_json_from_file('../schema_test_files/10x_pbmc8k_sample_0_ingest.json')
validate(sample_ingest_validator, sample_ingest_file)

sample_ingest_file = get_json_from_file('../schema_test_files/10x_pbmc8k_donor_0_ingest.json')
validate(sample_ingest_validator, sample_ingest_file)
#
sample_bundle_validator = get_validator('sample_bundle.json', base_uri)
sample_bundle_file = get_json_from_file('../schema_test_files/10x_pbmc8k_sample_bundle.json')
validate(sample_bundle_validator, sample_bundle_file)
