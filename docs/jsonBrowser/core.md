# Core
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## File core<a name='File core'></a>
_Information about a file produced from any process._

Location: core/file/file_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
file_name | The name of the file. | string | yes |  | File name |  | R1.fastq.gz; codebook.json
file_format | The format of the file. | string | yes |  | File format |  | fastq.gz; tif
checksum | MD5 checksum of the file. | string | no |  | Checksum |  | e09a986c2e630130b1849d4bf9a94c06

## Protocol core<a name='Protocol core'></a>
_Information about an intended protocol that was followed in the project._

Location: core/protocol/protocol_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
protocol_id | A unique ID for the protocol. | string | yes |  | Protocol ID |  | 
protocol_name | A short name for the protocol. | string | no |  | Protocol name |  | 
protocol_description | A general description of the protocol. | string | no |  | Protocol description |  | 
publication_doi | The publication digital object identifier (doi) for the protocol. | string | no |  | Publication DOI |  | 10.1101/193219
protocols_io_doi | The protocols.io digital object identifier (doi) for the protocol. | string | no |  | protocols.io DOI |  | 10.17504/protocols.io.mgjc3un
document | A filename of a PDF document containing the details of the protocol. | string | no |  | Document filename |  | my_cool_protocol.pdf

## Project core<a name='Project core'></a>
_Information about the project._

Location: core/project/project_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
project_short_name | A short name for the project. | string | yes |  | Project label |  | CoolOrganProject.
project_title | An official title for the project. | string | yes |  | Project title |  | Study of single cells in the human body.
project_description | A longer description of the project which includes research goals and experimental approach. | string | yes |  | Project description |  | 

