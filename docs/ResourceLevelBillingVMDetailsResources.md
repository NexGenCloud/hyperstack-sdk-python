# ResourceLevelBillingVMDetailsResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ResourceLevelBillingDetailsAttributes**](ResourceLevelBillingDetailsAttributes.md) |  | [optional] 
**metrics** | [**ResourceLevelBillingDetailsMetrics**](ResourceLevelBillingDetailsMetrics.md) |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_billing_vm_details_resources import ResourceLevelBillingVMDetailsResources

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelBillingVMDetailsResources from a JSON string
resource_level_billing_vm_details_resources_instance = ResourceLevelBillingVMDetailsResources.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelBillingVMDetailsResources.to_json())

# convert the object into a dict
resource_level_billing_vm_details_resources_dict = resource_level_billing_vm_details_resources_instance.to_dict()
# create an instance of ResourceLevelBillingVMDetailsResources from a dict
resource_level_billing_vm_details_resources_from_dict = ResourceLevelBillingVMDetailsResources.from_dict(resource_level_billing_vm_details_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


