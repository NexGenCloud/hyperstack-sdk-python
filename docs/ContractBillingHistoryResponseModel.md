# ContractBillingHistoryResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_contract** | [**ContractBillingHistory**](ContractBillingHistory.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.contract_billing_history_response_model import ContractBillingHistoryResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ContractBillingHistoryResponseModel from a JSON string
contract_billing_history_response_model_instance = ContractBillingHistoryResponseModel.from_json(json)
# print the JSON string representation of the object
print(ContractBillingHistoryResponseModel.to_json())

# convert the object into a dict
contract_billing_history_response_model_dict = contract_billing_history_response_model_instance.to_dict()
# create an instance of ContractBillingHistoryResponseModel from a dict
contract_billing_history_response_model_from_dict = ContractBillingHistoryResponseModel.from_dict(contract_billing_history_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


