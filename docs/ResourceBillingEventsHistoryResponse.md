# ResourceBillingEventsHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_events_history** | [**List[ResourceBillingEventsHistoryMetrics]**](ResourceBillingEventsHistoryMetrics.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.resource_billing_events_history_response import ResourceBillingEventsHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceBillingEventsHistoryResponse from a JSON string
resource_billing_events_history_response_instance = ResourceBillingEventsHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceBillingEventsHistoryResponse.to_json())

# convert the object into a dict
resource_billing_events_history_response_dict = resource_billing_events_history_response_instance.to_dict()
# create an instance of ResourceBillingEventsHistoryResponse from a dict
resource_billing_events_history_response_from_dict = ResourceBillingEventsHistoryResponse.from_dict(resource_billing_events_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


