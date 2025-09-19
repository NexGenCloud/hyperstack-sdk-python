# CreateProfilePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, str]** | The data object containing the configuration details of the virtual machine profile being created. | 
**description** | **str** | The optional description for the profile being created. | [optional] 
**name** | **str** | The name of the profile being created. | 

## Example

```python
from hyperstack.models.create_profile_payload import CreateProfilePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProfilePayload from a JSON string
create_profile_payload_instance = CreateProfilePayload.from_json(json)
# print the JSON string representation of the object
print(CreateProfilePayload.to_json())

# convert the object into a dict
create_profile_payload_dict = create_profile_payload_instance.to_dict()
# create an instance of CreateProfilePayload from a dict
create_profile_payload_from_dict = CreateProfilePayload.from_dict(create_profile_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


