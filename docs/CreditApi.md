# hyperstack.CreditApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_credit**](CreditApi.md#get_user_credit) | **GET** /billing/user-credit/credit | GET: View credit and threshold


# **get_user_credit**
> GetCreditAndThresholdInfoInResponse get_user_credit()

GET: View credit and threshold

Retrieves the current credit balance for your [**organization**](/docs/rbac/organization). Ensuring a positive credit balance allows you to create resources. However, for prepaid accounts, if the credit balance falls below $0, all associated resources will be temporarily suspended until a [**payment**](/docs/api-reference/billing-resources/create-payment) is made. For additional information, [**click here**](None/docs/api-reference/billing-resources/retrieve-credit-balance/).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.get_credit_and_threshold_info_in_response import GetCreditAndThresholdInfoInResponse
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
    api_instance = hyperstack.CreditApi(api_client)

    try:
        # GET: View credit and threshold
        api_response = api_instance.get_user_credit()
        print("The response of CreditApi->get_user_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditApi->get_user_credit: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetCreditAndThresholdInfoInResponse**](GetCreditAndThresholdInfoInResponse.md)

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

