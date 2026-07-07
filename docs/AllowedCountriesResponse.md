# AllowedCountriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **List[str]** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.allowed_countries_response import AllowedCountriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedCountriesResponse from a JSON string
allowed_countries_response_instance = AllowedCountriesResponse.from_json(json)
# print the JSON string representation of the object
print(AllowedCountriesResponse.to_json())

# convert the object into a dict
allowed_countries_response_dict = allowed_countries_response_instance.to_dict()
# create an instance of AllowedCountriesResponse from a dict
allowed_countries_response_from_dict = AllowedCountriesResponse.from_dict(allowed_countries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


