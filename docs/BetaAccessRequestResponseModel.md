# BetaAccessRequestResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beta_access_request** | [**BetaAccessRequestFields**](BetaAccessRequestFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.beta_access_request_response_model import BetaAccessRequestResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of BetaAccessRequestResponseModel from a JSON string
beta_access_request_response_model_instance = BetaAccessRequestResponseModel.from_json(json)
# print the JSON string representation of the object
print(BetaAccessRequestResponseModel.to_json())

# convert the object into a dict
beta_access_request_response_model_dict = beta_access_request_response_model_instance.to_dict()
# create an instance of BetaAccessRequestResponseModel from a dict
beta_access_request_response_model_from_dict = BetaAccessRequestResponseModel.from_dict(beta_access_request_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


