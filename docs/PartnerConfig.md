# PartnerConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_image_url** | **str** |  | [optional] 
**colors** | [**Colors**](Colors.md) |  | [optional] 
**logos** | [**Logos**](Logos.md) |  | [optional] 
**name** | **str** |  | 
**support_email** | **str** |  | [optional] 
**uris** | [**URIs**](URIs.md) |  | [optional] 
**user_type** | **str** |  | 

## Example

```python
from hyperstack.models.partner_config import PartnerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerConfig from a JSON string
partner_config_instance = PartnerConfig.from_json(json)
# print the JSON string representation of the object
print(PartnerConfig.to_json())

# convert the object into a dict
partner_config_dict = partner_config_instance.to_dict()
# create an instance of PartnerConfig from a dict
partner_config_from_dict = PartnerConfig.from_dict(partner_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


