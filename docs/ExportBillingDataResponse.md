# ExportBillingDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measures** | **List[object]** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.export_billing_data_response import ExportBillingDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExportBillingDataResponse from a JSON string
export_billing_data_response_instance = ExportBillingDataResponse.from_json(json)
# print the JSON string representation of the object
print(ExportBillingDataResponse.to_json())

# convert the object into a dict
export_billing_data_response_dict = export_billing_data_response_instance.to_dict()
# create an instance of ExportBillingDataResponse from a dict
export_billing_data_response_from_dict = ExportBillingDataResponse.from_dict(export_billing_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


