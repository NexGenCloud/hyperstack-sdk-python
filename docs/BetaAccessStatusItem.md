# BetaAccessStatusItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_name** | **str** | Name of the beta program | [optional] 
**request_date** | **datetime** | When the request was made | [optional] 
**status** | **str** | Status of the request (requested, approved, denied, revoked) | [optional] 

## Example

```python
from hyperstack.models.beta_access_status_item import BetaAccessStatusItem

# TODO update the JSON string below
json = "{}"
# create an instance of BetaAccessStatusItem from a JSON string
beta_access_status_item_instance = BetaAccessStatusItem.from_json(json)
# print the JSON string representation of the object
print(BetaAccessStatusItem.to_json())

# convert the object into a dict
beta_access_status_item_dict = beta_access_status_item_instance.to_dict()
# create an instance of BetaAccessStatusItem from a dict
beta_access_status_item_from_dict = BetaAccessStatusItem.from_dict(beta_access_status_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


