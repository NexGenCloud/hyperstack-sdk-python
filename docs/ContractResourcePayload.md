# ContractResourcePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_amount** | **float** |  | [optional] 
**discount_percent** | **float** |  | [optional] 
**discount_type** | **str** |  | 
**resource_count** | **int** |  | [optional] 
**resource_id** | **int** |  | 

## Example

```python
from hyperstack.models.contract_resource_payload import ContractResourcePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ContractResourcePayload from a JSON string
contract_resource_payload_instance = ContractResourcePayload.from_json(json)
# print the JSON string representation of the object
print(ContractResourcePayload.to_json())

# convert the object into a dict
contract_resource_payload_dict = contract_resource_payload_instance.to_dict()
# create an instance of ContractResourcePayload from a dict
contract_resource_payload_from_dict = ContractResourcePayload.from_dict(contract_resource_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


