# Core
## project_core<a name='project_core'></a>
_A project contains information about the overall project._

Location: core/project/project_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
$schema | The URL reference to the schema. | string | yes |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no |  |  |  | 4.6.1
project_shortname | A unique label for the project. | string | yes |  | Project shortname |  | Tissue Stability
project_title | A summary of the project in a sentence. | string | yes |  | Project title |  | A title of a grant proposal or publication. Approximately 30 words.
project_description | A longer description of the project which can include research goals and experimental approach. | string | no |  | Project description |  | An abstract from a grant application or publication. Approximately 300 words.

## biomaterial_core<a name='biomaterial_core'></a>
_A biomaterial entity contains information about biological material that was generated/used in the project and includes everything from a whole organism down to subcellular components._

Location: core/biomaterial/biomaterial_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
$schema | The URL reference to the schema. | string | yes |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no |  |  |  | 4.6.1
biomaterial_id | A unique ID for this biomaterial. | string | yes |  | Biomaterial ID |  | 
biomaterial_name | A short, descriptive name for the biomaterial that need not be unique. | string | no |  | Biomaterial name |  | 
biomaterial_description | A general description of the biomaterial. | string | no |  | Biomaterial description |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. Multiple IDs can be provided for multi-species samples. | array | yes |  | NCBI taxon ID |  | 
derived_from | If this biomaterial is derived from another biomaterial, enter the biomaterial_id for the biomaterial it was derived from. | string | no |  | Derived from |  | 
genotype | Genotype of biomaterial including strain, cross, and genetic modification information. | string | no |  | Genotype |  | 
karyotype | The karyotype of the biomaterial. | string | no |  | Karyotype |  | 
supplementary_files | A list of filenames of biomaterial-level supplementary files. | array | no |  | Supplementary files |  | 
biosd_biomaterial | A DDBJ, NCBI, or EBI BioSample ID. Accessions must start with SAMD, SAMN, or SAME. | string | no |  | BioSample ID |  | 
insdc_biomaterial | An INSDC (International Nucleotide Sequence Database Collaboration) sample accession. Can be from the DDBJ, EMBL-EBI, or NCBI. Accession must start with DRS, ERS, or SRS. | string | no |  | INSDC ID |  | 

## process_core<a name='process_core'></a>
_A process entity contains information relevant to how a biomaterial/file entity was converted into another biomaterial/file entity._

Location: core/process/process_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
$schema | The URL reference to the schema. | string | yes |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no |  |  |  | 4.6.1
process_id | A unique ID for this process. | string | yes |  | Process ID |  | 
process_name | A short, descriptive name for the process that need not be unique. | string | no |  | Process name |  | 
process_description | A general description of the process. | string | no |  | Process description |  | 
start_time | When the process started, in date-time format, yyyy-mm-ddThh:mm:ssZ. | string | no |  | Start time |  | 2018-01-31T08:30:00Z
process_location | Where the process took place. | string | no |  | Location |  | Wellcome Sanger Institute, Teichman Lab.
operator_identity | Identifier for individual(s) who executed this process. | array | no |  | Operator identity |  | Technician 1

## protocol_core<a name='protocol_core'></a>
_A protocol entity contains information about an intended protocol that was followed in the project._

Location: core/protocol/protocol_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
$schema | The URL reference to the schema. | string | yes |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no |  |  |  | 4.6.1
protocol_id | A unique ID for this protocol. | string | yes |  | Protocol ID |  | 
protocol_name | A short, descriptive name for the protocol that need not be unique. | string | no |  | Protocol name |  | 
protocol_description | A general description of the protocol. | string | no |  | Protocol description |  | 
publication_doi | The publication digital object identifier (doi) associated with the protocol. | string | no |  | Publication DOI |  | 10.1101/193219
protocols_io_doi | The protocols.io digital object identifier (doi) associated with the protocol. | string | no |  | protocols.io DOI |  | 10.17504/protocols.io.mgjc3un
document | A filename of a PDF document containing the details of the protocol. | string | no |  | Document filename |  | 

## file_core<a name='file_core'></a>
_A file entity contains information about a data file produced from any process._

Location: core/file/file_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
$schema | The URL reference to the schema. | string | yes |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no |  |  |  | 4.6.1
file_name | The filename of the data file. | string | yes |  | File name |  | 
file_format | The format of the data file. | string | yes |  | File format |  | 
checksum | MD5 checksum of the data file. | string | no |  | Checksum |  | 

