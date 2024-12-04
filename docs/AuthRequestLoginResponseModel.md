# AuthRequestLoginResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AuthRequestLoginFields**](AuthRequestLoginFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.auth_request_login_response_model import AuthRequestLoginResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRequestLoginResponseModel from a JSON string
auth_request_login_response_model_instance = AuthRequestLoginResponseModel.from_json(json)
# print the JSON string representation of the object
print(AuthRequestLoginResponseModel.to_json())

# convert the object into a dict
auth_request_login_response_model_dict = auth_request_login_response_model_instance.to_dict()
# create an instance of AuthRequestLoginResponseModel from a dict
auth_request_login_response_model_from_dict = AuthRequestLoginResponseModel.from_dict(auth_request_login_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


