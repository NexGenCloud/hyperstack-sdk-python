# FirewallsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**firewalls** | [**List[FirewallDetailFields]**](FirewallDetailFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.firewalls_list_response import FirewallsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallsListResponse from a JSON string
firewalls_list_response_instance = FirewallsListResponse.from_json(json)
# print the JSON string representation of the object
print(FirewallsListResponse.to_json())

# convert the object into a dict
firewalls_list_response_dict = firewalls_list_response_instance.to_dict()
# create an instance of FirewallsListResponse from a dict
firewalls_list_response_from_dict = FirewallsListResponse.from_dict(firewalls_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


