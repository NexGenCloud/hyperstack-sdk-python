# UserDefaultChoicesForUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**user_default_choices** | [**List[UserDefaultChoiceForUserFields]**](UserDefaultChoiceForUserFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.user_default_choices_for_user_response import UserDefaultChoicesForUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserDefaultChoicesForUserResponse from a JSON string
user_default_choices_for_user_response_instance = UserDefaultChoicesForUserResponse.from_json(json)
# print the JSON string representation of the object
print(UserDefaultChoicesForUserResponse.to_json())

# convert the object into a dict
user_default_choices_for_user_response_dict = user_default_choices_for_user_response_instance.to_dict()
# create an instance of UserDefaultChoicesForUserResponse from a dict
user_default_choices_for_user_response_from_dict = UserDefaultChoicesForUserResponse.from_dict(user_default_choices_for_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


