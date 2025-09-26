# SubscribeOrUnsubscribeUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscribe** | **bool** | &#x60;false&#x60; indicates that the user will no longer receive notifications for this specific threshold, whereas &#x60;true&#x60; signifies that the user will receive notification emails. | 

## Example

```python
from hyperstack.models.subscribe_or_unsubscribe_update_payload import SubscribeOrUnsubscribeUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribeOrUnsubscribeUpdatePayload from a JSON string
subscribe_or_unsubscribe_update_payload_instance = SubscribeOrUnsubscribeUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(SubscribeOrUnsubscribeUpdatePayload.to_json())

# convert the object into a dict
subscribe_or_unsubscribe_update_payload_dict = subscribe_or_unsubscribe_update_payload_instance.to_dict()
# create an instance of SubscribeOrUnsubscribeUpdatePayload from a dict
subscribe_or_unsubscribe_update_payload_from_dict = SubscribeOrUnsubscribeUpdatePayload.from_dict(subscribe_or_unsubscribe_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


