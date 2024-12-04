# FirewallAttachmentVMModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**environment** | **str** |  | [optional] 
**flavor** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.firewall_attachment_vm_model import FirewallAttachmentVMModel

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallAttachmentVMModel from a JSON string
firewall_attachment_vm_model_instance = FirewallAttachmentVMModel.from_json(json)
# print the JSON string representation of the object
print(FirewallAttachmentVMModel.to_json())

# convert the object into a dict
firewall_attachment_vm_model_dict = firewall_attachment_vm_model_instance.to_dict()
# create an instance of FirewallAttachmentVMModel from a dict
firewall_attachment_vm_model_from_dict = FirewallAttachmentVMModel.from_dict(firewall_attachment_vm_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


