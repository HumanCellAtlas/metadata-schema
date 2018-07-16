# Core
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## biomaterial_core<a name='biomaterial_core'></a>
_A biomaterial entity contains information about biological material that was generated/used in the project and includes everything from a whole organism down to subcellular components._

Location: core/biomaterial/biomaterial_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
biomaterial_id | A unique ID for the biomaterial. | string | yes |  | Biomaterial ID |  | 
biomaterial_name | A short, descriptive name for the biomaterial that need not be unique. | string | no |  | Biomaterial name |  | 
biomaterial_description | A general description of the biomaterial. | string | no |  | Biomaterial description |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | array | yes |  | NCBI taxon ID |  | 9606
genotype | Genotype of the biomaterial. | string | no |  | Genotype |  | DRB1 0401 protective allele
supplementary_files | A list of filenames of biomaterial-level supplementary files. | array | no |  | Supplementary files |  | 
biosd_biomaterial | A DDBJ, NCBI, or EMBL-EBI BioSample ID. Accessions must start with SAMD, SAMN, or SAME. | string | no |  | BioSample ID |  | SAMN00000000
insdc_biomaterial | An INSDC (International Nucleotide Sequence Database Collaboration) sample accession. Can be from the DDBJ, NCBI, or EMBL-EBI. Accessions must start with DRS, SRS, or ERS. | string | no |  | INSDC ID |  | SRS0000000

## file_core<a name='file_core'></a>
_A file entity contains information about a file produced from any process._

Location: core/file/file_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
file_name | The filename of the file. | string | yes |  | File name |  | 
file_format | The format of the file. | string | yes |  | File format |  | fastq.gz
checksum | MD5 checksum of the file. | string | no |  | Checksum |  | 

## process_core<a name='process_core'></a>
_A process entity contains information relevant to how a biomaterial/file entity was converted into another biomaterial/file entity._

Location: core/process/process_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
process_id | A unique ID for this process. | string | yes |  | Process ID |  | 
process_name | A short, descriptive name for the process that need not be unique. | string | no |  | Process name |  | 
process_description | A general description of the process. | string | no |  | Process description |  | 
process_location | Where the process took place. | string | no |  | Location |  | Wellcome Sanger Institute, Teichman Lab.
operator_identity | Identifier for individual(s) who executed this process. | array | no |  | Operator identity |  | Technician 1

## project_core<a name='project_core'></a>
_A project contains information about the overall project._

Location: core/project/project_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
project_short_name | A short name for the project. | string | yes |  | Project label |  | For example, a short label by which you refer to the project. This will be used for quick orientation and reference.
project_title | An official title for your project. | string | yes |  | Project title |  | For example, the title of a grant proposal or a publication, approximately 30 words. This is how the project title will appear on the Human Cell Atlas data portal.
project_description | A longer description of the project which includes research goals and experimental approach. | string | yes |  | Project description |  | For example, an abstract from a grant application or publication. Approximately 300 words.

## protocol_core<a name='protocol_core'></a>
_A protocol entity contains information about an intended protocol that was followed in the project._

Location: core/protocol/protocol_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
protocol_id | A unique ID for this protocol. | string | yes |  | Protocol ID |  | 
protocol_name | A short, descriptive name for the protocol that need not be unique. | string | no |  | Protocol name |  | 
protocol_description | A general description of the protocol. | string | no |  | Protocol description |  | 
publication_doi | The publication digital object identifier (doi) associated with the protocol. | string | no |  | Publication DOI |  | 10.1101/193219
protocols_io_doi | The protocols.io digital object identifier (doi) associated with the protocol. | string | no |  | protocols.io DOI |  | 10.17504/protocols.io.mgjc3un
document | A filename of a PDF document containing the details of the protocol. | string | no |  | Document filename |  | 

