# GetAllContractsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contracts** | [**List[GetAllContractFields]**](GetAllContractFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.get_all_contracts_response_model import GetAllContractsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllContractsResponseModel from a JSON string
get_all_contracts_response_model_instance = GetAllContractsResponseModel.from_json(json)
# print the JSON string representation of the object
print(GetAllContractsResponseModel.to_json())

# convert the object into a dict
get_all_contracts_response_model_dict = get_all_contracts_response_model_instance.to_dict()
# create an instance of GetAllContractsResponseModel from a dict
get_all_contracts_response_model_from_dict = GetAllContractsResponseModel.from_dict(get_all_contracts_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


