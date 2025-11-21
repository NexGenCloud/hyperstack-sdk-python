# hyperstack.FIPExclusionsApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_if_org_is_excluded_from_floating_ip_detachment**](FIPExclusionsApi.md#check_if_org_is_excluded_from_floating_ip_detachment) | **GET** /core/fip-detachment-exclusions/org/{org_id} | 


# **check_if_org_is_excluded_from_floating_ip_detachment**
> ResponseModel check_if_org_is_excluded_from_floating_ip_detachment(org_id)



is org excluded from floating ip detachment

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.response_model import ResponseModel
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
    api_instance = hyperstack.FIPExclusionsApi(api_client)
    org_id = 56 # int | 

    try:
        api_response = api_instance.check_if_org_is_excluded_from_floating_ip_detachment(org_id)
        print("The response of FIPExclusionsApi->check_if_org_is_excluded_from_floating_ip_detachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FIPExclusionsApi->check_if_org_is_excluded_from_floating_ip_detachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

