# Core
## file_core
_A file entity contains information about a data file produced from any process._

Location: core/file/file_core.json

Property name | Description | Type | User friendly name 
--- | --- | --- | ---
$schema | The URL reference to the schema. | string | 
schema_version | The version number of the schema in major.minor.patch format. | string | 
file_name | The filename of the data file. | string | File name
file_format | The format of the data file. | string | File format
checksum | MD5 checksum of the data file. | string | Checksum

## protocol_core
_A protocol entity contains information about an intended protocol that was followed in the project._

Location: core/protocol/protocol_core.json

Property name | Description | Type | User friendly name 
--- | --- | --- | ---
$schema | The URL reference to the schema. | string | 
schema_version | The version number of the schema in major.minor.patch format. | string | 
protocol_id | A unique ID for this protocol. | string | Protocol ID
protocol_name | A short, descriptive name for the protocol that need not be unique. | string | Protocol name
protocol_description | A general description of the protocol. | string | Protocol description
publication_doi | The publication digital object identifier (doi) associated with the protocol. | string | Publication DOI
protocols_io_doi | The protocols.io digital object identifier (doi) associated with the protocol. | string | protocols.io DOI
document | A filename of a PDF document containing the details of the protocol. | string | Document filename

## project_core
_A project contains information about the overall project._

Location: core/project/project_core.json

Property name | Description | Type | User friendly name 
--- | --- | --- | ---
$schema | The URL reference to the schema. | string | 
schema_version | The version number of the schema in major.minor.patch format. | string | 
project_shortname | A unique label for the project. | string | Project shortname
project_title | A summary of the project in a sentence. | string | Project title
project_description | A longer description of the project which can include research goals and experimental approach. | string | Project description

## biomaterial_core
_A biomaterial entity contains information about biological material that was generated/used in the project and includes everything from a whole organism down to subcellular components._

Location: core/biomaterial/biomaterial_core.json

Property name | Description | Type | User friendly name 
--- | --- | --- | ---
$schema | The URL reference to the schema. | string | 
schema_version | The version number of the schema in major.minor.patch format. | string | 
biomaterial_id | A unique ID for this biomaterial. | string | Biomaterial ID
biomaterial_name | A short, descriptive name for the biomaterial that need not be unique. | string | Biomaterial name
biomaterial_description | A general description of the biomaterial. | string | Biomaterial description
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. Multiple IDs can be provided for multi-species samples. | array | NCBI taxon ID
derived_from | If this biomaterial is derived from another biomaterial, enter the biomaterial_id for the biomaterial it was derived from. | string | Derived from
genotype | Genotype of biomaterial including strain, cross, and genetic modification information. | string | Genotype
karyotype | The karyotype of the biomaterial. | string | Karyotype
supplementary_files | A list of filenames of biomaterial-level supplementary files. | array | Supplementary files
biosd_biomaterial | A DDBJ, NCBI, or EBI BioSample ID. Accessions must start with SAMD, SAMN, or SAME. | string | BioSample ID
insdc_biomaterial | An INSDC (International Nucleotide Sequence Database Collaboration) sample accession. Can be from the DDBJ, EMBL-EBI, or NCBI. Accession must start with DRS, ERS, or SRS. | string | INSDC ID

## process_core
_A process entity contains information relevant to how a biomaterial/file entity was converted into another biomaterial/file entity._

Location: core/process/process_core.json

Property name | Description | Type | User friendly name 
--- | --- | --- | ---
$schema | The URL reference to the schema. | string | 
schema_version | The version number of the schema in major.minor.patch format. | string | 
process_id | A unique ID for this process. | string | Process ID
process_name | A short, descriptive name for the process that need not be unique. | string | Process name
process_description | A general description of the process. | string | Process description
start_time | When the process started, in date-time format, yyyy-mm-ddThh:mm:ssZ. | string | Start time
process_location | Where the process took place. | string | Location
operator_identity | Identifier for individual(s) who executed this process. | array | Operator identity

