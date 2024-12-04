# CreateFirewallRulePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | The direction of traffic that the firewall rule applies to. | 
**ethertype** | **str** | The Ethernet type associated with the rule. | 
**port_range_max** | **int** | The maximum port number in the range of ports to be allowed by the firewall rule. | [optional] 
**port_range_min** | **int** | The minimum port number in the range of ports to be allowed by the firewall rule. | [optional] 
**protocol** | **str** | The network protocol associated with the rule. Call the [&#x60;GET /core/sg-rules-protocols&#x60;](https://infrahub-api-doc.nexgencloud.com/#get-/core/sg-rules-protocols) endpoint to retrieve a list of permitted network protocols. | 
**remote_ip_prefix** | **str** | The IP address range that is allowed to access the specified port. Use \&quot;0.0.0.0/0\&quot; to allow any IP address. | 

## Example

```python
from hyperstack.models.create_firewall_rule_payload import CreateFirewallRulePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFirewallRulePayload from a JSON string
create_firewall_rule_payload_instance = CreateFirewallRulePayload.from_json(json)
# print the JSON string representation of the object
print(CreateFirewallRulePayload.to_json())

# convert the object into a dict
create_firewall_rule_payload_dict = create_firewall_rule_payload_instance.to_dict()
# create an instance of CreateFirewallRulePayload from a dict
create_firewall_rule_payload_from_dict = CreateFirewallRulePayload.from_dict(create_firewall_rule_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


