# VolumesLastStatusChangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**volume_status_list** | [**List[VolumeStatusChangeFields]**](VolumeStatusChangeFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.volumes_last_status_change_response import VolumesLastStatusChangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VolumesLastStatusChangeResponse from a JSON string
volumes_last_status_change_response_instance = VolumesLastStatusChangeResponse.from_json(json)
# print the JSON string representation of the object
print(VolumesLastStatusChangeResponse.to_json())

# convert the object into a dict
volumes_last_status_change_response_dict = volumes_last_status_change_response_instance.to_dict()
# create an instance of VolumesLastStatusChangeResponse from a dict
volumes_last_status_change_response_from_dict = VolumesLastStatusChangeResponse.from_dict(volumes_last_status_change_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


