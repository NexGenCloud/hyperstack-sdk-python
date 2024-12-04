# ResourceLevelGraphBillingVolumeDetailsResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ResourceLevelGraphBillingDetailsAttributes**](ResourceLevelGraphBillingDetailsAttributes.md) |  | [optional] 
**metrics** | [**ResourceLevelGraphBillingDetailsMetrics**](ResourceLevelGraphBillingDetailsMetrics.md) |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_graph_billing_volume_details_resources import ResourceLevelGraphBillingVolumeDetailsResources

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelGraphBillingVolumeDetailsResources from a JSON string
resource_level_graph_billing_volume_details_resources_instance = ResourceLevelGraphBillingVolumeDetailsResources.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelGraphBillingVolumeDetailsResources.to_json())

# convert the object into a dict
resource_level_graph_billing_volume_details_resources_dict = resource_level_graph_billing_volume_details_resources_instance.to_dict()
# create an instance of ResourceLevelGraphBillingVolumeDetailsResources from a dict
resource_level_graph_billing_volume_details_resources_from_dict = ResourceLevelGraphBillingVolumeDetailsResources.from_dict(resource_level_graph_billing_volume_details_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


