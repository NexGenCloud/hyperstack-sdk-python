# FlavorVMFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**host** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**openstack_id** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.flavor_vm_fields import FlavorVMFields

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorVMFields from a JSON string
flavor_vm_fields_instance = FlavorVMFields.from_json(json)
# print the JSON string representation of the object
print(FlavorVMFields.to_json())

# convert the object into a dict
flavor_vm_fields_dict = flavor_vm_fields_instance.to_dict()
# create an instance of FlavorVMFields from a dict
flavor_vm_fields_from_dict = FlavorVMFields.from_dict(flavor_vm_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


