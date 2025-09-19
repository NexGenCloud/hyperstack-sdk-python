# ClusterNodeGroupsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**node_groups** | [**List[ClusterNodeGroupFields]**](ClusterNodeGroupFields.md) |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_node_groups_list_response import ClusterNodeGroupsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeGroupsListResponse from a JSON string
cluster_node_groups_list_response_instance = ClusterNodeGroupsListResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterNodeGroupsListResponse.to_json())

# convert the object into a dict
cluster_node_groups_list_response_dict = cluster_node_groups_list_response_instance.to_dict()
# create an instance of ClusterNodeGroupsListResponse from a dict
cluster_node_groups_list_response_from_dict = ClusterNodeGroupsListResponse.from_dict(cluster_node_groups_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


