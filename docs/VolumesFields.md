# VolumesFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[AttachmentsFieldsForVolume]**](AttachmentsFieldsForVolume.md) |  | [optional] 
**bootable** | **bool** |  | [optional] 
**callback_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**environment** | [**EnvironmentFieldsForVolume**](EnvironmentFieldsForVolume.md) |  | [optional] 
**id** | **int** |  | [optional] 
**image_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**volume_type** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.volumes_fields import VolumesFields

# TODO update the JSON string below
json = "{}"
# create an instance of VolumesFields from a JSON string
volumes_fields_instance = VolumesFields.from_json(json)
# print the JSON string representation of the object
print(VolumesFields.to_json())

# convert the object into a dict
volumes_fields_dict = volumes_fields_instance.to_dict()
# create an instance of VolumesFields from a dict
volumes_fields_from_dict = VolumesFields.from_dict(volumes_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


