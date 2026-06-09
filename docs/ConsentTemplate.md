# ConsentTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocks** | [**List[ConsentBlock]**](ConsentBlock.md) |  | [optional] 
**version** | **str** | Template version identifier | [optional] 

## Example

```python
from hyperstack.models.consent_template import ConsentTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentTemplate from a JSON string
consent_template_instance = ConsentTemplate.from_json(json)
# print the JSON string representation of the object
print(ConsentTemplate.to_json())

# convert the object into a dict
consent_template_dict = consent_template_instance.to_dict()
# create an instance of ConsentTemplate from a dict
consent_template_from_dict = ConsentTemplate.from_dict(consent_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


