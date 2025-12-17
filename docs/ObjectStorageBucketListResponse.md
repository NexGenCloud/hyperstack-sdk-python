# ObjectStorageBucketListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | [**List[ObjectStorageBucketResponse]**](ObjectStorageBucketResponse.md) |  | 

## Example

```python
from hyperstack.models.object_storage_bucket_list_response import ObjectStorageBucketListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStorageBucketListResponse from a JSON string
object_storage_bucket_list_response_instance = ObjectStorageBucketListResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectStorageBucketListResponse.to_json())

# convert the object into a dict
object_storage_bucket_list_response_dict = object_storage_bucket_list_response_instance.to_dict()
# create an instance of ObjectStorageBucketListResponse from a dict
object_storage_bucket_list_response_from_dict = ObjectStorageBucketListResponse.from_dict(object_storage_bucket_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


