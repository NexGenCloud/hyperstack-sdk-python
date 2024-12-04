# InstanceFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**environment** | [**InstanceEnvironmentFields**](InstanceEnvironmentFields.md) |  | [optional] 
**fixed_ip** | **str** |  | [optional] 
**flavor** | [**InstanceFlavorFields**](InstanceFlavorFields.md) |  | [optional] 
**floating_ip** | **str** |  | [optional] 
**floating_ip_status** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**image** | [**InstanceImageFields**](InstanceImageFields.md) |  | [optional] 
**keypair** | [**InstanceKeypairFields**](InstanceKeypairFields.md) |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**locked** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**os** | **str** |  | [optional] 
**power_state** | **str** |  | [optional] 
**security_rules** | [**List[SecurityRulesFieldsforInstance]**](SecurityRulesFieldsforInstance.md) |  | [optional] 
**status** | **str** |  | [optional] 
**vm_state** | **str** |  | [optional] 
**volume_attachments** | [**List[VolumeAttachmentFields]**](VolumeAttachmentFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.instance_fields import InstanceFields

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceFields from a JSON string
instance_fields_instance = InstanceFields.from_json(json)
# print the JSON string representation of the object
print(InstanceFields.to_json())

# convert the object into a dict
instance_fields_dict = instance_fields_instance.to_dict()
# create an instance of InstanceFields from a dict
instance_fields_from_dict = InstanceFields.from_dict(instance_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


