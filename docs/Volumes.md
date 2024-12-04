# Volumes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**volume** | [**List[VolumeFields]**](VolumeFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.volumes import Volumes

# TODO update the JSON string below
json = "{}"
# create an instance of Volumes from a JSON string
volumes_instance = Volumes.from_json(json)
# print the JSON string representation of the object
print(Volumes.to_json())

# convert the object into a dict
volumes_dict = volumes_instance.to_dict()
# create an instance of Volumes from a dict
volumes_from_dict = Volumes.from_dict(volumes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

