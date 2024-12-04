# ImportKeypairResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keypair** | [**KeypairFields**](KeypairFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.import_keypair_response import ImportKeypairResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportKeypairResponse from a JSON string
import_keypair_response_instance = ImportKeypairResponse.from_json(json)
# print the JSON string representation of the object
print(ImportKeypairResponse.to_json())

# convert the object into a dict
import_keypair_response_dict = import_keypair_response_instance.to_dict()
# create an instance of ImportKeypairResponse from a dict
import_keypair_response_from_dict = ImportKeypairResponse.from_dict(import_keypair_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


