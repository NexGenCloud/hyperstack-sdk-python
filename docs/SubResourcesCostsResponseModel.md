# SubResourcesCostsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history** | [**List[SubResourcesGraphBillingHistoryFields]**](SubResourcesGraphBillingHistoryFields.md) |  | [optional] 
**granularity** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.sub_resources_costs_response_model import SubResourcesCostsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of SubResourcesCostsResponseModel from a JSON string
sub_resources_costs_response_model_instance = SubResourcesCostsResponseModel.from_json(json)
# print the JSON string representation of the object
print(SubResourcesCostsResponseModel.to_json())

# convert the object into a dict
sub_resources_costs_response_model_dict = sub_resources_costs_response_model_instance.to_dict()
# create an instance of SubResourcesCostsResponseModel from a dict
sub_resources_costs_response_model_from_dict = SubResourcesCostsResponseModel.from_dict(sub_resources_costs_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


