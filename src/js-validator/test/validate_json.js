const Ajv = require('ajv');
const fs = require('fs');
const path = require('path')

function fromDir(startPath,filter){
    var f = []
    if (!fs.existsSync(startPath)){
        console.log("no dir ",startPath);
        return;
    }

    var files=fs.readdirSync(startPath);
    for(var i=0;i<files.length;i++){
        var filename=path.join(startPath,files[i]);
        var stat = fs.lstatSync(filename);
        if (stat.isDirectory()){
            f.push(...fromDir(filename,filter)); //recurse
        }
        else if (filename.indexOf(filter)>=0) {
            console.log('-- found: ',filename);
            f.push(filename)
        };
    };
    return f;
};


function createConfiguredAjv(){
	var ajv = new Ajv({allErrors: true,
	    verbose : true,
	    meta: false, // optional, to prevent adding draft-06 meta-schema
	    extendRefs: true, // optional, current default is to 'fail', spec behaviour is to 'ignore'
	    unknownFormats: 'ignore',  // optional, current default is true (fail)
	    errorDataPath: 'property',
	    messages: true,
	    jsonPointers: false,
	    inlineRefs: false,
	    addUsedSchema: true,
	    passContext: true
	});

	var metaSchema = require('ajv/lib/refs/json-schema-draft-04.json');
	ajv.addMetaSchema(metaSchema);
	ajv._opts.defaultMeta = metaSchema.id;

	// optional, using unversioned URI is out of spec, see https://github.com/json-schema-org/json-schema-spec/issues/216
	ajv._refs['http://json-schema.org/schema'] = 'http://json-schema.org/draft-04/schema';

	// Optionally you can also disable keywords defined in draft-06
	ajv.removeKeyword('propertyNames');
	ajv.removeKeyword('contains');
	ajv.removeKeyword('const');

    // add the schemas
    var schemaFiles = fromDir("../../../json_schema/", ".json");

    schemaFiles
        .filter((schemaFile) => !schemaFile.includes("analysis.json"))
        .forEach((schemaFile) => {
            var schema = require(schemaFile);
            schema.id = schemaFile;
        ajv.addSchema(require(schemaFile), schemaFile);
    });

    return ajv;
}

function getValidatorFunctionForSchema(ajvValidator, schemaPath){
	schema = require(schemaPath);
	return ajvValidator.compile(schema);
}


var donor = require("../../../schema_tests/sample/pass/donor_test1.json");
var sample = require("../../../schema_tests/sample/fail/sample-test-current.json");


test(donor, "../../../json_schema/sample.json");
test(sample, "../../../json_schema/sample.json");

function test(data, schema) {	
    var ajv = createConfiguredAjv()
    var validator = getValidatorFunctionForSchema(ajv, schema)
    var valid = validator(data);
    if (valid) console.log('Valid!');
    else console.log('Invalid: ' + ajv.errorsText(validator.errors));
    
    validator.errors.forEach((error) =>{	
    	console.log(error);
    });

}
