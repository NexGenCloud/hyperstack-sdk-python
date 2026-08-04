# EmailCategoryChild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**email_category_id** | **int** |  | [optional] 
**icon** | **str** |  | [optional] 
**opted_in** | **bool** |  | [optional] 
**position** | **int** |  | [optional] 
**required** | **bool** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.email_category_child import EmailCategoryChild

# TODO update the JSON string below
json = "{}"
# create an instance of EmailCategoryChild from a JSON string
email_category_child_instance = EmailCategoryChild.from_json(json)
# print the JSON string representation of the object
print(EmailCategoryChild.to_json())

# convert the object into a dict
email_category_child_dict = email_category_child_instance.to_dict()
# create an instance of EmailCategoryChild from a dict
email_category_child_from_dict = EmailCategoryChild.from_dict(email_category_child_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


