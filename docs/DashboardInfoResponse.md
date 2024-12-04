# DashboardInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**overview** | [**OverviewInfo**](OverviewInfo.md) |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.dashboard_info_response import DashboardInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardInfoResponse from a JSON string
dashboard_info_response_instance = DashboardInfoResponse.from_json(json)
# print the JSON string representation of the object
print(DashboardInfoResponse.to_json())

# convert the object into a dict
dashboard_info_response_dict = dashboard_info_response_instance.to_dict()
# create an instance of DashboardInfoResponse from a dict
dashboard_info_response_from_dict = DashboardInfoResponse.from_dict(dashboard_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


