# VNCURL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**vnc_url** | [**VNCURLFields**](VNCURLFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.vncurl import VNCURL

# TODO update the JSON string below
json = "{}"
# create an instance of VNCURL from a JSON string
vncurl_instance = VNCURL.from_json(json)
# print the JSON string representation of the object
print(VNCURL.to_json())

# convert the object into a dict
vncurl_dict = vncurl_instance.to_dict()
# create an instance of VNCURL from a dict
vncurl_from_dict = VNCURL.from_dict(vncurl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


