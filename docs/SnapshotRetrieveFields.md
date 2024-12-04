# SnapshotRetrieveFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the snapshot | 
**has_floating_ip** | **bool** | Indicates if the VM had a floating IP assigned | [optional] 
**id** | **int** | Snapshot ID | 
**is_image** | **bool** | Indicates if the snapshot is an image | 
**name** | **str** | Snapshot name | 
**region_id** | **int** | Region where the snapshot will be available | 
**size** | **int** | Size in GB of the snapshot | 
**status** | **str** | Status of the snapshot | 
**vm_id** | **int** | ID of the VM from which the snapshot is created | 

## Example

```python
from hyperstack.models.snapshot_retrieve_fields import SnapshotRetrieveFields

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotRetrieveFields from a JSON string
snapshot_retrieve_fields_instance = SnapshotRetrieveFields.from_json(json)
# print the JSON string representation of the object
print(SnapshotRetrieveFields.to_json())

# convert the object into a dict
snapshot_retrieve_fields_dict = snapshot_retrieve_fields_instance.to_dict()
# create an instance of SnapshotRetrieveFields from a dict
snapshot_retrieve_fields_from_dict = SnapshotRetrieveFields.from_dict(snapshot_retrieve_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


