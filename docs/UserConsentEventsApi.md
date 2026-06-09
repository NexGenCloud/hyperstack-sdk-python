# hyperstack.UserConsentEventsApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_consent_audit_events**](UserConsentEventsApi.md#get_consent_audit_events) | **GET** /auth/user-consent-events/{consent_type}/events | Get audit trail for a consent


# **get_consent_audit_events**
> ConsentEventsResponse get_consent_audit_events(consent_type)

Get audit trail for a consent

Get all consent audit events

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.consent_events_response import ConsentEventsResponse
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
    api_instance = hyperstack.UserConsentEventsApi(api_client)
    consent_type = 'consent_type_example' # str | 

    try:
        # Get audit trail for a consent
        api_response = api_instance.get_consent_audit_events(consent_type)
        print("The response of UserConsentEventsApi->get_consent_audit_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserConsentEventsApi->get_consent_audit_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_type** | **str**|  | 

### Return type

[**ConsentEventsResponse**](ConsentEventsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

