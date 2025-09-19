# OrganizationThresholdUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**threshold** | [**OrganizationThresholdFields**](OrganizationThresholdFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.organization_threshold_update_response import OrganizationThresholdUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationThresholdUpdateResponse from a JSON string
organization_threshold_update_response_instance = OrganizationThresholdUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationThresholdUpdateResponse.to_json())

# convert the object into a dict
organization_threshold_update_response_dict = organization_threshold_update_response_instance.to_dict()
# create an instance of OrganizationThresholdUpdateResponse from a dict
organization_threshold_update_response_from_dict = OrganizationThresholdUpdateResponse.from_dict(organization_threshold_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


