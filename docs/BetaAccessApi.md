# hyperstack.BetaAccessApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_beta_access_request**](BetaAccessApi.md#create_a_beta_access_request) | **POST** /auth/beta-access/requests | Create a new beta access request
[**get_beta_access_status**](BetaAccessApi.md#get_beta_access_status) | **GET** /auth/beta-access/requests | Check the status of all beta access requests
[**get_beta_access_status2**](BetaAccessApi.md#get_beta_access_status2) | **GET** /auth/beta-access/requests/{program} | Check the status of beta access requests


# **create_a_beta_access_request**
> BetaAccessRequestResponseModel create_a_beta_access_request(payload)

Create a new beta access request

Creates a new beta access request for the current user

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.beta_access_request_payload import BetaAccessRequestPayload
from hyperstack.models.beta_access_request_response_model import BetaAccessRequestResponseModel
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
    api_instance = hyperstack.BetaAccessApi(api_client)
    payload = hyperstack.BetaAccessRequestPayload() # BetaAccessRequestPayload | 

    try:
        # Create a new beta access request
        api_response = api_instance.create_a_beta_access_request(payload)
        print("The response of BetaAccessApi->create_a_beta_access_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaAccessApi->create_a_beta_access_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**BetaAccessRequestPayload**](BetaAccessRequestPayload.md)|  | 

### Return type

[**BetaAccessRequestResponseModel**](BetaAccessRequestResponseModel.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_beta_access_status**
> BetaAccessStatusResponseModel get_beta_access_status()

Check the status of all beta access requests

Check the status of all beta access requests.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.beta_access_status_response_model import BetaAccessStatusResponseModel
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
    api_instance = hyperstack.BetaAccessApi(api_client)

    try:
        # Check the status of all beta access requests
        api_response = api_instance.get_beta_access_status()
        print("The response of BetaAccessApi->get_beta_access_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaAccessApi->get_beta_access_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BetaAccessStatusResponseModel**](BetaAccessStatusResponseModel.md)

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

# **get_beta_access_status2**
> BetaAccessStatusResponseModel get_beta_access_status2(program)

Check the status of beta access requests

Check the status of a particular beta access requests.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.beta_access_status_response_model import BetaAccessStatusResponseModel
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
    api_instance = hyperstack.BetaAccessApi(api_client)
    program = 'program_example' # str | 

    try:
        # Check the status of beta access requests
        api_response = api_instance.get_beta_access_status2(program)
        print("The response of BetaAccessApi->get_beta_access_status2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaAccessApi->get_beta_access_status2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program** | **str**|  | 

### Return type

[**BetaAccessStatusResponseModel**](BetaAccessStatusResponseModel.md)

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

