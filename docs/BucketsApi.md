# hyperstack.BucketsApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bucket_endpoint**](BucketsApi.md#delete_bucket_endpoint) | **DELETE** /object-storage/buckets/{bucket_name} | Delete a bucket
[**list_buckets_endpoint**](BucketsApi.md#list_buckets_endpoint) | **GET** /object-storage/buckets | List buckets
[**retrieve_bucket_endpoint**](BucketsApi.md#retrieve_bucket_endpoint) | **GET** /object-storage/buckets/{bucket_name} | Retrieve a bucket


# **delete_bucket_endpoint**
> ObjectStorageDeleteResponse delete_bucket_endpoint(bucket_name, region)

Delete a bucket

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
    api_instance = hyperstack.BucketsApi(api_client)
    bucket_name = 'bucket_name_example' # str | 
    region = 'region_example' # str | 

    try:
        # Delete a bucket
        api_response = api_instance.delete_bucket_endpoint(bucket_name, region)
        print("The response of BucketsApi->delete_bucket_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketsApi->delete_bucket_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**|  | 
 **region** | **str**|  | 

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

# **list_buckets_endpoint**
> ObjectStorageBucketListResponse list_buckets_endpoint(search=search)

List buckets

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.object_storage_bucket_list_response import ObjectStorageBucketListResponse
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
    api_instance = hyperstack.BucketsApi(api_client)
    search = 'search_example' # str |  (optional)

    try:
        # List buckets
        api_response = api_instance.list_buckets_endpoint(search=search)
        print("The response of BucketsApi->list_buckets_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketsApi->list_buckets_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 

### Return type

[**ObjectStorageBucketListResponse**](ObjectStorageBucketListResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_bucket_endpoint**
> ObjectStorageBucketResponse retrieve_bucket_endpoint(bucket_name, region)

Retrieve a bucket

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.object_storage_bucket_response import ObjectStorageBucketResponse
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
    api_instance = hyperstack.BucketsApi(api_client)
    bucket_name = 'bucket_name_example' # str | 
    region = 'region_example' # str | 

    try:
        # Retrieve a bucket
        api_response = api_instance.retrieve_bucket_endpoint(bucket_name, region)
        print("The response of BucketsApi->retrieve_bucket_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketsApi->retrieve_bucket_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**|  | 
 **region** | **str**|  | 

### Return type

[**ObjectStorageBucketResponse**](ObjectStorageBucketResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

