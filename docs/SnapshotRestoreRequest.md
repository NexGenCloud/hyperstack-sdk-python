# SnapshotRestoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **int** | Contract ID to assign to the newly restored VM | [optional] 
**new_vm_name** | **str** | The name of the newly restored VM | 

## Example

```python
from hyperstack.models.snapshot_restore_request import SnapshotRestoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotRestoreRequest from a JSON string
snapshot_restore_request_instance = SnapshotRestoreRequest.from_json(json)
# print the JSON string representation of the object
print(SnapshotRestoreRequest.to_json())

# convert the object into a dict
snapshot_restore_request_dict = snapshot_restore_request_instance.to_dict()
# create an instance of SnapshotRestoreRequest from a dict
snapshot_restore_request_from_dict = SnapshotRestoreRequest.from_dict(snapshot_restore_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


