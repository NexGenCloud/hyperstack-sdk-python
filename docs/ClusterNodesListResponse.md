# ClusterNodesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**nodes** | [**List[ClusterNodeFields]**](ClusterNodeFields.md) |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_nodes_list_response import ClusterNodesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodesListResponse from a JSON string
cluster_nodes_list_response_instance = ClusterNodesListResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterNodesListResponse.to_json())

# convert the object into a dict
cluster_nodes_list_response_dict = cluster_nodes_list_response_instance.to_dict()
# create an instance of ClusterNodesListResponse from a dict
cluster_nodes_list_response_from_dict = ClusterNodesListResponse.from_dict(cluster_nodes_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


