# ResourceLevelBucketBillingDetailsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_bucket_details** | [**ResourceLevelBillingBucketDetailsResources**](ResourceLevelBillingBucketDetailsResources.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.resource_level_bucket_billing_details_response_model import ResourceLevelBucketBillingDetailsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLevelBucketBillingDetailsResponseModel from a JSON string
resource_level_bucket_billing_details_response_model_instance = ResourceLevelBucketBillingDetailsResponseModel.from_json(json)
# print the JSON string representation of the object
print(ResourceLevelBucketBillingDetailsResponseModel.to_json())

# convert the object into a dict
resource_level_bucket_billing_details_response_model_dict = resource_level_bucket_billing_details_response_model_instance.to_dict()
# create an instance of ResourceLevelBucketBillingDetailsResponseModel from a dict
resource_level_bucket_billing_details_response_model_from_dict = ResourceLevelBucketBillingDetailsResponseModel.from_dict(resource_level_bucket_billing_details_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


