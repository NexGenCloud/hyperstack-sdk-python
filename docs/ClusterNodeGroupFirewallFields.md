# ClusterNodeGroupFirewallFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_node_group_firewall_fields import ClusterNodeGroupFirewallFields

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeGroupFirewallFields from a JSON string
cluster_node_group_firewall_fields_instance = ClusterNodeGroupFirewallFields.from_json(json)
# print the JSON string representation of the object
print(ClusterNodeGroupFirewallFields.to_json())

# convert the object into a dict
cluster_node_group_firewall_fields_dict = cluster_node_group_firewall_fields_instance.to_dict()
# create an instance of ClusterNodeGroupFirewallFields from a dict
cluster_node_group_firewall_fields_from_dict = ClusterNodeGroupFirewallFields.from_dict(cluster_node_group_firewall_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


