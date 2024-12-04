# WarningMailLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WarningMailLogFields]**](WarningMailLogFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.warning_mail_log_response import WarningMailLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WarningMailLogResponse from a JSON string
warning_mail_log_response_instance = WarningMailLogResponse.from_json(json)
# print the JSON string representation of the object
print(WarningMailLogResponse.to_json())

# convert the object into a dict
warning_mail_log_response_dict = warning_mail_log_response_instance.to_dict()
# create an instance of WarningMailLogResponse from a dict
warning_mail_log_response_from_dict = WarningMailLogResponse.from_dict(warning_mail_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


