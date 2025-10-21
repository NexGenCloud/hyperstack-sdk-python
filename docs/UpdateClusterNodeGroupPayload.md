# UpdateClusterNodeGroupPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_count** | **int** |  | [optional] 
**min_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.update_cluster_node_group_payload import UpdateClusterNodeGroupPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClusterNodeGroupPayload from a JSON string
update_cluster_node_group_payload_instance = UpdateClusterNodeGroupPayload.from_json(json)
# print the JSON string representation of the object
print(UpdateClusterNodeGroupPayload.to_json())

# convert the object into a dict
update_cluster_node_group_payload_dict = update_cluster_node_group_payload_instance.to_dict()
# create an instance of UpdateClusterNodeGroupPayload from a dict
update_cluster_node_group_payload_from_dict = UpdateClusterNodeGroupPayload.from_dict(update_cluster_node_group_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


