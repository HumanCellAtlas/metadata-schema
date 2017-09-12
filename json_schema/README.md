The "JSON schema" descriptions of HCA json modules lives here.
Some standards we try to adhere to about the structure of these things:

1) If a field symbol is made up of more than one word, use _ to separate the words.
2) Most field symbols are all lower case
3) All fields and all objects have a description.
4) The high level objects, found in json files in a bundle in storage, are described
   in separate files here.  The file names in a bundle, and the schema file names here
   are the same.
5) The high level objects can have embedded subobjects.  If these contain more than a few
   fields or are shared across high level objects they have their own schema file here
   that is referenced in the higher level file.
6) The we call the files here "modules."  Each module has a core field that includes
   a type, version, and a URL to a schema.
7) The version is composed of three parts, each a number separated by a dot.  The first
   part is major version number, and is only incremented when a change is likely to break
   software that depends on the version.  The next two numbers are minor version and patch.
   Each module is versioned separately.
  
