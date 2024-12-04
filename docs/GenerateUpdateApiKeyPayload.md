# GenerateUpdateApiKeyPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from hyperstack.models.generate_update_api_key_payload import GenerateUpdateApiKeyPayload

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateUpdateApiKeyPayload from a JSON string
generate_update_api_key_payload_instance = GenerateUpdateApiKeyPayload.from_json(json)
# print the JSON string representation of the object
print(GenerateUpdateApiKeyPayload.to_json())

# convert the object into a dict
generate_update_api_key_payload_dict = generate_update_api_key_payload_instance.to_dict()
# create an instance of GenerateUpdateApiKeyPayload from a dict
generate_update_api_key_payload_from_dict = GenerateUpdateApiKeyPayload.from_dict(generate_update_api_key_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


