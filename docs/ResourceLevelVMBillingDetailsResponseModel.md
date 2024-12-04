# ResourceLevelVMBillingDetailsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_vm_details** | [**ResourceLevelBillingDetailsVM**](ResourceLevelBillingDetailsVM.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_vm_billing_details_response_model import ResourceLevelVMBillingDetailsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelVMBillingDetailsResponseModel from a JSON string
resource_level_vm_billing_details_response_model_instance = ResourceLevelVMBillingDetailsResponseModel.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelVMBillingDetailsResponseModel.to_json())

# convert the object into a dict
resource_level_vm_billing_details_response_model_dict = resource_level_vm_billing_details_response_model_instance.to_dict()
# create an instance of ResourceLevelVMBillingDetailsResponseModel from a dict
resource_level_vm_billing_details_response_model_from_dict = ResourceLevelVMBillingDetailsResponseModel.from_dict(resource_level_vm_billing_details_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


