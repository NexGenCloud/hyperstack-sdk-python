# SubResourcesGraphBillingHistoryFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ResourceLevelBillingDetailsAttributes**](ResourceLevelBillingDetailsAttributes.md) |  | [optional] 
**metrics** | [**SubResourceGraphBillingDetailsMetrics**](SubResourceGraphBillingDetailsMetrics.md) |  | [optional] 

## Example

```python
from hyperstack.models.sub_resources_graph_billing_history_fields import SubResourcesGraphBillingHistoryFields

# TODO update the JSON string below
json = "{}"
# create an instance of SubResourcesGraphBillingHistoryFields from a JSON string
sub_resources_graph_billing_history_fields_instance = SubResourcesGraphBillingHistoryFields.from_json(json)
# print the JSON string representation of the object
print(SubResourcesGraphBillingHistoryFields.to_json())

# convert the object into a dict
sub_resources_graph_billing_history_fields_dict = sub_resources_graph_billing_history_fields_instance.to_dict()
# create an instance of SubResourcesGraphBillingHistoryFields from a dict
sub_resources_graph_billing_history_fields_from_dict = SubResourcesGraphBillingHistoryFields.from_dict(sub_resources_graph_billing_history_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


