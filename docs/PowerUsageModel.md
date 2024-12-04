# PowerUsageModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** |  | 
**value** | **float** |  | 

## Example

```python
from hyperstack.models.power_usage_model import PowerUsageModel

# TODO update the JSON string below
json = "{}"
# create an instance of PowerUsageModel from a JSON string
power_usage_model_instance = PowerUsageModel.from_json(json)
# print the JSON string representation of the object
print(PowerUsageModel.to_json())

# convert the object into a dict
power_usage_model_dict = power_usage_model_instance.to_dict()
# create an instance of PowerUsageModel from a dict
power_usage_model_from_dict = PowerUsageModel.from_dict(power_usage_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


