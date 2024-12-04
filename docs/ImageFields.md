# ImageFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_size** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**labels** | [**List[LableResonse]**](LableResonse.md) |  | [optional] 
**name** | **str** |  | [optional] 
**region_name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.image_fields import ImageFields

# TODO update the JSON string below
json = "{}"
# create an instance of ImageFields from a JSON string
image_fields_instance = ImageFields.from_json(json)
# print the JSON string representation of the object
print(ImageFields.to_json())

# convert the object into a dict
image_fields_dict = image_fields_instance.to_dict()
# create an instance of ImageFields from a dict
image_fields_from_dict = ImageFields.from_dict(image_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


