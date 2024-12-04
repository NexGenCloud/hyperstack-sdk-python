# GenerateUpdateApiKeyResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | [**ApiKeyFields**](ApiKeyFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.generate_update_api_key_response_model import GenerateUpdateApiKeyResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateUpdateApiKeyResponseModel from a JSON string
generate_update_api_key_response_model_instance = GenerateUpdateApiKeyResponseModel.from_json(json)
# print the JSON string representation of the object
print(GenerateUpdateApiKeyResponseModel.to_json())

# convert the object into a dict
generate_update_api_key_response_model_dict = generate_update_api_key_response_model_instance.to_dict()
# create an instance of GenerateUpdateApiKeyResponseModel from a dict
generate_update_api_key_response_model_from_dict = GenerateUpdateApiKeyResponseModel.from_dict(generate_update_api_key_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


