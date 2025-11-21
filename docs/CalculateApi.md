# hyperstack.CalculateApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_resource_billing_rate**](CalculateApi.md#calculate_resource_billing_rate) | **GET** /pricebook/calculate/resource/{resource_type}/{id} | Retrieve Billing Rate for Resource


# **calculate_resource_billing_rate**
> ResourceBillingResponseForCustomer calculate_resource_billing_rate(resource_type, id)

Retrieve Billing Rate for Resource

Calculate the hourly billing rate of a specified resource by including the resource ID in the path.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_billing_response_for_customer import ResourceBillingResponseForCustomer
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
    api_instance = hyperstack.CalculateApi(api_client)
    resource_type = 'resource_type_example' # str | 
    id = 56 # int | 

    try:
        # Retrieve Billing Rate for Resource
        api_response = api_instance.calculate_resource_billing_rate(resource_type, id)
        print("The response of CalculateApi->calculate_resource_billing_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculateApi->calculate_resource_billing_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**|  | 
 **id** | **int**|  | 

### Return type

[**ResourceBillingResponseForCustomer**](ResourceBillingResponseForCustomer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved billing rate. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

