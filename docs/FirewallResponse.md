# FirewallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall** | [**FirewallFields**](FirewallFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.firewall_response import FirewallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallResponse from a JSON string
firewall_response_instance = FirewallResponse.from_json(json)
# print the JSON string representation of the object
print(FirewallResponse.to_json())

# convert the object into a dict
firewall_response_dict = firewall_response_instance.to_dict()
# create an instance of FirewallResponse from a dict
firewall_response_from_dict = FirewallResponse.from_dict(firewall_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


