# ObjectStorageAccessKeyCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** |  | 
**created_at** | **datetime** |  | 
**description** | **object** |  | [optional] 
**id** | **int** |  | 
**region** | [**ObjectStorageRegionsEnum**](ObjectStorageRegionsEnum.md) |  | 
**secret_key** | **str** |  | 
**user_id** | **int** |  | 

## Example

```python
from hyperstack.models.object_storage_access_key_create_response import ObjectStorageAccessKeyCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStorageAccessKeyCreateResponse from a JSON string
object_storage_access_key_create_response_instance = ObjectStorageAccessKeyCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectStorageAccessKeyCreateResponse.to_json())

# convert the object into a dict
object_storage_access_key_create_response_dict = object_storage_access_key_create_response_instance.to_dict()
# create an instance of ObjectStorageAccessKeyCreateResponse from a dict
object_storage_access_key_create_response_from_dict = ObjectStorageAccessKeyCreateResponse.from_dict(object_storage_access_key_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


