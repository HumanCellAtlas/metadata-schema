# Core
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## links<a name='links'></a>
_A schema for a links bundle._

Location: core/links.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
links | An array of linking objects | array | no |  |  |  | 
schema_type | The type of the metadata schema entity. | string | yes |  |  | link_bundle | 

## provenance_core<a name='provenance_core'></a>
_Provenance information added or generated at time of ingest._

Location: core/provenance_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
updater_id | ID of contact who last updated project | string | no |  |  |  | 
accession | A unique accession for this entity, provided by the broker. | string | no |  |  |  | 
document_id | Identifier for document. | string | yes |  |  |  | 
update_date | When project was last updated | string | no |  |  |  | 
submission_date | When project was first submitted to database. | string | yes |  |  |  | 
submitter_id | ID of contact who first submitted project | string | no |  |  |  | 

## project_core<a name='project_core'></a>
_A project contains information about the overall project._

Location: core/project/project_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
project_description | A longer description of the project which can include research goals and experimental approach. Approximately 300 words. | string | yes |  | Project description |  | An abstract from a publication.
project_title | A summary of the project in one sentence. Approximately 30 words. | string | yes |  | Project title |  | A publication title.
project_shortname | A unique label for the project. | string | yes |  | Project label |  | my_project

## biomaterial_core<a name='biomaterial_core'></a>
_A biomaterial entity contains information about biological material that was generated/used in the project and includes everything from a whole organism down to subcellular components._

Location: core/biomaterial/biomaterial_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
biomaterial_name | A short, descriptive name for the biomaterial that need not be unique. | string | no |  | Biomaterial name |  | 
biomaterial_id | A unique ID for this biomaterial. | string | yes |  | Biomaterial ID |  | 
insdc_biomaterial | An INSDC (International Nucleotide Sequence Database Collaboration) sample accession. Can be from the DDBJ, EMBL-EBI, or NCBI. Accession must start with DRS, ERS, or SRS. | string | no |  | INSDC ID |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. Multiple IDs can be provided for multi-species samples. | array | yes |  | NCBI taxon ID |  | 
genotype | Genotype of biomaterial including strain, cross, and genetic modification information. | string | no |  | Genotype |  | 
biomaterial_description | A general description of the biomaterial. | string | no |  | Biomaterial description |  | 
supplementary_files | A list of filenames of biomaterial-level supplementary files. | array | no |  | Supplementary files |  | 
biosd_biomaterial | A DDBJ, NCBI, or EBI BioSample ID. Accessions must start with SAMD, SAMN, or SAME. | string | no |  | BioSample ID |  | 

## process_core<a name='process_core'></a>
_A process entity contains information relevant to how a biomaterial/file entity was converted into another biomaterial/file entity._

Location: core/process/process_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
operator_identity | Identifier for individual(s) who executed this process. | array | no |  | Operator identity |  | Technician 1
process_description | A general description of the process. | string | no |  | Process description |  | 
length_of_time_unit | The unit in which the length of time is expressed. Must be one of microsecond, second, minute, hour, day, week, month, or year. | object | no | [See module  time_unit_ontology](module.md/#time_unit_ontology) | Length of time unit |  | second
process_id | A unique ID for this process. | string | yes |  | Process ID |  | 
process_name | A short, descriptive name for the process that need not be unique. | string | no |  | Process name |  | 
length_of_time | Length of time the process took to execute, from start to finish, in an appropriate time unit. | string | no |  | Start time |  | 
process_location | Where the process took place. | string | no |  | Location |  | Wellcome Sanger Institute, Teichman Lab.

## protocol_core<a name='protocol_core'></a>
_A protocol entity contains information about an intended protocol that was followed in the project._

Location: core/protocol/protocol_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
publication_doi | The publication digital object identifier (doi) associated with the protocol. | string | no |  | Publication DOI |  | 10.1101/193219
protocol_description | A general description of the protocol. | string | no |  | Protocol description |  | 
protocol_id | A unique ID for this protocol. | string | yes |  | Protocol ID |  | 
protocols_io_doi | The protocols.io digital object identifier (doi) associated with the protocol. | string | no |  | protocols.io DOI |  | 10.17504/protocols.io.mgjc3un
protocol_name | A short, descriptive name for the protocol that need not be unique. | string | no |  | Protocol name |  | 
document | A filename of a PDF document containing the details of the protocol. | string | no |  | Document filename |  | 

## file_core<a name='file_core'></a>
_A file entity contains information about a data file produced from any process._

Location: core/file/file_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
checksum | MD5 checksum of the data file. | string | no |  | Checksum |  | 
file_name | The filename of the data file. | string | yes |  | File name |  | 
file_format | The format of the data file. | string | yes |  | File format |  | 

