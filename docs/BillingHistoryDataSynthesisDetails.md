# BillingHistoryDataSynthesisDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history** | [**List[BillingHistory]**](BillingHistory.md) |  | [optional] 
**org_id** | **int** |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.billing_history_data_synthesis_details import BillingHistoryDataSynthesisDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BillingHistoryDataSynthesisDetails from a JSON string
billing_history_data_synthesis_details_instance = BillingHistoryDataSynthesisDetails.from_json(json)
# print the JSON string representation of the object
print(BillingHistoryDataSynthesisDetails.to_json())

# convert the object into a dict
billing_history_data_synthesis_details_dict = billing_history_data_synthesis_details_instance.to_dict()
# create an instance of BillingHistoryDataSynthesisDetails from a dict
billing_history_data_synthesis_details_from_dict = BillingHistoryDataSynthesisDetails.from_dict(billing_history_data_synthesis_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


