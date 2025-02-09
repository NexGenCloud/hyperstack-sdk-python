# CreateInstancesPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assign_floating_ip** | **bool** | When this field is set to &#x60;true&#x60;, it attaches a [public IP address](https://infrahub-doc.nexgencloud.com/docs/virtual-machines/public-ip)to the virtual machine, enabling internet accessibility. | [optional] 
**callback_url** | **str** | An optional URL where actions performed on the virtual machine will be sent. For additional information on event callbacks, [**click here**](https://infrahub-doc.nexgencloud.com/docs/features/webhooks-callbacks). | [optional] 
**count** | **int** | The number of virtual machines to be created. | 
**create_bootable_volume** | **bool** | Indicates whether to create a bootable volume for the virtual machine. When set to &#x60;true&#x60;, a bootable volume will be created; the default value is &#x60;false&#x60;. | [optional] 
**enable_port_randomization** | **bool** | Indicates whether to enable port randomization.This setting is only effective if &#39;assign_floating_ip&#39; is true. Defaults to true. | [optional] [default to True]
**environment_name** | **str** | The name of the [environment](https://infrahub-doc.nexgencloud.com/docs/features/environments-available-features) in which the virtual machine is to be created. | 
**flavor** | [**FlavorObjectFields**](FlavorObjectFields.md) |  | [optional] 
**flavor_name** | **str** | The name of the GPU hardware configuration ([flavor](https://infrahub-doc.nexgencloud.com/docs/hardware/flavors)) for the virtual machines being created. | 
**image_name** | **str** | The [operating system (OS) image](https://infrahub-doc.nexgencloud.com/docs/virtual-machines/images) name designated for installation on the virtual machine.It also accepts custom, private images, created from [existing snapshots](https://infrahub-doc.nexgencloud.com/docs/virtual-machines/custom-images). | [optional] 
**key_name** | **str** | The name of the existing SSH key pair to be used for secure access to the virtual machine. For additional information on SSH key pairs, [**click here**](https://infrahub-doc.nexgencloud.com/docs/getting-started/create-keypair). | 
**labels** | **List[str]** |  | [optional] 
**name** | **str** | The name of the virtual machine being created. | 
**profile** | [**ProfileObjectFields**](ProfileObjectFields.md) |  | [optional] 
**security_rules** | [**List[CreateSecurityRulePayload]**](CreateSecurityRulePayload.md) |  | [optional] 
**user_data** | **str** | Optional initialization configuration commands to manage the configuration of a virtual machine at launch using cloud-init scripts. For more information about custom VM configuration using cloud-init, [**click here**](https://infrahub-doc.nexgencloud.com/docs/virtual-machines/initialization-configuration). | [optional] 
**volume_name** | **str** | The names of the volume(s) to be attached to the virtual machine being created. | [optional] 

## Example

```python
from hyperstack.models.create_instances_payload import CreateInstancesPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInstancesPayload from a JSON string
create_instances_payload_instance = CreateInstancesPayload.from_json(json)
# print the JSON string representation of the object
print(CreateInstancesPayload.to_json())

# convert the object into a dict
create_instances_payload_dict = create_instances_payload_instance.to_dict()
# create an instance of CreateInstancesPayload from a dict
create_instances_payload_from_dict = CreateInstancesPayload.from_dict(create_instances_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


