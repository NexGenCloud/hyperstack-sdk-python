# VolumeFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootable** | **bool** |  | [optional] 
**callback_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**environment** | [**EnvironmentFieldsforVolume**](EnvironmentFieldsforVolume.md) |  | [optional] 
**id** | **int** |  | [optional] 
**image_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**os_image** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**volume_type** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.volume_fields import VolumeFields

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeFields from a JSON string
volume_fields_instance = VolumeFields.from_json(json)
# print the JSON string representation of the object
print(VolumeFields.to_json())

# convert the object into a dict
volume_fields_dict = volume_fields_instance.to_dict()
# create an instance of VolumeFields from a dict
volume_fields_from_dict = VolumeFields.from_dict(volume_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


