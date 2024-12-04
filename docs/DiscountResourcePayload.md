# DiscountResourcePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_amount** | **float** |  | 
**discount_percent** | **float** |  | 
**discount_type** | **str** |  | 
**resource_id** | **int** |  | 

## Example

```python
from hyperstack.models.discount_resource_payload import DiscountResourcePayload

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountResourcePayload from a JSON string
discount_resource_payload_instance = DiscountResourcePayload.from_json(json)
# print the JSON string representation of the object
print(DiscountResourcePayload.to_json())

# convert the object into a dict
discount_resource_payload_dict = discount_resource_payload_instance.to_dict()
# create an instance of DiscountResourcePayload from a dict
discount_resource_payload_from_dict = DiscountResourcePayload.from_dict(discount_resource_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


