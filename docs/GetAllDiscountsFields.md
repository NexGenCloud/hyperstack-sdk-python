# GetAllDiscountsFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_resources** | [**List[DiscountResourceFields]**](DiscountResourceFields.md) |  | [optional] 
**discount_status** | **str** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**org_id** | **int** |  | [optional] 
**org_name** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.get_all_discounts_fields import GetAllDiscountsFields

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllDiscountsFields from a JSON string
get_all_discounts_fields_instance = GetAllDiscountsFields.from_json(json)
# print the JSON string representation of the object
print(GetAllDiscountsFields.to_json())

# convert the object into a dict
get_all_discounts_fields_dict = get_all_discounts_fields_instance.to_dict()
# create an instance of GetAllDiscountsFields from a dict
get_all_discounts_fields_from_dict = GetAllDiscountsFields.from_dict(get_all_discounts_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


