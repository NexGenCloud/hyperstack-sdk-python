# CreateContractPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**discount_resources** | [**List[ContractResourcePayload]**](ContractResourcePayload.md) |  | 
**end_date** | **datetime** |  | [optional] 
**expiration_policy** | **int** |  | 
**org_id** | **int** |  | 
**start_date** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.create_contract_payload import CreateContractPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContractPayload from a JSON string
create_contract_payload_instance = CreateContractPayload.from_json(json)
# print the JSON string representation of the object
print(CreateContractPayload.to_json())

# convert the object into a dict
create_contract_payload_dict = create_contract_payload_instance.to_dict()
# create an instance of CreateContractPayload from a dict
create_contract_payload_from_dict = CreateContractPayload.from_dict(create_contract_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


