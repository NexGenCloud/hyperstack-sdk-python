# InternalInstanceFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_source** | **str** |  | [optional] 
**callback_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**environment** | [**InternalEnvironmentFields**](InternalEnvironmentFields.md) |  | [optional] 
**fixed_ip** | **str** |  | [optional] 
**flavor** | [**InternalInstanceFlavorFields**](InternalInstanceFlavorFields.md) |  | [optional] 
**floating_ip** | **str** |  | [optional] 
**floating_ip_status** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**image** | [**InternalInstanceImageFields**](InternalInstanceImageFields.md) |  | [optional] 
**keypair** | [**InternalInstanceKeypairFields**](InternalInstanceKeypairFields.md) |  | [optional] 
**name** | **str** |  | [optional] 
**openstack_id** | **str** |  | [optional] 
**power_state** | **str** |  | [optional] 
**security_rules** | [**List[InternalSecurityRulesFieldsForInstance]**](InternalSecurityRulesFieldsForInstance.md) |  | [optional] 
**status** | **str** |  | [optional] 
**user_data** | **str** |  | [optional] 
**vm_state** | **str** |  | [optional] 
**volume_attachments** | [**List[InternalVolumeAttachmentFields]**](InternalVolumeAttachmentFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.internal_instance_fields import InternalInstanceFields

# TODO update the JSON string below
json = "{}"
# create an instance of InternalInstanceFields from a JSON string
internal_instance_fields_instance = InternalInstanceFields.from_json(json)
# print the JSON string representation of the object
print(InternalInstanceFields.to_json())

# convert the object into a dict
internal_instance_fields_dict = internal_instance_fields_instance.to_dict()
# create an instance of InternalInstanceFields from a dict
internal_instance_fields_from_dict = InternalInstanceFields.from_dict(internal_instance_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


