# CreateContractFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**discount_plans** | [**List[ContractDiscountPlanFields]**](ContractDiscountPlanFields.md) |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**expiration_policy** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**start_date** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.create_contract_fields import CreateContractFields

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContractFields from a JSON string
create_contract_fields_instance = CreateContractFields.from_json(json)
# print the JSON string representation of the object
print(CreateContractFields.to_json())

# convert the object into a dict
create_contract_fields_dict = create_contract_fields_instance.to_dict()
# create an instance of CreateContractFields from a dict
create_contract_fields_from_dict = CreateContractFields.from_dict(create_contract_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


