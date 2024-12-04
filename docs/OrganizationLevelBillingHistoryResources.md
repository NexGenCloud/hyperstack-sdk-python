# OrganizationLevelBillingHistoryResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**OrganizationLevelBillingHistoryResponseAttributes**](OrganizationLevelBillingHistoryResponseAttributes.md) |  | [optional] 
**metrics** | [**OrganizationLevelBillingHistoryResponseMetrics**](OrganizationLevelBillingHistoryResponseMetrics.md) |  | [optional] 

## Example

```python
from hyperstack.models.organization_level_billing_history_resources import OrganizationLevelBillingHistoryResources

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationLevelBillingHistoryResources from a JSON string
organization_level_billing_history_resources_instance = OrganizationLevelBillingHistoryResources.from_json(json)
# print the JSON string representation of the object
print(OrganizationLevelBillingHistoryResources.to_json())

# convert the object into a dict
organization_level_billing_history_resources_dict = organization_level_billing_history_resources_instance.to_dict()
# create an instance of OrganizationLevelBillingHistoryResources from a dict
organization_level_billing_history_resources_from_dict = OrganizationLevelBillingHistoryResources.from_dict(organization_level_billing_history_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


