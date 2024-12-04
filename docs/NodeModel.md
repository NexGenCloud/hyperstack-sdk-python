# NodeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flavors** | **List[str]** |  | [optional] 
**nexgen_name** | **str** |  | [optional] 
**openstack_id** | **str** |  | 
**openstack_name** | **str** |  | [optional] 
**organizations** | **List[int]** |  | [optional] 
**projects** | **List[str]** |  | [optional] 
**provision_date** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**stocks** | [**List[NodeStocksPayload]**](NodeStocksPayload.md) |  | [optional] 
**sunset_date** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.node_model import NodeModel

# TODO update the JSON string below
json = "{}"
# create an instance of NodeModel from a JSON string
node_model_instance = NodeModel.from_json(json)
# print the JSON string representation of the object
print(NodeModel.to_json())

# convert the object into a dict
node_model_dict = node_model_instance.to_dict()
# create an instance of NodeModel from a dict
node_model_from_dict = NodeModel.from_dict(node_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


