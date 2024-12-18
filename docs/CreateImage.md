# CreateImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.create_image import CreateImage

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImage from a JSON string
create_image_instance = CreateImage.from_json(json)
# print the JSON string representation of the object
print(CreateImage.to_json())

# convert the object into a dict
create_image_dict = create_image_instance.to_dict()
# create an instance of CreateImage from a dict
create_image_from_dict = CreateImage.from_dict(create_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


