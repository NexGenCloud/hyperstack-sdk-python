# FirewallDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall** | [**FirewallDetailFields**](FirewallDetailFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.firewall_detail_response import FirewallDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallDetailResponse from a JSON string
firewall_detail_response_instance = FirewallDetailResponse.from_json(json)
# print the JSON string representation of the object
print(FirewallDetailResponse.to_json())

# convert the object into a dict
firewall_detail_response_dict = firewall_detail_response_instance.to_dict()
# create an instance of FirewallDetailResponse from a dict
firewall_detail_response_from_dict = FirewallDetailResponse.from_dict(firewall_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


