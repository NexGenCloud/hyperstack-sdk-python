# hyperstack.BillingApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_thresholds_for_organization**](BillingApi.md#get_all_thresholds_for_organization) | **GET** /billing/billing/threshold | GET: All Thresholds for Organization
[**get_billing_usage**](BillingApi.md#get_billing_usage) | **GET** /billing/billing/usage | GET: Billing usage
[**get_last_day_cost**](BillingApi.md#get_last_day_cost) | **GET** /billing/billing/last-day-cost | GET: Last Day Cost
[**retrieve_billing_history_for_a_specific_billing_cycle**](BillingApi.md#retrieve_billing_history_for_a_specific_billing_cycle) | **GET** /billing/billing/history | Retrieve Billing History for a specific Billing Cycle
[**retrieve_billing_history_of_a_specific_virtual_machine_for_a_specific_billing_cycle**](BillingApi.md#retrieve_billing_history_of_a_specific_virtual_machine_for_a_specific_billing_cycle) | **GET** /billing/billing/history/virtual-machine/{vm_id} | Retrieve Billing History of a Specific Virtual Machine for a specific Billing Cycle
[**retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle**](BillingApi.md#retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle) | **GET** /billing/billing/history/snapshot/{snapshot_id} | Retrieve Billing History of a Specific Volume for a specific Billing Cycle
[**retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle_0**](BillingApi.md#retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle_0) | **GET** /billing/billing/history/volume/{volume_id} | Retrieve Billing History of a Specific Volume for a specific Billing Cycle
[**retrieve_billing_history_of_contract_for_a_specific_billing_cycle**](BillingApi.md#retrieve_billing_history_of_contract_for_a_specific_billing_cycle) | **GET** /billing/billing/history/contract | Retrieve Billing History of Contract for a specific Billing Cycle
[**retrieve_billing_history_of_snapshot_for_a_specific_billing_cycle**](BillingApi.md#retrieve_billing_history_of_snapshot_for_a_specific_billing_cycle) | **GET** /billing/billing/history/snapshot | Retrieve Billing History of Snapshot for a specific Billing Cycle
[**retrieve_billing_history_of_virtual_machine_for_a_specific_billing_cycle**](BillingApi.md#retrieve_billing_history_of_virtual_machine_for_a_specific_billing_cycle) | **GET** /billing/billing/history/virtual-machine | Retrieve Billing History of Virtual Machine for a specific Billing Cycle
[**retrieve_billing_history_of_volume_for_a_specific_billing_cycle**](BillingApi.md#retrieve_billing_history_of_volume_for_a_specific_billing_cycle) | **GET** /billing/billing/history/volume | Retrieve Billing History of Volume for a specific Billing Cycle
[**retrieve_hourly_cost_datapoints_of_a_specific_snapshot_for_a_specific_billing_cycle**](BillingApi.md#retrieve_hourly_cost_datapoints_of_a_specific_snapshot_for_a_specific_billing_cycle) | **GET** /billing/billing/history/snapshot/{snapshot_id}/graph | Retrieve hourly cost datapoints of a Specific Snapshot for a specific billing cycle
[**retrieve_hourly_cost_datapoints_of_a_specific_virtual_machine_for_a_specific_billing_cycle**](BillingApi.md#retrieve_hourly_cost_datapoints_of_a_specific_virtual_machine_for_a_specific_billing_cycle) | **GET** /billing/billing/history/virtual-machine/{vm_id}/graph | Retrieve hourly cost datapoints of a Specific Virtual Machine for a specific billing cycle
[**retrieve_hourly_cost_datapoints_of_a_specific_volume_for_a_specific_billing_cycle**](BillingApi.md#retrieve_hourly_cost_datapoints_of_a_specific_volume_for_a_specific_billing_cycle) | **GET** /billing/billing/history/volume/{volume_id}/graph | Retrieve hourly cost datapoints of a Specific Volume for a specific billing cycle
[**retrieve_sub_resources_historical_cost_datapoints_of_a_virtual**](BillingApi.md#retrieve_sub_resources_historical_cost_datapoints_of_a_virtual) | **GET** /billing/billing/virtual-machine/{vm_id}/sub-resource/graph | Retrieve Sub-Resources Historical Cost datapoints of a Virtual
[**retrieve_total_costs_and_non_discount_costs_for_sub_resources**](BillingApi.md#retrieve_total_costs_and_non_discount_costs_for_sub_resources) | **GET** /billing/billing/virtual-machine/{vm_id}/sub-resource | Retrieve Total Costs and Non Discount Costs for Sub Resources
[**retrieve_vm_billing_events_history**](BillingApi.md#retrieve_vm_billing_events_history) | **GET** /billing/billing/virtual-machine/{vm_id}/billing-events | Retrieve VM billing events history
[**retrieve_volume_billing_events_history**](BillingApi.md#retrieve_volume_billing_events_history) | **GET** /billing/billing/volume/{volume_id}/billing-events | Retrieve Volume billing events history
[**update_subscribe_or_unsubscribe_notification_threshold**](BillingApi.md#update_subscribe_or_unsubscribe_notification_threshold) | **PUT** /billing/billing/threshold/{threshold_id} | Update: Subscribe or Unsubscribe Notification Threshold


# **get_all_thresholds_for_organization**
> Organizationthresholdsresponse get_all_thresholds_for_organization()

GET: All Thresholds for Organization

Retrieve all the notification thresholds for an organization.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.organizationthresholdsresponse import Organizationthresholdsresponse
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
    api_instance = hyperstack.BillingApi(api_client)

    try:
        # GET: All Thresholds for Organization
        api_response = api_instance.get_all_thresholds_for_organization()
        print("The response of BillingApi->get_all_thresholds_for_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_all_thresholds_for_organization: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Organizationthresholdsresponse**](Organizationthresholdsresponse.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_usage**
> Billingmetricesresponse get_billing_usage(deleted=deleted, environment=environment)

GET: Billing usage

Retrieve active billing metrics for the organization's resources, including pricing, uptime, and total cost. Returns usage details for each active resource by defualt(`deleted=false` will return active resources). Additionally, adding `deleted=true` in query parameter will return inactive resources. For additional information on view usage costs for all resources, [**click here**](https://infrahub-doc.nexgencloud.com/docs/billing-and-payment/billing-features#view-usage-costs-for-all-resources)

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.billingmetricesresponse import Billingmetricesresponse
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
    api_instance = hyperstack.BillingApi(api_client)
    deleted = 'deleted_example' # str | `true` will return inactive resources and `false` will return active resources. By defualt(`deleted=false`) (optional)
    environment = 'environment_example' # str | Filter resources by environment ID or Name (optional)

    try:
        # GET: Billing usage
        api_response = api_instance.get_billing_usage(deleted=deleted, environment=environment)
        print("The response of BillingApi->get_billing_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_billing_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deleted** | **str**| &#x60;true&#x60; will return inactive resources and &#x60;false&#x60; will return active resources. By defualt(&#x60;deleted&#x3D;false&#x60;) | [optional] 
 **environment** | **str**| Filter resources by environment ID or Name | [optional] 

### Return type

[**Billingmetricesresponse**](Billingmetricesresponse.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_day_cost**
> Lastdaycostresponse get_last_day_cost()

GET: Last Day Cost

Retrieve the previous day's costs for instances, volumes, and clusters. Returns a breakdown of the costs and the total cost for the last day. For additional information on Retrieve Previous Day Usage Costs, [**click here**](https://infrahub-doc.nexgencloud.com/docs/api-reference/billing-resources/last-day-usage/)

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.lastdaycostresponse import Lastdaycostresponse
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

[**Lastdaycostresponse**](Lastdaycostresponse.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_billing_history_for_a_specific_billing_cycle**
> OrganizationLevelBillingHistoryResponseModel retrieve_billing_history_for_a_specific_billing_cycle(start_date=start_date, end_date=end_date, graph=graph)

Retrieve Billing History for a specific Billing Cycle

User will recieve billing history for the specified billing cycle. This data will include 'incurred_bill', 'non_discounted_bill', 'vm_cost', 'volume_cost'

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    graph = 'graph_example' # str | Set this value to \"true\" for getting graph value (optional)

    try:
        # Retrieve Billing History for a specific Billing Cycle
        api_response = api_instance.retrieve_billing_history_for_a_specific_billing_cycle(start_date=start_date, end_date=end_date, graph=graph)
        print("The response of BillingApi->retrieve_billing_history_for_a_specific_billing_cycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_billing_history_for_a_specific_billing_cycle: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_billing_history_of_a_specific_virtual_machine_for_a_specific_billing_cycle**
> ResourceLevelVMBillingDetailsResponseModel retrieve_billing_history_of_a_specific_virtual_machine_for_a_specific_billing_cycle(vm_id, start_date=start_date, end_date=end_date)

Retrieve Billing History of a Specific Virtual Machine for a specific Billing Cycle

User will recieve billing history of a specific Virtual Machine for the specified billing cycle. This data will include 'resource_name', 'infrahub_id', 'price_per_hour', 'non_discounted_price_per_hour', 'incurred_bill', 'non_discounted_bill', 'usage_time', 'usage_time_ACTIVE', 'usage_time_SHUTOFF', 'usage_time_HIBERNATED'

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    vm_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Billing History of a Specific Virtual Machine for a specific Billing Cycle
        api_response = api_instance.retrieve_billing_history_of_a_specific_virtual_machine_for_a_specific_billing_cycle(vm_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->retrieve_billing_history_of_a_specific_virtual_machine_for_a_specific_billing_cycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_billing_history_of_a_specific_virtual_machine_for_a_specific_billing_cycle: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle**
> ResourceLevelVolumeBillingDetailsResponseModel retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle(snapshot_id, start_date=start_date, end_date=end_date)

Retrieve Billing History of a Specific Volume for a specific Billing Cycle

Retrieve billing history of a specific Snapshot for the specified billing cycle. This data will include 'resource_name', 'infrahub_id', 'price_per_hour', 'incurred_bill', 'usage_time', 'non_discounted_price_per_hour', 'non_discounted_bill'.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    snapshot_id = 56 # int | 
    start_date = 'start_date_example' # str | Datetime should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Datetime should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Billing History of a Specific Volume for a specific Billing Cycle
        api_response = api_instance.retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle(snapshot_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle_0**
> ResourceLevelVolumeBillingDetailsResponseModel retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle_0(volume_id, start_date=start_date, end_date=end_date)

Retrieve Billing History of a Specific Volume for a specific Billing Cycle

Retrieve billing history of a specific Volume for the specified billing cycle. This data will include 'resource_name', 'infrahub_id', 'price_per_hour', 'incurred_bill', 'usage_time', 'non_discounted_price_per_hour', 'non_discounted_bill'.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    volume_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Billing History of a Specific Volume for a specific Billing Cycle
        api_response = api_instance.retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle_0(volume_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle_0: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_billing_history_of_contract_for_a_specific_billing_cycle**
> retrieve_billing_history_of_contract_for_a_specific_billing_cycle(start_date=start_date, end_date=end_date, search=search)

Retrieve Billing History of Contract for a specific Billing Cycle

User will recieve billing history of contracts for the specified billing cycle. This data will include 'description', gpu_type','infrahub_id', 'status', 'incurred_bill', 'price_per_hour'

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by Contract \"Description\" or \"ID\" (optional)

    try:
        # Retrieve Billing History of Contract for a specific Billing Cycle
        api_instance.retrieve_billing_history_of_contract_for_a_specific_billing_cycle(start_date=start_date, end_date=end_date, search=search)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_billing_history_of_contract_for_a_specific_billing_cycle: %s\n" % e)
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

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **retrieve_billing_history_of_snapshot_for_a_specific_billing_cycle**
> ResourceLevelVolumeBillingHistoryResponseModel retrieve_billing_history_of_snapshot_for_a_specific_billing_cycle(start_date=start_date, end_date=end_date, search=search)

Retrieve Billing History of Snapshot for a specific Billing Cycle

User will recieve billing history of snapshots for thespecified billing cycle. This data will include 'resource_name', 'infrahub_id', 'status', 'incurred_bill', 'usage_time', 'price_per_hour'

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by Volume \"Name\" or \"ID\" (optional)

    try:
        # Retrieve Billing History of Snapshot for a specific Billing Cycle
        api_response = api_instance.retrieve_billing_history_of_snapshot_for_a_specific_billing_cycle(start_date=start_date, end_date=end_date, search=search)
        print("The response of BillingApi->retrieve_billing_history_of_snapshot_for_a_specific_billing_cycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_billing_history_of_snapshot_for_a_specific_billing_cycle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **search** | **str**| Search by Volume \&quot;Name\&quot; or \&quot;ID\&quot; | [optional] 

### Return type

[**ResourceLevelVolumeBillingHistoryResponseModel**](ResourceLevelVolumeBillingHistoryResponseModel.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_billing_history_of_virtual_machine_for_a_specific_billing_cycle**
> ResourceLevelVmBillingHistoryResponseModel retrieve_billing_history_of_virtual_machine_for_a_specific_billing_cycle(start_date=start_date, end_date=end_date, search=search)

Retrieve Billing History of Virtual Machine for a specific Billing Cycle

User will recieve billing history of virtual machine for the specified billing cycle. This data will include 'resource_name', 'infrahub_id', 'status', 'incurred_bill', 'usage_time', 'price_per_hour'

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by Virtual Machine \"Name\" or \"ID\" (optional)

    try:
        # Retrieve Billing History of Virtual Machine for a specific Billing Cycle
        api_response = api_instance.retrieve_billing_history_of_virtual_machine_for_a_specific_billing_cycle(start_date=start_date, end_date=end_date, search=search)
        print("The response of BillingApi->retrieve_billing_history_of_virtual_machine_for_a_specific_billing_cycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_billing_history_of_virtual_machine_for_a_specific_billing_cycle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **search** | **str**| Search by Virtual Machine \&quot;Name\&quot; or \&quot;ID\&quot; | [optional] 

### Return type

[**ResourceLevelVmBillingHistoryResponseModel**](ResourceLevelVmBillingHistoryResponseModel.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_billing_history_of_volume_for_a_specific_billing_cycle**
> ResourceLevelVolumeBillingHistoryResponseModel retrieve_billing_history_of_volume_for_a_specific_billing_cycle(start_date=start_date, end_date=end_date, search=search)

Retrieve Billing History of Volume for a specific Billing Cycle

User will recieve billing history of volumes for thespecified billing cycle. This data will include 'resource_name', 'infrahub_id', 'status', 'incurred_bill', 'usage_time', 'price_per_hour'

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    search = 'search_example' # str | Search by Volume \"Name\" or \"ID\" (optional)

    try:
        # Retrieve Billing History of Volume for a specific Billing Cycle
        api_response = api_instance.retrieve_billing_history_of_volume_for_a_specific_billing_cycle(start_date=start_date, end_date=end_date, search=search)
        print("The response of BillingApi->retrieve_billing_history_of_volume_for_a_specific_billing_cycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_billing_history_of_volume_for_a_specific_billing_cycle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **search** | **str**| Search by Volume \&quot;Name\&quot; or \&quot;ID\&quot; | [optional] 

### Return type

[**ResourceLevelVolumeBillingHistoryResponseModel**](ResourceLevelVolumeBillingHistoryResponseModel.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_hourly_cost_datapoints_of_a_specific_snapshot_for_a_specific_billing_cycle**
> ResourceLevelVolumeGraphBillingDetailsResponseModel retrieve_hourly_cost_datapoints_of_a_specific_snapshot_for_a_specific_billing_cycle(snapshot_id, start_date=start_date, end_date=end_date)

Retrieve hourly cost datapoints of a Specific Snapshot for a specific billing cycle

User will recieve hourly cost datapoints for a Snapshot for a specified billing cycle. This data will include 'incurred_bill' graph datapoints.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    snapshot_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve hourly cost datapoints of a Specific Snapshot for a specific billing cycle
        api_response = api_instance.retrieve_hourly_cost_datapoints_of_a_specific_snapshot_for_a_specific_billing_cycle(snapshot_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->retrieve_hourly_cost_datapoints_of_a_specific_snapshot_for_a_specific_billing_cycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_hourly_cost_datapoints_of_a_specific_snapshot_for_a_specific_billing_cycle: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_hourly_cost_datapoints_of_a_specific_virtual_machine_for_a_specific_billing_cycle**
> ResourceLevelVmGraphBillingDetailsResponseModel retrieve_hourly_cost_datapoints_of_a_specific_virtual_machine_for_a_specific_billing_cycle(vm_id, start_date=start_date, end_date=end_date)

Retrieve hourly cost datapoints of a Specific Virtual Machine for a specific billing cycle

User will recieve hourly cost datapoints for a VM for a specified billing cycle. This data will include 'incurred_bill' graph datapoints.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    vm_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve hourly cost datapoints of a Specific Virtual Machine for a specific billing cycle
        api_response = api_instance.retrieve_hourly_cost_datapoints_of_a_specific_virtual_machine_for_a_specific_billing_cycle(vm_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->retrieve_hourly_cost_datapoints_of_a_specific_virtual_machine_for_a_specific_billing_cycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_hourly_cost_datapoints_of_a_specific_virtual_machine_for_a_specific_billing_cycle: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_hourly_cost_datapoints_of_a_specific_volume_for_a_specific_billing_cycle**
> ResourceLevelVolumeGraphBillingDetailsResponseModel retrieve_hourly_cost_datapoints_of_a_specific_volume_for_a_specific_billing_cycle(volume_id, start_date=start_date, end_date=end_date)

Retrieve hourly cost datapoints of a Specific Volume for a specific billing cycle

User will recieve hourly cost datapoints for a Volume for a specified billing cycle. This data will include 'incurred_bill' graph datapoints.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    volume_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve hourly cost datapoints of a Specific Volume for a specific billing cycle
        api_response = api_instance.retrieve_hourly_cost_datapoints_of_a_specific_volume_for_a_specific_billing_cycle(volume_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->retrieve_hourly_cost_datapoints_of_a_specific_volume_for_a_specific_billing_cycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_hourly_cost_datapoints_of_a_specific_volume_for_a_specific_billing_cycle: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_sub_resources_historical_cost_datapoints_of_a_virtual**
> SubResourcesGraphResponseModel retrieve_sub_resources_historical_cost_datapoints_of_a_virtual(vm_id, start_date=start_date, end_date=end_date)

Retrieve Sub-Resources Historical Cost datapoints of a Virtual

User will recieve sub-resources historical cost datapoints for a VM sub resources for a specified billing cycle. This data will include 'incurred_bill' graph datapoints. Machine sub resources for a specific billing cycle

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    vm_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Sub-Resources Historical Cost datapoints of a Virtual
        api_response = api_instance.retrieve_sub_resources_historical_cost_datapoints_of_a_virtual(vm_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->retrieve_sub_resources_historical_cost_datapoints_of_a_virtual:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_sub_resources_historical_cost_datapoints_of_a_virtual: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_total_costs_and_non_discount_costs_for_sub_resources**
> SubResourcesCostsResponseModel retrieve_total_costs_and_non_discount_costs_for_sub_resources(vm_id, start_date=start_date, end_date=end_date)

Retrieve Total Costs and Non Discount Costs for Sub Resources

User will get total costs and non_discount costs of sub resources on a specific Virtual Machine for the specified billing cycle. on a Specific VM for the Specified Billing Cycle

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    vm_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Total Costs and Non Discount Costs for Sub Resources
        api_response = api_instance.retrieve_total_costs_and_non_discount_costs_for_sub_resources(vm_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->retrieve_total_costs_and_non_discount_costs_for_sub_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_total_costs_and_non_discount_costs_for_sub_resources: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_vm_billing_events_history**
> ResourceBillingEventsHistoryResponse retrieve_vm_billing_events_history(vm_id, start_date=start_date, end_date=end_date)

Retrieve VM billing events history

User will receive vm billing events history

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    vm_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve VM billing events history
        api_response = api_instance.retrieve_vm_billing_events_history(vm_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->retrieve_vm_billing_events_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_vm_billing_events_history: %s\n" % e)
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
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_volume_billing_events_history**
> ResourceBillingEventsHistoryResponse retrieve_volume_billing_events_history(volume_id, start_date=start_date, end_date=end_date)

Retrieve Volume billing events history

User will receive volume billing events history

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.BillingApi(api_client)
    volume_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve Volume billing events history
        api_response = api_instance.retrieve_volume_billing_events_history(volume_id, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->retrieve_volume_billing_events_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retrieve_volume_billing_events_history: %s\n" % e)
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
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscribe_or_unsubscribe_notification_threshold**
> Organizationthresholdupdateresponse update_subscribe_or_unsubscribe_notification_threshold(threshold_id, payload)

Update: Subscribe or Unsubscribe Notification Threshold

By default, you are subscribed to all the threshold values and you will be receiving the email notification for these default thresholds values. `false` indicates that the user will no longer receive notifications for this specific threshold, whereas `true` signifies that the user will receive notification emails.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.organizationthresholdupdateresponse import Organizationthresholdupdateresponse
from hyperstack.models.subscribeorunsubscribeupdatepayload import Subscribeorunsubscribeupdatepayload
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
    api_instance = hyperstack.BillingApi(api_client)
    threshold_id = 56 # int | 
    payload = hyperstack.Subscribeorunsubscribeupdatepayload() # Subscribeorunsubscribeupdatepayload | 

    try:
        # Update: Subscribe or Unsubscribe Notification Threshold
        api_response = api_instance.update_subscribe_or_unsubscribe_notification_threshold(threshold_id, payload)
        print("The response of BillingApi->update_subscribe_or_unsubscribe_notification_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->update_subscribe_or_unsubscribe_notification_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threshold_id** | **int**|  | 
 **payload** | [**Subscribeorunsubscribeupdatepayload**](Subscribeorunsubscribeupdatepayload.md)|  | 

### Return type

[**Organizationthresholdupdateresponse**](Organizationthresholdupdateresponse.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

