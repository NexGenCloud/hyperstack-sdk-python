# GPUFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**example_metadata** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**regions** | [**List[GPURegionFields]**](GPURegionFields.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.gpu_fields import GPUFields

# TODO update the JSON string below
json = "{}"
# create an instance of GPUFields from a JSON string
gpu_fields_instance = GPUFields.from_json(json)
# print the JSON string representation of the object
print(GPUFields.to_json())

# convert the object into a dict
gpu_fields_dict = gpu_fields_instance.to_dict()
# create an instance of GPUFields from a dict
gpu_fields_from_dict = GPUFields.from_dict(gpu_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


