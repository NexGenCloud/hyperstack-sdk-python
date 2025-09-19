# UpdateVolumePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_name** | **str** | The name of the target environment to move the volume to. The target environment must be in the same region as the current environment. | 

## Example

```python
from hyperstack.models.update_volume_payload import UpdateVolumePayload

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVolumePayload from a JSON string
update_volume_payload_instance = UpdateVolumePayload.from_json(json)
# print the JSON string representation of the object
print(UpdateVolumePayload.to_json())

# convert the object into a dict
update_volume_payload_dict = update_volume_payload_instance.to_dict()
# create an instance of UpdateVolumePayload from a dict
update_volume_payload_from_dict = UpdateVolumePayload.from_dict(update_volume_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


