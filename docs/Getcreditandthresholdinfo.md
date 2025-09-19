# GetCreditAndThresholdInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_create_instance** | **bool** |  | [optional] 
**credit** | **float** |  | [optional] 
**threshold** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.get_credit_and_threshold_info import GetCreditAndThresholdInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetCreditAndThresholdInfo from a JSON string
get_credit_and_threshold_info_instance = GetCreditAndThresholdInfo.from_json(json)
# print the JSON string representation of the object
print(GetCreditAndThresholdInfo.to_json())

# convert the object into a dict
get_credit_and_threshold_info_dict = get_credit_and_threshold_info_instance.to_dict()
# create an instance of GetCreditAndThresholdInfo from a dict
get_credit_and_threshold_info_from_dict = GetCreditAndThresholdInfo.from_dict(get_credit_and_threshold_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


