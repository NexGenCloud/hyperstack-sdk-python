# ClusterNodeGroupsCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**node_group** | [**ClusterNodeGroupFields**](ClusterNodeGroupFields.md) |  | [optional] 
**nodes** | [**List[ClusterNodeFields]**](ClusterNodeFields.md) |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_node_groups_create_response import ClusterNodeGroupsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeGroupsCreateResponse from a JSON string
cluster_node_groups_create_response_instance = ClusterNodeGroupsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterNodeGroupsCreateResponse.to_json())

# convert the object into a dict
cluster_node_groups_create_response_dict = cluster_node_groups_create_response_instance.to_dict()
# create an instance of ClusterNodeGroupsCreateResponse from a dict
cluster_node_groups_create_response_from_dict = ClusterNodeGroupsCreateResponse.from_dict(cluster_node_groups_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


