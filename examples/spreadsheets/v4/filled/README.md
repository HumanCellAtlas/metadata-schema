## Example spreadsheets and toy data files valid against v4.4.0-v4.6.1 of the metadata schema.

    v4/filled/
        ├── 10x_v2/                               # 10x_v2 experiments
        │   ├── 10x_pbmc_8k.xlsx                            # Spreadsheet valid against schema v4.4.0-4.6.1
        │   ├── 10x_pbmc_8k_extended.xlsx                   # Spreadsheet valid against schema v4.4.0-4.6.1; additional metadata from 10x_pbmc_8k.xlsx
        │   └── 10x_t_k4.xlsx                               # Spreadsheet valid against schema v4.4.0-4.6.1
        ├── SmartSeq2/                            # SmartSeq2 experiments
        │   ├── ArrayExpress_E-MTAB-5061.xlsx               # Spreadsheet valid against schema v4.4.0-4.6.1
        │   ├── ArrayExpress_E-MTAB-5061_downsampled.xlsx   # Spreadsheet valid against schema v4.4.0-4.6.1; fewer cells from ArrayExpress_E-MTAB-5061.xlsx
        │   ├── Q4DemoSS2Metadata_VALID.xlsx                # Spreadsheet valid against schema v4.4.0-4.6.1
        │   ├── Q4DemoSS2Metadata_INVALID_1.xlsx            # Spreadsheet invalid against schema v4.4.0-4.6.1 (missing required field `donor.ncbi_taxon_id`)
        │   └── Q4DemoSS2Metadata_INVALID_2.xlsx            # Spreadsheet invalid against schema v4.4.0-4.6.1 (missing required field `donor.is_living`, `file.format` field should be `file.file_format`)
        └── other/                                # Other single-cell experiments
            ├── ArrayExpress_E-ERAD-357.xlsx                # Spreadsheet valid against schema v4.4.0-4.6.1
            ├── ArrayExpress_E-MTAB-2805.xlsx               # Spreadsheet valid against schema v4.4.0-4.6.1
            └── GSE36552.xlsx                               # Spreadsheet valid against schema v4.4.0-4.6.1
