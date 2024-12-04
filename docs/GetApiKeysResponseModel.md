# GetApiKeysResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_keys** | [**List[ApiKeyFields]**](ApiKeyFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.get_api_keys_response_model import GetApiKeysResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiKeysResponseModel from a JSON string
get_api_keys_response_model_instance = GetApiKeysResponseModel.from_json(json)
# print the JSON string representation of the object
print(GetApiKeysResponseModel.to_json())

# convert the object into a dict
get_api_keys_response_model_dict = get_api_keys_response_model_instance.to_dict()
# create an instance of GetApiKeysResponseModel from a dict
get_api_keys_response_model_from_dict = GetApiKeysResponseModel.from_dict(get_api_keys_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


