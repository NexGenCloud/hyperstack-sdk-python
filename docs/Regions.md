# Regions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**regions** | [**List[RegionFields]**](RegionFields.md) |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.regions import Regions

# TODO update the JSON string below
json = "{}"
# create an instance of Regions from a JSON string
regions_instance = Regions.from_json(json)
# print the JSON string representation of the object
print(Regions.to_json())

# convert the object into a dict
regions_dict = regions_instance.to_dict()
# create an instance of Regions from a dict
regions_from_dict = Regions.from_dict(regions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


