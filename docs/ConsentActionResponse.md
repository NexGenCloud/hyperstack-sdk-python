# ConsentActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent** | [**UserConsent**](UserConsent.md) |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.consent_action_response import ConsentActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentActionResponse from a JSON string
consent_action_response_instance = ConsentActionResponse.from_json(json)
# print the JSON string representation of the object
print(ConsentActionResponse.to_json())

# convert the object into a dict
consent_action_response_dict = consent_action_response_instance.to_dict()
# create an instance of ConsentActionResponse from a dict
consent_action_response_from_dict = ConsentActionResponse.from_dict(consent_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


