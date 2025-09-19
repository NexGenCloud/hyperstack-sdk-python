# hyperstack.VncUrlApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vnc_url**](VncUrlApi.md#get_vnc_url) | **GET** /core/virtual-machines/{vm_id}/console/{job_id} | Get VNC Console Link
[**get_vnc_url2**](VncUrlApi.md#get_vnc_url2) | **GET** /core/virtual-machines/{vm_id}/request-console | Request Instance Console


# **get_vnc_url**
> VNCURL get_vnc_url(vm_id, job_id)

Get VNC Console Link

Retrieves the URL to access the VNC console for a specified virtual machine by providing the virtual machine ID and the job ID in the path. For more information, [**click here**](https://docs.hyperstack.cloud/docs/api-reference/core-resources/virtual-machines/vnc-console/retrieve-vnc-url).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.vncurl import VNCURL
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
    api_instance = hyperstack.VncUrlApi(api_client)
    vm_id = 56 # int | 
    job_id = 56 # int | 

    try:
        # Get VNC Console Link
        api_response = api_instance.get_vnc_url(vm_id, job_id)
        print("The response of VncUrlApi->get_vnc_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VncUrlApi->get_vnc_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **job_id** | **int**|  | 

### Return type

[**VNCURL**](VNCURL.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get VNC Console Link Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vnc_url2**
> RequestConsole get_vnc_url2(vm_id)

Request Instance Console

Retrieves the path of the VNC console for the given virtual machine ID by providing the virtual machine ID in the path. For more information, [**click here**](https://docs.hyperstack.cloud/docs/api-reference/core-resources/virtual-machines/vnc-console/retrieve-console-path).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.request_console import RequestConsole
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
    api_instance = hyperstack.VncUrlApi(api_client)
    vm_id = 56 # int | 

    try:
        # Request Instance Console
        api_response = api_instance.get_vnc_url2(vm_id)
        print("The response of VncUrlApi->get_vnc_url2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VncUrlApi->get_vnc_url2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 

### Return type

[**RequestConsole**](RequestConsole.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Please wait a few seconds and visit the below link to access your VNC console URL |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

