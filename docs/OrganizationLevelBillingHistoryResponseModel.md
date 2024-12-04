# OrganizationLevelBillingHistoryResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history** | [**OrganizationLevelBillingHistory**](OrganizationLevelBillingHistory.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.organization_level_billing_history_response_model import OrganizationLevelBillingHistoryResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationLevelBillingHistoryResponseModel from a JSON string
organization_level_billing_history_response_model_instance = OrganizationLevelBillingHistoryResponseModel.from_json(json)
# print the JSON string representation of the object
print(OrganizationLevelBillingHistoryResponseModel.to_json())

# convert the object into a dict
organization_level_billing_history_response_model_dict = organization_level_billing_history_response_model_instance.to_dict()
# create an instance of OrganizationLevelBillingHistoryResponseModel from a dict
organization_level_billing_history_response_model_from_dict = OrganizationLevelBillingHistoryResponseModel.from_dict(organization_level_billing_history_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


