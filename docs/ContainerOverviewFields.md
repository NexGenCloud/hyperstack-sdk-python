# ContainerOverviewFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_per_hour** | **float** |  | [optional] 
**count** | **int** |  | [optional] 
**gpus** | **int** |  | [optional] 
**ram** | **float** |  | [optional] 
**vcpus** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.container_overview_fields import ContainerOverviewFields

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerOverviewFields from a JSON string
container_overview_fields_instance = ContainerOverviewFields.from_json(json)
# print the JSON string representation of the object
print(ContainerOverviewFields.to_json())

# convert the object into a dict
container_overview_fields_dict = container_overview_fields_instance.to_dict()
# create an instance of ContainerOverviewFields from a dict
container_overview_fields_from_dict = ContainerOverviewFields.from_dict(container_overview_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


