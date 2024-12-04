# ResourceLevelBillingHistoryResponseMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incurred_bill** | **float** |  | [optional] 
**price_per_hour** | **float** |  | [optional] 
**usage_time** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_billing_history_response_metrics import ResourceLevelBillingHistoryResponseMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelBillingHistoryResponseMetrics from a JSON string
resource_level_billing_history_response_metrics_instance = ResourceLevelBillingHistoryResponseMetrics.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelBillingHistoryResponseMetrics.to_json())

# convert the object into a dict
resource_level_billing_history_response_metrics_dict = resource_level_billing_history_response_metrics_instance.to_dict()
# create an instance of ResourceLevelBillingHistoryResponseMetrics from a dict
resource_level_billing_history_response_metrics_from_dict = ResourceLevelBillingHistoryResponseMetrics.from_dict(resource_level_billing_history_response_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


