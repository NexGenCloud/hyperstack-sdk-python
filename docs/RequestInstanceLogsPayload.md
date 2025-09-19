# RequestInstanceLogsPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** | The amount of lines to fetch | [optional] 

## Example

```python
from hyperstack.models.request_instance_logs_payload import RequestInstanceLogsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RequestInstanceLogsPayload from a JSON string
request_instance_logs_payload_instance = RequestInstanceLogsPayload.from_json(json)
# print the JSON string representation of the object
print(RequestInstanceLogsPayload.to_json())

# convert the object into a dict
request_instance_logs_payload_dict = request_instance_logs_payload_instance.to_dict()
# create an instance of RequestInstanceLogsPayload from a dict
request_instance_logs_payload_from_dict = RequestInstanceLogsPayload.from_dict(request_instance_logs_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


