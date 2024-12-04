# ContractGPUAllocationGraphResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | [**Contract**](Contract.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.contract_gpu_allocation_graph_response import ContractGPUAllocationGraphResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractGPUAllocationGraphResponse from a JSON string
contract_gpu_allocation_graph_response_instance = ContractGPUAllocationGraphResponse.from_json(json)
# print the JSON string representation of the object
print(ContractGPUAllocationGraphResponse.to_json())

# convert the object into a dict
contract_gpu_allocation_graph_response_dict = contract_gpu_allocation_graph_response_instance.to_dict()
# create an instance of ContractGPUAllocationGraphResponse from a dict
contract_gpu_allocation_graph_response_from_dict = ContractGPUAllocationGraphResponse.from_dict(contract_gpu_allocation_graph_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


