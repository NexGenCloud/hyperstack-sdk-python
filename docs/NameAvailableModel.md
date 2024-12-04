# NameAvailableModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.name_available_model import NameAvailableModel

# TODO update the JSON string below
json = "{}"
# create an instance of NameAvailableModel from a JSON string
name_available_model_instance = NameAvailableModel.from_json(json)
# print the JSON string representation of the object
print(NameAvailableModel.to_json())

# convert the object into a dict
name_available_model_dict = name_available_model_instance.to_dict()
# create an instance of NameAvailableModel from a dict
name_available_model_from_dict = NameAvailableModel.from_dict(name_available_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


