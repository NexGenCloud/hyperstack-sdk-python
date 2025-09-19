# UserInfoPostPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_address1** | **str** |  | [optional] 
**billing_address2** | **str** |  | [optional] 
**business** | **bool** |  | 
**company_name** | **str** |  | [optional] 
**country** | **str** |  | 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**zip_code** | **str** |  | 

## Example

```python
from hyperstack.models.user_info_post_payload import UserInfoPostPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfoPostPayload from a JSON string
user_info_post_payload_instance = UserInfoPostPayload.from_json(json)
# print the JSON string representation of the object
print(UserInfoPostPayload.to_json())

# convert the object into a dict
user_info_post_payload_dict = user_info_post_payload_instance.to_dict()
# create an instance of UserInfoPostPayload from a dict
user_info_post_payload_from_dict = UserInfoPostPayload.from_dict(user_info_post_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


