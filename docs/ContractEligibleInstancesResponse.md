# ContractEligibleInstancesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_count** | **int** |  | [optional] 
**instances** | [**List[ContractEligibleInstanceFields]**](ContractEligibleInstanceFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.contract_eligible_instances_response import ContractEligibleInstancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractEligibleInstancesResponse from a JSON string
contract_eligible_instances_response_instance = ContractEligibleInstancesResponse.from_json(json)
# print the JSON string representation of the object
print(ContractEligibleInstancesResponse.to_json())

# convert the object into a dict
contract_eligible_instances_response_dict = contract_eligible_instances_response_instance.to_dict()
# create an instance of ContractEligibleInstancesResponse from a dict
contract_eligible_instances_response_from_dict = ContractEligibleInstancesResponse.from_dict(contract_eligible_instances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


