# AuthGetTokenResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**token** | [**AccessTokenField**](AccessTokenField.md) |  | [optional] 

## Example

```python
from hyperstack.models.auth_get_token_response_model import AuthGetTokenResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AuthGetTokenResponseModel from a JSON string
auth_get_token_response_model_instance = AuthGetTokenResponseModel.from_json(json)
# print the JSON string representation of the object
print(AuthGetTokenResponseModel.to_json())

# convert the object into a dict
auth_get_token_response_model_dict = auth_get_token_response_model_instance.to_dict()
# create an instance of AuthGetTokenResponseModel from a dict
auth_get_token_response_model_from_dict = AuthGetTokenResponseModel.from_dict(auth_get_token_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


