# ClusterEventsFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**reason** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_events_fields import ClusterEventsFields

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEventsFields from a JSON string
cluster_events_fields_instance = ClusterEventsFields.from_json(json)
# print the JSON string representation of the object
print(ClusterEventsFields.to_json())

# convert the object into a dict
cluster_events_fields_dict = cluster_events_fields_instance.to_dict()
# create an instance of ClusterEventsFields from a dict
cluster_events_fields_from_dict = ClusterEventsFields.from_dict(cluster_events_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


