# Voucher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Voucher code | 
**id** | **int** | Voucher ID | 
**status** | **str** | Voucher status | 

## Example

```python
from hyperstack.models.voucher import Voucher

# TODO update the JSON string below
json = "{}"
# create an instance of Voucher from a JSON string
voucher_instance = Voucher.from_json(json)
# print the JSON string representation of the object
print(Voucher.to_json())

# convert the object into a dict
voucher_dict = voucher_instance.to_dict()
# create an instance of Voucher from a dict
voucher_from_dict = Voucher.from_dict(voucher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


