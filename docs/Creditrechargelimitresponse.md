# Creditrechargelimitresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Creditrechargelimitfield]**](Creditrechargelimitfield.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.creditrechargelimitresponse import Creditrechargelimitresponse

# TODO update the JSON string below
json = "{}"
# create an instance of Creditrechargelimitresponse from a JSON string
creditrechargelimitresponse_instance = Creditrechargelimitresponse.from_json(json)
# print the JSON string representation of the object
print(Creditrechargelimitresponse.to_json())

# convert the object into a dict
creditrechargelimitresponse_dict = creditrechargelimitresponse_instance.to_dict()
# create an instance of Creditrechargelimitresponse from a dict
creditrechargelimitresponse_from_dict = Creditrechargelimitresponse.from_dict(creditrechargelimitresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


