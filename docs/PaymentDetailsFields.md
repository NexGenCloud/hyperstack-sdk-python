# PaymentDetailsFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**gateway_response** | **str** |  | [optional] 
**paid_from** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.payment_details_fields import PaymentDetailsFields

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDetailsFields from a JSON string
payment_details_fields_instance = PaymentDetailsFields.from_json(json)
# print the JSON string representation of the object
print(PaymentDetailsFields.to_json())

# convert the object into a dict
payment_details_fields_dict = payment_details_fields_instance.to_dict()
# create an instance of PaymentDetailsFields from a dict
payment_details_fields_from_dict = PaymentDetailsFields.from_dict(payment_details_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


