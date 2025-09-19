# hyperstack.AssigningMemberRoleApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_rbac_role_to_user**](AssigningMemberRoleApi.md#assign_rbac_role_to_user) | **PUT** /auth/users/{user_id}/assign-roles | Assign RBAC Role
[**remove_rbac_role_from_user**](AssigningMemberRoleApi.md#remove_rbac_role_from_user) | **DELETE** /auth/users/{user_id}/roles | Remove RBAC Role From User


# **assign_rbac_role_to_user**
> RbacRoleDetailResponseModel assign_rbac_role_to_user(user_id, payload)

Assign RBAC Role

Assigns a specific RBAC role to a user within your organization, granting them access to the resource actions permitted by the role. Provide the user ID in the path and the role ID in the request body. For additional information, [click here](https://docs.hyperstack.cloud/docs/api-reference/auth-resources/rbac/manage-member-roles/assign-rbac-role).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.assign_rbac_role_payload import AssignRbacRolePayload
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

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.AssigningMemberRoleApi(api_client)
    user_id = 56 # int | 
    payload = hyperstack.AssignRbacRolePayload() # AssignRbacRolePayload | 

    try:
        # Assign RBAC Role
        api_response = api_instance.assign_rbac_role_to_user(user_id, payload)
        print("The response of AssigningMemberRoleApi->assign_rbac_role_to_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssigningMemberRoleApi->assign_rbac_role_to_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **payload** | [**AssignRbacRolePayload**](AssignRbacRolePayload.md)|  | 

### Return type

[**RbacRoleDetailResponseModel**](RbacRoleDetailResponseModel.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_rbac_role_from_user**
> CommonResponseModel remove_rbac_role_from_user(user_id)

Remove RBAC Role From User

Removes an RBAC role from a user within your organization, revoking the resource permissions they had access to. Provide the user ID in the path. For additional information, [click here](https://docs.hyperstack.cloud/docs/api-reference/auth-resources/rbac/manage-member-roles/revoke-rbac-role).

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
    api_instance = hyperstack.AssigningMemberRoleApi(api_client)
    user_id = 56 # int | 

    try:
        # Remove RBAC Role From User
        api_response = api_instance.remove_rbac_role_from_user(user_id)
        print("The response of AssigningMemberRoleApi->remove_rbac_role_from_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssigningMemberRoleApi->remove_rbac_role_from_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

