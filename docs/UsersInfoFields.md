# UsersInfoFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_address1** | **str** |  | [optional] 
**billing_address2** | **str** |  | [optional] 
**business** | **bool** |  | [optional] 
**company_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**phone** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.users_info_fields import UsersInfoFields

# TODO update the JSON string below
json = "{}"
# create an instance of UsersInfoFields from a JSON string
users_info_fields_instance = UsersInfoFields.from_json(json)
# print the JSON string representation of the object
print(UsersInfoFields.to_json())

# convert the object into a dict
users_info_fields_dict = users_info_fields_instance.to_dict()
# create an instance of UsersInfoFields from a dict
users_info_fields_from_dict = UsersInfoFields.from_dict(users_info_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


