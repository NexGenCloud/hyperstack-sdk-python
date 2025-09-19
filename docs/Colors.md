# Colors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | [**PrimaryColor**](PrimaryColor.md) |  | [optional] 
**secondary** | [**SecondaryColor**](SecondaryColor.md) |  | [optional] 

## Example

```python
from hyperstack.models.colors import Colors

# TODO update the JSON string below
json = "{}"
# create an instance of Colors from a JSON string
colors_instance = Colors.from_json(json)
# print the JSON string representation of the object
print(Colors.to_json())

# convert the object into a dict
colors_dict = colors_instance.to_dict()
# create an instance of Colors from a dict
colors_from_dict = Colors.from_dict(colors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


