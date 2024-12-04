# ResourceLevelVolumeGraphBillingDetailsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_snapshot_details** | [**ResourceLevelGraphBillingDetailVolume**](ResourceLevelGraphBillingDetailVolume.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_volume_graph_billing_details_response_model import ResourceLevelVolumeGraphBillingDetailsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelVolumeGraphBillingDetailsResponseModel from a JSON string
resource_level_volume_graph_billing_details_response_model_instance = ResourceLevelVolumeGraphBillingDetailsResponseModel.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelVolumeGraphBillingDetailsResponseModel.to_json())

# convert the object into a dict
resource_level_volume_graph_billing_details_response_model_dict = resource_level_volume_graph_billing_details_response_model_instance.to_dict()
# create an instance of ResourceLevelVolumeGraphBillingDetailsResponseModel from a dict
resource_level_volume_graph_billing_details_response_model_from_dict = ResourceLevelVolumeGraphBillingDetailsResponseModel.from_dict(resource_level_volume_graph_billing_details_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


