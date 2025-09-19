# OrganizationThresholdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**thresholds** | [**List[OrganizationThresholdFields]**](OrganizationThresholdFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.organization_thresholds_response import OrganizationThresholdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationThresholdsResponse from a JSON string
organization_thresholds_response_instance = OrganizationThresholdsResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationThresholdsResponse.to_json())

# convert the object into a dict
organization_thresholds_response_dict = organization_thresholds_response_instance.to_dict()
# create an instance of OrganizationThresholdsResponse from a dict
organization_thresholds_response_from_dict = OrganizationThresholdsResponse.from_dict(organization_thresholds_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


