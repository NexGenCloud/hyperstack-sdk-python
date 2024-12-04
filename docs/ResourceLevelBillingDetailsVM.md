# ResourceLevelBillingDetailsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history** | [**List[ResourceLevelBillingVMDetailsResources]**](ResourceLevelBillingVMDetailsResources.md) |  | [optional] 
**org_id** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_billing_details_vm import ResourceLevelBillingDetailsVM

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelBillingDetailsVM from a JSON string
resource_level_billing_details_vm_instance = ResourceLevelBillingDetailsVM.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelBillingDetailsVM.to_json())

# convert the object into a dict
resource_level_billing_details_vm_dict = resource_level_billing_details_vm_instance.to_dict()
# create an instance of ResourceLevelBillingDetailsVM from a dict
resource_level_billing_details_vm_from_dict = ResourceLevelBillingDetailsVM.from_dict(resource_level_billing_details_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


