# ComplianceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compliance** | [**ComplianceFields**](ComplianceFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.compliance_response import ComplianceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceResponse from a JSON string
compliance_response_instance = ComplianceResponse.from_json(json)
# print the JSON string representation of the object
print(ComplianceResponse.to_json())

# convert the object into a dict
compliance_response_dict = compliance_response_instance.to_dict()
# create an instance of ComplianceResponse from a dict
compliance_response_from_dict = ComplianceResponse.from_dict(compliance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


