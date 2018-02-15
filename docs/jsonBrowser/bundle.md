# Bundle
## biomaterial_bundle
_A schema for a biomaterial bundle._

Location: bundle/biomaterial_bundle.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
$schema | The URL reference to the schema. | string | yes |  |  |  | 
biomaterials |  | array | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no |  |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial_bundle | 

## ingest
_Information added or generated at time of ingest._

Location: bundle/ingest_audit.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
accession | A unique accession for this entity, provided by the broker. | string | no |  |  |  | 
submissionDate | When project was first submitted to database. | string | yes |  |  |  | 
submitter_id | ID of contact who first submitted project | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no |  |  |  | 4.6.1
updateDate | When project was last updated | string | no |  |  |  | 
$schema | The URL reference to the schema. | string | yes |  |  |  | 
document_id | Identifier for document. | string | yes |  |  |  | 
updater_id | ID of contact who last updated project | string | no |  |  |  | 

## process_bundle
_A schema for a process bundle._

Location: bundle/process_bundle.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
$schema | The URL reference to the schema. | string | yes |  |  |  | 
processes |  | array | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no |  |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | process_bundle | 

## project_bundle
_A schema for a project bundle._

Location: bundle/project_bundle.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
content | Content for a project type entity. | object | yes | [See   project](.md/#project) |  |  | 
$schema | The URL reference to the schema. | string | yes |  |  |  | 
hca_ingest | Core fields added by HCA ingest service | object | yes | [See   ingest_audit](.md/#ingest_audit) |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no |  |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | project_bundle | 

## protocol_bundle
_A schema for a protocol bundle._

Location: bundle/protocol_bundle.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
$schema | The URL reference to the schema. | string | yes |  |  |  | 
protocols |  | array | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no |  |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | project_bundle | 

## submission
_Information added to a submission at ingest._

Location: bundle/submission.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
submitted_files |  |  | yes |  |  |  | 
$schema | The URL reference to the schema. | string | yes |  |  |  | 
transfer_service_version |  |  | yes |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no |  |  |  | 4.6.1
schema_type | The type of the metadata schema entity. | string | no |  |  | submission | 

