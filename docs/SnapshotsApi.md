# hyperstack.SnapshotsApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_new_custom_image**](SnapshotsApi.md#create_a_new_custom_image) | **POST** /core/snapshots/{snapshot_id}/image | Create an image from a snapshot
[**delete_an_existing_snapshot**](SnapshotsApi.md#delete_an_existing_snapshot) | **DELETE** /core/snapshots/{id} | Delete snapshot
[**fetch_snapshot_name_availability**](SnapshotsApi.md#fetch_snapshot_name_availability) | **GET** /core/snapshots/name-availability/{name} | Fetch snapshot name availability
[**restore_a_snapshot**](SnapshotsApi.md#restore_a_snapshot) | **POST** /core/snapshots/{id}/restore | Restore a snapshot
[**retrieve_an_existing_snapshot**](SnapshotsApi.md#retrieve_an_existing_snapshot) | **GET** /core/snapshots/{id} | Retrieve a snapshot
[**retrieves_a_list_of_snapshots**](SnapshotsApi.md#retrieves_a_list_of_snapshots) | **GET** /core/snapshots | Retrieve list of snapshots with pagination


# **create_a_new_custom_image**
> CreateImage create_a_new_custom_image(snapshot_id, payload)

Create an image from a snapshot

Create a new custom image from an existing snapshot.Requires a name and any labels for your new custom image.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.create_image import CreateImage
from hyperstack.models.create_image_payload import CreateImagePayload
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
    api_instance = hyperstack.SnapshotsApi(api_client)
    snapshot_id = 56 # int | 
    payload = hyperstack.CreateImagePayload() # CreateImagePayload | 

    try:
        # Create an image from a snapshot
        api_response = api_instance.create_a_new_custom_image(snapshot_id, payload)
        print("The response of SnapshotsApi->create_a_new_custom_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->create_a_new_custom_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **int**|  | 
 **payload** | [**CreateImagePayload**](CreateImagePayload.md)|  | 

### Return type

[**CreateImage**](CreateImage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creation of image successful. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_an_existing_snapshot**
> ResponseModel delete_an_existing_snapshot(id)

Delete snapshot

Delete a snapshot. Provide the snapshot ID in the path to delete the specified snapshot. If the snapshot is connected with an image, that image will also bedeleted and the deleted image ID will be returned in the success message response.

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
    api_instance = hyperstack.SnapshotsApi(api_client)
    id = 56 # int | 

    try:
        # Delete snapshot
        api_response = api_instance.delete_an_existing_snapshot(id)
        print("The response of SnapshotsApi->delete_an_existing_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->delete_an_existing_snapshot: %s\n" % e)
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_snapshot_name_availability**
> NameAvailableModel fetch_snapshot_name_availability(name)

Fetch snapshot name availability

Check if a Snapshot name is available

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
    api_instance = hyperstack.SnapshotsApi(api_client)
    name = 'name_example' # str | 

    try:
        # Fetch snapshot name availability
        api_response = api_instance.fetch_snapshot_name_availability(name)
        print("The response of SnapshotsApi->fetch_snapshot_name_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->fetch_snapshot_name_availability: %s\n" % e)
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

# **restore_a_snapshot**
> Instance restore_a_snapshot(id, payload)

Restore a snapshot

Restore a snapshot.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.instance import Instance
from hyperstack.models.snapshot_restore_request import SnapshotRestoreRequest
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
    api_instance = hyperstack.SnapshotsApi(api_client)
    id = 56 # int | 
    payload = hyperstack.SnapshotRestoreRequest() # SnapshotRestoreRequest | 

    try:
        # Restore a snapshot
        api_response = api_instance.restore_a_snapshot(id, payload)
        print("The response of SnapshotsApi->restore_a_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->restore_a_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **payload** | [**SnapshotRestoreRequest**](SnapshotRestoreRequest.md)|  | 

### Return type

[**Instance**](Instance.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_an_existing_snapshot**
> SnapshotRetrieve retrieve_an_existing_snapshot(id)

Retrieve a snapshot

Retrieve a snapshot.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.snapshot_retrieve import SnapshotRetrieve
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
    api_instance = hyperstack.SnapshotsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve a snapshot
        api_response = api_instance.retrieve_an_existing_snapshot(id)
        print("The response of SnapshotsApi->retrieve_an_existing_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->retrieve_an_existing_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SnapshotRetrieve**](SnapshotRetrieve.md)

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

# **retrieves_a_list_of_snapshots**
> Snapshots retrieves_a_list_of_snapshots(page=page, page_size=page_size, search=search)

Retrieve list of snapshots with pagination

Retrieves a list of snapshots, providing details such as snapshot name, timestamp, VM ID, and other relevant information.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.snapshots import Snapshots
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
    api_instance = hyperstack.SnapshotsApi(api_client)
    page = 'page_example' # str | Page Number (optional)
    page_size = 'page_size_example' # str | Data Per Page (optional)
    search = 'search_example' # str | Search By Snapshot ID or Name (optional)

    try:
        # Retrieve list of snapshots with pagination
        api_response = api_instance.retrieves_a_list_of_snapshots(page=page, page_size=page_size, search=search)
        print("The response of SnapshotsApi->retrieves_a_list_of_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->retrieves_a_list_of_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Page Number | [optional] 
 **page_size** | **str**| Data Per Page | [optional] 
 **search** | **str**| Search By Snapshot ID or Name | [optional] 

### Return type

[**Snapshots**](Snapshots.md)

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

