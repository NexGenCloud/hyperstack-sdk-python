# ObjectStorageBucketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**endpoint** | **str** |  | 
**name** | **str** |  | 
**num_objects** | **int** | Number of objects | 
**region** | [**ObjectStorageRegionsEnum**](ObjectStorageRegionsEnum.md) |  | 
**size_bytes** | **int** | Accumulated size in bytes | 
**size_bytes_actual** | **int** | Size utilized in bytes | 

## Example

```python
from hyperstack.models.object_storage_bucket_response import ObjectStorageBucketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStorageBucketResponse from a JSON string
object_storage_bucket_response_instance = ObjectStorageBucketResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectStorageBucketResponse.to_json())

# convert the object into a dict
object_storage_bucket_response_dict = object_storage_bucket_response_instance.to_dict()
# create an instance of ObjectStorageBucketResponse from a dict
object_storage_bucket_response_from_dict = ObjectStorageBucketResponse.from_dict(object_storage_bucket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


