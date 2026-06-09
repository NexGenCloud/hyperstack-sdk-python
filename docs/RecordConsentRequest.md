# RecordConsentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**consent_method** | **str** |  | [optional] [default to 'web_checkbox']
**consent_type** | **str** |  | 
**consent_version** | **str** | Version identifier. Defaults to the current version for the consent type | [optional] 
**metadata** | **object** | Consent-type-specific metadata | [optional] 

## Example

```python
from hyperstack.models.record_consent_request import RecordConsentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordConsentRequest from a JSON string
record_consent_request_instance = RecordConsentRequest.from_json(json)
# print the JSON string representation of the object
print(RecordConsentRequest.to_json())

# convert the object into a dict
record_consent_request_dict = record_consent_request_instance.to_dict()
# create an instance of RecordConsentRequest from a dict
record_consent_request_from_dict = RecordConsentRequest.from_dict(record_consent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


