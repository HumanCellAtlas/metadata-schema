# Bundle
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## ingest
_Information added or generated at time of ingest._

Location: bundle/ingest_audit.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
updater_id | ID of contact who last updated project | string | no |  |  |  | 
document_id | Identifier for document. | string | yes |  |  |  | 
updateDate | When project was last updated | string | no |  |  |  | 
submissionDate | When project was first submitted to database. | string | yes |  |  |  | 
submitter_id | ID of contact who first submitted project | string | no |  |  |  | 
accession | A unique accession for this entity, provided by the broker. | string | no |  |  |  | 

## links
_A schema for a links bundle._

Location: bundle/links.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | link_bundle | 
links | An array of linking objects | array | no |  |  |  | 

## project
_A schema for a project bundle._

Location: bundle/project.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | project_bundle | 
hca_ingest | Core fields added by HCA ingest service | object | yes | [See   ingest_audit](.md/#ingest_audit) |  |  | 
content | Content for a project type entity. | object | yes | [See   project](.md/#project) |  |  | 

## file
_A schema for a file bundle._

Location: bundle/file.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | file_bundle | 
files | An array of files. | array | no |  |  |  | 

## process
_A schema for a process bundle._

Location: bundle/process.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | process_bundle | 
processes | An array of processes. | array | no |  |  |  | 

## reference
_A schema for a reference bundle._

Location: bundle/reference.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
references | An array of reference files. | array | no |  |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | reference_bundle | 

## biomaterial
_A schema for a biomaterial bundle._

Location: bundle/biomaterial.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | biomaterial_bundle | 
biomaterials | An array of biomaterials. | array | no |  |  |  | 

## protocol
_A schema for a protocol bundle._

Location: bundle/protocol.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | yes |  |  | protocol_bundle | 
protocols | An array of protocols. | array | no |  |  |  | 

## submission
_Information added to a submission at ingest._

Location: bundle/submission.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string | no |  |  | submission | 
transfer_service_version |  |  | yes |  |  |  | 
submitted_files |  |  | yes |  |  |  | 

