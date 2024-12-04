# GetCustomerContractsListResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contracts** | [**List[CustomerContractFields]**](CustomerContractFields.md) |  | [optional] 
**count** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.get_customer_contracts_list_response_model import GetCustomerContractsListResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerContractsListResponseModel from a JSON string
get_customer_contracts_list_response_model_instance = GetCustomerContractsListResponseModel.from_json(json)
# print the JSON string representation of the object
print(GetCustomerContractsListResponseModel.to_json())

# convert the object into a dict
get_customer_contracts_list_response_model_dict = get_customer_contracts_list_response_model_instance.to_dict()
# create an instance of GetCustomerContractsListResponseModel from a dict
get_customer_contracts_list_response_model_from_dict = GetCustomerContractsListResponseModel.from_dict(get_customer_contracts_list_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


