# InternalSecurityRulesFieldsForInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**direction** | **str** |  | [optional] 
**ethertype** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**port_range_max** | **int** |  | [optional] 
**port_range_min** | **int** |  | [optional] 
**protocol** | **str** |  | [optional] 
**remote_ip_prefix** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.internal_security_rules_fields_for_instance import InternalSecurityRulesFieldsForInstance

# TODO update the JSON string below
json = "{}"
# create an instance of InternalSecurityRulesFieldsForInstance from a JSON string
internal_security_rules_fields_for_instance_instance = InternalSecurityRulesFieldsForInstance.from_json(json)
# print the JSON string representation of the object
print(InternalSecurityRulesFieldsForInstance.to_json())

# convert the object into a dict
internal_security_rules_fields_for_instance_dict = internal_security_rules_fields_for_instance_instance.to_dict()
# create an instance of InternalSecurityRulesFieldsForInstance from a dict
internal_security_rules_fields_for_instance_from_dict = InternalSecurityRulesFieldsForInstance.from_dict(internal_security_rules_fields_for_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


