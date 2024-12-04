# ResourceLevelBillingHistoryResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ResourceLevelBillingHistoryResponseAttributes**](ResourceLevelBillingHistoryResponseAttributes.md) |  | [optional] 
**metrics** | [**ResourceLevelBillingHistoryResponseMetrics**](ResourceLevelBillingHistoryResponseMetrics.md) |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_billing_history_resources import ResourceLevelBillingHistoryResources

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelBillingHistoryResources from a JSON string
resource_level_billing_history_resources_instance = ResourceLevelBillingHistoryResources.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelBillingHistoryResources.to_json())

# convert the object into a dict
resource_level_billing_history_resources_dict = resource_level_billing_history_resources_instance.to_dict()
# create an instance of ResourceLevelBillingHistoryResources from a dict
resource_level_billing_history_resources_from_dict = ResourceLevelBillingHistoryResources.from_dict(resource_level_billing_history_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


