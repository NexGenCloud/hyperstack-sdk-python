# ZendeskMessagingToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**token** | **str** | Signed HS256 JWT to pass to the Zendesk Web Widget loginUser API | [optional] 

## Example

```python
from hyperstack.models.zendesk_messaging_token import ZendeskMessagingToken

# TODO update the JSON string below
json = "{}"
# create an instance of ZendeskMessagingToken from a JSON string
zendesk_messaging_token_instance = ZendeskMessagingToken.from_json(json)
# print the JSON string representation of the object
print(ZendeskMessagingToken.to_json())

# convert the object into a dict
zendesk_messaging_token_dict = zendesk_messaging_token_instance.to_dict()
# create an instance of ZendeskMessagingToken from a dict
zendesk_messaging_token_from_dict = ZendeskMessagingToken.from_dict(zendesk_messaging_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


