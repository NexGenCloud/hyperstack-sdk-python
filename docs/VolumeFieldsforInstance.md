# VolumeFieldsforInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootable** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**volume_type** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.volume_fieldsfor_instance import VolumeFieldsforInstance

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeFieldsforInstance from a JSON string
volume_fieldsfor_instance_instance = VolumeFieldsforInstance.from_json(json)
# print the JSON string representation of the object
print(VolumeFieldsforInstance.to_json())

# convert the object into a dict
volume_fieldsfor_instance_dict = volume_fieldsfor_instance_instance.to_dict()
# create an instance of VolumeFieldsforInstance from a dict
volume_fieldsfor_instance_from_dict = VolumeFieldsforInstance.from_dict(volume_fieldsfor_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


