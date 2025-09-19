# CreateVolumePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | A URL that can be attached to the volume you are creating. This &#x60;callback_url&#x60; will post any action events that occur to your volume to the provided URL. | [optional] 
**description** | **str** | A brief description or comment about the volume. | [optional] 
**environment_name** | **str** | The name of the [environment](https://docs.hyperstack.cloud/docs/api-reference/core-resources/environments/) within which the volume is being created. | 
**image_id** | **int** | The ID of the operating system image that will be associated with the volume. By providing an &#x60;image_id&#x60; in the create volume request, you will create a bootable volume. | [optional] 
**name** | **str** | The name of the volume being created. | 
**size** | **int** | The size of the volume in GB. 1048576GB storage capacity per volume. | 
**volume_type** | **str** | Specifies the type of volume being created, which determines the storage technology it will use. Call the [List volume types](https://infrahub-api-doc.nexgencloud.com/#get-/core/volumes) endpoint to retrieve a list of available volume model types. | 

## Example

```python
from hyperstack.models.create_volume_payload import CreateVolumePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVolumePayload from a JSON string
create_volume_payload_instance = CreateVolumePayload.from_json(json)
# print the JSON string representation of the object
print(CreateVolumePayload.to_json())

# convert the object into a dict
create_volume_payload_dict = create_volume_payload_instance.to_dict()
# create an instance of CreateVolumePayload from a dict
create_volume_payload_from_dict = CreateVolumePayload.from_dict(create_volume_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


