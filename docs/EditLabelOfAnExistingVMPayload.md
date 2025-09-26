# EditLabelOfAnExistingVMPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** | Multiple labels can be added by separating with spaces | [optional] 

## Example

```python
from hyperstack.models.edit_label_of_an_existing_vm_payload import EditLabelOfAnExistingVMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EditLabelOfAnExistingVMPayload from a JSON string
edit_label_of_an_existing_vm_payload_instance = EditLabelOfAnExistingVMPayload.from_json(json)
# print the JSON string representation of the object
print(EditLabelOfAnExistingVMPayload.to_json())

# convert the object into a dict
edit_label_of_an_existing_vm_payload_dict = edit_label_of_an_existing_vm_payload_instance.to_dict()
# create an instance of EditLabelOfAnExistingVMPayload from a dict
edit_label_of_an_existing_vm_payload_from_dict = EditLabelOfAnExistingVMPayload.from_dict(edit_label_of_an_existing_vm_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


