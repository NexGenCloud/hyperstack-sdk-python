# BetaAccessStatusResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beta_access_requests** | [**List[BetaAccessStatusItem]**](BetaAccessStatusItem.md) | List of beta access requests | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.beta_access_status_response_model import BetaAccessStatusResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of BetaAccessStatusResponseModel from a JSON string
beta_access_status_response_model_instance = BetaAccessStatusResponseModel.from_json(json)
# print the JSON string representation of the object
print(BetaAccessStatusResponseModel.to_json())

# convert the object into a dict
beta_access_status_response_model_dict = beta_access_status_response_model_instance.to_dict()
# create an instance of BetaAccessStatusResponseModel from a dict
beta_access_status_response_model_from_dict = BetaAccessStatusResponseModel.from_dict(beta_access_status_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


