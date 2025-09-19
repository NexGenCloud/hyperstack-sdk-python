# MFAStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**mfa** | [**MFAStatusFields**](MFAStatusFields.md) |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.mfa_status_response import MFAStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MFAStatusResponse from a JSON string
mfa_status_response_instance = MFAStatusResponse.from_json(json)
# print the JSON string representation of the object
print(MFAStatusResponse.to_json())

# convert the object into a dict
mfa_status_response_dict = mfa_status_response_instance.to_dict()
# create an instance of MFAStatusResponse from a dict
mfa_status_response_from_dict = MFAStatusResponse.from_dict(mfa_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


