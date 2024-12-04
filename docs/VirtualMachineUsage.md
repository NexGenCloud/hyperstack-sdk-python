# VirtualMachineUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**total_usage_time** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.virtual_machine_usage import VirtualMachineUsage

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineUsage from a JSON string
virtual_machine_usage_instance = VirtualMachineUsage.from_json(json)
# print the JSON string representation of the object
print(VirtualMachineUsage.to_json())

# convert the object into a dict
virtual_machine_usage_dict = virtual_machine_usage_instance.to_dict()
# create an instance of VirtualMachineUsage from a dict
virtual_machine_usage_from_dict = VirtualMachineUsage.from_dict(virtual_machine_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


