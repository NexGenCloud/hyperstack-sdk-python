# GPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu** | [**GPUFields**](GPUFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.gpu import GPU

# TODO update the JSON string below
json = "{}"
# create an instance of GPU from a JSON string
gpu_instance = GPU.from_json(json)
# print the JSON string representation of the object
print(GPU.to_json())

# convert the object into a dict
gpu_dict = gpu_instance.to_dict()
# create an instance of GPU from a dict
gpu_from_dict = GPU.from_dict(gpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


