# ObjectStorageRegionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regions** | [**List[ObjectStorageRegionResponse]**](ObjectStorageRegionResponse.md) |  | 

## Example

```python
from hyperstack.models.object_storage_region_list_response import ObjectStorageRegionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStorageRegionListResponse from a JSON string
object_storage_region_list_response_instance = ObjectStorageRegionListResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectStorageRegionListResponse.to_json())

# convert the object into a dict
object_storage_region_list_response_dict = object_storage_region_list_response_instance.to_dict()
# create an instance of ObjectStorageRegionListResponse from a dict
object_storage_region_list_response_from_dict = ObjectStorageRegionListResponse.from_dict(object_storage_region_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


