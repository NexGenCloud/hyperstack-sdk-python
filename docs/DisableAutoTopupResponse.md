# DisableAutoTopupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_topup** | [**AutoTopup**](AutoTopup.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.disable_auto_topup_response import DisableAutoTopupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DisableAutoTopupResponse from a JSON string
disable_auto_topup_response_instance = DisableAutoTopupResponse.from_json(json)
# print the JSON string representation of the object
print(DisableAutoTopupResponse.to_json())

# convert the object into a dict
disable_auto_topup_response_dict = disable_auto_topup_response_instance.to_dict()
# create an instance of DisableAutoTopupResponse from a dict
disable_auto_topup_response_from_dict = DisableAutoTopupResponse.from_dict(disable_auto_topup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


