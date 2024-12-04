# RbacRoleDetailResponseModelFixed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**roles** | [**RbacRoleFields**](RbacRoleFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.rbac_role_detail_response_model_fixed import RbacRoleDetailResponseModelFixed

# TODO update the JSON string below
json = "{}"
# create an instance of RbacRoleDetailResponseModelFixed from a JSON string
rbac_role_detail_response_model_fixed_instance = RbacRoleDetailResponseModelFixed.from_json(json)
# print the JSON string representation of the object
print(RbacRoleDetailResponseModelFixed.to_json())

# convert the object into a dict
rbac_role_detail_response_model_fixed_dict = rbac_role_detail_response_model_fixed_instance.to_dict()
# create an instance of RbacRoleDetailResponseModelFixed from a dict
rbac_role_detail_response_model_fixed_from_dict = RbacRoleDetailResponseModelFixed.from_dict(rbac_role_detail_response_model_fixed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


