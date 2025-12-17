# ObjectStoragePaginationMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**current_page** | **int** |  | 
**total_pages** | **int** |  | 

## Example

```python
from hyperstack.models.object_storage_pagination_meta import ObjectStoragePaginationMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStoragePaginationMeta from a JSON string
object_storage_pagination_meta_instance = ObjectStoragePaginationMeta.from_json(json)
# print the JSON string representation of the object
print(ObjectStoragePaginationMeta.to_json())

# convert the object into a dict
object_storage_pagination_meta_dict = object_storage_pagination_meta_instance.to_dict()
# create an instance of ObjectStoragePaginationMeta from a dict
object_storage_pagination_meta_from_dict = ObjectStoragePaginationMeta.from_dict(object_storage_pagination_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


