# UpdateConsentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**consent_method** | **str** |  | [optional] [default to 'web_checkbox']
**consent_version** | **str** | Version identifier. Defaults to the current version for the consent type | [optional] 
**metadata** | **object** | Consent-type-specific metadata | [optional] 

## Example

```python
from hyperstack.models.update_consent_request import UpdateConsentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConsentRequest from a JSON string
update_consent_request_instance = UpdateConsentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateConsentRequest.to_json())

# convert the object into a dict
update_consent_request_dict = update_consent_request_instance.to_dict()
# create an instance of UpdateConsentRequest from a dict
update_consent_request_from_dict = UpdateConsentRequest.from_dict(update_consent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


