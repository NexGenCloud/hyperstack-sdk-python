# OrganizationThresholdfields


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
from hyperstack.models.organization_thresholdfields import OrganizationThresholdfields

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationThresholdfields from a JSON string
organization_thresholdfields_instance = OrganizationThresholdfields.from_json(json)
# print the JSON string representation of the object
print(OrganizationThresholdfields.to_json())

# convert the object into a dict
organization_thresholdfields_dict = organization_thresholdfields_instance.to_dict()
# create an instance of OrganizationThresholdfields from a dict
organization_thresholdfields_from_dict = OrganizationThresholdfields.from_dict(organization_thresholdfields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


