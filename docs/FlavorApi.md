# hyperstack.FlavorApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_flavors**](FlavorApi.md#list_flavors) | **GET** /core/flavors | List Flavors


# **list_flavors**
> FlavorListResponse list_flavors(region=region)

List Flavors

Returns a list of available virtual machine hardware configurations, known as**flavors**. You can specify a `region_name` in the query string of the request toretrieve flavors available only in the specified region; by default, it returnsflavors available in all regions. For more details on flavors,[**click here**](https://docs.hyperstack.cloud/docs/hardware/flavors).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.flavor_list_response import FlavorListResponse
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
    api_instance = hyperstack.FlavorApi(api_client)
    region = 'region_example' # str | Region Name (optional)

    try:
        # List Flavors
        api_response = api_instance.list_flavors(region=region)
        print("The response of FlavorApi->list_flavors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlavorApi->list_flavors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| Region Name | [optional] 

### Return type

[**FlavorListResponse**](FlavorListResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of flavors list. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

