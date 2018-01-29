from schema_test_suite import get_validator, get_json_from_file, validate
import os
import sys
import subprocess

"""
json_examples_validate_against_schema: 
Do JSON files and bundles in the schema_test_files folders
validate against their correspondoing JSON schema?
"""

# Flag for tracking the exit status of validate() calls
status_flag = True

os.chdir('../json_schema')
pwd = subprocess.check_output('pwd').decode("utf-8").rstrip()
print('pwd: %s' % pwd)
base_uri = "file://" + pwd + "/"
print('base URI: %s' % base_uri)

# Specific schema tests follow

# Testing valid project JSON example
print('\nValidating type/project/project.json schema')
sv = get_validator('type/project/project.json', base_uri)
print('Validating project/test_pass_project_0.json JSON against schema')
p1 = get_json_from_file('../schema_test_files/project/test_pass_project_0.json')
if not validate(sv, p1):
    status_flag = False

# Testing invalid project JSON example
# It is missing required project_id field
print('\nValidating type/project/project.json schema')
sv = get_validator('type/project/project.json', base_uri)
print('Validating project/test_fail_project_0.json JSON against schema\n(This should fail, missing project_id)')
p1 = get_json_from_file('../schema_test_files/project/test_fail_project_0.json')
if validate(sv, p1):
    status_flag = False

# Testing valid organism JSON example
print('\nValidating type/biomaterial/organism.json schema')
sv = get_validator('type/biomaterial/organism.json', base_uri)
print('Validating biomaterial/test_pass_organism_0.json JSON against schema')
o1 = get_json_from_file('../schema_test_files/biomaterial/test_pass_organism_0.json')
if not validate(sv, o1):
    status_flag = False

# Testing valid specimen JSON example
print('\nValidating type/biomaterial/specimen_from_organism.json schema')
sv = get_validator('type/biomaterial/specimen_from_organism.json', base_uri)
print('Validating biomaterial/test_pass_specimen_0.json JSON against schema')
s1 = get_json_from_file('../schema_test_files/biomaterial/test_pass_specimen_0.json')
if not validate(sv, s1):
    status_flag = False

# Testing invalid specimen JSON example
# It is missing required ncbi_taxon_id field
print('\nValidating type/biomaterial/specimen_from_organism.json schema')
sv = get_validator('type/biomaterial/specimen_from_organism.json', base_uri)
print('Validating biomaterial/test_fail_specimen_0.json JSON against schema\n(This should fail, missing ncbi_taxon_id)')
s2 = get_json_from_file('../schema_test_files/biomaterial/test_fail_specimen_0.json')
if validate(sv, s2):
    status_flag = False

# Specific bundle tests follow

# Testing valid biomaterial bundle example
print('\nValidating bundle/biomaterial_bundle.json schema')
sv = get_validator('bundle/biomaterial_bundle.json', base_uri)
print('Validating biomaterial/test_pass_biomaterial_bundle.json JSON against schema')
b1 = get_json_from_file('../schema_test_files/biomaterial/test_pass_biomaterial_bundle.json')
if not validate(sv, b1):
    status_flag = False

# Testing invalid biomaterial bundle example
# Bundle is missing hca_ingest property in one of the biomaterials
print('\nValidating bundle/biomaterial_bundle.json schema')
sv = get_validator('bundle/biomaterial_bundle.json', base_uri)
print('Validating biomaterial/test_fail_biomaterial_bundle.json JSON against schema\n(This should fail, missing hca_ingest)')
b2 = get_json_from_file('../schema_test_files/biomaterial/test_fail_biomaterial_bundle.json')
if validate(sv, b2):
    status_flag = False

# Testing valid project bundle example
print('\nValidating bundle/project_bundle.json schema')
sv = get_validator('bundle/project_bundle.json', base_uri)
print('Validating project/test_pass_project_bundle.json JSON against schema')
b1 = get_json_from_file('../schema_test_files/project/test_pass_project_bundle.json')
if not validate(sv, b1):
    status_flag = False

# If any of the validate() calls fail, set exit status to 1.
# Failed validate() calls on things that are supposed to fail will not affect exit status.
# Without the following line, failed validate() will result in exit status 0, which is not desirable.
if not status_flag:
    sys.exit(1)
