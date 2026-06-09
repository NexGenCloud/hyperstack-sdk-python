# ConsentTemplatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates** | **object** | Templates keyed by consent type | [optional] 

## Example

```python
from hyperstack.models.consent_templates_response import ConsentTemplatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentTemplatesResponse from a JSON string
consent_templates_response_instance = ConsentTemplatesResponse.from_json(json)
# print the JSON string representation of the object
print(ConsentTemplatesResponse.to_json())

# convert the object into a dict
consent_templates_response_dict = consent_templates_response_instance.to_dict()
# create an instance of ConsentTemplatesResponse from a dict
consent_templates_response_from_dict = ConsentTemplatesResponse.from_dict(consent_templates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


