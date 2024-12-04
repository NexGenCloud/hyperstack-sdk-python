# AllocatedGPUCountGraph


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datetime** | **str** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.allocated_gpu_count_graph import AllocatedGPUCountGraph

# TODO update the JSON string below
json = "{}"
# create an instance of AllocatedGPUCountGraph from a JSON string
allocated_gpu_count_graph_instance = AllocatedGPUCountGraph.from_json(json)
# print the JSON string representation of the object
print(AllocatedGPUCountGraph.to_json())

# convert the object into a dict
allocated_gpu_count_graph_dict = allocated_gpu_count_graph_instance.to_dict()
# create an instance of AllocatedGPUCountGraph from a dict
allocated_gpu_count_graph_from_dict = AllocatedGPUCountGraph.from_dict(allocated_gpu_count_graph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


