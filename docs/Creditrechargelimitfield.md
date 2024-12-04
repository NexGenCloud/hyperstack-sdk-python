# Creditrechargelimitfield


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_granted** | **float** |  | [optional] 
**credit_limit** | **float** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.creditrechargelimitfield import Creditrechargelimitfield

# TODO update the JSON string below
json = "{}"
# create an instance of Creditrechargelimitfield from a JSON string
creditrechargelimitfield_instance = Creditrechargelimitfield.from_json(json)
# print the JSON string representation of the object
print(Creditrechargelimitfield.to_json())

# convert the object into a dict
creditrechargelimitfield_dict = creditrechargelimitfield_instance.to_dict()
# create an instance of Creditrechargelimitfield from a dict
creditrechargelimitfield_from_dict = Creditrechargelimitfield.from_dict(creditrechargelimitfield_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


