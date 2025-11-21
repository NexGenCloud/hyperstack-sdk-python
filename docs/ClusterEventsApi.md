# hyperstack.ClusterEventsApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_cluster_events**](ClusterEventsApi.md#list_cluster_events) | **GET** /core/clusters/{cluster_id}/events | Fetch all of a cluster events


# **list_cluster_events**
> ClusterEvents list_cluster_events(cluster_id)

Fetch all of a cluster events

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.cluster_events import ClusterEvents
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
    api_instance = hyperstack.ClusterEventsApi(api_client)
    cluster_id = 'cluster_id_example' # str | 

    try:
        # Fetch all of a cluster events
        api_response = api_instance.list_cluster_events(cluster_id)
        print("The response of ClusterEventsApi->list_cluster_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterEventsApi->list_cluster_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ClusterEvents**](ClusterEvents.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

