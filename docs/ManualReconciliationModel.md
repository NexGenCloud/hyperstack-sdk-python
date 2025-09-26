# ManualReconciliationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**ClusterFields**](ClusterFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.manual_reconciliation_model import ManualReconciliationModel

# TODO update the JSON string below
json = "{}"
# create an instance of ManualReconciliationModel from a JSON string
manual_reconciliation_model_instance = ManualReconciliationModel.from_json(json)
# print the JSON string representation of the object
print(ManualReconciliationModel.to_json())

# convert the object into a dict
manual_reconciliation_model_dict = manual_reconciliation_model_instance.to_dict()
# create an instance of ManualReconciliationModel from a dict
manual_reconciliation_model_from_dict = ManualReconciliationModel.from_dict(manual_reconciliation_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


