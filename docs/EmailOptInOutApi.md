# hyperstack.EmailOptInOutApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_email_preferences_for_a_user**](EmailOptInOutApi.md#get_email_preferences_for_a_user) | **GET** /auth/email/opt-out | Get all email preferences for the authenticated user
[**toggle_all_optional_email_preferences_for_the_user**](EmailOptInOutApi.md#toggle_all_optional_email_preferences_for_the_user) | **PUT** /auth/email/opt-out | Toggle all optional email preferences for the authenticated user
[**update_email_preference_for_a_category_by_slug**](EmailOptInOutApi.md#update_email_preference_for_a_category_by_slug) | **PUT** /auth/email/opt-out/{slug} | Update email preference opted_in status for a category slug


# **get_email_preferences_for_a_user**
> EmailPreferencesResponse get_email_preferences_for_a_user()

Get all email preferences for the authenticated user

Returns all email categories with the user's opt-in status. Categories without an explicit preference default to opted_in=true.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.email_preferences_response import EmailPreferencesResponse
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
    api_instance = hyperstack.EmailOptInOutApi(api_client)

    try:
        # Get all email preferences for the authenticated user
        api_response = api_instance.get_email_preferences_for_a_user()
        print("The response of EmailOptInOutApi->get_email_preferences_for_a_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailOptInOutApi->get_email_preferences_for_a_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EmailPreferencesResponse**](EmailPreferencesResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_all_optional_email_preferences_for_the_user**
> UpdateEmailPreferenceResponse toggle_all_optional_email_preferences_for_the_user(payload)

Toggle all optional email preferences for the authenticated user

Sets opted_in to the given value for every non-required, non-deleted email category. Required categories are not affected.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.update_email_preference_input import UpdateEmailPreferenceInput
from hyperstack.models.update_email_preference_response import UpdateEmailPreferenceResponse
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
    api_instance = hyperstack.EmailOptInOutApi(api_client)
    payload = hyperstack.UpdateEmailPreferenceInput() # UpdateEmailPreferenceInput | 

    try:
        # Toggle all optional email preferences for the authenticated user
        api_response = api_instance.toggle_all_optional_email_preferences_for_the_user(payload)
        print("The response of EmailOptInOutApi->toggle_all_optional_email_preferences_for_the_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailOptInOutApi->toggle_all_optional_email_preferences_for_the_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UpdateEmailPreferenceInput**](UpdateEmailPreferenceInput.md)|  | 

### Return type

[**UpdateEmailPreferenceResponse**](UpdateEmailPreferenceResponse.md)

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
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_preference_for_a_category_by_slug**
> UpdateEmailPreferenceResponse update_email_preference_for_a_category_by_slug(slug, payload)

Update email preference opted_in status for a category slug

Updates the opted_in status for the given email category slug. If the slug belongs to a parent category (email_category_id is null), all non-deleted child categories are updated. If the slug belongs to a child category, only that category is updated.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.update_email_preference_input import UpdateEmailPreferenceInput
from hyperstack.models.update_email_preference_response import UpdateEmailPreferenceResponse
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
    api_instance = hyperstack.EmailOptInOutApi(api_client)
    slug = 'slug_example' # str | 
    payload = hyperstack.UpdateEmailPreferenceInput() # UpdateEmailPreferenceInput | 

    try:
        # Update email preference opted_in status for a category slug
        api_response = api_instance.update_email_preference_for_a_category_by_slug(slug, payload)
        print("The response of EmailOptInOutApi->update_email_preference_for_a_category_by_slug:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailOptInOutApi->update_email_preference_for_a_category_by_slug: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **payload** | [**UpdateEmailPreferenceInput**](UpdateEmailPreferenceInput.md)|  | 

### Return type

[**UpdateEmailPreferenceResponse**](UpdateEmailPreferenceResponse.md)

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
**401** | Unauthorized |  -  |
**404** | Email category not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

