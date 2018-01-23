import unittest
from schema_test_suite import get_validator, validate
import os
import subprocess

# This => instant tests, but still not sure it is best way to manage.
# Might be better to have configs mapping schemas to tests.
# Or could run the whole thing with a generic script using a 
# standard directory struc and file name convention (brittle to dir 
# restructuring).  Even with that, probably need a config to list which
# tests to run. 


def get_local_base_uri(script_to_json_relative_path):
    """
    Takes the relative path from script to json schema files as an input.
    Switches script to run in json schema folder.
    returns base URI for schema folder on local file system
    """
    # Might be better done in shell as part of travis job and stored as env?
    os.chdir(script_to_json_relative_path)
    pwd = subprocess.check_output('pwd').decode("utf-8").rstrip()
    return "file://" + pwd + '/'

class TestSchemas(unittest.TestCase):

    def setUp(self):
        # Need a better way to manage paths.  Nasty bit of hard wiring for now
        base_uri = get_local_base_uri('../jsonschema/')
        
    def positive_tests(self):
        v = get_validator('collection_process.json', self.base_uri)
        validate(v, {})
        return
        
    def negative_tests(self):
        return
        
        
        