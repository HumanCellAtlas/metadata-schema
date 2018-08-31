# Core
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## project_core<a name='project_core'></a>
_A project entity contains information about the overall project._

Location: core/project/project_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
project_description | A longer description of the project which includes research goals and experimental approach. | string | yes |  | Project description |  | For example, an abstract from a grant application or publication. Approximately 300 words.
project_short_name | A short name for the project. | string | yes |  | Project label |  | For example, a short label by which you refer to the project. This label will be used for quick reference.
project_title | An official title for the project. | string | yes |  | Project title |  | For example, the title of a grant proposal or a publication. Approximately 30 words. This title will appear on the Human Cell Atlas data portal.

## biomaterial_core<a name='biomaterial_core'></a>
_A biomaterial entity contains information about biological material that was generated/used in the project and includes everything from a whole organism down to subcellular components._

Location: core/biomaterial/biomaterial_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | array | yes |  | NCBI taxon ID |  | 9606
insdc_biomaterial | An INSDC (International Nucleotide Sequence Database Collaboration) sample accession. Can be from the DDBJ, NCBI, or EMBL-EBI. Accession must start with DRS, SRS, or ERS. | string | no |  | INSDC ID |  | SRS0000000
supplementary_files | A list of filenames of biomaterial-level supplementary files. | array | no |  | Supplementary files |  | 
biosd_biomaterial | A DDBJ, NCBI, or EMBL-EBI BioSample ID. Accession must start with SAMD, SAMN, or SAME. | string | no |  | BioSample ID |  | SAMN00000000
genotype | Genotype of the biomaterial. | string | no |  | Genotype |  | DRB1 0401 protective allele
biomaterial_name | A short, descriptive name for the biomaterial that need not be unique. | string | no |  | Biomaterial name |  | 
biomaterial_description | A general description of the biomaterial. | string | no |  | Biomaterial description |  | 
biomaterial_id | A unique ID for the biomaterial. | string | yes |  | Biomaterial ID |  | 

## process_core<a name='process_core'></a>
_A process entity contains information relevant to how a biomaterial/file entity was converted into another biomaterial/file entity._

Location: core/process/process_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
process_description | A general description of the process. | string | no |  | Process description |  | 
process_location | Location where the process took place. | string | no |  | Process location |  | Wellcome Trust Sanger Institute
process_name | A short, descriptive name for the process that need not be unique. | string | no |  | Process name |  | 
operator | Identifier for individual(s) who executed the process. | array | no |  | Operator identity |  | Technician 1
process_id | A unique ID for the process. | string | yes |  | Process ID |  | 

## protocol_core<a name='protocol_core'></a>
_A protocol entity contains information about an intended protocol that was followed in the project._

Location: core/protocol/protocol_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
document | A filename of a PDF document containing the details of the protocol. | string | no |  | Document filename |  | my_cool_protocol.pdf
protocol_name | A short, descriptive name for the protocol that need not be unique. | string | no |  | Protocol name |  | 
protocol_id | A unique ID for the protocol. | string | yes |  | Protocol ID |  | 
protocols_io_doi | The protocols.io digital object identifier (doi) for the protocol. | string | no |  | protocols.io DOI |  | 10.17504/protocols.io.mgjc3un
protocol_description | A general description of the protocol. | string | no |  | Protocol description |  | 
publication_doi | The publication digital object identifier (doi) for the protocol. | string | no |  | Publication DOI |  | 10.1101/193219

## file_core<a name='file_core'></a>
_A file entity contains information about a file produced from any process._

Location: core/file/file_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
checksum | MD5 checksum of the file. | string | no |  | Checksum |  | 
file_format | The format of the file. | string | yes |  | File format |  | fastq.gz
file_name | The filename of the file. | string | yes |  | File name |  | 

