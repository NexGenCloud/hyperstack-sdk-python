# Organizationcreditrechargelimitresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Creditrechargelimitfield**](Creditrechargelimitfield.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.organizationcreditrechargelimitresponse import Organizationcreditrechargelimitresponse

# TODO update the JSON string below
json = "{}"
# create an instance of Organizationcreditrechargelimitresponse from a JSON string
organizationcreditrechargelimitresponse_instance = Organizationcreditrechargelimitresponse.from_json(json)
# print the JSON string representation of the object
print(Organizationcreditrechargelimitresponse.to_json())

# convert the object into a dict
organizationcreditrechargelimitresponse_dict = organizationcreditrechargelimitresponse_instance.to_dict()
# create an instance of Organizationcreditrechargelimitresponse from a dict
organizationcreditrechargelimitresponse_from_dict = Organizationcreditrechargelimitresponse.from_dict(organizationcreditrechargelimitresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


