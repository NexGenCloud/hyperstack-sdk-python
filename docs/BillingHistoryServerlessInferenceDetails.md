# BillingHistoryServerlessInferenceDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history** | [**List[BillingHistory]**](BillingHistory.md) |  | [optional] 
**org_id** | **int** |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.billing_history_serverless_inference_details import BillingHistoryServerlessInferenceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BillingHistoryServerlessInferenceDetails from a JSON string
billing_history_serverless_inference_details_instance = BillingHistoryServerlessInferenceDetails.from_json(json)
# print the JSON string representation of the object
print(BillingHistoryServerlessInferenceDetails.to_json())

# convert the object into a dict
billing_history_serverless_inference_details_dict = billing_history_serverless_inference_details_instance.to_dict()
# create an instance of BillingHistoryServerlessInferenceDetails from a dict
billing_history_serverless_inference_details_from_dict = BillingHistoryServerlessInferenceDetails.from_dict(billing_history_serverless_inference_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


