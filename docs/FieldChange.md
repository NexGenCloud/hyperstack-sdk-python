# FieldChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | The name of the field that was changed | [optional] 
**new_value** | **str** | The new value of the field | [optional] 
**old_value** | **str** | The old value of the field | [optional] 

## Example

```python
from hyperstack.models.field_change import FieldChange

# TODO update the JSON string below
json = "{}"
# create an instance of FieldChange from a JSON string
field_change_instance = FieldChange.from_json(json)
# print the JSON string representation of the object
print(FieldChange.to_json())

# convert the object into a dict
field_change_dict = field_change_instance.to_dict()
# create an instance of FieldChange from a dict
field_change_from_dict = FieldChange.from_dict(field_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


