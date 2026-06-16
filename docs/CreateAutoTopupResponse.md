# CreateAutoTopupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_topup** | [**AutoTopup**](AutoTopup.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.create_auto_topup_response import CreateAutoTopupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutoTopupResponse from a JSON string
create_auto_topup_response_instance = CreateAutoTopupResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAutoTopupResponse.to_json())

# convert the object into a dict
create_auto_topup_response_dict = create_auto_topup_response_instance.to_dict()
# create an instance of CreateAutoTopupResponse from a dict
create_auto_topup_response_from_dict = CreateAutoTopupResponse.from_dict(create_auto_topup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


