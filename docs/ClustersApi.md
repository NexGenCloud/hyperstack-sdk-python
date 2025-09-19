# hyperstack.ClustersApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster**](ClustersApi.md#create_cluster) | **POST** /core/clusters | Create Cluster
[**create_node**](ClustersApi.md#create_node) | **POST** /core/clusters/{cluster_id}/nodes | Create Node
[**create_node_group**](ClustersApi.md#create_node_group) | **POST** /core/clusters/{cluster_id}/node-groups | Create a node group in a cluster
[**delete_a_cluster**](ClustersApi.md#delete_a_cluster) | **DELETE** /core/clusters/{id} | Delete a cluster
[**delete_a_node_group**](ClustersApi.md#delete_a_node_group) | **DELETE** /core/clusters/{cluster_id}/node-groups/{node_group_id} | Delete a node group
[**delete_cluster_node**](ClustersApi.md#delete_cluster_node) | **DELETE** /core/clusters/{cluster_id}/nodes/{node_id} | Delete Cluster Node
[**fetch_cluster_name_availability**](ClustersApi.md#fetch_cluster_name_availability) | **GET** /core/clusters/name-availability/{name} | Fetch cluster name availability
[**get_cluster_master_flavors**](ClustersApi.md#get_cluster_master_flavors) | **GET** /core/clusters/master-flavors | Get Cluster Master Flavors
[**get_cluster_nodes**](ClustersApi.md#get_cluster_nodes) | **GET** /core/clusters/{cluster_id}/nodes | Get Cluster Nodes
[**get_cluster_versions**](ClustersApi.md#get_cluster_versions) | **GET** /core/clusters/versions | List Cluster Versions
[**getting_cluster_detail**](ClustersApi.md#getting_cluster_detail) | **GET** /core/clusters/{id} | Getting Cluster Detail
[**list_clusters**](ClustersApi.md#list_clusters) | **GET** /core/clusters | List Clusters
[**list_node_groups**](ClustersApi.md#list_node_groups) | **GET** /core/clusters/{cluster_id}/node-groups | List node groups for a cluster
[**retrieve_a_node_group**](ClustersApi.md#retrieve_a_node_group) | **GET** /core/clusters/{cluster_id}/node-groups/{node_group_id} | Retrieve a node group in a cluster


# **create_cluster**
> ClusterResponse create_cluster(payload)

Create Cluster

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.cluster_response import ClusterResponse
from hyperstack.models.create_cluster_payload import CreateClusterPayload
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
    api_instance = hyperstack.ClustersApi(api_client)
    payload = hyperstack.CreateClusterPayload() # CreateClusterPayload | 

    try:
        # Create Cluster
        api_response = api_instance.create_cluster(payload)
        print("The response of ClustersApi->create_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->create_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateClusterPayload**](CreateClusterPayload.md)|  | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node**
> ClusterNodesListResponse create_node(cluster_id, payload)

Create Node

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.cluster_nodes_list_response import ClusterNodesListResponse
from hyperstack.models.create_cluster_node_fields import CreateClusterNodeFields
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
    api_instance = hyperstack.ClustersApi(api_client)
    cluster_id = 56 # int | 
    payload = hyperstack.CreateClusterNodeFields() # CreateClusterNodeFields | 

    try:
        # Create Node
        api_response = api_instance.create_node(cluster_id, payload)
        print("The response of ClustersApi->create_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->create_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **payload** | [**CreateClusterNodeFields**](CreateClusterNodeFields.md)|  | 

### Return type

[**ClusterNodesListResponse**](ClusterNodesListResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node_group**
> ClusterNodeGroupsCreateResponse create_node_group(cluster_id, payload)

Create a node group in a cluster

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.cluster_node_groups_create_response import ClusterNodeGroupsCreateResponse
from hyperstack.models.create_cluster_node_group_payload import CreateClusterNodeGroupPayload
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
    api_instance = hyperstack.ClustersApi(api_client)
    cluster_id = 56 # int | 
    payload = hyperstack.CreateClusterNodeGroupPayload() # CreateClusterNodeGroupPayload | 

    try:
        # Create a node group in a cluster
        api_response = api_instance.create_node_group(cluster_id, payload)
        print("The response of ClustersApi->create_node_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->create_node_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **payload** | [**CreateClusterNodeGroupPayload**](CreateClusterNodeGroupPayload.md)|  | 

### Return type

[**ClusterNodeGroupsCreateResponse**](ClusterNodeGroupsCreateResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_cluster**
> ResponseModel delete_a_cluster(id)

Delete a cluster

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
    api_instance = hyperstack.ClustersApi(api_client)
    id = 56 # int | 

    try:
        # Delete a cluster
        api_response = api_instance.delete_a_cluster(id)
        print("The response of ClustersApi->delete_a_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_a_cluster: %s\n" % e)
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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_node_group**
> ResponseModel delete_a_node_group(cluster_id, node_group_id)

Delete a node group

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
    api_instance = hyperstack.ClustersApi(api_client)
    cluster_id = 56 # int | 
    node_group_id = 56 # int | 

    try:
        # Delete a node group
        api_response = api_instance.delete_a_node_group(cluster_id, node_group_id)
        print("The response of ClustersApi->delete_a_node_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_a_node_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **node_group_id** | **int**|  | 

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

# **delete_cluster_node**
> ResponseModel delete_cluster_node(cluster_id, node_id)

Delete Cluster Node

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
    api_instance = hyperstack.ClustersApi(api_client)
    cluster_id = 56 # int | 
    node_id = 56 # int | 

    try:
        # Delete Cluster Node
        api_response = api_instance.delete_cluster_node(cluster_id, node_id)
        print("The response of ClustersApi->delete_cluster_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_cluster_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **node_id** | **int**|  | 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_cluster_name_availability**
> NameAvailableModel fetch_cluster_name_availability(name)

Fetch cluster name availability

Check if a Cluster name is available

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
    api_instance = hyperstack.ClustersApi(api_client)
    name = 'name_example' # str | 

    try:
        # Fetch cluster name availability
        api_response = api_instance.fetch_cluster_name_availability(name)
        print("The response of ClustersApi->fetch_cluster_name_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->fetch_cluster_name_availability: %s\n" % e)
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

# **get_cluster_master_flavors**
> MasterFlavorsResponse get_cluster_master_flavors()

Get Cluster Master Flavors

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.master_flavors_response import MasterFlavorsResponse
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
    api_instance = hyperstack.ClustersApi(api_client)

    try:
        # Get Cluster Master Flavors
        api_response = api_instance.get_cluster_master_flavors()
        print("The response of ClustersApi->get_cluster_master_flavors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_master_flavors: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MasterFlavorsResponse**](MasterFlavorsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved Flavors. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_nodes**
> ClusterNodesListResponse get_cluster_nodes(cluster_id)

Get Cluster Nodes

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.cluster_nodes_list_response import ClusterNodesListResponse
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
    api_instance = hyperstack.ClustersApi(api_client)
    cluster_id = 56 # int | 

    try:
        # Get Cluster Nodes
        api_response = api_instance.get_cluster_nodes(cluster_id)
        print("The response of ClustersApi->get_cluster_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 

### Return type

[**ClusterNodesListResponse**](ClusterNodesListResponse.md)

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

# **get_cluster_versions**
> ClusterVersions get_cluster_versions(region=region)

List Cluster Versions

Lists available Kubernetes versions, optionally filtered by region.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.cluster_versions import ClusterVersions
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
    api_instance = hyperstack.ClustersApi(api_client)
    region = 'region_example' # str | Filter versions by region name (optional) (optional)

    try:
        # List Cluster Versions
        api_response = api_instance.get_cluster_versions(region=region)
        print("The response of ClustersApi->get_cluster_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| Filter versions by region name (optional) | [optional] 

### Return type

[**ClusterVersions**](ClusterVersions.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved Cluster Versions. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getting_cluster_detail**
> ClusterResponse getting_cluster_detail(id)

Getting Cluster Detail

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.cluster_response import ClusterResponse
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
    api_instance = hyperstack.ClustersApi(api_client)
    id = 56 # int | 

    try:
        # Getting Cluster Detail
        api_response = api_instance.getting_cluster_detail(id)
        print("The response of ClustersApi->getting_cluster_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->getting_cluster_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

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

# **list_clusters**
> ClusterListResponse list_clusters(page=page, page_size=page_size, environment=environment, search=search)

List Clusters

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.cluster_list_response import ClusterListResponse
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
    api_instance = hyperstack.ClustersApi(api_client)
    page = 56 # int | Page number for pagination (optional)
    page_size = 56 # int | Number of items per page (optional)
    environment = 'environment_example' # str | Environment Filter (optional)
    search = 'search_example' # str | Search query to filter cluster by name (optional)

    try:
        # List Clusters
        api_response = api_instance.list_clusters(page=page, page_size=page_size, environment=environment, search=search)
        print("The response of ClustersApi->list_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->list_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number for pagination | [optional] 
 **page_size** | **int**| Number of items per page | [optional] 
 **environment** | **str**| Environment Filter | [optional] 
 **search** | **str**| Search query to filter cluster by name | [optional] 

### Return type

[**ClusterListResponse**](ClusterListResponse.md)

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

# **list_node_groups**
> ClusterNodeGroupsListResponse list_node_groups(cluster_id)

List node groups for a cluster

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.cluster_node_groups_list_response import ClusterNodeGroupsListResponse
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
    api_instance = hyperstack.ClustersApi(api_client)
    cluster_id = 56 # int | 

    try:
        # List node groups for a cluster
        api_response = api_instance.list_node_groups(cluster_id)
        print("The response of ClustersApi->list_node_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->list_node_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 

### Return type

[**ClusterNodeGroupsListResponse**](ClusterNodeGroupsListResponse.md)

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

# **retrieve_a_node_group**
> ClusterNodeGroupsGetResponse retrieve_a_node_group(cluster_id, node_group_id)

Retrieve a node group in a cluster

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.cluster_node_groups_get_response import ClusterNodeGroupsGetResponse
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
    api_instance = hyperstack.ClustersApi(api_client)
    cluster_id = 56 # int | 
    node_group_id = 56 # int | 

    try:
        # Retrieve a node group in a cluster
        api_response = api_instance.retrieve_a_node_group(cluster_id, node_group_id)
        print("The response of ClustersApi->retrieve_a_node_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->retrieve_a_node_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **node_group_id** | **int**|  | 

### Return type

[**ClusterNodeGroupsGetResponse**](ClusterNodeGroupsGetResponse.md)

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

