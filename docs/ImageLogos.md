# ImageLogos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logos** | [**List[LogoGetResponse]**](LogoGetResponse.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.image_logos import ImageLogos

# TODO update the JSON string below
json = "{}"
# create an instance of ImageLogos from a JSON string
image_logos_instance = ImageLogos.from_json(json)
# print the JSON string representation of the object
print(ImageLogos.to_json())

# convert the object into a dict
image_logos_dict = image_logos_instance.to_dict()
# create an instance of ImageLogos from a dict
image_logos_from_dict = ImageLogos.from_dict(image_logos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


