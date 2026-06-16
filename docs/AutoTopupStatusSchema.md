# AutoTopupStatusSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Auto top-up status: active, disabled, pending_setup, cancelled, or null | [optional] 
**threshold_amount** | **float** | Balance threshold that triggers auto top-up | [optional] 
**topup_amount** | **float** | Amount to top up when threshold is reached | [optional] 

## Example

```python
from hyperstack.models.auto_topup_status_schema import AutoTopupStatusSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTopupStatusSchema from a JSON string
auto_topup_status_schema_instance = AutoTopupStatusSchema.from_json(json)
# print the JSON string representation of the object
print(AutoTopupStatusSchema.to_json())

# convert the object into a dict
auto_topup_status_schema_dict = auto_topup_status_schema_instance.to_dict()
# create an instance of AutoTopupStatusSchema from a dict
auto_topup_status_schema_from_dict = AutoTopupStatusSchema.from_dict(auto_topup_status_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


