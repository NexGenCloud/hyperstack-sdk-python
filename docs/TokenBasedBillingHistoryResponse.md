# TokenBasedBillingHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_serverless_inference** | [**BillingHistoryServerlessInference**](BillingHistoryServerlessInference.md) |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.token_based_billing_history_response import TokenBasedBillingHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenBasedBillingHistoryResponse from a JSON string
token_based_billing_history_response_instance = TokenBasedBillingHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(TokenBasedBillingHistoryResponse.to_json())

# convert the object into a dict
token_based_billing_history_response_dict = token_based_billing_history_response_instance.to_dict()
# create an instance of TokenBasedBillingHistoryResponse from a dict
token_based_billing_history_response_from_dict = TokenBasedBillingHistoryResponse.from_dict(token_based_billing_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


