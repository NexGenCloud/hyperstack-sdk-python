# hyperstack.ApiKeyApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_key**](ApiKeyApi.md#delete_api_key) | **DELETE** /api-key/{api_key_id} | Delete API Key
[**generate_api_key**](ApiKeyApi.md#generate_api_key) | **POST** /api-key/generate | Generate API Key
[**retrieve_api_keys**](ApiKeyApi.md#retrieve_api_keys) | **GET** /api-key | Retrieve API Keys
[**update_api_key**](ApiKeyApi.md#update_api_key) | **PUT** /api-key/{api_key_id} | Update API Key


# **delete_api_key**
> CommonResponseModel delete_api_key(api_key_id)

Delete API Key

Delete a specified API key by including the ID of the API key in the path.

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
    api_instance = hyperstack.ApiKeyApi(api_client)
    api_key_id = 56 # int | 

    try:
        # Delete API Key
        api_response = api_instance.delete_api_key(api_key_id)
        print("The response of ApiKeyApi->delete_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->delete_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **int**|  | 

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

# **generate_api_key**
> GenerateUpdateApiKeyResponseModel generate_api_key(payload)

Generate API Key

Generates your API key, providing access to the Infrahub APIs. For further details on API keys, [**click here**](https://infrahub-doc.nexgencloud.com/docs/api-reference/auth-resources/api-key/generate-api-key).

### Example

* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.generate_update_api_key_payload import GenerateUpdateApiKeyPayload
from hyperstack.models.generate_update_api_key_response_model import GenerateUpdateApiKeyResponseModel
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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.ApiKeyApi(api_client)
    payload = hyperstack.GenerateUpdateApiKeyPayload() # GenerateUpdateApiKeyPayload | 

    try:
        # Generate API Key
        api_response = api_instance.generate_api_key(payload)
        print("The response of ApiKeyApi->generate_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->generate_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**GenerateUpdateApiKeyPayload**](GenerateUpdateApiKeyPayload.md)|  | 

### Return type

[**GenerateUpdateApiKeyResponseModel**](GenerateUpdateApiKeyResponseModel.md)

### Authorization

[accessToken](../README.md#accessToken)

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
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_api_keys**
> GetApiKeysResponseModel retrieve_api_keys()

Retrieve API Keys

Retrieves your API keys, granting access to the Infrahub APIs. For further details on API keys, [**click here**](https://infrahub-doc.nexgencloud.com/docs/api-reference/auth-resources/api-key/retrieve-api-key).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.get_api_keys_response_model import GetApiKeysResponseModel
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
    api_instance = hyperstack.ApiKeyApi(api_client)

    try:
        # Retrieve API Keys
        api_response = api_instance.retrieve_api_keys()
        print("The response of ApiKeyApi->retrieve_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->retrieve_api_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetApiKeysResponseModel**](GetApiKeysResponseModel.md)

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

# **update_api_key**
> GenerateUpdateApiKeyResponseModel update_api_key(api_key_id, payload)

Update API Key

Updates the name and optionally the description of a specified API key. Include the ID of the API key in the path and the new name and optional description in the body of the request.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.generate_update_api_key_payload import GenerateUpdateApiKeyPayload
from hyperstack.models.generate_update_api_key_response_model import GenerateUpdateApiKeyResponseModel
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
    api_instance = hyperstack.ApiKeyApi(api_client)
    api_key_id = 56 # int | 
    payload = hyperstack.GenerateUpdateApiKeyPayload() # GenerateUpdateApiKeyPayload | 

    try:
        # Update API Key
        api_response = api_instance.update_api_key(api_key_id, payload)
        print("The response of ApiKeyApi->update_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeyApi->update_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **int**|  | 
 **payload** | [**GenerateUpdateApiKeyPayload**](GenerateUpdateApiKeyPayload.md)|  | 

### Return type

[**GenerateUpdateApiKeyResponseModel**](GenerateUpdateApiKeyResponseModel.md)

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

