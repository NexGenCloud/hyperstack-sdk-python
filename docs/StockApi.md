# hyperstack.StockApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_gpu_stock**](StockApi.md#get_gpu_stock) | **GET** /core/stocks | Retrieve GPU stocks


# **get_gpu_stock**
> NewStockRetriveResponse get_gpu_stock()

Retrieve GPU stocks

Returns information on current and upcoming GPU availability, organized byregion and GPU model. For additional information on GPU stocks,[**click here**](https://docs.hyperstack.cloud/docs/hardware/gpu-stock-information).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.new_stock_retrive_response import NewStockRetriveResponse
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
    api_instance = hyperstack.StockApi(api_client)

    try:
        # Retrieve GPU stocks
        api_response = api_instance.get_gpu_stock()
        print("The response of StockApi->get_gpu_stock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockApi->get_gpu_stock: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NewStockRetriveResponse**](NewStockRetriveResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GPU stocks retrieved successfully. |  -  |
**401** | Unauthorized |  -  |
**404** | Stocks Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

