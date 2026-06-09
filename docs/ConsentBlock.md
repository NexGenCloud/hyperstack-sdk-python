# ConsentBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Block text, may contain ${variable} placeholders | [optional] 
**type** | **str** | Block display type | [optional] 

## Example

```python
from hyperstack.models.consent_block import ConsentBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentBlock from a JSON string
consent_block_instance = ConsentBlock.from_json(json)
# print the JSON string representation of the object
print(ConsentBlock.to_json())

# convert the object into a dict
consent_block_dict = consent_block_instance.to_dict()
# create an instance of ConsentBlock from a dict
consent_block_from_dict = ConsentBlock.from_dict(consent_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


