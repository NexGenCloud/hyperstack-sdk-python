# WorkloadBillingHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_fine_tuning** | [**BillingHistoryFineTuning**](BillingHistoryFineTuning.md) |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.workload_billing_history_response import WorkloadBillingHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadBillingHistoryResponse from a JSON string
workload_billing_history_response_instance = WorkloadBillingHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(WorkloadBillingHistoryResponse.to_json())

# convert the object into a dict
workload_billing_history_response_dict = workload_billing_history_response_instance.to_dict()
# create an instance of WorkloadBillingHistoryResponse from a dict
workload_billing_history_response_from_dict = WorkloadBillingHistoryResponse.from_dict(workload_billing_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


