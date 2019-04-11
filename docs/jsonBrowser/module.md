# Module
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## Target<a name='Target'></a>
_Information about a single microscope channel._

Location: module/protocol/target.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
molecule_name | The name of a target molecule (small molecule or gene product) whose distribution is assayed by this experiment. | string | no |  | Target molecule name |  | ACTA1; cFos
molecule_id | An identifier referring to the the target molecule. | string | no |  | Target molecule identifier |  | CHEBI:85345; ENSG00000170345
subcellular_structure | Target subcellular structure. This should be a term from the GO cell component ontology. | object | no | [See module  cellular_component_ontology](module.md/#cellular_component_ontology) | Target subcellular structure |  | 
reagent_name | Name of reagent used to detect target. | string | no |  | Reagent name |  | 
purchased_reagent_details | Information describing purchased reagent used to detect target. | object | no | [See module  purchased_reagents](module.md/#purchased_reagents) | Purchased reagent details |  | 
probe_sequence | Sequence of a probe used to detect target. | string | no |  | Probe sequence |  | AGGCTATAGCGGAGCTACG; aggctatagcggagctacg
fluorophore | Fluorophore used to detect target. | string | no |  | Fluorophore |  | FITC
assay_type | Type of assay used to detect target. | object | yes | [See module  process_type_ontology](module.md/#process_type_ontology) | Assay type |  | MERFISH; in situ sequencing
multiplexed | Whether multiple targets were detected simultaneously in this channel. | string | yes |  | Multiplexed experiment? | yes, no | Should be one of: yes, or no.
channel_id | Channel ID used to assay signal. Should be consistent with the ID in the channel tab. | array | no |  | Channel |  | 1; A

## Channel<a name='Channel'></a>
_Information about a single microscope channel._

Location: module/protocol/channel.json

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
channel_id | User given ID.  If there is an accompanying codebook, this name should correspond to the channel id used in the codebook. | string | yes |  | Channel ID |  | 1; A
excitation_wavelength | Excitation wavelength of the lightsource in nanometers. | number | yes |  | Excitation wavelength |  | 640
filter_range | Emission filter in nanometers. | string | yes |  | Filter range |  | 461/70
multiplexed | Whether multiple targets were detected simultaneously in this channel. | string | yes |  | Multiplexed experiment? | yes, no | Should be one of: yes, or no.
target_fluorophore | The name of the fluorophore this channel is designed to assay. | string | no |  | Target fluorophore |  | Alexa 647
exposure_time | Acquisition time for a single image per channel, in milliseconds. | number | yes |  | Exposure time |  | 400

