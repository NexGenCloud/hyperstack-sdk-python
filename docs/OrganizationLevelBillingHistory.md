# OrganizationLevelBillingHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history** | [**List[OrganizationLevelBillingHistoryResources]**](OrganizationLevelBillingHistoryResources.md) |  | [optional] 
**org_id** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.organization_level_billing_history import OrganizationLevelBillingHistory

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationLevelBillingHistory from a JSON string
organization_level_billing_history_instance = OrganizationLevelBillingHistory.from_json(json)
# print the JSON string representation of the object
print(OrganizationLevelBillingHistory.to_json())

# convert the object into a dict
organization_level_billing_history_dict = organization_level_billing_history_instance.to_dict()
# create an instance of OrganizationLevelBillingHistory from a dict
organization_level_billing_history_from_dict = OrganizationLevelBillingHistory.from_dict(organization_level_billing_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


