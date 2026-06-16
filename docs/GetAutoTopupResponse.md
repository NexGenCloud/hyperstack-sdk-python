# GetAutoTopupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_topup** | [**AutoTopup**](AutoTopup.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.get_auto_topup_response import GetAutoTopupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAutoTopupResponse from a JSON string
get_auto_topup_response_instance = GetAutoTopupResponse.from_json(json)
# print the JSON string representation of the object
print(GetAutoTopupResponse.to_json())

# convert the object into a dict
get_auto_topup_response_dict = get_auto_topup_response_instance.to_dict()
# create an instance of GetAutoTopupResponse from a dict
get_auto_topup_response_from_dict = GetAutoTopupResponse.from_dict(get_auto_topup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


