# AttachmentsFieldsForVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**instance_id** | **int** |  | [optional] 
**protected** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.attachments_fields_for_volume import AttachmentsFieldsForVolume

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsFieldsForVolume from a JSON string
attachments_fields_for_volume_instance = AttachmentsFieldsForVolume.from_json(json)
# print the JSON string representation of the object
print(AttachmentsFieldsForVolume.to_json())

# convert the object into a dict
attachments_fields_for_volume_dict = attachments_fields_for_volume_instance.to_dict()
# create an instance of AttachmentsFieldsForVolume from a dict
attachments_fields_for_volume_from_dict = AttachmentsFieldsForVolume.from_dict(attachments_fields_for_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


