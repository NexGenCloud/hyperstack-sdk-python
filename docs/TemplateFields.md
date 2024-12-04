# TemplateFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.template_fields import TemplateFields

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateFields from a JSON string
template_fields_instance = TemplateFields.from_json(json)
# print the JSON string representation of the object
print(TemplateFields.to_json())

# convert the object into a dict
template_fields_dict = template_fields_instance.to_dict()
# create an instance of TemplateFields from a dict
template_fields_from_dict = TemplateFields.from_dict(template_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


