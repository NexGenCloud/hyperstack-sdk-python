# HistoricalInstancesFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**environment** | **str** |  | [optional] 
**environment_id** | **int** |  | [optional] 
**flavor** | **str** |  | [optional] 
**flavor_id** | **int** |  | [optional] 
**floating_ip** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**openstack_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.historical_instances_fields import HistoricalInstancesFields

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricalInstancesFields from a JSON string
historical_instances_fields_instance = HistoricalInstancesFields.from_json(json)
# print the JSON string representation of the object
print(HistoricalInstancesFields.to_json())

# convert the object into a dict
historical_instances_fields_dict = historical_instances_fields_instance.to_dict()
# create an instance of HistoricalInstancesFields from a dict
historical_instances_fields_from_dict = HistoricalInstancesFields.from_dict(historical_instances_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


