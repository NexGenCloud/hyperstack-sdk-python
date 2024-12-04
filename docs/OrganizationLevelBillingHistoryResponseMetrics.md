# OrganizationLevelBillingHistoryResponseMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_cost** | **float** |  | [optional] 
**incurred_bill** | **float** |  | [optional] 
**non_discounted_bill** | **float** |  | [optional] 
**snapshot_cost** | **float** |  | [optional] 
**vm_cost** | **float** |  | [optional] 
**volume_cost** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.organization_level_billing_history_response_metrics import OrganizationLevelBillingHistoryResponseMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationLevelBillingHistoryResponseMetrics from a JSON string
organization_level_billing_history_response_metrics_instance = OrganizationLevelBillingHistoryResponseMetrics.from_json(json)
# print the JSON string representation of the object
print(OrganizationLevelBillingHistoryResponseMetrics.to_json())

# convert the object into a dict
organization_level_billing_history_response_metrics_dict = organization_level_billing_history_response_metrics_instance.to_dict()
# create an instance of OrganizationLevelBillingHistoryResponseMetrics from a dict
organization_level_billing_history_response_metrics_from_dict = OrganizationLevelBillingHistoryResponseMetrics.from_dict(organization_level_billing_history_response_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


