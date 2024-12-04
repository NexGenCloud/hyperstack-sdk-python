# EnvironmentFeatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_optimised** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.environment_features import EnvironmentFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentFeatures from a JSON string
environment_features_instance = EnvironmentFeatures.from_json(json)
# print the JSON string representation of the object
print(EnvironmentFeatures.to_json())

# convert the object into a dict
environment_features_dict = environment_features_instance.to_dict()
# create an instance of EnvironmentFeatures from a dict
environment_features_from_dict = EnvironmentFeatures.from_dict(environment_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


