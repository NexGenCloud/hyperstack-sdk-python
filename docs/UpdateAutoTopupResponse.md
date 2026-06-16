# UpdateAutoTopupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_topup** | [**AutoTopup**](AutoTopup.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.update_auto_topup_response import UpdateAutoTopupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAutoTopupResponse from a JSON string
update_auto_topup_response_instance = UpdateAutoTopupResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAutoTopupResponse.to_json())

# convert the object into a dict
update_auto_topup_response_dict = update_auto_topup_response_instance.to_dict()
# create an instance of UpdateAutoTopupResponse from a dict
update_auto_topup_response_from_dict = UpdateAutoTopupResponse.from_dict(update_auto_topup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


