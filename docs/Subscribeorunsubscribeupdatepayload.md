# Subscribeorunsubscribeupdatepayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscribe** | **bool** | &#x60;false&#x60; indicates that the user will no longer receive notifications for this specific threshold, whereas &#x60;true&#x60; signifies that the user will receive notification emails. | 

## Example

```python
from hyperstack.models.subscribeorunsubscribeupdatepayload import Subscribeorunsubscribeupdatepayload

# TODO update the JSON string below
json = "{}"
# create an instance of Subscribeorunsubscribeupdatepayload from a JSON string
subscribeorunsubscribeupdatepayload_instance = Subscribeorunsubscribeupdatepayload.from_json(json)
# print the JSON string representation of the object
print(Subscribeorunsubscribeupdatepayload.to_json())

# convert the object into a dict
subscribeorunsubscribeupdatepayload_dict = subscribeorunsubscribeupdatepayload_instance.to_dict()
# create an instance of Subscribeorunsubscribeupdatepayload from a dict
subscribeorunsubscribeupdatepayload_from_dict = Subscribeorunsubscribeupdatepayload.from_dict(subscribeorunsubscribeupdatepayload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


