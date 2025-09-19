# ClusterFlavorFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** |  | [optional] 
**disk** | **int** |  | [optional] 
**ephemeral** | **int** |  | [optional] 
**features** | **object** |  | [optional] 
**gpu** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**labels** | [**List[LableResonse]**](LableResonse.md) |  | [optional] 
**name** | **str** |  | [optional] 
**ram** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_flavor_fields import ClusterFlavorFields

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFlavorFields from a JSON string
cluster_flavor_fields_instance = ClusterFlavorFields.from_json(json)
# print the JSON string representation of the object
print(ClusterFlavorFields.to_json())

# convert the object into a dict
cluster_flavor_fields_dict = cluster_flavor_fields_instance.to_dict()
# create an instance of ClusterFlavorFields from a dict
cluster_flavor_fields_from_dict = ClusterFlavorFields.from_dict(cluster_flavor_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


