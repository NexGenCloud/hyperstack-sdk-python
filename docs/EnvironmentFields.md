# EnvironmentFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**features** | [**EnvironmentFeatures**](EnvironmentFeatures.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.environment_fields import EnvironmentFields

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentFields from a JSON string
environment_fields_instance = EnvironmentFields.from_json(json)
# print the JSON string representation of the object
print(EnvironmentFields.to_json())

# convert the object into a dict
environment_fields_dict = environment_fields_instance.to_dict()
# create an instance of EnvironmentFields from a dict
environment_fields_from_dict = EnvironmentFields.from_dict(environment_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


