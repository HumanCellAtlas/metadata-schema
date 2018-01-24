## Schema test files

* For each schema to be tested:
   * Add a directory to this folder named for the schema.  
       - e.g. to test sample.json, add a directory called 'sample'. 

   * Add the name of the schema to conf.json
   * Under this add a directory called 'pass' (for all instances that are meant
 to pass), and a directory called 'fail' (for all instances that are meant
 to fail). Any files with the .json extension in these directories will be
 tested against the relevant schema.
 
 
 
 This behavior relies on /src/test.py.