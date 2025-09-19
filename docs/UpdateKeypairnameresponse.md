# UpdateKeypairNameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keypair** | [**KeypairFields**](KeypairFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.update_keypair_name_response import UpdateKeypairNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKeypairNameResponse from a JSON string
update_keypair_name_response_instance = UpdateKeypairNameResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateKeypairNameResponse.to_json())

# convert the object into a dict
update_keypair_name_response_dict = update_keypair_name_response_instance.to_dict()
# create an instance of UpdateKeypairNameResponse from a dict
update_keypair_name_response_from_dict = UpdateKeypairNameResponse.from_dict(update_keypair_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


