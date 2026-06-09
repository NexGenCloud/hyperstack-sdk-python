# UserConsentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consents** | [**List[UserConsent]**](UserConsent.md) |  | [optional] 

## Example

```python
from hyperstack.models.user_consents_response import UserConsentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserConsentsResponse from a JSON string
user_consents_response_instance = UserConsentsResponse.from_json(json)
# print the JSON string representation of the object
print(UserConsentsResponse.to_json())

# convert the object into a dict
user_consents_response_dict = user_consents_response_instance.to_dict()
# create an instance of UserConsentsResponse from a dict
user_consents_response_from_dict = UserConsentsResponse.from_dict(user_consents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


