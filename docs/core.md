# Core
## file_core
_A file entity contains information about a data file produced from any process._

Location: core/file/file_core.json

Property name | Description | Type 
--- | --- | --- 
$schema | The URL reference to the schema. | string
schema_version | The version number of the schema in major.minor.patch format. | string
file_name | The filename of the data file. | string
file_format | The format of the data file. | string
checksum | MD5 checksum of the data file. | string

## protocol_core
_A protocol entity contains information about an intended protocol that was followed in the project._

Location: core/protocol/protocol_core.json

Property name | Description | Type 
--- | --- | --- 
$schema | The URL reference to the schema. | string
schema_version | The version number of the schema in major.minor.patch format. | string
protocol_id | A unique ID for this protocol. | string
protocol_name | A short, descriptive name for the protocol that need not be unique. | string
protocol_description | A general description of the protocol. | string
publication_doi | The publication digital object identifier (doi) associated with the protocol. | string
protocols_io_doi | The protocols.io digital object identifier (doi) associated with the protocol. | string
document | A filename of a PDF document containing the details of the protocol. | string

## project_core
_A project contains information about the overall project._

Location: core/project/project_core.json

Property name | Description | Type 
--- | --- | --- 
$schema | The URL reference to the schema. | string
schema_version | The version number of the schema in major.minor.patch format. | string
project_shortname | A unique label for the project. | string
project_title | A summary of the project in a sentence. | string
project_description | A longer description of the project which can include research goals and experimental approach. | string

## biomaterial_core
_A biomaterial entity contains information about biological material that was generated/used in the project and includes everything from a whole organism down to subcellular components._

Location: core/biomaterial/biomaterial_core.json

Property name | Description | Type 
--- | --- | --- 
$schema | The URL reference to the schema. | string
schema_version | The version number of the schema in major.minor.patch format. | string
biomaterial_id | A unique ID for this biomaterial. | string
biomaterial_name | A short, descriptive name for the biomaterial that need not be unique. | string
biomaterial_description | A general description of the biomaterial. | string
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. Multiple IDs can be provided for multi-species samples. | array
derived_from | If this biomaterial is derived from another biomaterial, enter the biomaterial_id for the biomaterial it was derived from. | string
genotype | Genotype of biomaterial including strain, cross, and genetic modification information. | string
karyotype | The karyotype of the biomaterial. | string
supplementary_files | A list of filenames of biomaterial-level supplementary files. | array
biosd_biomaterial | A DDBJ, NCBI, or EBI BioSample ID. Accessions must start with SAMD, SAMN, or SAME. | string
insdc_biomaterial | An INSDC (International Nucleotide Sequence Database Collaboration) sample accession. Can be from the DDBJ, EMBL-EBI, or NCBI. Accession must start with DRS, ERS, or SRS. | string

## process_core
_A process entity contains information relevant to how a biomaterial/file entity was converted into another biomaterial/file entity._

Location: core/process/process_core.json

Property name | Description | Type 
--- | --- | --- 
$schema | The URL reference to the schema. | string
schema_version | The version number of the schema in major.minor.patch format. | string
process_id | A unique ID for this process. | string
process_name | A short, descriptive name for the process that need not be unique. | string
process_description | A general description of the process. | string
start_time | When the process started, in date-time format, yyyy-mm-ddThh:mm:ssZ. | string
process_location | Where the process took place. | string
operator_identity | Identifier for individual(s) who executed this process. | array

