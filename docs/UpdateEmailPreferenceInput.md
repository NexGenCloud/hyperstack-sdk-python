# UpdateEmailPreferenceInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opted_in** | **bool** | Set opted_in status | 

## Example

```python
from hyperstack.models.update_email_preference_input import UpdateEmailPreferenceInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmailPreferenceInput from a JSON string
update_email_preference_input_instance = UpdateEmailPreferenceInput.from_json(json)
# print the JSON string representation of the object
print(UpdateEmailPreferenceInput.to_json())

# convert the object into a dict
update_email_preference_input_dict = update_email_preference_input_instance.to_dict()
# create an instance of UpdateEmailPreferenceInput from a dict
update_email_preference_input_from_dict = UpdateEmailPreferenceInput.from_dict(update_email_preference_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


