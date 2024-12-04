# GetAllContractFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**expiration_policy** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**start_date** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.get_all_contract_fields import GetAllContractFields

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllContractFields from a JSON string
get_all_contract_fields_instance = GetAllContractFields.from_json(json)
# print the JSON string representation of the object
print(GetAllContractFields.to_json())

# convert the object into a dict
get_all_contract_fields_dict = get_all_contract_fields_instance.to_dict()
# create an instance of GetAllContractFields from a dict
get_all_contract_fields_from_dict = GetAllContractFields.from_dict(get_all_contract_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


