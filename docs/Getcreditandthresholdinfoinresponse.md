# GetCreditAndThresholdInfoInResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetCreditAndThresholdInfo**](GetCreditAndThresholdInfo.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.get_credit_and_threshold_info_in_response import GetCreditAndThresholdInfoInResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCreditAndThresholdInfoInResponse from a JSON string
get_credit_and_threshold_info_in_response_instance = GetCreditAndThresholdInfoInResponse.from_json(json)
# print the JSON string representation of the object
print(GetCreditAndThresholdInfoInResponse.to_json())

# convert the object into a dict
get_credit_and_threshold_info_in_response_dict = get_credit_and_threshold_info_in_response_instance.to_dict()
# create an instance of GetCreditAndThresholdInfoInResponse from a dict
get_credit_and_threshold_info_in_response_from_dict = GetCreditAndThresholdInfoInResponse.from_dict(get_credit_and_threshold_info_in_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


