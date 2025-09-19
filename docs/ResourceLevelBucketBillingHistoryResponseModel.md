# ResourceLevelBucketBillingHistoryResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_bucket** | [**ResourceLevelBillingHistory**](ResourceLevelBillingHistory.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_bucket_billing_history_response_model import ResourceLevelBucketBillingHistoryResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelBucketBillingHistoryResponseModel from a JSON string
resource_level_bucket_billing_history_response_model_instance = ResourceLevelBucketBillingHistoryResponseModel.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelBucketBillingHistoryResponseModel.to_json())

# convert the object into a dict
resource_level_bucket_billing_history_response_model_dict = resource_level_bucket_billing_history_response_model_instance.to_dict()
# create an instance of ResourceLevelBucketBillingHistoryResponseModel from a dict
resource_level_bucket_billing_history_response_model_from_dict = ResourceLevelBucketBillingHistoryResponseModel.from_dict(resource_level_bucket_billing_history_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


