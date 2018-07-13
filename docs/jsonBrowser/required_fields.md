# Required fields
_This document contains a list of all required fields in the HCA metadata schema. For a fulldescription of each schema, please refer to the relevant entity specification document._
## Core
### file_core<a name='file_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
file_name | The filename of the data file. | string |  | File name |  | 
file_format | The format of the data file. | string |  | File format |  | 
### protocol_core<a name='protocol_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
protocol_id | A unique ID for this protocol. | string |  | Protocol ID |  | 
### project_core<a name='project_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
project_short_name | A short name for the project. | string |  | Project label |  | For example, a short label by which you refer to the project. This will be used for quick orientation and reference.
project_title | An official title for your project. | string |  | Project title |  | For example, the title of a grant proposal or a publication, approximately 30 words. This is how the project title will appear on the Human Cell Atlas data portal.
project_description | A longer description of the project which includes research goals and experimental approach. | string |  | Project description |  | For example, an abstract from a grant application or publication. Approximately 300 words.
### biomaterial_core<a name='biomaterial_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
biomaterial_id | A unique ID for this biomaterial. | string |  | Biomaterial ID |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. Multiple IDs can be provided for multi-species samples. | array |  | NCBI taxon ID |  | 
### process_core<a name='process_core'></a>
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
process_id | A unique ID for this process. | string |  | Process ID |  | 
## Type
### sequence_file
Property name | Description | Type | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- 
schema_type | The type of the metadata schema entity. | string |  |  | file | 
file_core | Core file-level information. | object | [See core  file_core](core.md/#file_core) |  |  | 
read_index | Whether the read file contains the read1, read2, index1, or index2 part of the sequencing read. If read file represents a single-end, non-indexed library, indicate that here. | string |  | Read index | read1, read2, index1, index2, single-end, non-indexed | read1
