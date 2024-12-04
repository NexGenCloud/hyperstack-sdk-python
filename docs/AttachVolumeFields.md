# AttachVolumeFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**instance_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**volume_id** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.attach_volume_fields import AttachVolumeFields

# TODO update the JSON string below
json = "{}"
# create an instance of AttachVolumeFields from a JSON string
attach_volume_fields_instance = AttachVolumeFields.from_json(json)
# print the JSON string representation of the object
print(AttachVolumeFields.to_json())

# convert the object into a dict
attach_volume_fields_dict = attach_volume_fields_instance.to_dict()
# create an instance of AttachVolumeFields from a dict
attach_volume_fields_from_dict = AttachVolumeFields.from_dict(attach_volume_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


