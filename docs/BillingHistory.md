# BillingHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Attributes**](Attributes.md) |  | [optional] 
**metrics** | **object** |  | [optional] 

## Example

```python
from hyperstack.models.billing_history import BillingHistory

# TODO update the JSON string below
json = "{}"
# create an instance of BillingHistory from a JSON string
billing_history_instance = BillingHistory.from_json(json)
# print the JSON string representation of the object
print(BillingHistory.to_json())

# convert the object into a dict
billing_history_dict = billing_history_instance.to_dict()
# create an instance of BillingHistory from a dict
billing_history_from_dict = BillingHistory.from_dict(billing_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


