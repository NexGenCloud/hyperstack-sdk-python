# Logos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dark** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**favicon** | **str** |  | [optional] 
**light** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.logos import Logos

# TODO update the JSON string below
json = "{}"
# create an instance of Logos from a JSON string
logos_instance = Logos.from_json(json)
# print the JSON string representation of the object
print(Logos.to_json())

# convert the object into a dict
logos_dict = logos_instance.to_dict()
# create an instance of Logos from a dict
logos_from_dict = Logos.from_dict(logos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


