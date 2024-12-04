# Organizationthresholdsresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**thresholds** | [**List[OrganizationThresholdfields]**](OrganizationThresholdfields.md) |  | [optional] 

## Example

```python
from hyperstack.models.organizationthresholdsresponse import Organizationthresholdsresponse

# TODO update the JSON string below
json = "{}"
# create an instance of Organizationthresholdsresponse from a JSON string
organizationthresholdsresponse_instance = Organizationthresholdsresponse.from_json(json)
# print the JSON string representation of the object
print(Organizationthresholdsresponse.to_json())

# convert the object into a dict
organizationthresholdsresponse_dict = organizationthresholdsresponse_instance.to_dict()
# create an instance of Organizationthresholdsresponse from a dict
organizationthresholdsresponse_from_dict = Organizationthresholdsresponse.from_dict(organizationthresholdsresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


