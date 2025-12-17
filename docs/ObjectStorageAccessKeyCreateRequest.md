# ObjectStorageAccessKeyCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **object** |  | [optional] 
**region** | [**ObjectStorageRegionsEnum**](ObjectStorageRegionsEnum.md) |  | 

## Example

```python
from hyperstack.models.object_storage_access_key_create_request import ObjectStorageAccessKeyCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStorageAccessKeyCreateRequest from a JSON string
object_storage_access_key_create_request_instance = ObjectStorageAccessKeyCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ObjectStorageAccessKeyCreateRequest.to_json())

# convert the object into a dict
object_storage_access_key_create_request_dict = object_storage_access_key_create_request_instance.to_dict()
# create an instance of ObjectStorageAccessKeyCreateRequest from a dict
object_storage_access_key_create_request_from_dict = ObjectStorageAccessKeyCreateRequest.from_dict(object_storage_access_key_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


