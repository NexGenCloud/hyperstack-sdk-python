# VolumeAttachmentFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**device** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**volume** | [**VolumeFieldsforInstance**](VolumeFieldsforInstance.md) |  | [optional] 

## Example

```python
from hyperstack.models.volume_attachment_fields import VolumeAttachmentFields

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeAttachmentFields from a JSON string
volume_attachment_fields_instance = VolumeAttachmentFields.from_json(json)
# print the JSON string representation of the object
print(VolumeAttachmentFields.to_json())

# convert the object into a dict
volume_attachment_fields_dict = volume_attachment_fields_instance.to_dict()
# create an instance of VolumeAttachmentFields from a dict
volume_attachment_fields_from_dict = VolumeAttachmentFields.from_dict(volume_attachment_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


