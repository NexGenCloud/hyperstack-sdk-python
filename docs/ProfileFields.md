# ProfileFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**data** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.profile_fields import ProfileFields

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileFields from a JSON string
profile_fields_instance = ProfileFields.from_json(json)
# print the JSON string representation of the object
print(ProfileFields.to_json())

# convert the object into a dict
profile_fields_dict = profile_fields_instance.to_dict()
# create an instance of ProfileFields from a dict
profile_fields_from_dict = ProfileFields.from_dict(profile_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


