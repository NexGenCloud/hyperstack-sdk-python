# CreateClusterPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_name** | **str** |  | 
**image_name** | **str** |  | 
**keypair_name** | **str** |  | 
**kubernetes_version** | **str** |  | 
**master_flavor_name** | **str** |  | 
**name** | **str** |  | 
**node_count** | **int** |  | 
**node_flavor_name** | **str** |  | 

## Example

```python
from hyperstack.models.create_cluster_payload import CreateClusterPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterPayload from a JSON string
create_cluster_payload_instance = CreateClusterPayload.from_json(json)
# print the JSON string representation of the object
print(CreateClusterPayload.to_json())

# convert the object into a dict
create_cluster_payload_dict = create_cluster_payload_instance.to_dict()
# create an instance of CreateClusterPayload from a dict
create_cluster_payload_from_dict = CreateClusterPayload.from_dict(create_cluster_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


