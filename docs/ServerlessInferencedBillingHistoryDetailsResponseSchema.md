# ServerlessInferencedBillingHistoryDetailsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_serverless_inference_details** | [**BillingHistoryServerlessInferenceDetails**](BillingHistoryServerlessInferenceDetails.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.serverless_inferenced_billing_history_details_response_schema import ServerlessInferencedBillingHistoryDetailsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ServerlessInferencedBillingHistoryDetailsResponseSchema from a JSON string
serverless_inferenced_billing_history_details_response_schema_instance = ServerlessInferencedBillingHistoryDetailsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ServerlessInferencedBillingHistoryDetailsResponseSchema.to_json())

# convert the object into a dict
serverless_inferenced_billing_history_details_response_schema_dict = serverless_inferenced_billing_history_details_response_schema_instance.to_dict()
# create an instance of ServerlessInferencedBillingHistoryDetailsResponseSchema from a dict
serverless_inferenced_billing_history_details_response_schema_from_dict = ServerlessInferencedBillingHistoryDetailsResponseSchema.from_dict(serverless_inferenced_billing_history_details_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


