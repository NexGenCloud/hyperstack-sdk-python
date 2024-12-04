# hyperstack.OrganizationApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_organization_member**](OrganizationApi.md#remove_organization_member) | **POST** /auth/organizations/remove-member | Remove Organization Member
[**retrieve_organization_information**](OrganizationApi.md#retrieve_organization_information) | **GET** /auth/organizations | Retrieve Organization Information
[**update_organization_information**](OrganizationApi.md#update_organization_information) | **PUT** /auth/organizations/update | Update Organization Information


# **remove_organization_member**
> RemoveMemberFromOrganizationResponseModel remove_organization_member(payload)

Remove Organization Member

Removes a member from your organization. For additional information, [click here](https://infrahub-doc.nexgencloud.com/docs/api-reference/auth-resources/organization/remove-member).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.remove_member_from_organization_response_model import RemoveMemberFromOrganizationResponseModel
from hyperstack.models.remove_member_payload import RemoveMemberPayload
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
    api_instance = hyperstack.OrganizationApi(api_client)
    payload = hyperstack.RemoveMemberPayload() # RemoveMemberPayload | 

    try:
        # Remove Organization Member
        api_response = api_instance.remove_organization_member(payload)
        print("The response of OrganizationApi->remove_organization_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->remove_organization_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**RemoveMemberPayload**](RemoveMemberPayload.md)|  | 

### Return type

[**RemoveMemberFromOrganizationResponseModel**](RemoveMemberFromOrganizationResponseModel.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_organization_information**
> GetOrganizationResponseModel retrieve_organization_information()

Retrieve Organization Information

Retrieves detailed information about your organization, including current credit, threshold, number of instances, and number of volumes. For additional information on organizations, [click here](https://infrahub-doc.nexgencloud.com/docs/api-reference/auth-resources/organization/retrieve-org-details).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.get_organization_response_model import GetOrganizationResponseModel
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
    api_instance = hyperstack.OrganizationApi(api_client)

    try:
        # Retrieve Organization Information
        api_response = api_instance.retrieve_organization_information()
        print("The response of OrganizationApi->retrieve_organization_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->retrieve_organization_information: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetOrganizationResponseModel**](GetOrganizationResponseModel.md)

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

# **update_organization_information**
> UpdateOrganizationResponseModel update_organization_information(payload)

Update Organization Information

Updates the name of the organization. For additional information, [click here](https://infrahub-doc.nexgencloud.com/docs/api-reference/auth-resources/organization/update-org-name).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.update_organization_payload import UpdateOrganizationPayload
from hyperstack.models.update_organization_response_model import UpdateOrganizationResponseModel
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
    api_instance = hyperstack.OrganizationApi(api_client)
    payload = hyperstack.UpdateOrganizationPayload() # UpdateOrganizationPayload | 

    try:
        # Update Organization Information
        api_response = api_instance.update_organization_information(payload)
        print("The response of OrganizationApi->update_organization_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->update_organization_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UpdateOrganizationPayload**](UpdateOrganizationPayload.md)|  | 

### Return type

[**UpdateOrganizationResponseModel**](UpdateOrganizationResponseModel.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

