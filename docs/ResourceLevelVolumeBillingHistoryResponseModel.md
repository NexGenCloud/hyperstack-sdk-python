# ResourceLevelVolumeBillingHistoryResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_volume** | [**ResourceLevelBillingHistory**](ResourceLevelBillingHistory.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_volume_billing_history_response_model import ResourceLevelVolumeBillingHistoryResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelVolumeBillingHistoryResponseModel from a JSON string
resource_level_volume_billing_history_response_model_instance = ResourceLevelVolumeBillingHistoryResponseModel.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelVolumeBillingHistoryResponseModel.to_json())

# convert the object into a dict
resource_level_volume_billing_history_response_model_dict = resource_level_volume_billing_history_response_model_instance.to_dict()
# create an instance of ResourceLevelVolumeBillingHistoryResponseModel from a dict
resource_level_volume_billing_history_response_model_from_dict = ResourceLevelVolumeBillingHistoryResponseModel.from_dict(resource_level_volume_billing_history_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


