# SubResourceGraphBillingDetailsMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_incurred_bill** | **float** |  | [optional] 
**cpu_incurred_bill_graph** | [**List[GraphDatetimeValueModel]**](GraphDatetimeValueModel.md) |  | [optional] 
**disk_incurred_bill** | **float** |  | [optional] 
**disk_incurred_bill_graph** | [**List[GraphDatetimeValueModel]**](GraphDatetimeValueModel.md) |  | [optional] 
**ephemeral_incurred_bill** | **float** |  | [optional] 
**ephemeral_incurred_bill_graph** | [**List[GraphDatetimeValueModel]**](GraphDatetimeValueModel.md) |  | [optional] 
**gpu_incurred_bill** | **float** |  | [optional] 
**gpu_incurred_bill_graph** | [**List[GraphDatetimeValueModel]**](GraphDatetimeValueModel.md) |  | [optional] 
**publicip_incurred_bill** | **float** |  | [optional] 
**publicip_incurred_bill_graph** | [**List[GraphDatetimeValueModel]**](GraphDatetimeValueModel.md) |  | [optional] 
**ram_incurred_bill** | **float** |  | [optional] 
**ram_incurred_bill_graph** | [**List[GraphDatetimeValueModel]**](GraphDatetimeValueModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.sub_resource_graph_billing_details_metrics import SubResourceGraphBillingDetailsMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of SubResourceGraphBillingDetailsMetrics from a JSON string
sub_resource_graph_billing_details_metrics_instance = SubResourceGraphBillingDetailsMetrics.from_json(json)
# print the JSON string representation of the object
print(SubResourceGraphBillingDetailsMetrics.to_json())

# convert the object into a dict
sub_resource_graph_billing_details_metrics_dict = sub_resource_graph_billing_details_metrics_instance.to_dict()
# create an instance of SubResourceGraphBillingDetailsMetrics from a dict
sub_resource_graph_billing_details_metrics_from_dict = SubResourceGraphBillingDetailsMetrics.from_dict(sub_resource_graph_billing_details_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


