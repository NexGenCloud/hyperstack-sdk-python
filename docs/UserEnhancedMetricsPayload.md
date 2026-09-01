# UserEnhancedMetricsPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Set to true to opt this VM into Enhanced Metrics, false to opt out. | 

## Example

```python
from hyperstack.models.user_enhanced_metrics_payload import UserEnhancedMetricsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserEnhancedMetricsPayload from a JSON string
user_enhanced_metrics_payload_instance = UserEnhancedMetricsPayload.from_json(json)
# print the JSON string representation of the object
print(UserEnhancedMetricsPayload.to_json())

# convert the object into a dict
user_enhanced_metrics_payload_dict = user_enhanced_metrics_payload_instance.to_dict()
# create an instance of UserEnhancedMetricsPayload from a dict
user_enhanced_metrics_payload_from_dict = UserEnhancedMetricsPayload.from_dict(user_enhanced_metrics_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


