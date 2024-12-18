# PaginationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.pagination_data import PaginationData

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationData from a JSON string
pagination_data_instance = PaginationData.from_json(json)
# print the JSON string representation of the object
print(PaginationData.to_json())

# convert the object into a dict
pagination_data_dict = pagination_data_instance.to_dict()
# create an instance of PaginationData from a dict
pagination_data_from_dict = PaginationData.from_dict(pagination_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


