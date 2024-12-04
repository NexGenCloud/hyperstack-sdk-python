# PricebookResourceObjectResponseForCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_price** | **float** |  | [optional] 
**amount** | **int** |  | [optional] 
**discounted_rate** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**rate** | **float** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.pricebook_resource_object_response_for_customer import PricebookResourceObjectResponseForCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of PricebookResourceObjectResponseForCustomer from a JSON string
pricebook_resource_object_response_for_customer_instance = PricebookResourceObjectResponseForCustomer.from_json(json)
# print the JSON string representation of the object
print(PricebookResourceObjectResponseForCustomer.to_json())

# convert the object into a dict
pricebook_resource_object_response_for_customer_dict = pricebook_resource_object_response_for_customer_instance.to_dict()
# create an instance of PricebookResourceObjectResponseForCustomer from a dict
pricebook_resource_object_response_for_customer_from_dict = PricebookResourceObjectResponseForCustomer.from_dict(pricebook_resource_object_response_for_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


