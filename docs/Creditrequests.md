# Creditrequests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_user_id** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**reason** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.creditrequests import Creditrequests

# TODO update the JSON string below
json = "{}"
# create an instance of Creditrequests from a JSON string
creditrequests_instance = Creditrequests.from_json(json)
# print the JSON string representation of the object
print(Creditrequests.to_json())

# convert the object into a dict
creditrequests_dict = creditrequests_instance.to_dict()
# create an instance of Creditrequests from a dict
creditrequests_from_dict = Creditrequests.from_dict(creditrequests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


