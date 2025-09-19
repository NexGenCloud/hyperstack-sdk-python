# OrganizationThresholdFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**interface_title** | **str** |  | [optional] 
**interface_tooltip** | **str** |  | [optional] 
**subscribed** | **bool** |  | [optional] 
**threshold** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.organization_threshold_fields import OrganizationThresholdFields

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationThresholdFields from a JSON string
organization_threshold_fields_instance = OrganizationThresholdFields.from_json(json)
# print the JSON string representation of the object
print(OrganizationThresholdFields.to_json())

# convert the object into a dict
organization_threshold_fields_dict = organization_threshold_fields_instance.to_dict()
# create an instance of OrganizationThresholdFields from a dict
organization_threshold_fields_from_dict = OrganizationThresholdFields.from_dict(organization_threshold_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


