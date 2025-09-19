# KeypairEnvironmentFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**features** | [**KeypairEnvironmentFeatures**](KeypairEnvironmentFeatures.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.keypair_environment_fields import KeypairEnvironmentFields

# TODO update the JSON string below
json = "{}"
# create an instance of KeypairEnvironmentFields from a JSON string
keypair_environment_fields_instance = KeypairEnvironmentFields.from_json(json)
# print the JSON string representation of the object
print(KeypairEnvironmentFields.to_json())

# convert the object into a dict
keypair_environment_fields_dict = keypair_environment_fields_instance.to_dict()
# create an instance of KeypairEnvironmentFields from a dict
keypair_environment_fields_from_dict = KeypairEnvironmentFields.from_dict(keypair_environment_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


