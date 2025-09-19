# AccessTokenField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.access_token_field import AccessTokenField

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenField from a JSON string
access_token_field_instance = AccessTokenField.from_json(json)
# print the JSON string representation of the object
print(AccessTokenField.to_json())

# convert the object into a dict
access_token_field_dict = access_token_field_instance.to_dict()
# create an instance of AccessTokenField from a dict
access_token_field_from_dict = AccessTokenField.from_dict(access_token_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


