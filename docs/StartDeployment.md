# StartDeployment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment** | [**DeploymentFieldsforstartdeployments**](DeploymentFieldsforstartdeployments.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from hyperstack.models.start_deployment import StartDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of StartDeployment from a JSON string
start_deployment_instance = StartDeployment.from_json(json)
# print the JSON string representation of the object
print(StartDeployment.to_json())

# convert the object into a dict
start_deployment_dict = start_deployment_instance.to_dict()
# create an instance of StartDeployment from a dict
start_deployment_from_dict = StartDeployment.from_dict(start_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


