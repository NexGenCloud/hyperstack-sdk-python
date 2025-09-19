# UserOrganizationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**List[OrganizationFields]**](OrganizationFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.user_organizations_response import UserOrganizationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserOrganizationsResponse from a JSON string
user_organizations_response_instance = UserOrganizationsResponse.from_json(json)
# print the JSON string representation of the object
print(UserOrganizationsResponse.to_json())

# convert the object into a dict
user_organizations_response_dict = user_organizations_response_instance.to_dict()
# create an instance of UserOrganizationsResponse from a dict
user_organizations_response_from_dict = UserOrganizationsResponse.from_dict(user_organizations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


