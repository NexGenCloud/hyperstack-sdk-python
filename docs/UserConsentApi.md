# hyperstack.UserConsentApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_a_new_consent_for_a_user**](UserConsentApi.md#add_a_new_consent_for_a_user) | **POST** /auth/user-consent | Add a new User consent
[**get_all_consent_templates**](UserConsentApi.md#get_all_consent_templates) | **GET** /auth/user-consent/templates | Get all consent templates
[**get_all_consents_for_a_user**](UserConsentApi.md#get_all_consents_for_a_user) | **GET** /auth/user-consent | Get Consents for a User
[**get_consent_template_by_type**](UserConsentApi.md#get_consent_template_by_type) | **GET** /auth/user-consent/templates/{consent_type} | Get consent template for a specific type
[**update_a_consent_action_by_type**](UserConsentApi.md#update_a_consent_action_by_type) | **PATCH** /auth/user-consent/{consent_type} | Grant or revoke an existing consent


# **add_a_new_consent_for_a_user**
> ConsentActionResponse add_a_new_consent_for_a_user(payload)

Add a new User consent

Add a new consent given by the User

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.consent_action_response import ConsentActionResponse
from hyperstack.models.record_consent_request import RecordConsentRequest
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
    api_instance = hyperstack.UserConsentApi(api_client)
    payload = hyperstack.RecordConsentRequest() # RecordConsentRequest | 

    try:
        # Add a new User consent
        api_response = api_instance.add_a_new_consent_for_a_user(payload)
        print("The response of UserConsentApi->add_a_new_consent_for_a_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserConsentApi->add_a_new_consent_for_a_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**RecordConsentRequest**](RecordConsentRequest.md)|  | 

### Return type

[**ConsentActionResponse**](ConsentActionResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_consent_templates**
> ConsentTemplatesResponse get_all_consent_templates()

Get all consent templates

Returns current consent templates for all consent types

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.consent_templates_response import ConsentTemplatesResponse
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
    api_instance = hyperstack.UserConsentApi(api_client)

    try:
        # Get all consent templates
        api_response = api_instance.get_all_consent_templates()
        print("The response of UserConsentApi->get_all_consent_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserConsentApi->get_all_consent_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ConsentTemplatesResponse**](ConsentTemplatesResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_consents_for_a_user**
> UserConsentsResponse get_all_consents_for_a_user(consent_type=consent_type)

Get Consents for a User

Fetch all the recorded consents given from a User

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.user_consents_response import UserConsentsResponse
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
    api_instance = hyperstack.UserConsentApi(api_client)
    consent_type = 'consent_type_example' # str | Filter by consent type (optional)

    try:
        # Get Consents for a User
        api_response = api_instance.get_all_consents_for_a_user(consent_type=consent_type)
        print("The response of UserConsentApi->get_all_consents_for_a_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserConsentApi->get_all_consents_for_a_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_type** | **str**| Filter by consent type | [optional] 

### Return type

[**UserConsentsResponse**](UserConsentsResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_template_by_type**
> ConsentTemplate get_consent_template_by_type(consent_type)

Get consent template for a specific type

Returns the current consent template for a specific consent type

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.consent_template import ConsentTemplate
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
    api_instance = hyperstack.UserConsentApi(api_client)
    consent_type = 'consent_type_example' # str | 

    try:
        # Get consent template for a specific type
        api_response = api_instance.get_consent_template_by_type(consent_type)
        print("The response of UserConsentApi->get_consent_template_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserConsentApi->get_consent_template_by_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_type** | **str**|  | 

### Return type

[**ConsentTemplate**](ConsentTemplate.md)

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

# **update_a_consent_action_by_type**
> ConsentActionResponse update_a_consent_action_by_type(consent_type, payload)

Grant or revoke an existing consent

Revoke or grant a consent to the User

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.consent_action_response import ConsentActionResponse
from hyperstack.models.update_consent_request import UpdateConsentRequest
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
    api_instance = hyperstack.UserConsentApi(api_client)
    consent_type = 'consent_type_example' # str | 
    payload = hyperstack.UpdateConsentRequest() # UpdateConsentRequest | 

    try:
        # Grant or revoke an existing consent
        api_response = api_instance.update_a_consent_action_by_type(consent_type, payload)
        print("The response of UserConsentApi->update_a_consent_action_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserConsentApi->update_a_consent_action_by_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_type** | **str**|  | 
 **payload** | [**UpdateConsentRequest**](UpdateConsentRequest.md)|  | 

### Return type

[**ConsentActionResponse**](ConsentActionResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

