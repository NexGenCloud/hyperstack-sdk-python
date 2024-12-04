# HistoricalInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_count** | **int** |  | [optional] 
**instances** | [**List[HistoricalInstancesFields]**](HistoricalInstancesFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.historical_instance import HistoricalInstance

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricalInstance from a JSON string
historical_instance_instance = HistoricalInstance.from_json(json)
# print the JSON string representation of the object
print(HistoricalInstance.to_json())

# convert the object into a dict
historical_instance_dict = historical_instance_instance.to_dict()
# create an instance of HistoricalInstance from a dict
historical_instance_from_dict = HistoricalInstance.from_dict(historical_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


