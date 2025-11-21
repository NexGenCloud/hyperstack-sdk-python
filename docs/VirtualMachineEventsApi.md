# hyperstack.VirtualMachineEventsApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_vm_events**](VirtualMachineEventsApi.md#list_vm_events) | **GET** /core/virtual-machines/{vm_id}/events | List virtual machine events


# **list_vm_events**
> InstanceEvents list_vm_events(vm_id)

List virtual machine events

Retrieves a list of all events in a virtual machine's history, which records actions performed on the specified virtual machine. Include the virtual machine ID in the path to retrieve the history of events. For more details on virtual machine events history, [**click here**](https://docs.hyperstack.cloud/docs/virtual-machines/vm-performance-metrics-and-events-history#events-history).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.instance_events import InstanceEvents
from hyperstack.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://infrahub-api.nexgencloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperstack.Configuration(
    host = "https://infrahub-api.nexgencloud.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineEventsApi(api_client)
    vm_id = 56 # int | 

    try:
        # List virtual machine events
        api_response = api_instance.list_vm_events(vm_id)
        print("The response of VirtualMachineEventsApi->list_vm_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineEventsApi->list_vm_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 

### Return type

[**InstanceEvents**](InstanceEvents.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Virtual machines event list successfully retrieved. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

