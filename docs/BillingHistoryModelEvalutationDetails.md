# BillingHistoryModelEvalutationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history** | [**List[BillingHistory]**](BillingHistory.md) |  | [optional] 
**org_id** | **int** |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.billing_history_model_evalutation_details import BillingHistoryModelEvalutationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BillingHistoryModelEvalutationDetails from a JSON string
billing_history_model_evalutation_details_instance = BillingHistoryModelEvalutationDetails.from_json(json)
# print the JSON string representation of the object
print(BillingHistoryModelEvalutationDetails.to_json())

# convert the object into a dict
billing_history_model_evalutation_details_dict = billing_history_model_evalutation_details_instance.to_dict()
# create an instance of BillingHistoryModelEvalutationDetails from a dict
billing_history_model_evalutation_details_from_dict = BillingHistoryModelEvalutationDetails.from_dict(billing_history_model_evalutation_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


