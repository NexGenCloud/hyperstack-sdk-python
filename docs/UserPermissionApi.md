# hyperstack.UserPermissionApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_my_user_permissions**](UserPermissionApi.md#list_my_user_permissions) | **GET** /auth/users/me/permissions | List My User Permissions
[**list_user_permissions**](UserPermissionApi.md#list_user_permissions) | **GET** /auth/users/{id}/permissions | List User Permissions


# **list_my_user_permissions**
> GetUserPermissionsResponseModel list_my_user_permissions()

List My User Permissions

Retrieves a list of permissions granted to your account. For additional information on your permissions, [click here](https://docs.hyperstack.cloud/docs/api-reference/auth-resources/permission/list-my-permissions).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.get_user_permissions_response_model import GetUserPermissionsResponseModel
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
    api_instance = hyperstack.UserPermissionApi(api_client)

    try:
        # List My User Permissions
        api_response = api_instance.list_my_user_permissions()
        print("The response of UserPermissionApi->list_my_user_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPermissionApi->list_my_user_permissions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetUserPermissionsResponseModel**](GetUserPermissionsResponseModel.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_permissions**
> GetUserPermissionsResponseModel list_user_permissions(id)

List User Permissions

Retrieves a list of permissions granted to a specific user within your organization. Provide the ID of the user in the path. For additional information on user permissions, [click here](https://docs.hyperstack.cloud/docs/api-reference/auth-resources/permission/list-user-permissions).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.get_user_permissions_response_model import GetUserPermissionsResponseModel
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
    api_instance = hyperstack.UserPermissionApi(api_client)
    id = 56 # int | 

    try:
        # List User Permissions
        api_response = api_instance.list_user_permissions(id)
        print("The response of UserPermissionApi->list_user_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPermissionApi->list_user_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetUserPermissionsResponseModel**](GetUserPermissionsResponseModel.md)

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

