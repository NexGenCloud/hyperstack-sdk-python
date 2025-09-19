# SnapshotFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Creation timestamp | 
**description** | **str** | Description of the snapshot | 
**has_floating_ip** | **bool** | Indicates if the VM had a floating IP assigned | [optional] 
**id** | **int** | Snapshot ID | 
**is_image** | **bool** | Indicates if the snapshot is an image | 
**labels** | **List[str]** | Labels associated with snapshot | [optional] 
**name** | **str** | Snapshot name | 
**region_id** | **int** | Region where the snapshot will be available | 
**size** | **int** | Size in GB of the snapshot | 
**status** | **str** | Status of the snapshot | 
**updated_at** | **datetime** | Last update timestamp | 
**vm_id** | **int** | ID of the VM from which the snapshot is created | 

## Example

```python
from hyperstack.models.snapshot_fields import SnapshotFields

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotFields from a JSON string
snapshot_fields_instance = SnapshotFields.from_json(json)
# print the JSON string representation of the object
print(SnapshotFields.to_json())

# convert the object into a dict
snapshot_fields_dict = snapshot_fields_instance.to_dict()
# create an instance of SnapshotFields from a dict
snapshot_fields_from_dict = SnapshotFields.from_dict(snapshot_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


