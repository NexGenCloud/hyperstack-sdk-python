# hyperstack.AutoTopupApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auto_top_up**](AutoTopupApi.md#create_auto_top_up) | **POST** /billing/auto-topup | Create an auto top up configuration and initiate Stripe setup
[**disable_auto_top_up**](AutoTopupApi.md#disable_auto_top_up) | **DELETE** /billing/auto-topup | Disable auto top up, preventing any future automatic charges
[**get_auto_top_up**](AutoTopupApi.md#get_auto_top_up) | **GET** /billing/auto-topup | Retrieve the current auto top up configuration and transaction history
[**get_auto_top_up_status**](AutoTopupApi.md#get_auto_top_up_status) | **GET** /billing/auto-topup/status | Get auto top-up status and configuration
[**update_auto_top_up**](AutoTopupApi.md#update_auto_top_up) | **PUT** /billing/auto-topup | Update an existing active auto top up configuration


# **create_auto_top_up**
> CreateAutoTopupResponse create_auto_top_up(payload)

Create an auto top up configuration and initiate Stripe setup

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.create_auto_topup_payload import CreateAutoTopupPayload
from hyperstack.models.create_auto_topup_response import CreateAutoTopupResponse
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
    api_instance = hyperstack.AutoTopupApi(api_client)
    payload = hyperstack.CreateAutoTopupPayload() # CreateAutoTopupPayload | 

    try:
        # Create an auto top up configuration and initiate Stripe setup
        api_response = api_instance.create_auto_top_up(payload)
        print("The response of AutoTopupApi->create_auto_top_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->create_auto_top_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateAutoTopupPayload**](CreateAutoTopupPayload.md)|  | 

### Return type

[**CreateAutoTopupResponse**](CreateAutoTopupResponse.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_auto_top_up**
> DisableAutoTopupResponse disable_auto_top_up()

Disable auto top up, preventing any future automatic charges

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.disable_auto_topup_response import DisableAutoTopupResponse
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
    api_instance = hyperstack.AutoTopupApi(api_client)

    try:
        # Disable auto top up, preventing any future automatic charges
        api_response = api_instance.disable_auto_top_up()
        print("The response of AutoTopupApi->disable_auto_top_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->disable_auto_top_up: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DisableAutoTopupResponse**](DisableAutoTopupResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_top_up**
> GetAutoTopupResponse get_auto_top_up()

Retrieve the current auto top up configuration and transaction history

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.get_auto_topup_response import GetAutoTopupResponse
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
    api_instance = hyperstack.AutoTopupApi(api_client)

    try:
        # Retrieve the current auto top up configuration and transaction history
        api_response = api_instance.get_auto_top_up()
        print("The response of AutoTopupApi->get_auto_top_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->get_auto_top_up: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAutoTopupResponse**](GetAutoTopupResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_top_up_status**
> AutoTopupStatusSchema get_auto_top_up_status()

Get auto top-up status and configuration

Retrieves the current auto top-up configuration and status for your organization. Returns the status (active, disabled, pending_setup, or null if never configured), along with the threshold and top-up amounts. For additional information, [**click here**](None/docs/api-reference/billing-resources/).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.auto_topup_status_schema import AutoTopupStatusSchema
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
    api_instance = hyperstack.AutoTopupApi(api_client)

    try:
        # Get auto top-up status and configuration
        api_response = api_instance.get_auto_top_up_status()
        print("The response of AutoTopupApi->get_auto_top_up_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->get_auto_top_up_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AutoTopupStatusSchema**](AutoTopupStatusSchema.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_top_up**
> UpdateAutoTopupResponse update_auto_top_up(payload)

Update an existing active auto top up configuration

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.update_auto_topup_payload import UpdateAutoTopupPayload
from hyperstack.models.update_auto_topup_response import UpdateAutoTopupResponse
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
    api_instance = hyperstack.AutoTopupApi(api_client)
    payload = hyperstack.UpdateAutoTopupPayload() # UpdateAutoTopupPayload | 

    try:
        # Update an existing active auto top up configuration
        api_response = api_instance.update_auto_top_up(payload)
        print("The response of AutoTopupApi->update_auto_top_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->update_auto_top_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UpdateAutoTopupPayload**](UpdateAutoTopupPayload.md)|  | 

### Return type

[**UpdateAutoTopupResponse**](UpdateAutoTopupResponse.md)

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

