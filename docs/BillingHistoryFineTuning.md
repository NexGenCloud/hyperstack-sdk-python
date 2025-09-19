# BillingHistoryFineTuning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history** | [**List[BillingHistory]**](BillingHistory.md) |  | [optional] 
**org_id** | **int** |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.billing_history_fine_tuning import BillingHistoryFineTuning

# TODO update the JSON string below
json = "{}"
# create an instance of BillingHistoryFineTuning from a JSON string
billing_history_fine_tuning_instance = BillingHistoryFineTuning.from_json(json)
# print the JSON string representation of the object
print(BillingHistoryFineTuning.to_json())

# convert the object into a dict
billing_history_fine_tuning_dict = billing_history_fine_tuning_instance.to_dict()
# create an instance of BillingHistoryFineTuning from a dict
billing_history_fine_tuning_from_dict = BillingHistoryFineTuning.from_dict(billing_history_fine_tuning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


