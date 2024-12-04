# RegionFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.region_fields import RegionFields

# TODO update the JSON string below
json = "{}"
# create an instance of RegionFields from a JSON string
region_fields_instance = RegionFields.from_json(json)
# print the JSON string representation of the object
print(RegionFields.to_json())

# convert the object into a dict
region_fields_dict = region_fields_instance.to_dict()
# create an instance of RegionFields from a dict
region_fields_from_dict = RegionFields.from_dict(region_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


