# ExcludeBillingPostPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **bool** | &#x60;true&#x60; excludes the resource from billing while &#x60;false&#x60; does not. | 
**resource_id** | **int** | The ID of the resource which is being excluded from billing. | 
**resource_type** | **str** | The type of the resource which is being excluded from billing. | 

## Example

```python
from hyperstack.models.exclude_billing_post_payload import ExcludeBillingPostPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ExcludeBillingPostPayload from a JSON string
exclude_billing_post_payload_instance = ExcludeBillingPostPayload.from_json(json)
# print the JSON string representation of the object
print(ExcludeBillingPostPayload.to_json())

# convert the object into a dict
exclude_billing_post_payload_dict = exclude_billing_post_payload_instance.to_dict()
# create an instance of ExcludeBillingPostPayload from a dict
exclude_billing_post_payload_from_dict = ExcludeBillingPostPayload.from_dict(exclude_billing_post_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


