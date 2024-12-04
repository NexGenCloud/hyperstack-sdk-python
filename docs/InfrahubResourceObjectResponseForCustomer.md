# InfrahubResourceObjectResponseForCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_price** | **float** |  | [optional] 
**host** | **str** |  | [optional] 
**infrahub_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**resources** | [**List[PricebookResourceObjectResponseForCustomer]**](PricebookResourceObjectResponseForCustomer.md) |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.infrahub_resource_object_response_for_customer import InfrahubResourceObjectResponseForCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of InfrahubResourceObjectResponseForCustomer from a JSON string
infrahub_resource_object_response_for_customer_instance = InfrahubResourceObjectResponseForCustomer.from_json(json)
# print the JSON string representation of the object
print(InfrahubResourceObjectResponseForCustomer.to_json())

# convert the object into a dict
infrahub_resource_object_response_for_customer_dict = infrahub_resource_object_response_for_customer_instance.to_dict()
# create an instance of InfrahubResourceObjectResponseForCustomer from a dict
infrahub_resource_object_response_for_customer_from_dict = InfrahubResourceObjectResponseForCustomer.from_dict(infrahub_resource_object_response_for_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


