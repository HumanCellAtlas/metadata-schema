# Core
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## Biomaterial core<a name='Biomaterial core'></a>
_Information about any biological material that was generated/used in the project including everything from a whole organism to subcellular components._

Location: core/biomaterial/biomaterial_core.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
biomaterial_id | A unique ID for the biomaterial. | string | yes |  | Biomaterial ID |  | 
biomaterial_name | A short, descriptive name for the biomaterial that need not be unique. | string | no |  | Biomaterial name |  | 
biomaterial_description | A general description of the biomaterial. | string | no |  | Biomaterial description |  | 
ncbi_taxon_id | A taxonomy ID (taxonID) from NCBI. | array | yes |  | NCBI taxon ID |  | 9606
genotype | Genotype of the biomaterial. | string | no |  | Genotype |  | DRB1 0401 protective allele; HLA-B*3901 allele
supplementary_files | A list of filenames of biomaterial-level supplementary files. | array | no |  | Supplementary files |  | sample_site_image.jpg
biosamples_accession | A BioSamples accession. | string | no |  | BioSamples accession |  | SAMN00000000
insdc_sample_accession | An International Nucleotide Sequence Database Collaboration (INSDC) sample accession. | string | no |  | INSDC sample accession |  | SRS0000000
HDBR_accession | A Human Developmental Biology Resource (HDBR) sample accession. | string | no |  | HDBR accession |  | 34526; 14758, 2, liver

