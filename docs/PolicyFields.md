# PolicyFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**permissions** | [**List[PolicyPermissionFields]**](PolicyPermissionFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.policy_fields import PolicyFields

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyFields from a JSON string
policy_fields_instance = PolicyFields.from_json(json)
# print the JSON string representation of the object
print(PolicyFields.to_json())

# convert the object into a dict
policy_fields_dict = policy_fields_instance.to_dict()
# create an instance of PolicyFields from a dict
policy_fields_from_dict = PolicyFields.from_dict(policy_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


