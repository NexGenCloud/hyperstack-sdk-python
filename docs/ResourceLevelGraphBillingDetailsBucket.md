# ResourceLevelGraphBillingDetailsBucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history** | [**List[ResourceLevelBillingBucketDetailsResources]**](ResourceLevelBillingBucketDetailsResources.md) |  | [optional] 
**granularity** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_graph_billing_details_bucket import ResourceLevelGraphBillingDetailsBucket

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelGraphBillingDetailsBucket from a JSON string
resource_level_graph_billing_details_bucket_instance = ResourceLevelGraphBillingDetailsBucket.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelGraphBillingDetailsBucket.to_json())

# convert the object into a dict
resource_level_graph_billing_details_bucket_dict = resource_level_graph_billing_details_bucket_instance.to_dict()
# create an instance of ResourceLevelGraphBillingDetailsBucket from a dict
resource_level_graph_billing_details_bucket_from_dict = ResourceLevelGraphBillingDetailsBucket.from_dict(resource_level_graph_billing_details_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


