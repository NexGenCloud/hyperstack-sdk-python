# WarningMailLogFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**threshold** | **int** |  | [optional] 
**topic** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.warning_mail_log_fields import WarningMailLogFields

# TODO update the JSON string below
json = "{}"
# create an instance of WarningMailLogFields from a JSON string
warning_mail_log_fields_instance = WarningMailLogFields.from_json(json)
# print the JSON string representation of the object
print(WarningMailLogFields.to_json())

# convert the object into a dict
warning_mail_log_fields_dict = warning_mail_log_fields_instance.to_dict()
# create an instance of WarningMailLogFields from a dict
warning_mail_log_fields_from_dict = WarningMailLogFields.from_dict(warning_mail_log_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


