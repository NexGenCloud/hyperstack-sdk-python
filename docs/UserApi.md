# hyperstack.UserApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_billing_info**](UserApi.md#add_user_billing_info) | **POST** /billing/user/info | POST: Insert billing info
[**get_user_billing_info**](UserApi.md#get_user_billing_info) | **GET** /billing/user/info | GET: Retrieve billing info
[**update_user_billing_info**](UserApi.md#update_user_billing_info) | **PUT** /billing/user/info | PUT: Update billing info


# **add_user_billing_info**
> AddUserInfoSuccessResponseModel add_user_billing_info(payload)

POST: Insert billing info

Add billing details associated with your user in the request body.

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
        api_response = api_instance.add_user_billing_info(payload)
        print("The response of UserApi->add_user_billing_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->add_user_billing_info: %s\n" % e)
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

# **get_user_billing_info**
> UsersInfoListResponse get_user_billing_info()

GET: Retrieve billing info

Retrieve the billing details associated with your user.

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
        api_response = api_instance.get_user_billing_info()
        print("The response of UserApi->get_user_billing_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_billing_info: %s\n" % e)
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

# **update_user_billing_info**
> AddUserInfoSuccessResponseModel update_user_billing_info(payload)

PUT: Update billing info

Update the billing information for your user in the request body.

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
        api_response = api_instance.update_user_billing_info(payload)
        print("The response of UserApi->update_user_billing_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_user_billing_info: %s\n" % e)
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

