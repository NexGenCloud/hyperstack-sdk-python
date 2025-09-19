# DataSynthesisBillingHistoryDetailsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_data_synthesis_details** | [**BillingHistoryDataSynthesisDetails**](BillingHistoryDataSynthesisDetails.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.data_synthesis_billing_history_details_response_schema import DataSynthesisBillingHistoryDetailsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataSynthesisBillingHistoryDetailsResponseSchema from a JSON string
data_synthesis_billing_history_details_response_schema_instance = DataSynthesisBillingHistoryDetailsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DataSynthesisBillingHistoryDetailsResponseSchema.to_json())

# convert the object into a dict
data_synthesis_billing_history_details_response_schema_dict = data_synthesis_billing_history_details_response_schema_instance.to_dict()
# create an instance of DataSynthesisBillingHistoryDetailsResponseSchema from a dict
data_synthesis_billing_history_details_response_schema_from_dict = DataSynthesisBillingHistoryDetailsResponseSchema.from_dict(data_synthesis_billing_history_details_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


