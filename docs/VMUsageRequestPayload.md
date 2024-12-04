# VMUsageRequestPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_ids** | **List[int]** | List of virtual machine IDs | 

## Example

```python
from hyperstack.models.vm_usage_request_payload import VMUsageRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of VMUsageRequestPayload from a JSON string
vm_usage_request_payload_instance = VMUsageRequestPayload.from_json(json)
# print the JSON string representation of the object
print(VMUsageRequestPayload.to_json())

# convert the object into a dict
vm_usage_request_payload_dict = vm_usage_request_payload_instance.to_dict()
# create an instance of VMUsageRequestPayload from a dict
vm_usage_request_payload_from_dict = VMUsageRequestPayload.from_dict(vm_usage_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


