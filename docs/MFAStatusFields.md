# MFAStatusFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mfa_enabled** | **bool** | Whether MFA is enabled for the user | 

## Example

```python
from hyperstack.models.mfa_status_fields import MFAStatusFields

# TODO update the JSON string below
json = "{}"
# create an instance of MFAStatusFields from a JSON string
mfa_status_fields_instance = MFAStatusFields.from_json(json)
# print the JSON string representation of the object
print(MFAStatusFields.to_json())

# convert the object into a dict
mfa_status_fields_dict = mfa_status_fields_instance.to_dict()
# create an instance of MFAStatusFields from a dict
mfa_status_fields_from_dict = MFAStatusFields.from_dict(mfa_status_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


