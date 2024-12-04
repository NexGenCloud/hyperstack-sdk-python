# DiscountPlanFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_amount** | **float** |  | [optional] 
**discount_code** | **str** |  | [optional] 
**discount_percent** | **float** |  | [optional] 
**discount_status** | **str** |  | [optional] 
**discount_type** | **str** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**resource** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**validity_days** | **int** |  | [optional] 
**vm_id** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.discount_plan_fields import DiscountPlanFields

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountPlanFields from a JSON string
discount_plan_fields_instance = DiscountPlanFields.from_json(json)
# print the JSON string representation of the object
print(DiscountPlanFields.to_json())

# convert the object into a dict
discount_plan_fields_dict = discount_plan_fields_instance.to_dict()
# create an instance of DiscountPlanFields from a dict
discount_plan_fields_from_dict = DiscountPlanFields.from_dict(discount_plan_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


