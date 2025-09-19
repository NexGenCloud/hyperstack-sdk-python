# ResourceLevelBillingHistoryResourcesCluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ResourceLevelBillingHistoryResponseAttributes**](ResourceLevelBillingHistoryResponseAttributes.md) |  | [optional] 
**metrics** | [**ResourceLevelBillingHistoryResponseMetrics**](ResourceLevelBillingHistoryResponseMetrics.md) |  | [optional] 
**nodes** | [**List[ResourceLevelBillingHistoryResources]**](ResourceLevelBillingHistoryResources.md) |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_billing_history_resources_cluster import ResourceLevelBillingHistoryResourcesCluster

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelBillingHistoryResourcesCluster from a JSON string
resource_level_billing_history_resources_cluster_instance = ResourceLevelBillingHistoryResourcesCluster.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelBillingHistoryResourcesCluster.to_json())

# convert the object into a dict
resource_level_billing_history_resources_cluster_dict = resource_level_billing_history_resources_cluster_instance.to_dict()
# create an instance of ResourceLevelBillingHistoryResourcesCluster from a dict
resource_level_billing_history_resources_cluster_from_dict = ResourceLevelBillingHistoryResourcesCluster.from_dict(resource_level_billing_history_resources_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


