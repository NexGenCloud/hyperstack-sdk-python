# CreateClusterNodeFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**node_group** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.create_cluster_node_fields import CreateClusterNodeFields

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterNodeFields from a JSON string
create_cluster_node_fields_instance = CreateClusterNodeFields.from_json(json)
# print the JSON string representation of the object
print(CreateClusterNodeFields.to_json())

# convert the object into a dict
create_cluster_node_fields_dict = create_cluster_node_fields_instance.to_dict()
# create an instance of CreateClusterNodeFields from a dict
create_cluster_node_fields_from_dict = CreateClusterNodeFields.from_dict(create_cluster_node_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


