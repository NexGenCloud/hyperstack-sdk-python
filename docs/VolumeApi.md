# hyperstack.VolumeApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_volume**](VolumeApi.md#create_volume) | **POST** /core/volumes | Create volume
[**delete_volume**](VolumeApi.md#delete_volume) | **DELETE** /core/volumes/{volume_id} | Delete volume
[**fetch_volume_details**](VolumeApi.md#fetch_volume_details) | **GET** /core/volumes/{volume_id} | Fetch Volume Details
[**fetch_volume_name_availability**](VolumeApi.md#fetch_volume_name_availability) | **GET** /core/volume/name-availability/{name} | Fetch volume name availability
[**list_volume_types**](VolumeApi.md#list_volume_types) | **GET** /core/volume-types | List volume types
[**list_volumes**](VolumeApi.md#list_volumes) | **GET** /core/volumes | List volumes
[**update_volume**](VolumeApi.md#update_volume) | **PATCH** /core/volumes/{volume_id} | Update volume fields


# **create_volume**
> Volume create_volume(payload)

Create volume

Creates a volume that can be attached to a virtual machine, expanding its storage capacity. Specify the volume type and custom configuration in the request body. For additional details on volumes, [**click here**]({Config.INFRAHUB_DOCS_BASE}/docs/api-reference/core-resources/volumes/create-volume).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.create_volume_payload import CreateVolumePayload
from hyperstack.models.volume import Volume
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
    api_instance = hyperstack.VolumeApi(api_client)
    payload = hyperstack.CreateVolumePayload() # CreateVolumePayload | 

    try:
        # Create volume
        api_response = api_instance.create_volume(payload)
        print("The response of VolumeApi->create_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeApi->create_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateVolumePayload**](CreateVolumePayload.md)|  | 

### Return type

[**Volume**](Volume.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Volume successfully created. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_volume**
> ResponseModel delete_volume(volume_id)

Delete volume

Deletes a volume permanently. Provide the volume ID in the path to specify the volume to be deleted.

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
    api_instance = hyperstack.VolumeApi(api_client)
    volume_id = 56 # int | 

    try:
        # Delete volume
        api_response = api_instance.delete_volume(volume_id)
        print("The response of VolumeApi->delete_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeApi->delete_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **int**|  | 

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
**200** | Volume successfully deleted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_volume_details**
> Volume fetch_volume_details(volume_id)

Fetch Volume Details

Fetch volume details for specific volume. This endpoint returns id, name, volume size, volume type, status, description, image_id, os_image, created_at, updated_at etc.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.volume import Volume
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
    api_instance = hyperstack.VolumeApi(api_client)
    volume_id = 56 # int | 

    try:
        # Fetch Volume Details
        api_response = api_instance.fetch_volume_details(volume_id)
        print("The response of VolumeApi->fetch_volume_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeApi->fetch_volume_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **int**|  | 

### Return type

[**Volume**](Volume.md)

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
**405** | Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_volume_name_availability**
> NameAvailableModel fetch_volume_name_availability(name)

Fetch volume name availability

Check if a Volume name is available

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.name_available_model import NameAvailableModel
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
    api_instance = hyperstack.VolumeApi(api_client)
    name = 'name_example' # str | 

    try:
        # Fetch volume name availability
        api_response = api_instance.fetch_volume_name_availability(name)
        print("The response of VolumeApi->fetch_volume_name_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeApi->fetch_volume_name_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**NameAvailableModel**](NameAvailableModel.md)

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

# **list_volume_types**
> VolumeTypes list_volume_types()

List volume types

Retrieves a list of available volume types that can be used in the creation of a new volume.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.volume_types import VolumeTypes
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
    api_instance = hyperstack.VolumeApi(api_client)

    try:
        # List volume types
        api_response = api_instance.list_volume_types()
        print("The response of VolumeApi->list_volume_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeApi->list_volume_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VolumeTypes**](VolumeTypes.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of volume types list |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_volumes**
> Volumes list_volumes(page=page, page_size=page_size, search=search, environment=environment)

List volumes

Returns a list of your existing volumes, providing details for each. For more information on volumes, [**click here**]({Config.INFRAHUB_DOCS_BASE}/docs/api-reference/core-resources/volumes/).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.volumes import Volumes
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
    api_instance = hyperstack.VolumeApi(api_client)
    page = 'page_example' # str | Page Number (optional)
    page_size = 'page_size_example' # str | Data Per Page (optional)
    search = 'search_example' # str |  (optional)
    environment = 'environment_example' # str | Filter Environment ID or Name (optional)

    try:
        # List volumes
        api_response = api_instance.list_volumes(page=page, page_size=page_size, search=search, environment=environment)
        print("The response of VolumeApi->list_volumes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeApi->list_volumes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Page Number | [optional] 
 **page_size** | **str**| Data Per Page | [optional] 
 **search** | **str**|  | [optional] 
 **environment** | **str**| Filter Environment ID or Name | [optional] 

### Return type

[**Volumes**](Volumes.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_volume**
> UpdateVolumeResponse update_volume(volume_id, payload)

Update volume fields

Update volume properties. Currently supports updating the environment by providing 'environment_name'. The volume must not be attached to any instance when changing environments, and the target environment must be in the same region.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.update_volume_payload import UpdateVolumePayload
from hyperstack.models.update_volume_response import UpdateVolumeResponse
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
    api_instance = hyperstack.VolumeApi(api_client)
    volume_id = 56 # int | 
    payload = hyperstack.UpdateVolumePayload() # UpdateVolumePayload | 

    try:
        # Update volume fields
        api_response = api_instance.update_volume(volume_id, payload)
        print("The response of VolumeApi->update_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VolumeApi->update_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **int**|  | 
 **payload** | [**UpdateVolumePayload**](UpdateVolumePayload.md)|  | 

### Return type

[**UpdateVolumeResponse**](UpdateVolumeResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Volume successfully updated. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

