# ClusterNodeGroupsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**node_group** | [**ClusterNodeGroupFields**](ClusterNodeGroupFields.md) |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_node_groups_get_response import ClusterNodeGroupsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeGroupsGetResponse from a JSON string
cluster_node_groups_get_response_instance = ClusterNodeGroupsGetResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterNodeGroupsGetResponse.to_json())

# convert the object into a dict
cluster_node_groups_get_response_dict = cluster_node_groups_get_response_instance.to_dict()
# create an instance of ClusterNodeGroupsGetResponse from a dict
cluster_node_groups_get_response_from_dict = ClusterNodeGroupsGetResponse.from_dict(cluster_node_groups_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


