# ResourceBillingResponseForCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculated_resource_bills** | [**ResourceObjectResponseForCustomer**](ResourceObjectResponseForCustomer.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.resource_billing_response_for_customer import ResourceBillingResponseForCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceBillingResponseForCustomer from a JSON string
resource_billing_response_for_customer_instance = ResourceBillingResponseForCustomer.from_json(json)
# print the JSON string representation of the object
print(ResourceBillingResponseForCustomer.to_json())

# convert the object into a dict
resource_billing_response_for_customer_dict = resource_billing_response_for_customer_instance.to_dict()
# create an instance of ResourceBillingResponseForCustomer from a dict
resource_billing_response_for_customer_from_dict = ResourceBillingResponseForCustomer.from_dict(resource_billing_response_for_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


