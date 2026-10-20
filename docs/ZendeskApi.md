# hyperstack.ZendeskApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_zendesk_messaging_token**](ZendeskApi.md#get_zendesk_messaging_token) | **GET** /auth/zendesk/messaging-token | Retrieve a Zendesk messaging JWT for the current user


# **get_zendesk_messaging_token**
> ZendeskMessagingToken get_zendesk_messaging_token()

Retrieve a Zendesk messaging JWT for the current user

Returns a short-lived signed JWT for the currently authenticated user, to be passed to the Zendesk Web Widget's loginUser API so chat tickets are attributed to the real user instead of an anonymous 'Web User'.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.zendesk_messaging_token import ZendeskMessagingToken
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
    api_instance = hyperstack.ZendeskApi(api_client)

    try:
        # Retrieve a Zendesk messaging JWT for the current user
        api_response = api_instance.get_zendesk_messaging_token()
        print("The response of ZendeskApi->get_zendesk_messaging_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZendeskApi->get_zendesk_messaging_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ZendeskMessagingToken**](ZendeskMessagingToken.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signed messaging JWT |  -  |
**401** | Unauthorized |  -  |
**404** | Messaging authentication disabled |  -  |
**503** | Messaging authentication not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

