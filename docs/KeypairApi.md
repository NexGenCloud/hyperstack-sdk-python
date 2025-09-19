# hyperstack.KeypairApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_key_pair**](KeypairApi.md#delete_key_pair) | **DELETE** /core/keypair/{id} | Delete key pair
[**import_key_pair**](KeypairApi.md#import_key_pair) | **POST** /core/keypairs | Import key pair
[**list_key_pairs**](KeypairApi.md#list_key_pairs) | **GET** /core/keypairs | List key pairs
[**update_key_pair_name**](KeypairApi.md#update_key_pair_name) | **PUT** /core/keypair/{id} | Update key pair name


# **delete_key_pair**
> ResponseModel delete_key_pair(id)

Delete key pair

Permanently deletes a specified key pair. Provide the key pair ID in the path to remove the designated key pair.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.response_model import ResponseModel
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
    api_instance = hyperstack.KeypairApi(api_client)
    id = 56 # int | 

    try:
        # Delete key pair
        api_response = api_instance.delete_key_pair(id)
        print("The response of KeypairApi->delete_key_pair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeypairApi->delete_key_pair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Keypair successfully deleted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_key_pair**
> ImportKeypairResponse import_key_pair(payload)

Import key pair

Imports a new key pair for secure shell (SSH) access to your resources. Provide the key name, environment name, and public key in the request body. For more details on importing SSH key pairs, [**click here**](https://docs.hyperstack.cloud/docs/api-reference/core-resources/keypairs/import-keypair).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.import_keypair_payload import ImportKeypairPayload
from hyperstack.models.import_keypair_response import ImportKeypairResponse
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
    api_instance = hyperstack.KeypairApi(api_client)
    payload = hyperstack.ImportKeypairPayload() # ImportKeypairPayload | 

    try:
        # Import key pair
        api_response = api_instance.import_key_pair(payload)
        print("The response of KeypairApi->import_key_pair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeypairApi->import_key_pair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ImportKeypairPayload**](ImportKeypairPayload.md)|  | 

### Return type

[**ImportKeypairResponse**](ImportKeypairResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Keypair is imported successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_key_pairs**
> Keypairs list_key_pairs(page=page, page_size=page_size, search=search)

List key pairs

Retrieves a list of your existing SSH key pairs, providing details for each. For more information on SSH key pairs, [**click here**](https://docs.hyperstack.cloud/docs/api-reference/core-resources/keypairs/).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.keypairs import Keypairs
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
    api_instance = hyperstack.KeypairApi(api_client)
    page = 'page_example' # str | Page Number (optional)
    page_size = 'page_size_example' # str | Data Per Page (optional)
    search = 'search_example' # str |  (optional)

    try:
        # List key pairs
        api_response = api_instance.list_key_pairs(page=page, page_size=page_size, search=search)
        print("The response of KeypairApi->list_key_pairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeypairApi->list_key_pairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Page Number | [optional] 
 **page_size** | **str**| Data Per Page | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**Keypairs**](Keypairs.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieval of key pairs list successful. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_key_pair_name**
> UpdateKeypairNameResponse update_key_pair_name(id, payload)

Update key pair name

Updates the name of a specified key pair. Provide the key pair ID in the path, and include the new `name` in the request body.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.update_keypair_name import UpdateKeypairName
from hyperstack.models.update_keypair_name_response import UpdateKeypairNameResponse
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
    api_instance = hyperstack.KeypairApi(api_client)
    id = 56 # int | 
    payload = hyperstack.UpdateKeypairName() # UpdateKeypairName | 

    try:
        # Update key pair name
        api_response = api_instance.update_key_pair_name(id, payload)
        print("The response of KeypairApi->update_key_pair_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeypairApi->update_key_pair_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **payload** | [**UpdateKeypairName**](UpdateKeypairName.md)|  | 

### Return type

[**UpdateKeypairNameResponse**](UpdateKeypairNameResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Keypair name updated successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

