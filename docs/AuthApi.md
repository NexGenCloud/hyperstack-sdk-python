# hyperstack.AuthApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_organization_for_token**](AuthApi.md#change_organization_for_token) | **GET** /auth/token/change-org/{org_id} | 
[**disable_mfa**](AuthApi.md#disable_mfa) | **GET** /auth/me/mfa/disable | 
[**get_authenticated_user**](AuthApi.md#get_authenticated_user) | **GET** /auth/me | Retrieve Authenticated User Details
[**get_user_mfa_status**](AuthApi.md#get_user_mfa_status) | **GET** /auth/me/mfa | Get MFA status for authenticated user
[**get_user_organizations**](AuthApi.md#get_user_organizations) | **GET** /auth/me/organizations | Get User Organizations


# **change_organization_for_token**
> AuthGetTokenResponseModel change_organization_for_token(org_id)



Change the organization associated with the current token. This is useful for users who have access to multiple organizations.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.auth_get_token_response_model import AuthGetTokenResponseModel
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
    api_instance = hyperstack.AuthApi(api_client)
    org_id = 56 # int | 

    try:
        api_response = api_instance.change_organization_for_token(org_id)
        print("The response of AuthApi->change_organization_for_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->change_organization_for_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 

### Return type

[**AuthGetTokenResponseModel**](AuthGetTokenResponseModel.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_mfa**
> CommonResponseModel disable_mfa()



Disable Multi-Factor Authentication (MFA) for the currently authenticated user. This endpoint is used to turn off MFA.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.common_response_model import CommonResponseModel
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
    api_instance = hyperstack.AuthApi(api_client)

    try:
        api_response = api_instance.disable_mfa()
        print("The response of AuthApi->disable_mfa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->disable_mfa: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CommonResponseModel**](CommonResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MFA Disabled |  -  |
**401** | Unauthorized |  -  |
**404** | User not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authenticated_user**
> AuthUserInfoResponseModel get_authenticated_user()

Retrieve Authenticated User Details

Retrieves detailed information about the currently authenticated user. For additional information, [**click here**](https://docs.hyperstack.cloud/docs/api-reference/auth-resources/auth).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.auth_user_info_response_model import AuthUserInfoResponseModel
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
    api_instance = hyperstack.AuthApi(api_client)

    try:
        # Retrieve Authenticated User Details
        api_response = api_instance.get_authenticated_user()
        print("The response of AuthApi->get_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_authenticated_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthUserInfoResponseModel**](AuthUserInfoResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Information |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_mfa_status**
> MFAStatusResponse get_user_mfa_status()

Get MFA status for authenticated user

Retrieve the Multi-Factor Authentication (MFA) status for the currentlyauthenticated user. Includes whether MFA is enabled.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.mfa_status_response import MFAStatusResponse
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
    api_instance = hyperstack.AuthApi(api_client)

    try:
        # Get MFA status for authenticated user
        api_response = api_instance.get_user_mfa_status()
        print("The response of AuthApi->get_user_mfa_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_user_mfa_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MFAStatusResponse**](MFAStatusResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MFA Status |  -  |
**401** | Unauthorized |  -  |
**404** | User not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_organizations**
> UserOrganizationsResponse get_user_organizations()

Get User Organizations

Retrieve the organizations associated with a user by their user ID. This endpoint is useful for understanding the user's organizational affiliations.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.user_organizations_response import UserOrganizationsResponse
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
    api_instance = hyperstack.AuthApi(api_client)

    try:
        # Get User Organizations
        api_response = api_instance.get_user_organizations()
        print("The response of AuthApi->get_user_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_user_organizations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserOrganizationsResponse**](UserOrganizationsResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

