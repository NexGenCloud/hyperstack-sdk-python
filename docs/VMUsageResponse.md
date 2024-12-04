# VMUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**status** | **bool** |  | [optional] 
**virtual_machines** | [**List[VirtualMachineUsage]**](VirtualMachineUsage.md) |  | [optional] 

## Example

```python
from hyperstack.models.vm_usage_response import VMUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VMUsageResponse from a JSON string
vm_usage_response_instance = VMUsageResponse.from_json(json)
# print the JSON string representation of the object
print(VMUsageResponse.to_json())

# convert the object into a dict
vm_usage_response_dict = vm_usage_response_instance.to_dict()
# create an instance of VMUsageResponse from a dict
vm_usage_response_from_dict = VMUsageResponse.from_dict(vm_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


