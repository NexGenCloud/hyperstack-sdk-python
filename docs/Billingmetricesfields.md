# Billingmetricesfields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**bill_per_minute** | **float** |  | [optional] 
**create_time** | **datetime** |  | [optional] 
**exclude_billing** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**terminate_time** | **datetime** |  | [optional] 
**total_bill** | **float** |  | [optional] 
**total_up_time** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.billingmetricesfields import Billingmetricesfields

# TODO update the JSON string below
json = "{}"
# create an instance of Billingmetricesfields from a JSON string
billingmetricesfields_instance = Billingmetricesfields.from_json(json)
# print the JSON string representation of the object
print(Billingmetricesfields.to_json())

# convert the object into a dict
billingmetricesfields_dict = billingmetricesfields_instance.to_dict()
# create an instance of Billingmetricesfields from a dict
billingmetricesfields_from_dict = Billingmetricesfields.from_dict(billingmetricesfields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


