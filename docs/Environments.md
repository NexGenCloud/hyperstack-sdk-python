# Environments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**environments** | [**List[EnvironmentFields]**](EnvironmentFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.environments import Environments

# TODO update the JSON string below
json = "{}"
# create an instance of Environments from a JSON string
environments_instance = Environments.from_json(json)
# print the JSON string representation of the object
print(Environments.to_json())

# convert the object into a dict
environments_dict = environments_instance.to_dict()
# create an instance of Environments from a dict
environments_from_dict = Environments.from_dict(environments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


