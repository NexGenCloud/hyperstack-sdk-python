# GraphDatetimeValueModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datetime** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.graph_datetime_value_model import GraphDatetimeValueModel

# TODO update the JSON string below
json = "{}"
# create an instance of GraphDatetimeValueModel from a JSON string
graph_datetime_value_model_instance = GraphDatetimeValueModel.from_json(json)
# print the JSON string representation of the object
print(GraphDatetimeValueModel.to_json())

# convert the object into a dict
graph_datetime_value_model_dict = graph_datetime_value_model_instance.to_dict()
# create an instance of GraphDatetimeValueModel from a dict
graph_datetime_value_model_from_dict = GraphDatetimeValueModel.from_dict(graph_datetime_value_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


