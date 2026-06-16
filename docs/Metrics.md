# Metrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incurred_bill** | **float** |  | [optional] 
**input_tokens** | **float** |  | [optional] 
**input_tokens_incurred_bill** | **float** |  | [optional] 
**input_tokens_non_discounted_bill** | **float** |  | [optional] 
**non_discounted_bill** | **float** |  | [optional] 
**output_tokens** | **float** |  | [optional] 
**output_tokens_incurred_bill** | **float** |  | [optional] 
**output_tokens_non_discounted_bill** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.metrics import Metrics

# TODO update the JSON string below
json = "{}"
# create an instance of Metrics from a JSON string
metrics_instance = Metrics.from_json(json)
# print the JSON string representation of the object
print(Metrics.to_json())

# convert the object into a dict
metrics_dict = metrics_instance.to_dict()
# create an instance of Metrics from a dict
metrics_from_dict = Metrics.from_dict(metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


