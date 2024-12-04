# Organizationthresholdupdateresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**threshold** | [**OrganizationThresholdfields**](OrganizationThresholdfields.md) |  | [optional] 

## Example

```python
from hyperstack.models.organizationthresholdupdateresponse import Organizationthresholdupdateresponse

# TODO update the JSON string below
json = "{}"
# create an instance of Organizationthresholdupdateresponse from a JSON string
organizationthresholdupdateresponse_instance = Organizationthresholdupdateresponse.from_json(json)
# print the JSON string representation of the object
print(Organizationthresholdupdateresponse.to_json())

# convert the object into a dict
organizationthresholdupdateresponse_dict = organizationthresholdupdateresponse_instance.to_dict()
# create an instance of Organizationthresholdupdateresponse from a dict
organizationthresholdupdateresponse_from_dict = Organizationthresholdupdateresponse.from_dict(organizationthresholdupdateresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


