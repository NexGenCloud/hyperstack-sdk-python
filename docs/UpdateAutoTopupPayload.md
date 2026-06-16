# UpdateAutoTopupPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_amount** | **float** |  | 
**topup_amount** | **float** |  | 

## Example

```python
from hyperstack.models.update_auto_topup_payload import UpdateAutoTopupPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAutoTopupPayload from a JSON string
update_auto_topup_payload_instance = UpdateAutoTopupPayload.from_json(json)
# print the JSON string representation of the object
print(UpdateAutoTopupPayload.to_json())

# convert the object into a dict
update_auto_topup_payload_dict = update_auto_topup_payload_instance.to_dict()
# create an instance of UpdateAutoTopupPayload from a dict
update_auto_topup_payload_from_dict = UpdateAutoTopupPayload.from_dict(update_auto_topup_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


