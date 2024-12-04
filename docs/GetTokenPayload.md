# GetTokenPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_code** | **str** |  | 
**session_id** | **str** |  | 

## Example

```python
from hyperstack.models.get_token_payload import GetTokenPayload

# TODO update the JSON string below
json = "{}"
# create an instance of GetTokenPayload from a JSON string
get_token_payload_instance = GetTokenPayload.from_json(json)
# print the JSON string representation of the object
print(GetTokenPayload.to_json())

# convert the object into a dict
get_token_payload_dict = get_token_payload_instance.to_dict()
# create an instance of GetTokenPayload from a dict
get_token_payload_from_dict = GetTokenPayload.from_dict(get_token_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


