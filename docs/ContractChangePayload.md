# ContractChangePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**List[FieldChange]**](FieldChange.md) | List of field changes for &#39;updated&#39; type | [optional] 
**id** | **int** | The ID of the contract | 
**org_id** | **int** | The ORG ID of the contract | 
**type** | **str** | Purpose of the change: created, deleted, expired, or updated | 

## Example

```python
from hyperstack.models.contract_change_payload import ContractChangePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ContractChangePayload from a JSON string
contract_change_payload_instance = ContractChangePayload.from_json(json)
# print the JSON string representation of the object
print(ContractChangePayload.to_json())

# convert the object into a dict
contract_change_payload_dict = contract_change_payload_instance.to_dict()
# create an instance of ContractChangePayload from a dict
contract_change_payload_from_dict = ContractChangePayload.from_dict(contract_change_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


