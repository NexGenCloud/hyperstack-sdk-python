# ResourceLevelBillingHistoryResponseAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**infrahub_id** | **int** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_billing_history_response_attributes import ResourceLevelBillingHistoryResponseAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelBillingHistoryResponseAttributes from a JSON string
resource_level_billing_history_response_attributes_instance = ResourceLevelBillingHistoryResponseAttributes.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelBillingHistoryResponseAttributes.to_json())

# convert the object into a dict
resource_level_billing_history_response_attributes_dict = resource_level_billing_history_response_attributes_instance.to_dict()
# create an instance of ResourceLevelBillingHistoryResponseAttributes from a dict
resource_level_billing_history_response_attributes_from_dict = ResourceLevelBillingHistoryResponseAttributes.from_dict(resource_level_billing_history_response_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


