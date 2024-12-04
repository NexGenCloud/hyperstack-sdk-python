# FutureNodeUpdateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_provision_date** | **datetime** |  | 
**id** | **int** |  | [optional] [readonly] 
**nexgen_name** | **str** |  | 
**openstack_name** | **str** |  | 
**region_id** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.future_node_update_model import FutureNodeUpdateModel

# TODO update the JSON string below
json = "{}"
# create an instance of FutureNodeUpdateModel from a JSON string
future_node_update_model_instance = FutureNodeUpdateModel.from_json(json)
# print the JSON string representation of the object
print(FutureNodeUpdateModel.to_json())

# convert the object into a dict
future_node_update_model_dict = future_node_update_model_instance.to_dict()
# create an instance of FutureNodeUpdateModel from a dict
future_node_update_model_from_dict = FutureNodeUpdateModel.from_dict(future_node_update_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


