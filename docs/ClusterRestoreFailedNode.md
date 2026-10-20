# ClusterRestoreFailedNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_restore_failed_node import ClusterRestoreFailedNode

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRestoreFailedNode from a JSON string
cluster_restore_failed_node_instance = ClusterRestoreFailedNode.from_json(json)
# print the JSON string representation of the object
print(ClusterRestoreFailedNode.to_json())

# convert the object into a dict
cluster_restore_failed_node_dict = cluster_restore_failed_node_instance.to_dict()
# create an instance of ClusterRestoreFailedNode from a dict
cluster_restore_failed_node_from_dict = ClusterRestoreFailedNode.from_dict(cluster_restore_failed_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


