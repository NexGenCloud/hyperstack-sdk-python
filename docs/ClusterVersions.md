# ClusterVersions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**versions** | **List[str]** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_versions import ClusterVersions

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterVersions from a JSON string
cluster_versions_instance = ClusterVersions.from_json(json)
# print the JSON string representation of the object
print(ClusterVersions.to_json())

# convert the object into a dict
cluster_versions_dict = cluster_versions_instance.to_dict()
# create an instance of ClusterVersions from a dict
cluster_versions_from_dict = ClusterVersions.from_dict(cluster_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


