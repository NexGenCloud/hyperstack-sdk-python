# DeploymentFieldsForStartDeployments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**variables** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.deployment_fields_for_start_deployments import DeploymentFieldsForStartDeployments

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentFieldsForStartDeployments from a JSON string
deployment_fields_for_start_deployments_instance = DeploymentFieldsForStartDeployments.from_json(json)
# print the JSON string representation of the object
print(DeploymentFieldsForStartDeployments.to_json())

# convert the object into a dict
deployment_fields_for_start_deployments_dict = deployment_fields_for_start_deployments_instance.to_dict()
# create an instance of DeploymentFieldsForStartDeployments from a dict
deployment_fields_for_start_deployments_from_dict = DeploymentFieldsForStartDeployments.from_dict(deployment_fields_for_start_deployments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


