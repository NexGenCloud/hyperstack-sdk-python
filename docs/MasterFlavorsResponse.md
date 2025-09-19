# MasterFlavorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flavors** | [**List[ClusterFlavorFields]**](ClusterFlavorFields.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.master_flavors_response import MasterFlavorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MasterFlavorsResponse from a JSON string
master_flavors_response_instance = MasterFlavorsResponse.from_json(json)
# print the JSON string representation of the object
print(MasterFlavorsResponse.to_json())

# convert the object into a dict
master_flavors_response_dict = master_flavors_response_instance.to_dict()
# create an instance of MasterFlavorsResponse from a dict
master_flavors_response_from_dict = MasterFlavorsResponse.from_dict(master_flavors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


