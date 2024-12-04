# GetPermissionsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**permissions** | [**List[PermissionFields]**](PermissionFields.md) |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.get_permissions_response_model import GetPermissionsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetPermissionsResponseModel from a JSON string
get_permissions_response_model_instance = GetPermissionsResponseModel.from_json(json)
# print the JSON string representation of the object
print(GetPermissionsResponseModel.to_json())

# convert the object into a dict
get_permissions_response_model_dict = get_permissions_response_model_instance.to_dict()
# create an instance of GetPermissionsResponseModel from a dict
get_permissions_response_model_from_dict = GetPermissionsResponseModel.from_dict(get_permissions_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

