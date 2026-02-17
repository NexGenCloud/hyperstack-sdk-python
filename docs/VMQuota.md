# VMQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_vms** | **int** |  | [optional] 
**cidr** | **str** |  | [optional] 
**current_vms** | **int** |  | [optional] 
**max_vms** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**percentage_used** | **float** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.vm_quota import VMQuota

# TODO update the JSON string below
json = "{}"
# create an instance of VMQuota from a JSON string
vm_quota_instance = VMQuota.from_json(json)
# print the JSON string representation of the object
print(VMQuota.to_json())

# convert the object into a dict
vm_quota_dict = vm_quota_instance.to_dict()
# create an instance of VMQuota from a dict
vm_quota_from_dict = VMQuota.from_dict(vm_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


