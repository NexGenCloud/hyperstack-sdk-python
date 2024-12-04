# InternalInstanceFlavorFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**disk** | **int** |  | [optional] 
**gpu** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**ram** | **int** |  | [optional] 
**region_name** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.internal_instance_flavor_fields import InternalInstanceFlavorFields

# TODO update the JSON string below
json = "{}"
# create an instance of InternalInstanceFlavorFields from a JSON string
internal_instance_flavor_fields_instance = InternalInstanceFlavorFields.from_json(json)
# print the JSON string representation of the object
print(InternalInstanceFlavorFields.to_json())

# convert the object into a dict
internal_instance_flavor_fields_dict = internal_instance_flavor_fields_instance.to_dict()
# create an instance of InternalInstanceFlavorFields from a dict
internal_instance_flavor_fields_from_dict = InternalInstanceFlavorFields.from_dict(internal_instance_flavor_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


