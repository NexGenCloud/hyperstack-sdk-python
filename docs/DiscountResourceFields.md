# DiscountResourceFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_amount** | **float** |  | [optional] 
**discount_percent** | **float** |  | [optional] 
**discount_type** | **str** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.discount_resource_fields import DiscountResourceFields

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountResourceFields from a JSON string
discount_resource_fields_instance = DiscountResourceFields.from_json(json)
# print the JSON string representation of the object
print(DiscountResourceFields.to_json())

# convert the object into a dict
discount_resource_fields_dict = discount_resource_fields_instance.to_dict()
# create an instance of DiscountResourceFields from a dict
discount_resource_fields_from_dict = DiscountResourceFields.from_dict(discount_resource_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


