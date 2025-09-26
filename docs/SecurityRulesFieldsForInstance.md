# SecurityRulesFieldsForInstance


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
from hyperstack.models.security_rules_fields_for_instance import SecurityRulesFieldsForInstance

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRulesFieldsForInstance from a JSON string
security_rules_fields_for_instance_instance = SecurityRulesFieldsForInstance.from_json(json)
# print the JSON string representation of the object
print(SecurityRulesFieldsForInstance.to_json())

# convert the object into a dict
security_rules_fields_for_instance_dict = security_rules_fields_for_instance_instance.to_dict()
# create an instance of SecurityRulesFieldsForInstance from a dict
security_rules_fields_for_instance_from_dict = SecurityRulesFieldsForInstance.from_dict(security_rules_fields_for_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


