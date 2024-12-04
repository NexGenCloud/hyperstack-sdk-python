# VolumeStatusChangeFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**current_status** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**previous_status** | **str** |  | [optional] 
**volume_id** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.volume_status_change_fields import VolumeStatusChangeFields

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeStatusChangeFields from a JSON string
volume_status_change_fields_instance = VolumeStatusChangeFields.from_json(json)
# print the JSON string representation of the object
print(VolumeStatusChangeFields.to_json())

# convert the object into a dict
volume_status_change_fields_dict = volume_status_change_fields_instance.to_dict()
# create an instance of VolumeStatusChangeFields from a dict
volume_status_change_fields_from_dict = VolumeStatusChangeFields.from_dict(volume_status_change_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


