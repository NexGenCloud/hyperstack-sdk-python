# CreateImagePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** | List of labels to attach to the image | [optional] 
**name** | **str** | Name for the new custom image | 

## Example

```python
from hyperstack.models.create_image_payload import CreateImagePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImagePayload from a JSON string
create_image_payload_instance = CreateImagePayload.from_json(json)
# print the JSON string representation of the object
print(CreateImagePayload.to_json())

# convert the object into a dict
create_image_payload_dict = create_image_payload_instance.to_dict()
# create an instance of CreateImagePayload from a dict
create_image_payload_from_dict = CreateImagePayload.from_dict(create_image_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


