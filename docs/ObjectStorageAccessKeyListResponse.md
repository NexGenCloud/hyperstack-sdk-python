# ObjectStorageAccessKeyListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_keys** | [**List[ObjectStorageAccessKeyResponse]**](ObjectStorageAccessKeyResponse.md) |  | 
**meta** | [**ObjectStoragePaginationMeta**](ObjectStoragePaginationMeta.md) |  | 

## Example

```python
from hyperstack.models.object_storage_access_key_list_response import ObjectStorageAccessKeyListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStorageAccessKeyListResponse from a JSON string
object_storage_access_key_list_response_instance = ObjectStorageAccessKeyListResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectStorageAccessKeyListResponse.to_json())

# convert the object into a dict
object_storage_access_key_list_response_dict = object_storage_access_key_list_response_instance.to_dict()
# create an instance of ObjectStorageAccessKeyListResponse from a dict
object_storage_access_key_list_response_from_dict = ObjectStorageAccessKeyListResponse.from_dict(object_storage_access_key_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


