# SecurityGroupRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**security_rule** | [**SecurityGroupRuleFields**](SecurityGroupRuleFields.md) |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.security_group_rule import SecurityGroupRule

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityGroupRule from a JSON string
security_group_rule_instance = SecurityGroupRule.from_json(json)
# print the JSON string representation of the object
print(SecurityGroupRule.to_json())

# convert the object into a dict
security_group_rule_dict = security_group_rule_instance.to_dict()
# create an instance of SecurityGroupRule from a dict
security_group_rule_from_dict = SecurityGroupRule.from_dict(security_group_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


