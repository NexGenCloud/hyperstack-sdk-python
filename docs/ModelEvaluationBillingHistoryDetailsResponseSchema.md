# ModelEvaluationBillingHistoryDetailsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_model_evalutation_details** | [**BillingHistoryModelEvalutationDetails**](BillingHistoryModelEvalutationDetails.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.model_evaluation_billing_history_details_response_schema import ModelEvaluationBillingHistoryDetailsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ModelEvaluationBillingHistoryDetailsResponseSchema from a JSON string
model_evaluation_billing_history_details_response_schema_instance = ModelEvaluationBillingHistoryDetailsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ModelEvaluationBillingHistoryDetailsResponseSchema.to_json())

# convert the object into a dict
model_evaluation_billing_history_details_response_schema_dict = model_evaluation_billing_history_details_response_schema_instance.to_dict()
# create an instance of ModelEvaluationBillingHistoryDetailsResponseSchema from a dict
model_evaluation_billing_history_details_response_schema_from_dict = ModelEvaluationBillingHistoryDetailsResponseSchema.from_dict(model_evaluation_billing_history_details_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


