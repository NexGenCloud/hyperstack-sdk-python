# ResourceLevelGraphBillingDetailVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history** | [**List[ResourceLevelGraphBillingVolumeDetailsResources]**](ResourceLevelGraphBillingVolumeDetailsResources.md) |  | [optional] 
**granularity** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_graph_billing_detail_volume import ResourceLevelGraphBillingDetailVolume

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelGraphBillingDetailVolume from a JSON string
resource_level_graph_billing_detail_volume_instance = ResourceLevelGraphBillingDetailVolume.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelGraphBillingDetailVolume.to_json())

# convert the object into a dict
resource_level_graph_billing_detail_volume_dict = resource_level_graph_billing_detail_volume_instance.to_dict()
# create an instance of ResourceLevelGraphBillingDetailVolume from a dict
resource_level_graph_billing_detail_volume_from_dict = ResourceLevelGraphBillingDetailVolume.from_dict(resource_level_graph_billing_detail_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


