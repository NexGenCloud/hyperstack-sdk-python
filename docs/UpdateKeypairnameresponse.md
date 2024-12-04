# UpdateKeypairnameresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keypair** | [**KeypairFields**](KeypairFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.update_keypairnameresponse import UpdateKeypairnameresponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKeypairnameresponse from a JSON string
update_keypairnameresponse_instance = UpdateKeypairnameresponse.from_json(json)
# print the JSON string representation of the object
print(UpdateKeypairnameresponse.to_json())

# convert the object into a dict
update_keypairnameresponse_dict = update_keypairnameresponse_instance.to_dict()
# create an instance of UpdateKeypairnameresponse from a dict
update_keypairnameresponse_from_dict = UpdateKeypairnameresponse.from_dict(update_keypairnameresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


