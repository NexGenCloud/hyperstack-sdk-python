# Lastdaycostresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Lastdaycostfields**](Lastdaycostfields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.lastdaycostresponse import Lastdaycostresponse

# TODO update the JSON string below
json = "{}"
# create an instance of Lastdaycostresponse from a JSON string
lastdaycostresponse_instance = Lastdaycostresponse.from_json(json)
# print the JSON string representation of the object
print(Lastdaycostresponse.to_json())

# convert the object into a dict
lastdaycostresponse_dict = lastdaycostresponse_instance.to_dict()
# create an instance of Lastdaycostresponse from a dict
lastdaycostresponse_from_dict = Lastdaycostresponse.from_dict(lastdaycostresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


