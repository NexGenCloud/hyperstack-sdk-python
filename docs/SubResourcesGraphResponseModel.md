# SubResourcesGraphResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**sub_resources_costs** | [**SubResourcesCostsResponseModel**](SubResourcesCostsResponseModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.sub_resources_graph_response_model import SubResourcesGraphResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of SubResourcesGraphResponseModel from a JSON string
sub_resources_graph_response_model_instance = SubResourcesGraphResponseModel.from_json(json)
# print the JSON string representation of the object
print(SubResourcesGraphResponseModel.to_json())

# convert the object into a dict
sub_resources_graph_response_model_dict = sub_resources_graph_response_model_instance.to_dict()
# create an instance of SubResourcesGraphResponseModel from a dict
sub_resources_graph_response_model_from_dict = SubResourcesGraphResponseModel.from_dict(sub_resources_graph_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


