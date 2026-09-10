# CompatibleImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | **object** | JSON constraints object | [optional] 
**image_id** | **int** |  | [optional] 
**image_name** | **str** |  | [optional] 
**link_type** | **str** | Either &#39;hard&#39; or &#39;soft&#39; | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.compatible_image import CompatibleImage

# TODO update the JSON string below
json = "{}"
# create an instance of CompatibleImage from a JSON string
compatible_image_instance = CompatibleImage.from_json(json)
# print the JSON string representation of the object
print(CompatibleImage.to_json())

# convert the object into a dict
compatible_image_dict = compatible_image_instance.to_dict()
# create an instance of CompatibleImage from a dict
compatible_image_from_dict = CompatibleImage.from_dict(compatible_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


