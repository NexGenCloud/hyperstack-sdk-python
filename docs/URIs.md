# URIs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_doc** | **str** |  | [optional] 
**api_uri** | **str** |  | [optional] 
**auth** | **str** |  | [optional] 
**console** | **str** |  | [optional] 
**contact_us** | **str** |  | [optional] 
**doc** | **str** |  | [optional] 
**landing_page** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.uris import URIs

# TODO update the JSON string below
json = "{}"
# create an instance of URIs from a JSON string
uris_instance = URIs.from_json(json)
# print the JSON string representation of the object
print(URIs.to_json())

# convert the object into a dict
uris_dict = uris_instance.to_dict()
# create an instance of URIs from a dict
uris_from_dict = URIs.from_dict(uris_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


