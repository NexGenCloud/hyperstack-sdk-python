# VoucherRedeemResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response message | 
**status** | **bool** | Success status of the operation | 
**voucher** | [**Voucher**](Voucher.md) | Redeemed voucher details | [optional] 

## Example

```python
from hyperstack.models.voucher_redeem_response_schema import VoucherRedeemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of VoucherRedeemResponseSchema from a JSON string
voucher_redeem_response_schema_instance = VoucherRedeemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(VoucherRedeemResponseSchema.to_json())

# convert the object into a dict
voucher_redeem_response_schema_dict = voucher_redeem_response_schema_instance.to_dict()
# create an instance of VoucherRedeemResponseSchema from a dict
voucher_redeem_response_schema_from_dict = VoucherRedeemResponseSchema.from_dict(voucher_redeem_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


