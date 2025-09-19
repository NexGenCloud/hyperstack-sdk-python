# ClusterNodeGroupFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**flavor** | [**ClusterFlavorFields**](ClusterFlavorFields.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_node_group_fields import ClusterNodeGroupFields

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeGroupFields from a JSON string
cluster_node_group_fields_instance = ClusterNodeGroupFields.from_json(json)
# print the JSON string representation of the object
print(ClusterNodeGroupFields.to_json())

# convert the object into a dict
cluster_node_group_fields_dict = cluster_node_group_fields_instance.to_dict()
# create an instance of ClusterNodeGroupFields from a dict
cluster_node_group_fields_from_dict = ClusterNodeGroupFields.from_dict(cluster_node_group_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


