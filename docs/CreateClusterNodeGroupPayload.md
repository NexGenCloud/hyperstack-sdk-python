# CreateClusterNodeGroupPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**flavor_name** | **str** |  | 
**max_count** | **int** |  | [optional] 
**min_count** | **int** |  | [optional] 
**name** | **str** |  | 
**role** | **str** |  | [default to 'worker']

## Example

```python
from hyperstack.models.create_cluster_node_group_payload import CreateClusterNodeGroupPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterNodeGroupPayload from a JSON string
create_cluster_node_group_payload_instance = CreateClusterNodeGroupPayload.from_json(json)
# print the JSON string representation of the object
print(CreateClusterNodeGroupPayload.to_json())

# convert the object into a dict
create_cluster_node_group_payload_dict = create_cluster_node_group_payload_instance.to_dict()
# create an instance of CreateClusterNodeGroupPayload from a dict
create_cluster_node_group_payload_from_dict = CreateClusterNodeGroupPayload.from_dict(create_cluster_node_group_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


