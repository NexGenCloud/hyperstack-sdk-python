# ResourceLevelGraphBillingDetailsMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incurred_bill** | **float** |  | [optional] 
**incurred_bill_graph** | [**List[GraphDatetimeValueModel]**](GraphDatetimeValueModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_graph_billing_details_metrics import ResourceLevelGraphBillingDetailsMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelGraphBillingDetailsMetrics from a JSON string
resource_level_graph_billing_details_metrics_instance = ResourceLevelGraphBillingDetailsMetrics.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelGraphBillingDetailsMetrics.to_json())

# convert the object into a dict
resource_level_graph_billing_details_metrics_dict = resource_level_graph_billing_details_metrics_instance.to_dict()
# create an instance of ResourceLevelGraphBillingDetailsMetrics from a dict
resource_level_graph_billing_details_metrics_from_dict = ResourceLevelGraphBillingDetailsMetrics.from_dict(resource_level_graph_billing_details_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


