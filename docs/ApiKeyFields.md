# ApiKeyFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.api_key_fields import ApiKeyFields

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyFields from a JSON string
api_key_fields_instance = ApiKeyFields.from_json(json)
# print the JSON string representation of the object
print(ApiKeyFields.to_json())

# convert the object into a dict
api_key_fields_dict = api_key_fields_instance.to_dict()
# create an instance of ApiKeyFields from a dict
api_key_fields_from_dict = ApiKeyFields.from_dict(api_key_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


