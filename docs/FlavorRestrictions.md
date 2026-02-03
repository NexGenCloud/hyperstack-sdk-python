# FlavorRestrictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compatible_flavors** | [**List[CompatibleFlavor]**](CompatibleFlavor.md) | List of compatible flavors with their link metadata | [optional] 
**has_flavor_restrictions** | **bool** | Whether the image has any flavor restrictions | [optional] 
**restriction_type** | **str** | Either &#39;hard&#39;, &#39;soft&#39;, or null if no restrictions | [optional] 

## Example

```python
from hyperstack.models.flavor_restrictions import FlavorRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorRestrictions from a JSON string
flavor_restrictions_instance = FlavorRestrictions.from_json(json)
# print the JSON string representation of the object
print(FlavorRestrictions.to_json())

# convert the object into a dict
flavor_restrictions_dict = flavor_restrictions_instance.to_dict()
# create an instance of FlavorRestrictions from a dict
flavor_restrictions_from_dict = FlavorRestrictions.from_dict(flavor_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


