# UpdateVolumeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**updates** | **object** | Summary of fields that were updated | [optional] 
**volume** | [**VolumeFields**](VolumeFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.update_volume_response import UpdateVolumeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVolumeResponse from a JSON string
update_volume_response_instance = UpdateVolumeResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateVolumeResponse.to_json())

# convert the object into a dict
update_volume_response_dict = update_volume_response_instance.to_dict()
# create an instance of UpdateVolumeResponse from a dict
update_volume_response_from_dict = UpdateVolumeResponse.from_dict(update_volume_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


