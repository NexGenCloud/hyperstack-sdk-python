# ImageGenerationBillingHistoryDetailsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_history_image_generation_details** | [**BillingHistoryImageGenerationDetails**](BillingHistoryImageGenerationDetails.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.image_generation_billing_history_details_response_schema import ImageGenerationBillingHistoryDetailsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImageGenerationBillingHistoryDetailsResponseSchema from a JSON string
image_generation_billing_history_details_response_schema_instance = ImageGenerationBillingHistoryDetailsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ImageGenerationBillingHistoryDetailsResponseSchema.to_json())

# convert the object into a dict
image_generation_billing_history_details_response_schema_dict = image_generation_billing_history_details_response_schema_instance.to_dict()
# create an instance of ImageGenerationBillingHistoryDetailsResponseSchema from a dict
image_generation_billing_history_details_response_schema_from_dict = ImageGenerationBillingHistoryDetailsResponseSchema.from_dict(image_generation_billing_history_details_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


