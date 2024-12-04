# ResourceBillingEventsHistoryMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | [optional] 
**event_duration** | **float** |  | [optional] 
**price_per_hour** | **float** |  | [optional] 
**start** | **str** |  | [optional] 
**total_cost** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.resource_billing_events_history_metrics import ResourceBillingEventsHistoryMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceBillingEventsHistoryMetrics from a JSON string
resource_billing_events_history_metrics_instance = ResourceBillingEventsHistoryMetrics.from_json(json)
# print the JSON string representation of the object
print(ResourceBillingEventsHistoryMetrics.to_json())

# convert the object into a dict
resource_billing_events_history_metrics_dict = resource_billing_events_history_metrics_instance.to_dict()
# create an instance of ResourceBillingEventsHistoryMetrics from a dict
resource_billing_events_history_metrics_from_dict = ResourceBillingEventsHistoryMetrics.from_dict(resource_billing_events_history_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


