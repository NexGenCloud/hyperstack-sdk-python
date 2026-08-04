# SupportedKeypairPublicKeyTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**supported_key_types** | **List[str]** |  | [optional] 

## Example

```python
from hyperstack.models.supported_keypair_public_key_types_response import SupportedKeypairPublicKeyTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedKeypairPublicKeyTypesResponse from a JSON string
supported_keypair_public_key_types_response_instance = SupportedKeypairPublicKeyTypesResponse.from_json(json)
# print the JSON string representation of the object
print(SupportedKeypairPublicKeyTypesResponse.to_json())

# convert the object into a dict
supported_keypair_public_key_types_response_dict = supported_keypair_public_key_types_response_instance.to_dict()
# create an instance of SupportedKeypairPublicKeyTypesResponse from a dict
supported_keypair_public_key_types_response_from_dict = SupportedKeypairPublicKeyTypesResponse.from_dict(supported_keypair_public_key_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


