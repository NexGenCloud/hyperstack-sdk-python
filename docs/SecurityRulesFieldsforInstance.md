# SecurityRulesFieldsforInstance


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
from hyperstack.models.security_rules_fieldsfor_instance import SecurityRulesFieldsforInstance

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRulesFieldsforInstance from a JSON string
security_rules_fieldsfor_instance_instance = SecurityRulesFieldsforInstance.from_json(json)
# print the JSON string representation of the object
print(SecurityRulesFieldsforInstance.to_json())

# convert the object into a dict
security_rules_fieldsfor_instance_dict = security_rules_fieldsfor_instance_instance.to_dict()
# create an instance of SecurityRulesFieldsforInstance from a dict
security_rules_fieldsfor_instance_from_dict = SecurityRulesFieldsforInstance.from_dict(security_rules_fieldsfor_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


