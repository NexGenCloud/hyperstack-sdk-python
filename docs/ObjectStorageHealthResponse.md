# ObjectStorageHealthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 

## Example

```python
from hyperstack.models.object_storage_health_response import ObjectStorageHealthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStorageHealthResponse from a JSON string
object_storage_health_response_instance = ObjectStorageHealthResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectStorageHealthResponse.to_json())

# convert the object into a dict
object_storage_health_response_dict = object_storage_health_response_instance.to_dict()
# create an instance of ObjectStorageHealthResponse from a dict
object_storage_health_response_from_dict = ObjectStorageHealthResponse.from_dict(object_storage_health_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


