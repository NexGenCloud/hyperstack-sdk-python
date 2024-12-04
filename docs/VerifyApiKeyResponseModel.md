# VerifyApiKeyResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | [**ApiKeyVerifyFields**](ApiKeyVerifyFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.verify_api_key_response_model import VerifyApiKeyResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyApiKeyResponseModel from a JSON string
verify_api_key_response_model_instance = VerifyApiKeyResponseModel.from_json(json)
# print the JSON string representation of the object
print(VerifyApiKeyResponseModel.to_json())

# convert the object into a dict
verify_api_key_response_model_dict = verify_api_key_response_model_instance.to_dict()
# create an instance of VerifyApiKeyResponseModel from a dict
verify_api_key_response_model_from_dict = VerifyApiKeyResponseModel.from_dict(verify_api_key_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


