# ContractBillingHistoryResponseAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**gpu_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**infrahub_id** | **int** |  | [optional] 
**price_per_hour** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.contract_billing_history_response_attributes import ContractBillingHistoryResponseAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ContractBillingHistoryResponseAttributes from a JSON string
contract_billing_history_response_attributes_instance = ContractBillingHistoryResponseAttributes.from_json(json)
# print the JSON string representation of the object
print(ContractBillingHistoryResponseAttributes.to_json())

# convert the object into a dict
contract_billing_history_response_attributes_dict = contract_billing_history_response_attributes_instance.to_dict()
# create an instance of ContractBillingHistoryResponseAttributes from a dict
contract_billing_history_response_attributes_from_dict = ContractBillingHistoryResponseAttributes.from_dict(contract_billing_history_response_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


