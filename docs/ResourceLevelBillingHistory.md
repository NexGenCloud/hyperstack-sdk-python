# ResourceLevelBillingHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history** | [**List[ResourceLevelBillingHistoryResources]**](ResourceLevelBillingHistoryResources.md) |  | [optional] 
**org_id** | **int** |  | [optional] 
**pagination** | [**PaginationData**](PaginationData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_billing_history import ResourceLevelBillingHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelBillingHistory from a JSON string
resource_level_billing_history_instance = ResourceLevelBillingHistory.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelBillingHistory.to_json())

# convert the object into a dict
resource_level_billing_history_dict = resource_level_billing_history_instance.to_dict()
# create an instance of ResourceLevelBillingHistory from a dict
resource_level_billing_history_from_dict = ResourceLevelBillingHistory.from_dict(resource_level_billing_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


