# EmailCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**childs** | [**List[EmailCategoryChild]**](EmailCategoryChild.md) |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**opted_in** | **bool** |  | [optional] 
**position** | **int** |  | [optional] 
**required** | **bool** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.email_category import EmailCategory

# TODO update the JSON string below
json = "{}"
# create an instance of EmailCategory from a JSON string
email_category_instance = EmailCategory.from_json(json)
# print the JSON string representation of the object
print(EmailCategory.to_json())

# convert the object into a dict
email_category_dict = email_category_instance.to_dict()
# create an instance of EmailCategory from a dict
email_category_from_dict = EmailCategory.from_dict(email_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


