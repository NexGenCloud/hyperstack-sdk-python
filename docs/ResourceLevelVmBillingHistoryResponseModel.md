# ResourceLevelVmBillingHistoryResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_vm** | [**ResourceLevelBillingHistory**](ResourceLevelBillingHistory.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_vm_billing_history_response_model import ResourceLevelVmBillingHistoryResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelVmBillingHistoryResponseModel from a JSON string
resource_level_vm_billing_history_response_model_instance = ResourceLevelVmBillingHistoryResponseModel.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelVmBillingHistoryResponseModel.to_json())

# convert the object into a dict
resource_level_vm_billing_history_response_model_dict = resource_level_vm_billing_history_response_model_instance.to_dict()
# create an instance of ResourceLevelVmBillingHistoryResponseModel from a dict
resource_level_vm_billing_history_response_model_from_dict = ResourceLevelVmBillingHistoryResponseModel.from_dict(resource_level_vm_billing_history_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


