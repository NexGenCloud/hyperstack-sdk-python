# UserConsentEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**consent_id** | **int** |  | [optional] 
**consent_method** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.user_consent_event import UserConsentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UserConsentEvent from a JSON string
user_consent_event_instance = UserConsentEvent.from_json(json)
# print the JSON string representation of the object
print(UserConsentEvent.to_json())

# convert the object into a dict
user_consent_event_dict = user_consent_event_instance.to_dict()
# create an instance of UserConsentEvent from a dict
user_consent_event_from_dict = UserConsentEvent.from_dict(user_consent_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


