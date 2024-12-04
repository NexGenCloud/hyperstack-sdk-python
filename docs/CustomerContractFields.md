# CustomerContractFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**discounts** | [**List[ContractDiscountPlanFields]**](ContractDiscountPlanFields.md) |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**expiration_policy** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.customer_contract_fields import CustomerContractFields

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerContractFields from a JSON string
customer_contract_fields_instance = CustomerContractFields.from_json(json)
# print the JSON string representation of the object
print(CustomerContractFields.to_json())

# convert the object into a dict
customer_contract_fields_dict = customer_contract_fields_instance.to_dict()
# create an instance of CustomerContractFields from a dict
customer_contract_fields_from_dict = CustomerContractFields.from_dict(customer_contract_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


