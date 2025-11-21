# hyperstack.BillingApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buckets_billing_history_hourly_chart**](BillingApi.md#buckets_billing_history_hourly_chart) | **GET** /billing/billing/history/bucket/{bucket_id}/graph | Retrieve hourly cost datapoints of a Specific Bucket for a specific billing cycle
[**get_bucket_billing_history**](BillingApi.md#get_bucket_billing_history) | **GET** /billing/billing/history/bucket/{bucket_id} | Retrieve Billing History of a Specific Snapshot for a specific Billing Cycle
[**get_cluster_billing_history**](BillingApi.md#get_cluster_billing_history) | **GET** /billing/billing/history/cluster/{cluster_id} | Retrieve Billing History of a Specific Cluster for a specific Billing Cycle
[**get_cluster_billing_history_graph**](BillingApi.md#get_cluster_billing_history_graph) | **GET** /billing/billing/history/cluster/{cluster_id}/graph | Retrieve hourly cost datapoints of a specific Cluster for a specific billing cycle
[**get_data_synthesis_billing_history**](BillingApi.md#get_data_synthesis_billing_history) | **GET** /billing/billing/history/data_synthesis | Retrieve Billing History of data synthesis for a specific Billing Cycle
[**get_data_synthesis_billing_history_graph**](BillingApi.md#get_data_synthesis_billing_history_graph) | **GET** /billing/billing/history/data_synthesis/{resource_id}/graph | Retrieve hourly cost datapoints of a Specific Data Synthesis for a specific
[**get_data_synthesis_history_for_resource**](BillingApi.md#get_data_synthesis_history_for_resource) | **GET** /billing/billing/history/data_synthesis/{resource_id} | 
[**get_fine_tuning_billing_history**](BillingApi.md#get_fine_tuning_billing_history) | **GET** /billing/billing/history/fine_tuning | Retrieve Billing History of model evaluation for a specific Billing Cycle
[**get_fine_tuning_billing_history_graph**](BillingApi.md#get_fine_tuning_billing_history_graph) | **GET** /billing/billing/history/fine_tuning/{resource_id}/graph | Retrieve hourly cost datapoints of a Specific Fine Tuning for a specific billing cycle
[**get_last_day_cost**](BillingApi.md#get_last_day_cost) | **GET** /billing/billing/last-day-cost | GET: Last Day Cost
[**get_model_evaluation_billing_history**](BillingApi.md#get_model_evaluation_billing_history) | **GET** /billing/billing/history/model_evaluation | Retrieve Billing History of model evaluation for a specific Billing Cycle
[**get_model_evaluation_billing_history_graph**](BillingApi.md#get_model_evaluation_billing_history_graph) | **GET** /billing/billing/history/model_evaluation/{resource_id}/graph | Retrieve hourly cost datapoints of a Specific Model Evaluation for a specific
[**get_notification_threshold**](BillingApi.md#get_notification_threshold) | **PUT** /billing/billing/threshold/{threshold_id} | Update: Subscribe or Unsubscribe Notification Threshold
[**get_resource_fine_tuning_billing_history**](BillingApi.md#get_resource_fine_tuning_billing_history) | **GET** /billing/billing/history/fine_tuning/{resource_id} | Retrieve Billing History of a Specific Fine Tuning for a specific Billing Cycle
[**get_resource_model_evaluation_billing_history**](BillingApi.md#get_resource_model_evaluation_billing_history) | **GET** /billing/billing/history/model_evaluation/{resource_id} | 
[**get_serverless_inference_billing_history_graph**](BillingApi.md#get_serverless_inference_billing_history_graph) | **GET** /billing/billing/history/serverless_inference/{resource_id}/graph | Retrieve hourly cost datapoints of a Specific Serverless Inference for a specific
[**get_serverless_inferences_billing_history**](BillingApi.md#get_serverless_inferences_billing_history) | **GET** /billing/billing/history/serverless_inference/{resource_id} | 
[**get_snapshot_billing_history**](BillingApi.md#get_snapshot_billing_history) | **GET** /billing/billing/history/snapshot/{snapshot_id} | Retrieve Billing History of a Specific Snapshot for a specific Billing Cycle
[**get_snapshot_billing_history_graph**](BillingApi.md#get_snapshot_billing_history_graph) | **GET** /billing/billing/history/snapshot/{snapshot_id}/graph | Retrieve hourly cost datapoints of a Specific Snapshot for a specific billing cycle
[**get_usage**](BillingApi.md#get_usage) | **GET** /billing/billing/usage | GET: Billing usage
[**get_user_billing_history**](BillingApi.md#get_user_billing_history) | **GET** /billing/billing/history | Retrieve Billing History for a specific Billing Cycle
[**get_vm_billing_details**](BillingApi.md#get_vm_billing_details) | **GET** /billing/billing/history/virtual-machine/{vm_id} | Retrieve Billing History of a Specific Virtual Machine for a specific Billing Cycle
[**get_vm_billing_events**](BillingApi.md#get_vm_billing_events) | **GET** /billing/billing/virtual-machine/{vm_id}/billing-events | Retrieve VM billing events history
[**get_vm_billing_graph**](BillingApi.md#get_vm_billing_graph) | **GET** /billing/billing/history/virtual-machine/{vm_id}/graph | Retrieve hourly cost datapoints of a Specific Virtual Machine for a specific billing cycle
[**get_vm_billing_history**](BillingApi.md#get_vm_billing_history) | **GET** /billing/billing/history/virtual-machine | Retrieve Billing History of Virtual Machine for a specific Billing Cycle
[**get_vm_sub_resource_costs**](BillingApi.md#get_vm_sub_resource_costs) | **GET** /billing/billing/virtual-machine/{vm_id}/sub-resource | Retrieve Total Costs and Non Discount Costs for Sub Resources
[**get_vm_sub_resource_graph**](BillingApi.md#get_vm_sub_resource_graph) | **GET** /billing/billing/virtual-machine/{vm_id}/sub-resource/graph | Retrieve Sub-Resources Historical Cost datapoints of a Virtual
[**get_volume_billing_details**](BillingApi.md#get_volume_billing_details) | **GET** /billing/billing/history/volume/{volume_id} | Retrieve Billing History of a Specific Volume for a specific Billing Cycle
[**get_volume_billing_events**](BillingApi.md#get_volume_billing_events) | **GET** /billing/billing/volume/{volume_id}/billing-events | Retrieve Volume billing events history
[**get_volume_billing_history**](BillingApi.md#get_volume_billing_history) | **GET** /billing/billing/history/volume | Retrieve Billing History of Volume for a specific Billing Cycle
[**get_volume_billing_history_graph**](BillingApi.md#get_volume_billing_history_graph) | **GET** /billing/billing/history/volume/{volume_id}/graph | Retrieve hourly cost datapoints of a Specific Volume for a specific billing cycle
[**list_billing_contract_history**](BillingApi.md#list_billing_contract_history) | **GET** /billing/billing/history/contract | Retrieve Billing History of Contract for a specific Billing Cycle
[**list_bucket_billing_history**](BillingApi.md#list_bucket_billing_history) | **GET** /billing/billing/history/bucket | Retrieve Billing History of a Bucket for a specific Billing Cycle
[**list_clusters_billing_history**](BillingApi.md#list_clusters_billing_history) | **GET** /billing/billing/history/cluster | Retrieve Billing History of Clusters for a specific Billing Cycle
[**list_org_notification_thresholds**](BillingApi.md#list_org_notification_thresholds) | **GET** /billing/billing/threshold | GET: All Thresholds for Organization
[**list_serverless_inference_billing_history**](BillingApi.md#list_serverless_inference_billing_history) | **GET** /billing/billing/history/serverless_inference | Retrieve Billing History of serverless inference for a specific Billing Cycle
[**list_snapshot_billing_history**](BillingApi.md#list_snapshot_billing_history) | **GET** /billing/billing/history/snapshot | Retrieve Billing History of Snapshot for a specific Billing Cycle


# **buckets_billing_history_hourly_chart**
> ResourceLevelGraphBillingDetailsBucket buckets_billing_history_hourly_chart(bucket_id, start_date=start_date, end_date=end_date)

Retrieve hourly cost datapoints of a Specific Bucket for a specific billing cycle

User will receive hourly cost datapoints for a Bucket for a specified billing cycle. This data will include 'incurred_bill' graph datapoints.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_graph_billing_details_bucket import ResourceLevelGraphBillingDetailsBucket
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
    api_instance = hyperstack.BillingApi(api_client)
    bucket_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve hourly cost datapoints of a Specific Bucket for a specific billing cycle
        api_response = api_instance.buckets_billing_history_hourly_chart(bucket_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->buckets_billing_history_hourly_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->buckets_billing_history_hourly_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceLevelGraphBillingDetailsBucket**](ResourceLevelGraphBillingDetailsBucket.md)

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

# **get_bucket_billing_history**
> ResourceLevelBucketBillingDetailsResponseModel get_bucket_billing_history(bucket_id, start_date=start_date, end_date=end_date)

Retrieve Billing History of a Specific Snapshot for a specific Billing Cycle

Retrieve billing history of a specific Bucket for the specified billing cycle. This data will include 'resource_name', 'infrahub_id', 'price_per_hour', 'incurred_bill', 'usage_time', 'non_discounted_price_per_hour', 'non_discounted_bill'.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_bucket_billing_details_response_model import ResourceLevelBucketBillingDetailsResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    bucket_id = 56 # int | 
    start_date = 'start_date_example' # str | Datetime should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Datetime should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Billing History of a Specific Snapshot for a specific Billing Cycle
        api_response = api_instance.get_bucket_billing_history(bucket_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_bucket_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_bucket_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**|  | 
 **start_date** | **str**| Datetime should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Datetime should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceLevelBucketBillingDetailsResponseModel**](ResourceLevelBucketBillingDetailsResponseModel.md)

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

# **get_cluster_billing_history**
> ResourceLevelClusterBillingDetailsResponseModel get_cluster_billing_history(cluster_id, start_date=start_date, end_date=end_date)

Retrieve Billing History of a Specific Cluster for a specific Billing Cycle

User will receive billing history of a specific Cluster for the specified billing cycle. This data will include 'resource_name', 'infrahub_id', 'price_per_hour', 'non_discounted_price_per_hour', 'incurred_bill', 'non_discounted_bill', 'usage_time', 'usage_time_ACTIVE', 'usage_time_SHUTOFF', 'usage_time_HIBERNATED'.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_cluster_billing_details_response_model import ResourceLevelClusterBillingDetailsResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    cluster_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Billing History of a Specific Cluster for a specific Billing Cycle
        api_response = api_instance.get_cluster_billing_history(cluster_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_cluster_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_cluster_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceLevelClusterBillingDetailsResponseModel**](ResourceLevelClusterBillingDetailsResponseModel.md)

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

# **get_cluster_billing_history_graph**
> ResourceLevelClusterGraphBillingDetailsResponseModel get_cluster_billing_history_graph(cluster_id, start_date=start_date, end_date=end_date)

Retrieve hourly cost datapoints of a specific Cluster for a specific billing cycle

User will receive hourly cost datapoints for a Cluster for a specified billing cycle. This data will include 'incurred_bill' graph datapoints.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_cluster_graph_billing_details_response_model import ResourceLevelClusterGraphBillingDetailsResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    cluster_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve hourly cost datapoints of a specific Cluster for a specific billing cycle
        api_response = api_instance.get_cluster_billing_history_graph(cluster_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_cluster_billing_history_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_cluster_billing_history_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceLevelClusterGraphBillingDetailsResponseModel**](ResourceLevelClusterGraphBillingDetailsResponseModel.md)

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

# **get_data_synthesis_billing_history**
> TokenBasedBillingHistoryResponse get_data_synthesis_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)

Retrieve Billing History of data synthesis for a specific Billing Cycle

User will receive billing history of data_synthesis for the specified billing cycle.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.token_based_billing_history_response import TokenBasedBillingHistoryResponse
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
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by resource \"Name\" or \"ID\" (optional)
    per_page = 56 # int | Number of items to return per page (optional)
    page = 56 # int | Page number (optional)

    try:
        # Retrieve Billing History of data synthesis for a specific Billing Cycle
        api_response = api_instance.get_data_synthesis_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)
        print("The response of BillingApi->get_data_synthesis_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_data_synthesis_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **search** | **str**| Search by resource \&quot;Name\&quot; or \&quot;ID\&quot; | [optional] 
 **per_page** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**TokenBasedBillingHistoryResponse**](TokenBasedBillingHistoryResponse.md)

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

# **get_data_synthesis_billing_history_graph**
> DataSynthesisBillingHistoryDetailsResponseSchema get_data_synthesis_billing_history_graph(resource_id, start_date=start_date, end_date=end_date)

Retrieve hourly cost datapoints of a Specific Data Synthesis for a specific

User will receive hourly cost datapoints for a data synthesis job for a specified billing cycle. This data will include 'incurred_bill' graph datapoints. billing cycle

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.data_synthesis_billing_history_details_response_schema import DataSynthesisBillingHistoryDetailsResponseSchema
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
    api_instance = hyperstack.BillingApi(api_client)
    resource_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve hourly cost datapoints of a Specific Data Synthesis for a specific
        api_response = api_instance.get_data_synthesis_billing_history_graph(resource_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_data_synthesis_billing_history_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_data_synthesis_billing_history_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**DataSynthesisBillingHistoryDetailsResponseSchema**](DataSynthesisBillingHistoryDetailsResponseSchema.md)

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

# **get_data_synthesis_history_for_resource**
> DataSynthesisBillingHistoryDetailsResponseSchema get_data_synthesis_history_for_resource(resource_id, start_date=start_date, end_date=end_date)



Retrieve billing history for a specific Data Synthesis resource. Includes: 'resource_name', 'infrahub_id', 'base_model', 'base_model_display_name', 'lora_adapter', 'incurred_bill', 'non_discounted_bill', 'usage_time', 'input_tokens', 'output_tokens', 'input_tokens_incurred_bill', 'input_tokens_non_discounted_bill', 'output_tokens_incurred_bill', 'output_tokens_non_discounted_bill'

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.data_synthesis_billing_history_details_response_schema import DataSynthesisBillingHistoryDetailsResponseSchema
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
    api_instance = hyperstack.BillingApi(api_client)
    resource_id = 56 # int | 
    start_date = 'start_date_example' # str | YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | YYYY-MM-DDTHH:MM:SS (optional)

    try:
        api_response = api_instance.get_data_synthesis_history_for_resource(resource_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_data_synthesis_history_for_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_data_synthesis_history_for_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 
 **start_date** | **str**| YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**DataSynthesisBillingHistoryDetailsResponseSchema**](DataSynthesisBillingHistoryDetailsResponseSchema.md)

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

# **get_fine_tuning_billing_history**
> WorkloadBillingHistoryResponse get_fine_tuning_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)

Retrieve Billing History of model evaluation for a specific Billing Cycle

User will receive billing history of fine_tuning for the specified billing cycle.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.workload_billing_history_response import WorkloadBillingHistoryResponse
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
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by resource \"Name\" or \"ID\" (optional)
    per_page = 56 # int | Number of items to return per page (optional)
    page = 56 # int | Page number (optional)

    try:
        # Retrieve Billing History of model evaluation for a specific Billing Cycle
        api_response = api_instance.get_fine_tuning_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)
        print("The response of BillingApi->get_fine_tuning_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_fine_tuning_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **search** | **str**| Search by resource \&quot;Name\&quot; or \&quot;ID\&quot; | [optional] 
 **per_page** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**WorkloadBillingHistoryResponse**](WorkloadBillingHistoryResponse.md)

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

# **get_fine_tuning_billing_history_graph**
> ResourceLevelVolumeGraphBillingDetailsResponseModel get_fine_tuning_billing_history_graph(resource_id, start_date=start_date, end_date=end_date)

Retrieve hourly cost datapoints of a Specific Fine Tuning for a specific billing cycle

User will receive hourly cost datapoints for a Fine Tunings for a specified billing cycle. This data will include 'incurred_bill' graph datapoints.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_volume_graph_billing_details_response_model import ResourceLevelVolumeGraphBillingDetailsResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    resource_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve hourly cost datapoints of a Specific Fine Tuning for a specific billing cycle
        api_response = api_instance.get_fine_tuning_billing_history_graph(resource_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_fine_tuning_billing_history_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_fine_tuning_billing_history_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceLevelVolumeGraphBillingDetailsResponseModel**](ResourceLevelVolumeGraphBillingDetailsResponseModel.md)

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

# **get_last_day_cost**
> LastDayCostResponse get_last_day_cost()

GET: Last Day Cost

Retrieve the previous day's costs for instances, volumes, and clusters. Returns a breakdown of  the costs and the total cost for the last day. For additional information on Retrieve Previous Day Usage Costs, [**click here**](None/docs/api-reference/billing-resources/last-day-usage/)

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.last_day_cost_response import LastDayCostResponse
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
    api_instance = hyperstack.BillingApi(api_client)

    try:
        # GET: Last Day Cost
        api_response = api_instance.get_last_day_cost()
        print("The response of BillingApi->get_last_day_cost:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_last_day_cost: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LastDayCostResponse**](LastDayCostResponse.md)

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

# **get_model_evaluation_billing_history**
> TokenBasedBillingHistoryResponse get_model_evaluation_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)

Retrieve Billing History of model evaluation for a specific Billing Cycle

User will receive billing history of model_evaluation for the specified billing cycle.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.token_based_billing_history_response import TokenBasedBillingHistoryResponse
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
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by resource \"Name\" or \"ID\" (optional)
    per_page = 56 # int | Number of items to return per page (optional)
    page = 56 # int | Page number (optional)

    try:
        # Retrieve Billing History of model evaluation for a specific Billing Cycle
        api_response = api_instance.get_model_evaluation_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)
        print("The response of BillingApi->get_model_evaluation_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_model_evaluation_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **search** | **str**| Search by resource \&quot;Name\&quot; or \&quot;ID\&quot; | [optional] 
 **per_page** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**TokenBasedBillingHistoryResponse**](TokenBasedBillingHistoryResponse.md)

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

# **get_model_evaluation_billing_history_graph**
> ModelEvaluationBillingHistoryDetailsResponseSchema get_model_evaluation_billing_history_graph(resource_id, start_date=start_date, end_date=end_date)

Retrieve hourly cost datapoints of a Specific Model Evaluation for a specific

User will receive hourly cost datapoints for a model evaluation for a specified billing cycle. This data will include 'incurred_bill' graph datapoints. billing cycle

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.model_evaluation_billing_history_details_response_schema import ModelEvaluationBillingHistoryDetailsResponseSchema
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
    api_instance = hyperstack.BillingApi(api_client)
    resource_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve hourly cost datapoints of a Specific Model Evaluation for a specific
        api_response = api_instance.get_model_evaluation_billing_history_graph(resource_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_model_evaluation_billing_history_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_model_evaluation_billing_history_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ModelEvaluationBillingHistoryDetailsResponseSchema**](ModelEvaluationBillingHistoryDetailsResponseSchema.md)

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

# **get_notification_threshold**
> OrganizationThresholdUpdateResponse get_notification_threshold(threshold_id, payload)

Update: Subscribe or Unsubscribe Notification Threshold

By default, you are subscribed to all the threshold values and you will be receiving the email notification for these default thresholds values. `false` indicates that the user will no longer receive notifications for this specific threshold, whereas `true` signifies that the user will receive notification emails.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.organization_threshold_update_response import OrganizationThresholdUpdateResponse
from hyperstack.models.subscribe_or_unsubscribe_update_payload import SubscribeOrUnsubscribeUpdatePayload
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
    api_instance = hyperstack.BillingApi(api_client)
    threshold_id = 56 # int | 
    payload = hyperstack.SubscribeOrUnsubscribeUpdatePayload() # SubscribeOrUnsubscribeUpdatePayload | 

    try:
        # Update: Subscribe or Unsubscribe Notification Threshold
        api_response = api_instance.get_notification_threshold(threshold_id, payload)
        print("The response of BillingApi->get_notification_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_notification_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threshold_id** | **int**|  | 
 **payload** | [**SubscribeOrUnsubscribeUpdatePayload**](SubscribeOrUnsubscribeUpdatePayload.md)|  | 

### Return type

[**OrganizationThresholdUpdateResponse**](OrganizationThresholdUpdateResponse.md)

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

# **get_resource_fine_tuning_billing_history**
> ResourceLevelVolumeBillingDetailsResponseModel get_resource_fine_tuning_billing_history(resource_id, start_date=start_date, end_date=end_date)

Retrieve Billing History of a Specific Fine Tuning for a specific Billing Cycle

Retrieve billing history of a specific Fine tuning for the specified billing cycle. This data will include 'resource_name', 'infrahub_id', 'price_per_hour', 'incurred_bill', 'usage_time', 'non_discounted_price_per_hour', 'non_discounted_bill'.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_volume_billing_details_response_model import ResourceLevelVolumeBillingDetailsResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    resource_id = 56 # int | 
    start_date = 'start_date_example' # str | Datetime should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Datetime should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Billing History of a Specific Fine Tuning for a specific Billing Cycle
        api_response = api_instance.get_resource_fine_tuning_billing_history(resource_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_resource_fine_tuning_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_resource_fine_tuning_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 
 **start_date** | **str**| Datetime should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Datetime should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceLevelVolumeBillingDetailsResponseModel**](ResourceLevelVolumeBillingDetailsResponseModel.md)

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

# **get_resource_model_evaluation_billing_history**
> ModelEvaluationBillingHistoryDetailsResponseSchema get_resource_model_evaluation_billing_history(resource_id, start_date=start_date, end_date=end_date)



Retrieve billing history for a specific Model Evaluation resource. Includes: 'resource_name', 'infrahub_id', 'base_model', 'base_model_display_name', 'lora_adapter', 'incurred_bill', 'non_discounted_bill', 'usage_time', 'input_tokens', 'output_tokens', 'input_tokens_incurred_bill', 'input_tokens_non_discounted_bill', 'output_tokens_incurred_bill', 'output_tokens_non_discounted_bill'

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.model_evaluation_billing_history_details_response_schema import ModelEvaluationBillingHistoryDetailsResponseSchema
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
    api_instance = hyperstack.BillingApi(api_client)
    resource_id = 56 # int | 
    start_date = 'start_date_example' # str | YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | YYYY-MM-DDTHH:MM:SS (optional)

    try:
        api_response = api_instance.get_resource_model_evaluation_billing_history(resource_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_resource_model_evaluation_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_resource_model_evaluation_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 
 **start_date** | **str**| YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ModelEvaluationBillingHistoryDetailsResponseSchema**](ModelEvaluationBillingHistoryDetailsResponseSchema.md)

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

# **get_serverless_inference_billing_history_graph**
> ServerlessInferencedBillingHistoryDetailsResponseSchema get_serverless_inference_billing_history_graph(resource_id, start_date=start_date, end_date=end_date)

Retrieve hourly cost datapoints of a Specific Serverless Inference for a specific

User will receive hourly cost datapoints for a serverless inference for a specified billing cycle. This data will include 'incurred_bill' graph datapoints. billing cycle

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.serverless_inferenced_billing_history_details_response_schema import ServerlessInferencedBillingHistoryDetailsResponseSchema
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
    api_instance = hyperstack.BillingApi(api_client)
    resource_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve hourly cost datapoints of a Specific Serverless Inference for a specific
        api_response = api_instance.get_serverless_inference_billing_history_graph(resource_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_serverless_inference_billing_history_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_serverless_inference_billing_history_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ServerlessInferencedBillingHistoryDetailsResponseSchema**](ServerlessInferencedBillingHistoryDetailsResponseSchema.md)

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

# **get_serverless_inferences_billing_history**
> ServerlessInferencedBillingHistoryDetailsResponseSchema get_serverless_inferences_billing_history(resource_id, start_date=start_date, end_date=end_date)



Retrieve billing history for a specific Serverless Inference resource. Includes: 'resource_name', 'infrahub_id', 'base_model', 'base_model_display_name', 'lora_adapter', 'incurred_bill', 'non_discounted_bill', 'usage_time', 'input_tokens', 'output_tokens', 'input_tokens_incurred_bill', 'input_tokens_non_discounted_bill', 'output_tokens_incurred_bill', 'output_tokens_non_discounted_bill'

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.serverless_inferenced_billing_history_details_response_schema import ServerlessInferencedBillingHistoryDetailsResponseSchema
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
    api_instance = hyperstack.BillingApi(api_client)
    resource_id = 56 # int | 
    start_date = 'start_date_example' # str | YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | YYYY-MM-DDTHH:MM:SS (optional)

    try:
        api_response = api_instance.get_serverless_inferences_billing_history(resource_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_serverless_inferences_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_serverless_inferences_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 
 **start_date** | **str**| YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ServerlessInferencedBillingHistoryDetailsResponseSchema**](ServerlessInferencedBillingHistoryDetailsResponseSchema.md)

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

# **get_snapshot_billing_history**
> ResourceLevelVolumeBillingDetailsResponseModel get_snapshot_billing_history(snapshot_id, start_date=start_date, end_date=end_date)

Retrieve Billing History of a Specific Snapshot for a specific Billing Cycle

Retrieve billing history of a specific Snapshot for the specified billing cycle. This data will include 'resource_name', 'infrahub_id', 'price_per_hour', 'incurred_bill', 'usage_time', 'non_discounted_price_per_hour', 'non_discounted_bill'.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_volume_billing_details_response_model import ResourceLevelVolumeBillingDetailsResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    snapshot_id = 56 # int | 
    start_date = 'start_date_example' # str | Datetime should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Datetime should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Billing History of a Specific Snapshot for a specific Billing Cycle
        api_response = api_instance.get_snapshot_billing_history(snapshot_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_snapshot_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_snapshot_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **int**|  | 
 **start_date** | **str**| Datetime should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Datetime should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceLevelVolumeBillingDetailsResponseModel**](ResourceLevelVolumeBillingDetailsResponseModel.md)

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

# **get_snapshot_billing_history_graph**
> ResourceLevelVolumeGraphBillingDetailsResponseModel get_snapshot_billing_history_graph(snapshot_id, start_date=start_date, end_date=end_date)

Retrieve hourly cost datapoints of a Specific Snapshot for a specific billing cycle

User will receive hourly cost datapoints for a Snapshot for a specified billing cycle. This data will include 'incurred_bill' graph datapoints.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_volume_graph_billing_details_response_model import ResourceLevelVolumeGraphBillingDetailsResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    snapshot_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve hourly cost datapoints of a Specific Snapshot for a specific billing cycle
        api_response = api_instance.get_snapshot_billing_history_graph(snapshot_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_snapshot_billing_history_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_snapshot_billing_history_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceLevelVolumeGraphBillingDetailsResponseModel**](ResourceLevelVolumeGraphBillingDetailsResponseModel.md)

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

# **get_usage**
> BillingMetricesResponse get_usage(deleted=deleted, environment=environment)

GET: Billing usage

Retrieve active billing metrics for the organization's resources, including pricing, uptime, and total cost. Returns usage details for each active resource by defualt(`deleted=false` will return active resources). Additionally, adding `deleted=true` in query parameter will return inactive resources. For additional information on view usage costs for all resources, [**click here**](None/docs/billing/pricebook/)

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.billing_metrices_response import BillingMetricesResponse
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
    api_instance = hyperstack.BillingApi(api_client)
    deleted = 'deleted_example' # str | `true` will return inactive resources and `false` will return active resources. By defualt(`deleted=false`) (optional)
    environment = 'environment_example' # str | Filter resources by environment ID or Name (optional)

    try:
        # GET: Billing usage
        api_response = api_instance.get_usage(deleted=deleted, environment=environment)
        print("The response of BillingApi->get_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deleted** | **str**| &#x60;true&#x60; will return inactive resources and &#x60;false&#x60; will return active resources. By defualt(&#x60;deleted&#x3D;false&#x60;) | [optional] 
 **environment** | **str**| Filter resources by environment ID or Name | [optional] 

### Return type

[**BillingMetricesResponse**](BillingMetricesResponse.md)

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

# **get_user_billing_history**
> OrganizationLevelBillingHistoryResponseModel get_user_billing_history(start_date=start_date, end_date=end_date, graph=graph)

Retrieve Billing History for a specific Billing Cycle

User will receive billing history for the specified billing cycle. This data will include 'incurred_bill', 'non_discounted_bill', 'vm_cost', 'volume_cost'

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.organization_level_billing_history_response_model import OrganizationLevelBillingHistoryResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    graph = 'graph_example' # str | Set this value to \"true\" for getting graph value (optional)

    try:
        # Retrieve Billing History for a specific Billing Cycle
        api_response = api_instance.get_user_billing_history(start_date=start_date, end_date=end_date, graph=graph)
        print("The response of BillingApi->get_user_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_user_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **graph** | **str**| Set this value to \&quot;true\&quot; for getting graph value | [optional] 

### Return type

[**OrganizationLevelBillingHistoryResponseModel**](OrganizationLevelBillingHistoryResponseModel.md)

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

# **get_vm_billing_details**
> ResourceLevelVMBillingDetailsResponseModel get_vm_billing_details(vm_id, start_date=start_date, end_date=end_date)

Retrieve Billing History of a Specific Virtual Machine for a specific Billing Cycle

User will receive billing history of a specific Virtual Machine for the specified billing cycle. This data will include 'resource_name', 'infrahub_id', 'price_per_hour', 'non_discounted_price_per_hour', 'incurred_bill', 'non_discounted_bill', 'usage_time', 'usage_time_ACTIVE', 'usage_time_SHUTOFF', 'usage_time_HIBERNATED'

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_vm_billing_details_response_model import ResourceLevelVMBillingDetailsResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    vm_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Billing History of a Specific Virtual Machine for a specific Billing Cycle
        api_response = api_instance.get_vm_billing_details(vm_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_vm_billing_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_vm_billing_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceLevelVMBillingDetailsResponseModel**](ResourceLevelVMBillingDetailsResponseModel.md)

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

# **get_vm_billing_events**
> ResourceBillingEventsHistoryResponse get_vm_billing_events(vm_id, start_date=start_date, end_date=end_date)

Retrieve VM billing events history

User will receive vm billing events history

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_billing_events_history_response import ResourceBillingEventsHistoryResponse
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
    api_instance = hyperstack.BillingApi(api_client)
    vm_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve VM billing events history
        api_response = api_instance.get_vm_billing_events(vm_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_vm_billing_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_vm_billing_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceBillingEventsHistoryResponse**](ResourceBillingEventsHistoryResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vm_billing_graph**
> ResourceLevelVmGraphBillingDetailsResponseModel get_vm_billing_graph(vm_id, start_date=start_date, end_date=end_date)

Retrieve hourly cost datapoints of a Specific Virtual Machine for a specific billing cycle

User will receive hourly cost datapoints for a VM for a specified billing cycle. This data will include 'incurred_bill' graph datapoints.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_vm_graph_billing_details_response_model import ResourceLevelVmGraphBillingDetailsResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    vm_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve hourly cost datapoints of a Specific Virtual Machine for a specific billing cycle
        api_response = api_instance.get_vm_billing_graph(vm_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_vm_billing_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_vm_billing_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceLevelVmGraphBillingDetailsResponseModel**](ResourceLevelVmGraphBillingDetailsResponseModel.md)

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

# **get_vm_billing_history**
> ResourceLevelVmBillingHistoryResponseModel get_vm_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)

Retrieve Billing History of Virtual Machine for a specific Billing Cycle

User will receive billing history of virtual machine for the specified billing cycle. This data will include 'resource_name', 'infrahub_id', 'status', 'incurred_bill', 'usage_time', 'price_per_hour'

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_vm_billing_history_response_model import ResourceLevelVmBillingHistoryResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by resource \"Name\" or \"ID\" (optional)
    per_page = 56 # int | Number of items to return per page (optional)
    page = 56 # int | Page number (optional)

    try:
        # Retrieve Billing History of Virtual Machine for a specific Billing Cycle
        api_response = api_instance.get_vm_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)
        print("The response of BillingApi->get_vm_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_vm_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **search** | **str**| Search by resource \&quot;Name\&quot; or \&quot;ID\&quot; | [optional] 
 **per_page** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**ResourceLevelVmBillingHistoryResponseModel**](ResourceLevelVmBillingHistoryResponseModel.md)

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

# **get_vm_sub_resource_costs**
> SubResourcesCostsResponseModel get_vm_sub_resource_costs(vm_id, start_date=start_date, end_date=end_date)

Retrieve Total Costs and Non Discount Costs for Sub Resources

User will get total costs and non_discount costs of sub resources on a specific Virtual Machine for the specified billing cycle. on a Specific VM for the Specified Billing Cycle

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.sub_resources_costs_response_model import SubResourcesCostsResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    vm_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Total Costs and Non Discount Costs for Sub Resources
        api_response = api_instance.get_vm_sub_resource_costs(vm_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_vm_sub_resource_costs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_vm_sub_resource_costs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**SubResourcesCostsResponseModel**](SubResourcesCostsResponseModel.md)

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

# **get_vm_sub_resource_graph**
> SubResourcesGraphResponseModel get_vm_sub_resource_graph(vm_id, start_date=start_date, end_date=end_date)

Retrieve Sub-Resources Historical Cost datapoints of a Virtual

User will receive sub-resources historical cost datapoints for a VM sub resources for a specified billing cycle. This data will include 'incurred_bill' graph datapoints. Machine sub resources for a specific billing cycle

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.sub_resources_graph_response_model import SubResourcesGraphResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    vm_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Sub-Resources Historical Cost datapoints of a Virtual
        api_response = api_instance.get_vm_sub_resource_graph(vm_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_vm_sub_resource_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_vm_sub_resource_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**SubResourcesGraphResponseModel**](SubResourcesGraphResponseModel.md)

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

# **get_volume_billing_details**
> ResourceLevelVolumeBillingDetailsResponseModel get_volume_billing_details(volume_id, start_date=start_date, end_date=end_date)

Retrieve Billing History of a Specific Volume for a specific Billing Cycle

Retrieve billing history of a specific Volume for the specified billing cycle. This data will include 'resource_name', 'infrahub_id', 'price_per_hour', 'incurred_bill', 'usage_time', 'non_discounted_price_per_hour', 'non_discounted_bill'.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_volume_billing_details_response_model import ResourceLevelVolumeBillingDetailsResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    volume_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Billing History of a Specific Volume for a specific Billing Cycle
        api_response = api_instance.get_volume_billing_details(volume_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_volume_billing_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_volume_billing_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceLevelVolumeBillingDetailsResponseModel**](ResourceLevelVolumeBillingDetailsResponseModel.md)

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

# **get_volume_billing_events**
> ResourceBillingEventsHistoryResponse get_volume_billing_events(volume_id, start_date=start_date, end_date=end_date)

Retrieve Volume billing events history

User will receive volume billing events history

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_billing_events_history_response import ResourceBillingEventsHistoryResponse
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
    api_instance = hyperstack.BillingApi(api_client)
    volume_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Volume billing events history
        api_response = api_instance.get_volume_billing_events(volume_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_volume_billing_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_volume_billing_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceBillingEventsHistoryResponse**](ResourceBillingEventsHistoryResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volume_billing_history**
> ResourceLevelVolumeBillingHistoryResponseModel get_volume_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)

Retrieve Billing History of Volume for a specific Billing Cycle

User will receive billing history of volumes for thespecified billing cycle. This data will include 'resource_name', 'infrahub_id', 'status', 'incurred_bill', 'usage_time', 'price_per_hour'

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_volume_billing_history_response_model import ResourceLevelVolumeBillingHistoryResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by resource \"Name\" or \"ID\" (optional)
    per_page = 56 # int | Number of items to return per page (optional)
    page = 56 # int | Page number (optional)

    try:
        # Retrieve Billing History of Volume for a specific Billing Cycle
        api_response = api_instance.get_volume_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)
        print("The response of BillingApi->get_volume_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_volume_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **search** | **str**| Search by resource \&quot;Name\&quot; or \&quot;ID\&quot; | [optional] 
 **per_page** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**ResourceLevelVolumeBillingHistoryResponseModel**](ResourceLevelVolumeBillingHistoryResponseModel.md)

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

# **get_volume_billing_history_graph**
> ResourceLevelVolumeGraphBillingDetailsResponseModel get_volume_billing_history_graph(volume_id, start_date=start_date, end_date=end_date)

Retrieve hourly cost datapoints of a Specific Volume for a specific billing cycle

User will receive hourly cost datapoints for a Volume for a specified billing cycle. This data will include 'incurred_bill' graph datapoints.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_volume_graph_billing_details_response_model import ResourceLevelVolumeGraphBillingDetailsResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    volume_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve hourly cost datapoints of a Specific Volume for a specific billing cycle
        api_response = api_instance.get_volume_billing_history_graph(volume_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_volume_billing_history_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_volume_billing_history_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ResourceLevelVolumeGraphBillingDetailsResponseModel**](ResourceLevelVolumeGraphBillingDetailsResponseModel.md)

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

# **list_billing_contract_history**
> list_billing_contract_history(start_date=start_date, end_date=end_date, search=search)

Retrieve Billing History of Contract for a specific Billing Cycle

User will receive billing history of contracts for the specified billing cycle. This data will include 'description', gpu_type','infrahub_id', 'status', 'incurred_bill', 'price_per_hour'

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
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
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by Contract \"Description\" or \"ID\" (optional)

    try:
        # Retrieve Billing History of Contract for a specific Billing Cycle
        api_instance.list_billing_contract_history(start_date=start_date, end_date=end_date, search=search)
    except Exception as e:
        print("Exception when calling BillingApi->list_billing_contract_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **search** | **str**| Search by Contract \&quot;Description\&quot; or \&quot;ID\&quot; | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bucket_billing_history**
> ResourceLevelBucketBillingHistoryResponseModel list_bucket_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)

Retrieve Billing History of a Bucket for a specific Billing Cycle

User will receive billing history of buckets for thespecified billing cycle. This data will include 'resource_name', 'infrahub_id', 'status', 'incurred_bill', 'usage_time', 'price_per_hour'

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_bucket_billing_history_response_model import ResourceLevelBucketBillingHistoryResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by resource \"Name\" or \"ID\" (optional)
    per_page = 56 # int | Number of items to return per page (optional)
    page = 56 # int | Page number (optional)

    try:
        # Retrieve Billing History of a Bucket for a specific Billing Cycle
        api_response = api_instance.list_bucket_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)
        print("The response of BillingApi->list_bucket_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_bucket_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **search** | **str**| Search by resource \&quot;Name\&quot; or \&quot;ID\&quot; | [optional] 
 **per_page** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**ResourceLevelBucketBillingHistoryResponseModel**](ResourceLevelBucketBillingHistoryResponseModel.md)

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

# **list_clusters_billing_history**
> ResourceLevelClusterBillingHistoryResponseModel list_clusters_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)

Retrieve Billing History of Clusters for a specific Billing Cycle

User will receive billing history of clusters for the specified billing cycle. This data will include 'resource_name', 'infrahub_id', 'status', 'incurred_bill', 'usage_time', 'price_per_hour'

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_cluster_billing_history_response_model import ResourceLevelClusterBillingHistoryResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by resource \"Name\" or \"ID\" (optional)
    per_page = 56 # int | Number of items to return per page (optional)
    page = 56 # int | Page number (optional)

    try:
        # Retrieve Billing History of Clusters for a specific Billing Cycle
        api_response = api_instance.list_clusters_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)
        print("The response of BillingApi->list_clusters_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_clusters_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **search** | **str**| Search by resource \&quot;Name\&quot; or \&quot;ID\&quot; | [optional] 
 **per_page** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**ResourceLevelClusterBillingHistoryResponseModel**](ResourceLevelClusterBillingHistoryResponseModel.md)

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

# **list_org_notification_thresholds**
> OrganizationThresholdsResponse list_org_notification_thresholds()

GET: All Thresholds for Organization

Retrieve all the notification thresholds for an organization.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.organization_thresholds_response import OrganizationThresholdsResponse
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
    api_instance = hyperstack.BillingApi(api_client)

    try:
        # GET: All Thresholds for Organization
        api_response = api_instance.list_org_notification_thresholds()
        print("The response of BillingApi->list_org_notification_thresholds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_org_notification_thresholds: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrganizationThresholdsResponse**](OrganizationThresholdsResponse.md)

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

# **list_serverless_inference_billing_history**
> TokenBasedBillingHistoryResponse list_serverless_inference_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)

Retrieve Billing History of serverless inference for a specific Billing Cycle

User will receive billing history of serverless_inference for the specified billing cycle.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.token_based_billing_history_response import TokenBasedBillingHistoryResponse
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
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by resource \"Name\" or \"ID\" (optional)
    per_page = 56 # int | Number of items to return per page (optional)
    page = 56 # int | Page number (optional)

    try:
        # Retrieve Billing History of serverless inference for a specific Billing Cycle
        api_response = api_instance.list_serverless_inference_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)
        print("The response of BillingApi->list_serverless_inference_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_serverless_inference_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **search** | **str**| Search by resource \&quot;Name\&quot; or \&quot;ID\&quot; | [optional] 
 **per_page** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**TokenBasedBillingHistoryResponse**](TokenBasedBillingHistoryResponse.md)

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

# **list_snapshot_billing_history**
> ResourceLevelVolumeBillingHistoryResponseModel list_snapshot_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)

Retrieve Billing History of Snapshot for a specific Billing Cycle

User will receive billing history of snapshots for thespecified billing cycle. This data will include 'resource_name', 'infrahub_id', 'status', 'incurred_bill', 'usage_time', 'price_per_hour'

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.resource_level_volume_billing_history_response_model import ResourceLevelVolumeBillingHistoryResponseModel
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
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by resource \"Name\" or \"ID\" (optional)
    per_page = 56 # int | Number of items to return per page (optional)
    page = 56 # int | Page number (optional)

    try:
        # Retrieve Billing History of Snapshot for a specific Billing Cycle
        api_response = api_instance.list_snapshot_billing_history(start_date=start_date, end_date=end_date, search=search, per_page=per_page, page=page)
        print("The response of BillingApi->list_snapshot_billing_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_snapshot_billing_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **search** | **str**| Search by resource \&quot;Name\&quot; or \&quot;ID\&quot; | [optional] 
 **per_page** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**ResourceLevelVolumeBillingHistoryResponseModel**](ResourceLevelVolumeBillingHistoryResponseModel.md)

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

