# ClusterNodeInstanceFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **int** |  | [optional] 
**fixed_ip** | **str** |  | [optional] 
**floating_ip** | **str** |  | [optional] 
**floating_ip_status** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**image_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_node_instance_fields import ClusterNodeInstanceFields

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeInstanceFields from a JSON string
cluster_node_instance_fields_instance = ClusterNodeInstanceFields.from_json(json)
# print the JSON string representation of the object
print(ClusterNodeInstanceFields.to_json())

# convert the object into a dict
cluster_node_instance_fields_dict = cluster_node_instance_fields_instance.to_dict()
# create an instance of ClusterNodeInstanceFields from a dict
cluster_node_instance_fields_from_dict = ClusterNodeInstanceFields.from_dict(cluster_node_instance_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


