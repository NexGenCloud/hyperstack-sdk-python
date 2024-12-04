# OrganizationFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**credit** | **int** |  | [optional] 
**id** | **int** |  | 
**name** | **str** |  | 
**threshold** | **int** |  | [optional] 
**total_clusters** | **int** |  | [optional] 
**total_containers** | **int** |  | [optional] 
**total_instances** | **int** |  | [optional] 
**total_volumes** | **int** |  | [optional] 
**users** | [**List[OrganizationUserResponseModel]**](OrganizationUserResponseModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.organization_fields import OrganizationFields

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationFields from a JSON string
organization_fields_instance = OrganizationFields.from_json(json)
# print the JSON string representation of the object
print(OrganizationFields.to_json())

# convert the object into a dict
organization_fields_dict = organization_fields_instance.to_dict()
# create an instance of OrganizationFields from a dict
organization_fields_from_dict = OrganizationFields.from_dict(organization_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


