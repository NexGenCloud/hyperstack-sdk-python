# hyperstack.RbacRoleApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rbac_role**](RbacRoleApi.md#create_rbac_role) | **POST** /auth/roles | Create RBAC Role
[**delete_rbac_role**](RbacRoleApi.md#delete_rbac_role) | **DELETE** /auth/roles/{id} | Delete RBAC Role
[**list_rbac_roles**](RbacRoleApi.md#list_rbac_roles) | **GET** /auth/roles | List RBAC Roles
[**retrieve_rbac_role_details**](RbacRoleApi.md#retrieve_rbac_role_details) | **GET** /auth/roles/{id} | Retrieve RBAC Role Details
[**update_rbac_role**](RbacRoleApi.md#update_rbac_role) | **PUT** /auth/roles/{id} | Update RBAC Role


# **create_rbac_role**
> RbacRoleDetailResponseModel create_rbac_role(payload)

Create RBAC Role

Creates an RBAC role that can be assigned to users, granting them access to specific resource actions. Provide the configuration of the RBAC role, including its name, description, and list of permissions and policy IDs in the request body. For additional information on creating RBAC roles, [click here](https://infrahub-doc.nexgencloud.com/docs/api-reference/auth-resources/rbac/create-rbac-role).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.create_update_rbac_role_payload import CreateUpdateRbacRolePayload
from hyperstack.models.rbac_role_detail_response_model import RbacRoleDetailResponseModel
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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.RbacRoleApi(api_client)
    payload = hyperstack.CreateUpdateRbacRolePayload() # CreateUpdateRbacRolePayload | 

    try:
        # Create RBAC Role
        api_response = api_instance.create_rbac_role(payload)
        print("The response of RbacRoleApi->create_rbac_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacRoleApi->create_rbac_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateUpdateRbacRolePayload**](CreateUpdateRbacRolePayload.md)|  | 

### Return type

[**RbacRoleDetailResponseModel**](RbacRoleDetailResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rbac_role**
> CommonResponseModel delete_rbac_role(id)

Delete RBAC Role

Deletes an RBAC role by providing its ID in the path. For additional information, [click here](https://infrahub-doc.nexgencloud.com/docs/api-reference/auth-resources/rbac/delete-rbac-role).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.RbacRoleApi(api_client)
    id = 56 # int | 

    try:
        # Delete RBAC Role
        api_response = api_instance.delete_rbac_role(id)
        print("The response of RbacRoleApi->delete_rbac_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacRoleApi->delete_rbac_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CommonResponseModel**](CommonResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **list_rbac_roles**
> GetRbacRolesResponseModel list_rbac_roles()

List RBAC Roles

Retrieves a list of RBAC roles that can be assigned to the users within an organization. For additional information on RBAC roles, [click here](https://infrahub-doc.nexgencloud.com/docs/api-reference/auth-resources/rbac/list-rbac-roles).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.get_rbac_roles_response_model import GetRbacRolesResponseModel
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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.RbacRoleApi(api_client)

    try:
        # List RBAC Roles
        api_response = api_instance.list_rbac_roles()
        print("The response of RbacRoleApi->list_rbac_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacRoleApi->list_rbac_roles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetRbacRolesResponseModel**](GetRbacRolesResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **retrieve_rbac_role_details**
> RbacRoleDetailResponseModelFixed retrieve_rbac_role_details(id)

Retrieve RBAC Role Details

Retrieves the details of a specified RBAC role by providing the RBAC role ID in the path. For additional information, [click here](https://infrahub-doc.nexgencloud.com/docs/api-reference/auth-resources/rbac/retrieve-rbac-details).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.rbac_role_detail_response_model_fixed import RbacRoleDetailResponseModelFixed
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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.RbacRoleApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve RBAC Role Details
        api_response = api_instance.retrieve_rbac_role_details(id)
        print("The response of RbacRoleApi->retrieve_rbac_role_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacRoleApi->retrieve_rbac_role_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RbacRoleDetailResponseModelFixed**](RbacRoleDetailResponseModelFixed.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **update_rbac_role**
> RbacRoleDetailResponseModel update_rbac_role(id, payload)

Update RBAC Role

Updates an RBAC role by providing the role ID in the path and the modified role configuration in the request body, including its name, description, and list of permissions and policy IDs. For additional information, [click here](https://infrahub-doc.nexgencloud.com/docs/api-reference/auth-resources/rbac/update-rbac-role).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.create_update_rbac_role_payload import CreateUpdateRbacRolePayload
from hyperstack.models.rbac_role_detail_response_model import RbacRoleDetailResponseModel
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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.RbacRoleApi(api_client)
    id = 56 # int | 
    payload = hyperstack.CreateUpdateRbacRolePayload() # CreateUpdateRbacRolePayload | 

    try:
        # Update RBAC Role
        api_response = api_instance.update_rbac_role(id, payload)
        print("The response of RbacRoleApi->update_rbac_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacRoleApi->update_rbac_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **payload** | [**CreateUpdateRbacRolePayload**](CreateUpdateRbacRolePayload.md)|  | 

### Return type

[**RbacRoleDetailResponseModel**](RbacRoleDetailResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
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

