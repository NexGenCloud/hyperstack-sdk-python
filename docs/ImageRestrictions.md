# ImageRestrictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compatible_images** | [**List[CompatibleImage]**](CompatibleImage.md) | List of images this flavor is allowed to launch, with link metadata | [optional] 
**has_image_restrictions** | **bool** | Whether the flavor is restricted to a set of images | [optional] 
**restriction_type** | **str** | Either &#39;hard&#39;, &#39;soft&#39;, or null if no restrictions | [optional] 

## Example

```python
from hyperstack.models.image_restrictions import ImageRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of ImageRestrictions from a JSON string
image_restrictions_instance = ImageRestrictions.from_json(json)
# print the JSON string representation of the object
print(ImageRestrictions.to_json())

# convert the object into a dict
image_restrictions_dict = image_restrictions_instance.to_dict()
# create an instance of ImageRestrictions from a dict
image_restrictions_from_dict = ImageRestrictions.from_dict(image_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


