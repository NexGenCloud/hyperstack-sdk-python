# AutoTopup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**threshold_amount** | **float** |  | [optional] 
**topup_amount** | **float** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.auto_topup import AutoTopup

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTopup from a JSON string
auto_topup_instance = AutoTopup.from_json(json)
# print the JSON string representation of the object
print(AutoTopup.to_json())

# convert the object into a dict
auto_topup_dict = auto_topup_instance.to_dict()
# create an instance of AutoTopup from a dict
auto_topup_from_dict = AutoTopup.from_dict(auto_topup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


