# ObjectStorageErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_reason** | **str** |  | 
**message** | **str** |  | 
**status** | **bool** |  | [optional] [default to False]

## Example

```python
from hyperstack.models.object_storage_error_response import ObjectStorageErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStorageErrorResponse from a JSON string
object_storage_error_response_instance = ObjectStorageErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectStorageErrorResponse.to_json())

# convert the object into a dict
object_storage_error_response_dict = object_storage_error_response_instance.to_dict()
# create an instance of ObjectStorageErrorResponse from a dict
object_storage_error_response_from_dict = ObjectStorageErrorResponse.from_dict(object_storage_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


