var Ajv = require('ajv');
var ajv = new Ajv({allErrors: true,
    verbose : true,
    meta: false, // optional, to prevent adding draft-06 meta-schema
    extendRefs: true, // optional, current default is to 'fail', spec behaviour is to 'ignore'
    unknownFormats: 'ignore',  // optional, current default is true (fail)
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


var fs = require('fs');
var path = require('path')

var f = [];

function fromDir(startPath,filter){
    if (!fs.existsSync(startPath)){
        console.log("no dir ",startPath);
        return;
    }

    var files=fs.readdirSync(startPath);
    for(var i=0;i<files.length;i++){
        var filename=path.join(startPath,files[i]);
        var stat = fs.lstatSync(filename);
        if (stat.isDirectory()){
            fromDir(filename,filter); //recurse
        }
        else if (filename.indexOf(filter)>=0) {
            console.log('-- found: ',filename);
            f.push(filename)
        };
    };
    return f;
};


var jsonFiles = fromDir("../../../json_schema/", ".json");





function getCompiledSchemas(){

    var schemas = []

    for(var i=0; i< jsonFiles.length; i++){

        if(jsonFiles[i].indexOf("analysis") == -1){
            var filename = jsonFiles[i];
            var schema = require(filename);

            if(schema.id === undefined){
                schema.id = filename
            }
            ajv.addSchema(schema);
            schemas.push(schema)

        }
        else{
            console.log("we don't want to look at " + jsonFiles[i]);
        }
    }

    var validate;
    for(var j=0; j< schemas.length; j++){

        validate = ajv.compile(schemas[j]);
        console.log("Schema " + schemas[j].title + ".json is a valid json schema")
    }
    return validate;
}


var donor = require("../../../schema_tests/sample/pass/donor_test1.json");
var sample = require("../../../schema_tests/sample/fail/sample-test-current.json");

var validate = getCompiledSchemas();

test(donor);
test(sample);

function test(data) {
    var valid = validate(data);
    if (valid) console.log('Valid!');
    else console.log('Invalid: ' + ajv.errorsText(validate.errors));
    
    validate.errors.forEach((error) =>{	
    	console.log(error);
    });

}
