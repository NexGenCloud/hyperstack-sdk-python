# InstanceOverviewFields


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
from hyperstack.models.instance_overview_fields import InstanceOverviewFields

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceOverviewFields from a JSON string
instance_overview_fields_instance = InstanceOverviewFields.from_json(json)
# print the JSON string representation of the object
print(InstanceOverviewFields.to_json())

# convert the object into a dict
instance_overview_fields_dict = instance_overview_fields_instance.to_dict()
# create an instance of InstanceOverviewFields from a dict
instance_overview_fields_from_dict = InstanceOverviewFields.from_dict(instance_overview_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


