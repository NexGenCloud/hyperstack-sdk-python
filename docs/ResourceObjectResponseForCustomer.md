# ResourceObjectResponseForCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** |  | [optional] 
**resource** | [**InfrahubResourceObjectResponseForCustomer**](InfrahubResourceObjectResponseForCustomer.md) |  | [optional] 

## Example

```python
from hyperstack.models.resource_object_response_for_customer import ResourceObjectResponseForCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceObjectResponseForCustomer from a JSON string
resource_object_response_for_customer_instance = ResourceObjectResponseForCustomer.from_json(json)
# print the JSON string representation of the object
print(ResourceObjectResponseForCustomer.to_json())

# convert the object into a dict
resource_object_response_for_customer_dict = resource_object_response_for_customer_instance.to_dict()
# create an instance of ResourceObjectResponseForCustomer from a dict
resource_object_response_for_customer_from_dict = ResourceObjectResponseForCustomer.from_dict(resource_object_response_for_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


