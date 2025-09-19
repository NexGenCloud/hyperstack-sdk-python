# LastDayCostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LastDayCostFields**](LastDayCostFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.last_day_cost_response import LastDayCostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LastDayCostResponse from a JSON string
last_day_cost_response_instance = LastDayCostResponse.from_json(json)
# print the JSON string representation of the object
print(LastDayCostResponse.to_json())

# convert the object into a dict
last_day_cost_response_dict = last_day_cost_response_instance.to_dict()
# create an instance of LastDayCostResponse from a dict
last_day_cost_response_from_dict = LastDayCostResponse.from_dict(last_day_cost_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


