# ClusterListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[ClusterFields]**](ClusterFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_list_response import ClusterListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterListResponse from a JSON string
cluster_list_response_instance = ClusterListResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterListResponse.to_json())

# convert the object into a dict
cluster_list_response_dict = cluster_list_response_instance.to_dict()
# create an instance of ClusterListResponse from a dict
cluster_list_response_from_dict = ClusterListResponse.from_dict(cluster_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


