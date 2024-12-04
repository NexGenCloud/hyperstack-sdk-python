# ExportBillingDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **datetime** |  | 
**org_id** | **int** |  | [optional] 
**required_attributes** | **List[str]** |  | 
**required_metrics** | **List[str]** |  | 
**resource_type** | **str** |  | 
**start_date** | **datetime** |  | 

## Example

```python
from hyperstack.models.export_billing_data_request import ExportBillingDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportBillingDataRequest from a JSON string
export_billing_data_request_instance = ExportBillingDataRequest.from_json(json)
# print the JSON string representation of the object
print(ExportBillingDataRequest.to_json())

# convert the object into a dict
export_billing_data_request_dict = export_billing_data_request_instance.to_dict()
# create an instance of ExportBillingDataRequest from a dict
export_billing_data_request_from_dict = ExportBillingDataRequest.from_dict(export_billing_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


