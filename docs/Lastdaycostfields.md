# LastDayCostFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters_cost** | **float** |  | [optional] 
**instances_cost** | **float** |  | [optional] 
**total_cost** | **float** |  | [optional] 
**volumes_cost** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.last_day_cost_fields import LastDayCostFields

# TODO update the JSON string below
json = "{}"
# create an instance of LastDayCostFields from a JSON string
last_day_cost_fields_instance = LastDayCostFields.from_json(json)
# print the JSON string representation of the object
print(LastDayCostFields.to_json())

# convert the object into a dict
last_day_cost_fields_dict = last_day_cost_fields_instance.to_dict()
# create an instance of LastDayCostFields from a dict
last_day_cost_fields_from_dict = LastDayCostFields.from_dict(last_day_cost_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


