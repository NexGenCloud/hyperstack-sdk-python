# FlavorPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** |  | 
**disk** | **int** |  | 
**gpu** | **str** |  | 
**gpu_count** | **int** |  | 
**is_public** | **bool** |  | 
**name** | **str** |  | 
**ram** | **float** |  | 
**region_name** | **str** |  | 

## Example

```python
from hyperstack.models.flavor_payload import FlavorPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FlavorPayload from a JSON string
flavor_payload_instance = FlavorPayload.from_json(json)
# print the JSON string representation of the object
print(FlavorPayload.to_json())

# convert the object into a dict
flavor_payload_dict = flavor_payload_instance.to_dict()
# create an instance of FlavorPayload from a dict
flavor_payload_from_dict = FlavorPayload.from_dict(flavor_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


