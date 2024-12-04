# Snapshots


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**snapshots** | [**List[SnapshotFields]**](SnapshotFields.md) |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.snapshots import Snapshots

# TODO update the JSON string below
json = "{}"
# create an instance of Snapshots from a JSON string
snapshots_instance = Snapshots.from_json(json)
# print the JSON string representation of the object
print(Snapshots.to_json())

# convert the object into a dict
snapshots_dict = snapshots_instance.to_dict()
# create an instance of Snapshots from a dict
snapshots_from_dict = Snapshots.from_dict(snapshots_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


