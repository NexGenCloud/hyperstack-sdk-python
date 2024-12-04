# ResourceLevelBillingVolumeDetailsResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ResourceLevelBillingDetailsVolumeAttributes**](ResourceLevelBillingDetailsVolumeAttributes.md) |  | [optional] 
**metrics** | [**ResourceLevelBillingDetailsVolumeMetrics**](ResourceLevelBillingDetailsVolumeMetrics.md) |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_billing_volume_details_resources import ResourceLevelBillingVolumeDetailsResources

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelBillingVolumeDetailsResources from a JSON string
resource_level_billing_volume_details_resources_instance = ResourceLevelBillingVolumeDetailsResources.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelBillingVolumeDetailsResources.to_json())

# convert the object into a dict
resource_level_billing_volume_details_resources_dict = resource_level_billing_volume_details_resources_instance.to_dict()
# create an instance of ResourceLevelBillingVolumeDetailsResources from a dict
resource_level_billing_volume_details_resources_from_dict = ResourceLevelBillingVolumeDetailsResources.from_dict(resource_level_billing_volume_details_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


