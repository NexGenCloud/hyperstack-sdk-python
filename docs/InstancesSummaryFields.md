# InstancesSummaryFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**environment** | **str** |  | [optional] 
**environment_id** | **int** |  | [optional] 
**fixed_ip** | **str** |  | [optional] 
**flavor** | **str** |  | [optional] 
**flavor_id** | **int** |  | [optional] 
**floating_ip** | **str** |  | [optional] 
**floating_ip_status** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**image** | **str** |  | [optional] 
**image_id** | **int** |  | [optional] 
**keypair** | **str** |  | [optional] 
**keypair_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.instances_summary_fields import InstancesSummaryFields

# TODO update the JSON string below
json = "{}"
# create an instance of InstancesSummaryFields from a JSON string
instances_summary_fields_instance = InstancesSummaryFields.from_json(json)
# print the JSON string representation of the object
print(InstancesSummaryFields.to_json())

# convert the object into a dict
instances_summary_fields_dict = instances_summary_fields_instance.to_dict()
# create an instance of InstancesSummaryFields from a dict
instances_summary_fields_from_dict = InstancesSummaryFields.from_dict(instances_summary_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


