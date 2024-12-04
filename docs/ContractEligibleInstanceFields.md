# ContractEligibleInstanceFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **int** |  | [optional] 
**host** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**openstack_id** | **str** |  | [optional] 
**public_ip** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.contract_eligible_instance_fields import ContractEligibleInstanceFields

# TODO update the JSON string below
json = "{}"
# create an instance of ContractEligibleInstanceFields from a JSON string
contract_eligible_instance_fields_instance = ContractEligibleInstanceFields.from_json(json)
# print the JSON string representation of the object
print(ContractEligibleInstanceFields.to_json())

# convert the object into a dict
contract_eligible_instance_fields_dict = contract_eligible_instance_fields_instance.to_dict()
# create an instance of ContractEligibleInstanceFields from a dict
contract_eligible_instance_fields_from_dict = ContractEligibleInstanceFields.from_dict(contract_eligible_instance_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


