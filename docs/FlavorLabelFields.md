# FlavorLabelFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.flavor_label_fields import FlavorLabelFields

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorLabelFields from a JSON string
flavor_label_fields_instance = FlavorLabelFields.from_json(json)
# print the JSON string representation of the object
print(FlavorLabelFields.to_json())

# convert the object into a dict
flavor_label_fields_dict = flavor_label_fields_instance.to_dict()
# create an instance of FlavorLabelFields from a dict
flavor_label_fields_from_dict = FlavorLabelFields.from_dict(flavor_label_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


