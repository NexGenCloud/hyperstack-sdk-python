# UserEnhancedMetricsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_command** | **str** | One-liner the user can run inside the VM to install the agent when enabling. Omitted when disabling. | [optional] 
**message** | **str** |  | [optional] 
**metrics** | [**UserEnhancedMetricsResponseFields**](UserEnhancedMetricsResponseFields.md) |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.user_enhanced_metrics_response import UserEnhancedMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserEnhancedMetricsResponse from a JSON string
user_enhanced_metrics_response_instance = UserEnhancedMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(UserEnhancedMetricsResponse.to_json())

# convert the object into a dict
user_enhanced_metrics_response_dict = user_enhanced_metrics_response_instance.to_dict()
# create an instance of UserEnhancedMetricsResponse from a dict
user_enhanced_metrics_response_from_dict = UserEnhancedMetricsResponse.from_dict(user_enhanced_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


