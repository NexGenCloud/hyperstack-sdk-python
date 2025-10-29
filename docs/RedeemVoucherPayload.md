# RedeemVoucherPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voucher_code** | **str** | The code of the voucher you want to redeem. | 

## Example

```python
from hyperstack.models.redeem_voucher_payload import RedeemVoucherPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RedeemVoucherPayload from a JSON string
redeem_voucher_payload_instance = RedeemVoucherPayload.from_json(json)
# print the JSON string representation of the object
print(RedeemVoucherPayload.to_json())

# convert the object into a dict
redeem_voucher_payload_dict = redeem_voucher_payload_instance.to_dict()
# create an instance of RedeemVoucherPayload from a dict
redeem_voucher_payload_from_dict = RedeemVoucherPayload.from_dict(redeem_voucher_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


