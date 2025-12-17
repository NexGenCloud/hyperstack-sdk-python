# hyperstack.AccessKeysApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_key_endpoint**](AccessKeysApi.md#create_access_key_endpoint) | **POST** /object-storage/access-keys | Generate a new access key
[**delete_access_key_endpoint**](AccessKeysApi.md#delete_access_key_endpoint) | **DELETE** /object-storage/access-keys/{access_key_id} | Remove an existing access key
[**list_access_keys_endpoint**](AccessKeysApi.md#list_access_keys_endpoint) | **GET** /object-storage/access-keys | List access keys


# **create_access_key_endpoint**
> ObjectStorageAccessKeyCreateResponse create_access_key_endpoint(body=body)

Generate a new access key

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.object_storage_access_key_create_request import ObjectStorageAccessKeyCreateRequest
from hyperstack.models.object_storage_access_key_create_response import ObjectStorageAccessKeyCreateResponse
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
    api_instance = hyperstack.AccessKeysApi(api_client)
    body = hyperstack.ObjectStorageAccessKeyCreateRequest() # ObjectStorageAccessKeyCreateRequest |  (optional)

    try:
        # Generate a new access key
        api_response = api_instance.create_access_key_endpoint(body=body)
        print("The response of AccessKeysApi->create_access_key_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessKeysApi->create_access_key_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectStorageAccessKeyCreateRequest**](ObjectStorageAccessKeyCreateRequest.md)|  | [optional] 

### Return type

[**ObjectStorageAccessKeyCreateResponse**](ObjectStorageAccessKeyCreateResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_key_endpoint**
> ObjectStorageDeleteResponse delete_access_key_endpoint(access_key_id)

Remove an existing access key

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.object_storage_delete_response import ObjectStorageDeleteResponse
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
    api_instance = hyperstack.AccessKeysApi(api_client)
    access_key_id = 'access_key_id_example' # str | 

    try:
        # Remove an existing access key
        api_response = api_instance.delete_access_key_endpoint(access_key_id)
        print("The response of AccessKeysApi->delete_access_key_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessKeysApi->delete_access_key_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key_id** | **str**|  | 

### Return type

[**ObjectStorageDeleteResponse**](ObjectStorageDeleteResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_access_keys_endpoint**
> ObjectStorageAccessKeyListResponse list_access_keys_endpoint(search=search, page=page, page_size=page_size)

List access keys

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.object_storage_access_key_list_response import ObjectStorageAccessKeyListResponse
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
    api_instance = hyperstack.AccessKeysApi(api_client)
    search = 'search_example' # str |  (optional)
    page = 'page_example' # str |  (optional)
    page_size = 'page_size_example' # str |  (optional)

    try:
        # List access keys
        api_response = api_instance.list_access_keys_endpoint(search=search, page=page, page_size=page_size)
        print("The response of AccessKeysApi->list_access_keys_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessKeysApi->list_access_keys_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 
 **page** | **str**|  | [optional] 
 **page_size** | **str**|  | [optional] 

### Return type

[**ObjectStorageAccessKeyListResponse**](ObjectStorageAccessKeyListResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

