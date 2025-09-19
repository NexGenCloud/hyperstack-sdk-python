# ClusterVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**image** | **object** |  | [optional] 
**region** | **object** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_version import ClusterVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterVersion from a JSON string
cluster_version_instance = ClusterVersion.from_json(json)
# print the JSON string representation of the object
print(ClusterVersion.to_json())

# convert the object into a dict
cluster_version_dict = cluster_version_instance.to_dict()
# create an instance of ClusterVersion from a dict
cluster_version_from_dict = ClusterVersion.from_dict(cluster_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


