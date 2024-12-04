# Billingmetricesresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Billingmetricesfields]**](Billingmetricesfields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.billingmetricesresponse import Billingmetricesresponse

# TODO update the JSON string below
json = "{}"
# create an instance of Billingmetricesresponse from a JSON string
billingmetricesresponse_instance = Billingmetricesresponse.from_json(json)
# print the JSON string representation of the object
print(Billingmetricesresponse.to_json())

# convert the object into a dict
billingmetricesresponse_dict = billingmetricesresponse_instance.to_dict()
# create an instance of Billingmetricesresponse from a dict
billingmetricesresponse_from_dict = Billingmetricesresponse.from_dict(billingmetricesresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


