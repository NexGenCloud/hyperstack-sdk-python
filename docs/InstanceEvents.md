# InstanceEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_events** | [**List[InstanceEventsFields]**](InstanceEventsFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.instance_events import InstanceEvents

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceEvents from a JSON string
instance_events_instance = InstanceEvents.from_json(json)
# print the JSON string representation of the object
print(InstanceEvents.to_json())

# convert the object into a dict
instance_events_dict = instance_events_instance.to_dict()
# create an instance of InstanceEvents from a dict
instance_events_from_dict = InstanceEvents.from_dict(instance_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


