# InternalInstanceKeypairFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**environment** | **str** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.internal_instance_keypair_fields import InternalInstanceKeypairFields

# TODO update the JSON string below
json = "{}"
# create an instance of InternalInstanceKeypairFields from a JSON string
internal_instance_keypair_fields_instance = InternalInstanceKeypairFields.from_json(json)
# print the JSON string representation of the object
print(InternalInstanceKeypairFields.to_json())

# convert the object into a dict
internal_instance_keypair_fields_dict = internal_instance_keypair_fields_instance.to_dict()
# create an instance of InternalInstanceKeypairFields from a dict
internal_instance_keypair_fields_from_dict = InternalInstanceKeypairFields.from_dict(internal_instance_keypair_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


