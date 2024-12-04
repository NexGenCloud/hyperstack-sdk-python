# ClusterFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_address** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**environment_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**keypair_name** | **str** |  | [optional] 
**kube_config** | **str** |  | [optional] 
**kubernetes_version** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**node_count** | **int** |  | [optional] 
**node_flavor** | [**InstanceFlavorFields**](InstanceFlavorFields.md) |  | [optional] 
**status** | **str** |  | [optional] 
**status_reason** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_fields import ClusterFields

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFields from a JSON string
cluster_fields_instance = ClusterFields.from_json(json)
# print the JSON string representation of the object
print(ClusterFields.to_json())

# convert the object into a dict
cluster_fields_dict = cluster_fields_instance.to_dict()
# create an instance of ClusterFields from a dict
cluster_fields_from_dict = ClusterFields.from_dict(cluster_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


