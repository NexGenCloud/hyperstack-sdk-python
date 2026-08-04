# EmailPreferencesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_categories** | [**List[EmailCategory]**](EmailCategory.md) |  | [optional] 

## Example

```python
from hyperstack.models.email_preferences_response import EmailPreferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailPreferencesResponse from a JSON string
email_preferences_response_instance = EmailPreferencesResponse.from_json(json)
# print the JSON string representation of the object
print(EmailPreferencesResponse.to_json())

# convert the object into a dict
email_preferences_response_dict = email_preferences_response_instance.to_dict()
# create an instance of EmailPreferencesResponse from a dict
email_preferences_response_from_dict = EmailPreferencesResponse.from_dict(email_preferences_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


