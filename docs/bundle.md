# Bundle
## process_bundle
_A schema for a process bundle._

Location: bundle/process_bundle.json

Property name | Description | Type | User friendly name 
--- | --- | --- | ---
$schema | The URL reference to the schema. | string | 
schema_version | The version number of the schema in major.minor.patch format. | string | 
schema_type | The type of the metadata schema entity. | string | 
processes |  | array | 

## biomaterial_bundle
_A schema for a biomaterial bundle._

Location: bundle/biomaterial_bundle.json

Property name | Description | Type | User friendly name 
--- | --- | --- | ---
$schema | The URL reference to the schema. | string | 
schema_version | The version number of the schema in major.minor.patch format. | string | 
schema_type | The type of the metadata schema entity. | string | 
biomaterials |  | array | 

## project_bundle
_A schema for a project bundle._

Location: bundle/project_bundle.json

Property name | Description | Type | User friendly name 
--- | --- | --- | ---
$schema | The URL reference to the schema. | string | 
schema_version | The version number of the schema in major.minor.patch format. | string | 
schema_type | The type of the metadata schema entity. | string | 
hca_ingest | Core fields added by HCA ingest service | object | 
content | Content for a project type entity. | object | 

## ingest
_Information added or generated at time of ingest._

Location: bundle/ingest_audit.json

Property name | Description | Type | User friendly name 
--- | --- | --- | ---
$schema | The URL reference to the schema. | string | 
schema_version | The version number of the schema in major.minor.patch format. | string | 
submissionDate | When project was first submitted to database. | string | 
submitter_id | ID of contact who first submitted project | string | 
updateDate | When project was last updated | string | 
updater_id | ID of contact who last updated project | string | 
document_id | Identifier for document. | string | 
accession | A unique accession for this entity, provided by the broker. | string | 

## submission
_Information added to a submission at ingest._

Location: bundle/submission.json

Property name | Description | Type | User friendly name 
--- | --- | --- | ---
$schema | The URL reference to the schema. | string | 
schema_version | The version number of the schema in major.minor.patch format. | string | 
schema_type | The type of the metadata schema entity. | string | 
transfer_service_version |  |  | 
submitted_files |  |  | 

## protocol_bundle
_A schema for a protocol bundle._

Location: bundle/protocol_bundle.json

Property name | Description | Type | User friendly name 
--- | --- | --- | ---
$schema | The URL reference to the schema. | string | 
schema_version | The version number of the schema in major.minor.patch format. | string | 
schema_type | The type of the metadata schema entity. | string | 
protocols |  | array | 

