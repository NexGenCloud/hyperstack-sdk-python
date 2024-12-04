# ClusterEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_events** | [**List[ClusterEventsFields]**](ClusterEventsFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.cluster_events import ClusterEvents

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEvents from a JSON string
cluster_events_instance = ClusterEvents.from_json(json)
# print the JSON string representation of the object
print(ClusterEvents.to_json())

# convert the object into a dict
cluster_events_dict = cluster_events_instance.to_dict()
# create an instance of ClusterEvents from a dict
cluster_events_from_dict = ClusterEvents.from_dict(cluster_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


