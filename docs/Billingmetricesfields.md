# BillingMetricesFields


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
from hyperstack.models.billing_metrices_fields import BillingMetricesFields

# TODO update the JSON string below
json = "{}"
# create an instance of BillingMetricesFields from a JSON string
billing_metrices_fields_instance = BillingMetricesFields.from_json(json)
# print the JSON string representation of the object
print(BillingMetricesFields.to_json())

# convert the object into a dict
billing_metrices_fields_dict = billing_metrices_fields_instance.to_dict()
# create an instance of BillingMetricesFields from a dict
billing_metrices_fields_from_dict = BillingMetricesFields.from_dict(billing_metrices_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


