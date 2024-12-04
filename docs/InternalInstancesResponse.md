# InternalInstancesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**List[InternalInstanceFields]**](InternalInstanceFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.internal_instances_response import InternalInstancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalInstancesResponse from a JSON string
internal_instances_response_instance = InternalInstancesResponse.from_json(json)
# print the JSON string representation of the object
print(InternalInstancesResponse.to_json())

# convert the object into a dict
internal_instances_response_dict = internal_instances_response_instance.to_dict()
# create an instance of InternalInstancesResponse from a dict
internal_instances_response_from_dict = InternalInstancesResponse.from_dict(internal_instances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


