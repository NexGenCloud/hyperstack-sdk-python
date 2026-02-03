# CompatibleFlavor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | **object** | JSON constraints object | [optional] 
**flavor_id** | **int** |  | [optional] 
**flavor_name** | **str** |  | [optional] 
**link_type** | **str** | Either &#39;hard&#39; or &#39;soft&#39; | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.compatible_flavor import CompatibleFlavor

# TODO update the JSON string below
json = "{}"
# create an instance of CompatibleFlavor from a JSON string
compatible_flavor_instance = CompatibleFlavor.from_json(json)
# print the JSON string representation of the object
print(CompatibleFlavor.to_json())

# convert the object into a dict
compatible_flavor_dict = compatible_flavor_instance.to_dict()
# create an instance of CompatibleFlavor from a dict
compatible_flavor_from_dict = CompatibleFlavor.from_dict(compatible_flavor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


