# BetaAccessRequestPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** | Optional metadata for the request | [optional] 
**program** | **str** | Name of the beta program | 

## Example

```python
from hyperstack.models.beta_access_request_payload import BetaAccessRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BetaAccessRequestPayload from a JSON string
beta_access_request_payload_instance = BetaAccessRequestPayload.from_json(json)
# print the JSON string representation of the object
print(BetaAccessRequestPayload.to_json())

# convert the object into a dict
beta_access_request_payload_dict = beta_access_request_payload_instance.to_dict()
# create an instance of BetaAccessRequestPayload from a dict
beta_access_request_payload_from_dict = BetaAccessRequestPayload.from_dict(beta_access_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


