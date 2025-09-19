# hyperstack.PricebookApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pricebook**](PricebookApi.md#get_pricebook) | **GET** /pricebook | 


# **get_pricebook**
> List[PricebookModel] get_pricebook()



Retrieves the Infrahub Pricebook, detailing hourly running costs for all resources offered by Infrahub. For more information on Pricebook [**click here**](None/docs/api-reference/pricebook-resources/pricebook/).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.pricebook_model import PricebookModel
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
    api_instance = hyperstack.PricebookApi(api_client)

    try:
        api_response = api_instance.get_pricebook()
        print("The response of PricebookApi->get_pricebook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricebookApi->get_pricebook: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PricebookModel]**](PricebookModel.md)

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
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

