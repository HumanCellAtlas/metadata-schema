var expect = require('chai').expect;
const readdirp = require("readdirp");
const path = require('path');
const fs = require('fs');
const Ajv = require('ajv');
const R = require('ramda');

// get all the custom extensions
// only use the graph_extension keyword
let { ElixirValidator, GraphRestriction} = require('elixir-jsonschema-validator');

const schemaDirs = 'json_schema';
const exampleDataDirs = path.join('tests', 'schema_test_files');

// set the base schema path
let baseSchemaPath = path.join(__dirname, '..', schemaDirs);

// set the example data path
let baseDataPath = path.join(__dirname, '..', exampleDataDirs);

let ajvOptions = {baseSchemaPath: baseSchemaPath, extendRefs: true, olsApiBaseUrl: 'http://ontology.archive.data.humancellatlas.org/api'};

let validator = new ElixirValidator([GraphRestriction], ajvOptions);
var ajv = new Ajv(ajvOptions);

// cache of all schema file paths
let schemaFiles = [];

// dynamically test a number of file against a schema
// extend this object to add new tests
var tests = [
    {args: ['type/project/project.json', 'project/test_pass_project_0.json'], expectedErrors: 0},
    {args: ['type/project/project.json', 'project/test_fail_project_0.json'], expectedErrors: 1},
    {args: ['type/biomaterial/donor_organism.json', 'biomaterial/test_pass_donor_organism_0.json'], expectedErrors: 0},
    {args: ['type/biomaterial/specimen_from_organism.json', 'biomaterial/test_pass_specimen_0.json'], expectedErrors: 0},
    {args: ['type/biomaterial/specimen_from_organism.json', 'biomaterial/test_fail_specimen_0.json'], expectedErrors: 1},
    {args: ['type/process/analysis/analysis_process.json', 'process/test_pass_analysis_process.json'], expectedErrors: 0},
    {args: ['type/process/analysis/analysis_process.json', 'process/test_pass_new_analysis_process.json'], expectedErrors: 0},
    {args: ['system/links.json', 'system/test_pass_links.json'], expectedErrors: 0},
    {args: ['system/links.json', 'system/test_fail_links.json'], expectedErrors: 10}

];


// start by reading all the files in the base path with e file filter
schemaFiles = getFilesSync(baseSchemaPath, '.json');

// wait 5 seconds until all files have ben cached, then dynamically run a number of
// unit tests on each file using the mocha testing framework

describe('Testing schema is valid', function() {

    // for each schema file in the cache execute a test
    schemaFiles.forEach(function(jsonSchemaInfo) {
        let jsonSchema = jsonSchemaInfo.schema;
        let schemaPath = jsonSchemaInfo.path;
        it('Testing schema is valid ' + schemaPath, function() {
            expect(jsonSchema).to.be.an('object');

            // set the $async property, needed for custom keyword validation with AJV
            jsonSchema["$async"] = true;

            // check the schema validates
            return validateSchema(jsonSchema).then( (data) => {

                // if we get the file must be valid as no errors were thrown
                expect(data).to.not.equal(null);
                expect(data.errors).to.equal(null);

            }).catch(  (err) => {

                // errors were thrown, file must be invalid, log the message
                expect.fail("invalid schema => " + err.message)
            })
        });
    });
});

describe ('Testing example data validates against schemas', function () {

    tests.forEach(function(testObject) {

        it('Testing ' + testObject.args[0] + ' against ' + testObject.args[1], function () {

            // get the schema file
            let inputSchema = fs.readFileSync(path.join(baseSchemaPath, testObject.args[0]));
            let inputData = fs.readFileSync(path.join(baseDataPath, testObject.args[1]));

            let jsonSchema = JSON.parse(inputSchema);
            // set the $async property, needed for custom keyword validation with AJV
            jsonSchema["$async"] = true;

            // check it is json
            let jsonDoc = JSON.parse(inputData);
            expect(jsonDoc).to.be.an('object');

            return validator.validate(jsonSchema, jsonDoc).then((data) => {

                    expect(testObject.expectedErrors).to.be.equal(data.validationErrors.length);
                    for (let message of data.validationErrors) {
                        console.log("Invalid JSON: " + message.message);
                    }
                });

            }).timeout(10000)

    });

});

describe('Testing allowable entity types in links.json supplementary links', function () {

    // Un-skip this test when we want to allow all concrete entity types in supplementary file links
    xit("should allow all concrete entity types only", function () {
        const linksJsonSchemaPath = baseSchemaPath + "/system/links.json";
        const linksJsonSchema = JSON.parse(fs.readFileSync(linksJsonSchemaPath));
        const allowableEntityTypes = linksJsonSchema["definitions"]["entity"]["properties"]["entity_type"]["enum"];


        const concreteSchemasPath = baseSchemaPath + "/type";
        const concreteSchemas = getFilesSync(concreteSchemasPath, '.json');
        const concreteSchemaTypes = concreteSchemas.map(schema => schema["schema"]["name"]);

        concreteSchemaTypes.forEach(concreteSchema => expect(allowableEntityTypes).to.contain(concreteSchema))
    });

    it("should allow only the 'project' entity type", function () {
        const linksJsonSchemaPath = baseSchemaPath + "/system/links.json";
        const linksJsonSchema = JSON.parse(fs.readFileSync(linksJsonSchemaPath));
        const allowableEntityTypes = linksJsonSchema["definitions"]["entity"]["properties"]["entity_type"]["enum"];

        expect(allowableEntityTypes).to.deep.equal(['project'])
    });
});

/**
 *
 * recursively read all the JSON schema file under the baseSchemaPath
 * @returns {Promise<*>} that will resolve a file entity from readdirp lib
 */
function getFiles(basePath, filter) {

    return new Promise((resolve, reject) => {

        readdirp(
            { root: basePath, fileFilter: filter },
            function(fileInfo) {
                console.log("reading file " + fileInfo.path);
                if (fileInfo.name != "versions.json") {
                    schemaFiles.push(fileInfo)
                }
            },
            function (err, res)  {
                resolve(schemaFiles);
            });

    });
}

/**
 *
 * recursively read all the JSON schema file under the baseSchemaPath
 *
 * @param basePath
 * @param filter
 * @returns {*|T[]|string} A list of objects of format {schema: <a json schema>, path: <full path to schema file> }
 */
function getFilesSync(basePath, filter, relPath) {
    // remove versions.json
    const versionsJsonFilter = (dirEntry) => dirEntry !== "versions.json" && dirEntry !== "property_migrations.json";
    const dirEntries =
        R.map(
            dirEntryName => basePath + "/" + dirEntryName,
            R.filter(versionsJsonFilter, fs.readdirSync(basePath))
        );

    const jsonFileFilterFn = (dirEntryPath) => fs.lstatSync(dirEntryPath).isFile() && dirEntryPath.endsWith(filter);
    const dirEntryFilterFn = (dirEntryPath) => fs.lstatSync(dirEntryPath).isDirectory();

    const jsonFilePaths = R.filter(jsonFileFilterFn, dirEntries);
    const subDirPaths = R.filter(dirEntryFilterFn, dirEntries);

    const jsonFiles = R.map((jsonFilePath) => {return {schema: JSON.parse(fs.readFileSync(jsonFilePath)), path: jsonFilePath} }, jsonFilePaths);

    return jsonFiles.concat(
        R.reduce(
            (acc, jsonFiles) => acc.concat(jsonFiles),
            [],
            R.map(subDirPath => getFilesSync(subDirPath, filter), subDirPaths)
        )
    )
}


/**
 *
 * Used to resolve local filesystem $refs when parsing JSON schema
 * @param relativePath
 * @returns {Promise<any>}
 */
function loadRefs(relativePath) {

    return new Promise((resolve, reject) => {

        let ref = path.join(baseSchemaPath, relativePath);
        console.log('loading ref ' + ref);
        try {
            jsonSchema = fs.readFileSync(ref);
            console.log("setting async for ref " + relativePath)
            jsonSchema["$async"] = true;

            resolve(JSON.parse(jsonSchema))
        } catch (err) {
            reject(err)
        }
    });
}

/**
 * Perform a number of validation and checks against a JSON schema
 * @param jsonSchema
 * @returns {PromiseLike<ajv.ValidateFunction | never>}
 */
function validateSchema(jsonSchema) {

    return ajv.compileAsync(jsonSchema)
        .then(customSchemaChecksValid(jsonSchema))

}

/**
 * One custom check that all JSON schemas must declare a $schema, add any addition
 * custom checks into this function
 * @param schema
 * @returns {Promise<any>}
 */
function customSchemaChecksValid(schema) {

    return new Promise((resolve, reject) => {

        if (! schema["$schema"]) {
            reject("Schema doesn't declare a schema version")
        }
        resolve(true)
    });
}

