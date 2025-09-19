# BetaAccessRequestFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | When the request was made | [optional] 
**id** | **int** | Unique identifier for the request | [optional] 
**program_id** | **int** | ID of the beta program | [optional] 
**program_name** | **str** | Name of the beta program | [optional] 
**status** | **str** | Status of the request | [optional] 
**user_id** | **int** | ID of the user who made the request | [optional] 

## Example

```python
from hyperstack.models.beta_access_request_fields import BetaAccessRequestFields

# TODO update the JSON string below
json = "{}"
# create an instance of BetaAccessRequestFields from a JSON string
beta_access_request_fields_instance = BetaAccessRequestFields.from_json(json)
# print the JSON string representation of the object
print(BetaAccessRequestFields.to_json())

# convert the object into a dict
beta_access_request_fields_dict = beta_access_request_fields_instance.to_dict()
# create an instance of BetaAccessRequestFields from a dict
beta_access_request_fields_from_dict = BetaAccessRequestFields.from_dict(beta_access_request_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


