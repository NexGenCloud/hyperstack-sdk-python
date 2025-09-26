# EnvironmentFieldsForVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.environment_fields_for_volume import EnvironmentFieldsForVolume

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentFieldsForVolume from a JSON string
environment_fields_for_volume_instance = EnvironmentFieldsForVolume.from_json(json)
# print the JSON string representation of the object
print(EnvironmentFieldsForVolume.to_json())

# convert the object into a dict
environment_fields_for_volume_dict = environment_fields_for_volume_instance.to_dict()
# create an instance of EnvironmentFieldsForVolume from a dict
environment_fields_for_volume_from_dict = EnvironmentFieldsForVolume.from_dict(environment_fields_for_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


