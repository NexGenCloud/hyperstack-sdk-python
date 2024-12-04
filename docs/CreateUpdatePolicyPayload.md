# CreateUpdatePolicyPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**is_public** | **bool** |  | 
**name** | **str** |  | 
**permissions** | **List[int]** |  | 

## Example

```python
from hyperstack.models.create_update_policy_payload import CreateUpdatePolicyPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpdatePolicyPayload from a JSON string
create_update_policy_payload_instance = CreateUpdatePolicyPayload.from_json(json)
# print the JSON string representation of the object
print(CreateUpdatePolicyPayload.to_json())

# convert the object into a dict
create_update_policy_payload_dict = create_update_policy_payload_instance.to_dict()
# create an instance of CreateUpdatePolicyPayload from a dict
create_update_policy_payload_from_dict = CreateUpdatePolicyPayload.from_dict(create_update_policy_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


