# CreateSnapshotPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description | 
**is_image** | **bool** | Indicates if the snapshot is an image | 
**labels** | **List[str]** | Labels associated with snapshot | [optional] 
**name** | **str** | Snapshot name | 

## Example

```python
from hyperstack.models.create_snapshot_payload import CreateSnapshotPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnapshotPayload from a JSON string
create_snapshot_payload_instance = CreateSnapshotPayload.from_json(json)
# print the JSON string representation of the object
print(CreateSnapshotPayload.to_json())

# convert the object into a dict
create_snapshot_payload_dict = create_snapshot_payload_instance.to_dict()
# create an instance of CreateSnapshotPayload from a dict
create_snapshot_payload_from_dict = CreateSnapshotPayload.from_dict(create_snapshot_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


