# AutoTopupErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_reason** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.auto_topup_error_response import AutoTopupErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTopupErrorResponse from a JSON string
auto_topup_error_response_instance = AutoTopupErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AutoTopupErrorResponse.to_json())

# convert the object into a dict
auto_topup_error_response_dict = auto_topup_error_response_instance.to_dict()
# create an instance of AutoTopupErrorResponse from a dict
auto_topup_error_response_from_dict = AutoTopupErrorResponse.from_dict(auto_topup_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


