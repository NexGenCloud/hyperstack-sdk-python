# RbacRoleFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**permissions** | [**List[RolePermissionFields]**](RolePermissionFields.md) |  | [optional] 
**policies** | [**List[RolePolicyFields]**](RolePolicyFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.rbac_role_fields import RbacRoleFields

# TODO update the JSON string below
json = "{}"
# create an instance of RbacRoleFields from a JSON string
rbac_role_fields_instance = RbacRoleFields.from_json(json)
# print the JSON string representation of the object
print(RbacRoleFields.to_json())

# convert the object into a dict
rbac_role_fields_dict = rbac_role_fields_instance.to_dict()
# create an instance of RbacRoleFields from a dict
rbac_role_fields_from_dict = RbacRoleFields.from_dict(rbac_role_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


