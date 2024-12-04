# SnapshotRetrieve


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**snapshot** | [**SnapshotRetrieveFields**](SnapshotRetrieveFields.md) |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.snapshot_retrieve import SnapshotRetrieve

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotRetrieve from a JSON string
snapshot_retrieve_instance = SnapshotRetrieve.from_json(json)
# print the JSON string representation of the object
print(SnapshotRetrieve.to_json())

# convert the object into a dict
snapshot_retrieve_dict = snapshot_retrieve_instance.to_dict()
# create an instance of SnapshotRetrieve from a dict
snapshot_retrieve_from_dict = SnapshotRetrieve.from_dict(snapshot_retrieve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


