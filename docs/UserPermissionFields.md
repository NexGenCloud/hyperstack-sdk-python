# UserPermissionFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**permission** | **str** |  | [optional] 
**resource** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.user_permission_fields import UserPermissionFields

# TODO update the JSON string below
json = "{}"
# create an instance of UserPermissionFields from a JSON string
user_permission_fields_instance = UserPermissionFields.from_json(json)
# print the JSON string representation of the object
print(UserPermissionFields.to_json())

# convert the object into a dict
user_permission_fields_dict = user_permission_fields_instance.to_dict()
# create an instance of UserPermissionFields from a dict
user_permission_fields_from_dict = UserPermissionFields.from_dict(user_permission_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


