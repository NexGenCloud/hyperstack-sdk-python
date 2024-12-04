# CreateInstancesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**List[InstanceFields]**](InstanceFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.create_instances_response import CreateInstancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInstancesResponse from a JSON string
create_instances_response_instance = CreateInstancesResponse.from_json(json)
# print the JSON string representation of the object
print(CreateInstancesResponse.to_json())

# convert the object into a dict
create_instances_response_dict = create_instances_response_instance.to_dict()
# create an instance of CreateInstancesResponse from a dict
create_instances_response_from_dict = CreateInstancesResponse.from_dict(create_instances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


