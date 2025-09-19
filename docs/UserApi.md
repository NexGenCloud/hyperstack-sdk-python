# hyperstack.UserApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user**](UserApi.md#get_user) | **GET** /billing/user/info | GET: Retrieve billing info
[**post_user**](UserApi.md#post_user) | **POST** /billing/user/info | POST: Insert billing info
[**put_user**](UserApi.md#put_user) | **PUT** /billing/user/info | PUT: Update billing info


# **get_user**
> UsersInfoListResponse get_user()

GET: Retrieve billing info

Retrieve the billing details associated with your organization.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.users_info_list_response import UsersInfoListResponse
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
    api_instance = hyperstack.UserApi(api_client)

    try:
        # GET: Retrieve billing info
        api_response = api_instance.get_user()
        print("The response of UserApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UsersInfoListResponse**](UsersInfoListResponse.md)

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

# **post_user**
> AddUserInfoSuccessResponseModel post_user(payload)

POST: Insert billing info

Add billing details associated with your organization in the request body.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.add_user_info_success_response_model import AddUserInfoSuccessResponseModel
from hyperstack.models.user_info_post_payload import UserInfoPostPayload
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
    api_instance = hyperstack.UserApi(api_client)
    payload = hyperstack.UserInfoPostPayload() # UserInfoPostPayload | 

    try:
        # POST: Insert billing info
        api_response = api_instance.post_user(payload)
        print("The response of UserApi->post_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->post_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UserInfoPostPayload**](UserInfoPostPayload.md)|  | 

### Return type

[**AddUserInfoSuccessResponseModel**](AddUserInfoSuccessResponseModel.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_user**
> AddUserInfoSuccessResponseModel put_user(payload)

PUT: Update billing info

Update the billing information for your organization in the request body.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.add_user_info_success_response_model import AddUserInfoSuccessResponseModel
from hyperstack.models.user_info_post_payload import UserInfoPostPayload
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
    api_instance = hyperstack.UserApi(api_client)
    payload = hyperstack.UserInfoPostPayload() # UserInfoPostPayload | 

    try:
        # PUT: Update billing info
        api_response = api_instance.put_user(payload)
        print("The response of UserApi->put_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->put_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UserInfoPostPayload**](UserInfoPostPayload.md)|  | 

### Return type

[**AddUserInfoSuccessResponseModel**](AddUserInfoSuccessResponseModel.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

