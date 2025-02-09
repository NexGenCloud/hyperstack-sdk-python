# CreateEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the environment being created. | 
**region** | **str** | The geographic location of the data center where the environment is being created. To learn more about regions, [**click here**](https://infrahub-doc.nexgencloud.com/docs/features/regions). | 

## Example

```python
from hyperstack.models.create_environment import CreateEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEnvironment from a JSON string
create_environment_instance = CreateEnvironment.from_json(json)
# print the JSON string representation of the object
print(CreateEnvironment.to_json())

# convert the object into a dict
create_environment_dict = create_environment_instance.to_dict()
# create an instance of CreateEnvironment from a dict
create_environment_from_dict = CreateEnvironment.from_dict(create_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


