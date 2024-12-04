# BillingImmuneResourcesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Data]**](Data.md) |  | [optional] 

## Example

```python
from hyperstack.models.billing_immune_resources_response import BillingImmuneResourcesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingImmuneResourcesResponse from a JSON string
billing_immune_resources_response_instance = BillingImmuneResourcesResponse.from_json(json)
# print the JSON string representation of the object
print(BillingImmuneResourcesResponse.to_json())

# convert the object into a dict
billing_immune_resources_response_dict = billing_immune_resources_response_instance.to_dict()
# create an instance of BillingImmuneResourcesResponse from a dict
billing_immune_resources_response_from_dict = BillingImmuneResourcesResponse.from_dict(billing_immune_resources_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


