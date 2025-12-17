# ObjectStorageAccessKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** |  | 
**created_at** | **datetime** |  | 
**description** | **object** |  | [optional] 
**id** | **int** |  | 
**region** | [**ObjectStorageRegionsEnum**](ObjectStorageRegionsEnum.md) |  | 
**user_id** | **int** |  | 

## Example

```python
from hyperstack.models.object_storage_access_key_response import ObjectStorageAccessKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStorageAccessKeyResponse from a JSON string
object_storage_access_key_response_instance = ObjectStorageAccessKeyResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectStorageAccessKeyResponse.to_json())

# convert the object into a dict
object_storage_access_key_response_dict = object_storage_access_key_response_instance.to_dict()
# create an instance of ObjectStorageAccessKeyResponse from a dict
object_storage_access_key_response_from_dict = ObjectStorageAccessKeyResponse.from_dict(object_storage_access_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


