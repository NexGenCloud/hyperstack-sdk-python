# ResourceLevelBillingDetailsMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incurred_bill** | **float** |  | [optional] 
**non_discounted_bill** | **float** |  | [optional] 
**non_discounted_price_per_hour** | **float** |  | [optional] 
**price_per_hour** | **float** |  | [optional] 
**usage_time** | **float** |  | [optional] 
**usage_time_active** | **float** |  | [optional] 
**usage_time_hibernated** | **float** |  | [optional] 
**usage_time_shutoff** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_billing_details_metrics import ResourceLevelBillingDetailsMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelBillingDetailsMetrics from a JSON string
resource_level_billing_details_metrics_instance = ResourceLevelBillingDetailsMetrics.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelBillingDetailsMetrics.to_json())

# convert the object into a dict
resource_level_billing_details_metrics_dict = resource_level_billing_details_metrics_instance.to_dict()
# create an instance of ResourceLevelBillingDetailsMetrics from a dict
resource_level_billing_details_metrics_from_dict = ResourceLevelBillingDetailsMetrics.from_dict(resource_level_billing_details_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


