# ContractEventCreateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message for the event | 
**reason** | **str** | Reason for the event | 
**type** | **str** | Event type | 

## Example

```python
from hyperstack.models.contract_event_create_model import ContractEventCreateModel

# TODO update the JSON string below
json = "{}"
# create an instance of ContractEventCreateModel from a JSON string
contract_event_create_model_instance = ContractEventCreateModel.from_json(json)
# print the JSON string representation of the object
print(ContractEventCreateModel.to_json())

# convert the object into a dict
contract_event_create_model_dict = contract_event_create_model_instance.to_dict()
# create an instance of ContractEventCreateModel from a dict
contract_event_create_model_from_dict = ContractEventCreateModel.from_dict(contract_event_create_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


