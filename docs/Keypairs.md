# Keypairs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**keypairs** | [**List[KeypairFields]**](KeypairFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.keypairs import Keypairs

# TODO update the JSON string below
json = "{}"
# create an instance of Keypairs from a JSON string
keypairs_instance = Keypairs.from_json(json)
# print the JSON string representation of the object
print(Keypairs.to_json())

# convert the object into a dict
keypairs_dict = keypairs_instance.to_dict()
# create an instance of Keypairs from a dict
keypairs_from_dict = Keypairs.from_dict(keypairs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


