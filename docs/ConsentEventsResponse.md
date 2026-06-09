# ConsentEventsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent** | [**UserConsent**](UserConsent.md) |  | [optional] 
**events** | [**List[UserConsentEvent]**](UserConsentEvent.md) |  | [optional] 

## Example

```python
from hyperstack.models.consent_events_response import ConsentEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentEventsResponse from a JSON string
consent_events_response_instance = ConsentEventsResponse.from_json(json)
# print the JSON string representation of the object
print(ConsentEventsResponse.to_json())

# convert the object into a dict
consent_events_response_dict = consent_events_response_instance.to_dict()
# create an instance of ConsentEventsResponse from a dict
consent_events_response_from_dict = ConsentEventsResponse.from_dict(consent_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


