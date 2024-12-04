# CreateFirewallPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the firewall. | [optional] 
**environment_id** | **int** | ID of the environment. | 
**name** | **str** | Name of the firewall. | 

## Example

```python
from hyperstack.models.create_firewall_payload import CreateFirewallPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFirewallPayload from a JSON string
create_firewall_payload_instance = CreateFirewallPayload.from_json(json)
# print the JSON string representation of the object
print(CreateFirewallPayload.to_json())

# convert the object into a dict
create_firewall_payload_dict = create_firewall_payload_instance.to_dict()
# create an instance of CreateFirewallPayload from a dict
create_firewall_payload_from_dict = CreateFirewallPayload.from_dict(create_firewall_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


