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

