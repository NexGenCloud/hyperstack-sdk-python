# ClusterRestoreResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_nodes** | [**List[ClusterRestoreFailedNode]**](ClusterRestoreFailedNode.md) |  | [optional] 
**message** | **str** |  | [optional] 
**restoring_nodes** | **List[int]** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_restore_response import ClusterRestoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRestoreResponse from a JSON string
cluster_restore_response_instance = ClusterRestoreResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterRestoreResponse.to_json())

# convert the object into a dict
cluster_restore_response_dict = cluster_restore_response_instance.to_dict()
# create an instance of ClusterRestoreResponse from a dict
cluster_restore_response_from_dict = ClusterRestoreResponse.from_dict(cluster_restore_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


