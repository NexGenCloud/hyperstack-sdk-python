# BillingMetricesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BillingMetricesFields]**](BillingMetricesFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.billing_metrices_response import BillingMetricesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingMetricesResponse from a JSON string
billing_metrices_response_instance = BillingMetricesResponse.from_json(json)
# print the JSON string representation of the object
print(BillingMetricesResponse.to_json())

# convert the object into a dict
billing_metrices_response_dict = billing_metrices_response_instance.to_dict()
# create an instance of BillingMetricesResponse from a dict
billing_metrices_response_from_dict = BillingMetricesResponse.from_dict(billing_metrices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


