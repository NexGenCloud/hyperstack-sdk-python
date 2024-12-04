# AddUpdateFlavorOrganizationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** |  | 
**description** | **str** |  | [optional] 
**disk** | **int** |  | 
**ephemeral** | **int** |  | [optional] 
**gpu_count** | **int** |  | 
**gpu_id** | **int** |  | 
**is_public** | **bool** |  | 
**labels** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**openstack_id** | **str** |  | 
**organizations** | **List[int]** |  | 
**ram** | **float** |  | 
**region_id** | **int** |  | 

## Example

```python
from hyperstack.models.add_update_flavor_organization_payload import AddUpdateFlavorOrganizationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AddUpdateFlavorOrganizationPayload from a JSON string
add_update_flavor_organization_payload_instance = AddUpdateFlavorOrganizationPayload.from_json(json)
# print the JSON string representation of the object
print(AddUpdateFlavorOrganizationPayload.to_json())

# convert the object into a dict
add_update_flavor_organization_payload_dict = add_update_flavor_organization_payload_instance.to_dict()
# create an instance of AddUpdateFlavorOrganizationPayload from a dict
add_update_flavor_organization_payload_from_dict = AddUpdateFlavorOrganizationPayload.from_dict(add_update_flavor_organization_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


