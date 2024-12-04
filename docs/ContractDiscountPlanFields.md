# ContractDiscountPlanFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_amount** | **float** |  | [optional] 
**discount_code** | **str** |  | [optional] 
**discount_percent** | **float** |  | [optional] 
**discount_status** | **str** |  | [optional] 
**discount_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**resource_count** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**resource_name** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.contract_discount_plan_fields import ContractDiscountPlanFields

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDiscountPlanFields from a JSON string
contract_discount_plan_fields_instance = ContractDiscountPlanFields.from_json(json)
# print the JSON string representation of the object
print(ContractDiscountPlanFields.to_json())

# convert the object into a dict
contract_discount_plan_fields_dict = contract_discount_plan_fields_instance.to_dict()
# create an instance of ContractDiscountPlanFields from a dict
contract_discount_plan_fields_from_dict = ContractDiscountPlanFields.from_dict(contract_discount_plan_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


