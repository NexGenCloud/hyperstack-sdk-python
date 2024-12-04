# ResourceLevelBillingDetailsVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history** | [**List[ResourceLevelBillingVolumeDetailsResources]**](ResourceLevelBillingVolumeDetailsResources.md) |  | [optional] 
**org_id** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_billing_details_volume import ResourceLevelBillingDetailsVolume

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelBillingDetailsVolume from a JSON string
resource_level_billing_details_volume_instance = ResourceLevelBillingDetailsVolume.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelBillingDetailsVolume.to_json())

# convert the object into a dict
resource_level_billing_details_volume_dict = resource_level_billing_details_volume_instance.to_dict()
# create an instance of ResourceLevelBillingDetailsVolume from a dict
resource_level_billing_details_volume_from_dict = ResourceLevelBillingDetailsVolume.from_dict(resource_level_billing_details_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


