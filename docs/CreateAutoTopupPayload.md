# CreateAutoTopupPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_amount** | **float** |  | 
**topup_amount** | **float** |  | 

## Example

```python
from hyperstack.models.create_auto_topup_payload import CreateAutoTopupPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutoTopupPayload from a JSON string
create_auto_topup_payload_instance = CreateAutoTopupPayload.from_json(json)
# print the JSON string representation of the object
print(CreateAutoTopupPayload.to_json())

# convert the object into a dict
create_auto_topup_payload_dict = create_auto_topup_payload_instance.to_dict()
# create an instance of CreateAutoTopupPayload from a dict
create_auto_topup_payload_from_dict = CreateAutoTopupPayload.from_dict(create_auto_topup_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


