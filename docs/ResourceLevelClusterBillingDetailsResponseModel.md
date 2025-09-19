# ResourceLevelClusterBillingDetailsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_cluster_details** | [**ResourceLevelBillingHistoryResourcesCluster**](ResourceLevelBillingHistoryResourcesCluster.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_cluster_billing_details_response_model import ResourceLevelClusterBillingDetailsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelClusterBillingDetailsResponseModel from a JSON string
resource_level_cluster_billing_details_response_model_instance = ResourceLevelClusterBillingDetailsResponseModel.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelClusterBillingDetailsResponseModel.to_json())

# convert the object into a dict
resource_level_cluster_billing_details_response_model_dict = resource_level_cluster_billing_details_response_model_instance.to_dict()
# create an instance of ResourceLevelClusterBillingDetailsResponseModel from a dict
resource_level_cluster_billing_details_response_model_from_dict = ResourceLevelClusterBillingDetailsResponseModel.from_dict(resource_level_cluster_billing_details_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


