# Creditrequestresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Creditrequests]**](Creditrequests.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.creditrequestresponse import Creditrequestresponse

# TODO update the JSON string below
json = "{}"
# create an instance of Creditrequestresponse from a JSON string
creditrequestresponse_instance = Creditrequestresponse.from_json(json)
# print the JSON string representation of the object
print(Creditrequestresponse.to_json())

# convert the object into a dict
creditrequestresponse_dict = creditrequestresponse_instance.to_dict()
# create an instance of Creditrequestresponse from a dict
creditrequestresponse_from_dict = Creditrequestresponse.from_dict(creditrequestresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


