# ObjectStorageAccessKeyUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 

## Example

```python
from hyperstack.models.object_storage_access_key_update_request import ObjectStorageAccessKeyUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStorageAccessKeyUpdateRequest from a JSON string
object_storage_access_key_update_request_instance = ObjectStorageAccessKeyUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ObjectStorageAccessKeyUpdateRequest.to_json())

# convert the object into a dict
object_storage_access_key_update_request_dict = object_storage_access_key_update_request_instance.to_dict()
# create an instance of ObjectStorageAccessKeyUpdateRequest from a dict
object_storage_access_key_update_request_from_dict = ObjectStorageAccessKeyUpdateRequest.from_dict(object_storage_access_key_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


