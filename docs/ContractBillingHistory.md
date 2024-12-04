# ContractBillingHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ContractBillingHistoryResponseAttributes**](ContractBillingHistoryResponseAttributes.md) |  | [optional] 
**metrics** | [**ContractlBillingHistoryResponseMetrics**](ContractlBillingHistoryResponseMetrics.md) |  | [optional] 

## Example

```python
from hyperstack.models.contract_billing_history import ContractBillingHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ContractBillingHistory from a JSON string
contract_billing_history_instance = ContractBillingHistory.from_json(json)
# print the JSON string representation of the object
print(ContractBillingHistory.to_json())

# convert the object into a dict
contract_billing_history_dict = contract_billing_history_instance.to_dict()
# create an instance of ContractBillingHistory from a dict
contract_billing_history_from_dict = ContractBillingHistory.from_dict(contract_billing_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


