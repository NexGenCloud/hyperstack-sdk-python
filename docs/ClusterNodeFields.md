# ClusterNodeFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**instance** | [**ClusterNodeInstanceFields**](ClusterNodeInstanceFields.md) |  | [optional] 
**is_bastion** | **bool** |  | [optional] 
**node_group_id** | **int** |  | [optional] 
**node_group_name** | **str** |  | [optional] 
**requires_public_ip** | **bool** |  | [optional] 
**role** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_reason** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_node_fields import ClusterNodeFields

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeFields from a JSON string
cluster_node_fields_instance = ClusterNodeFields.from_json(json)
# print the JSON string representation of the object
print(ClusterNodeFields.to_json())

# convert the object into a dict
cluster_node_fields_dict = cluster_node_fields_instance.to_dict()
# create an instance of ClusterNodeFields from a dict
cluster_node_fields_from_dict = ClusterNodeFields.from_dict(cluster_node_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


