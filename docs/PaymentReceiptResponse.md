# PaymentReceiptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**receipt_url** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.payment_receipt_response import PaymentReceiptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReceiptResponse from a JSON string
payment_receipt_response_instance = PaymentReceiptResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentReceiptResponse.to_json())

# convert the object into a dict
payment_receipt_response_dict = payment_receipt_response_instance.to_dict()
# create an instance of PaymentReceiptResponse from a dict
payment_receipt_response_from_dict = PaymentReceiptResponse.from_dict(payment_receipt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


