# hyperstack.CustomerContractApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_contract**](CustomerContractApi.md#get_customer_contract) | **GET** /pricebook/contracts | List Contracts
[**get_customer_contract_details**](CustomerContractApi.md#get_customer_contract_details) | **GET** /pricebook/contracts/{contract_id} | Retrieve Contract Details
[**get_customer_contract_gpu_allocation_graph**](CustomerContractApi.md#get_customer_contract_gpu_allocation_graph) | **GET** /pricebook/contracts/{contract_id}/gpu_allocation_graph | Retrieve GPU Allocation Graph for Contract


# **get_customer_contract**
> GetCustomerContractsListResponseModel get_customer_contract(page=page, per_page=per_page)

List Contracts

Retrieves a list of contracts and their details, including the terms of each contract and the discounts applied to all resources under each contract. Pagination can be controlled using the `page` and `per_page` query parameters. For additional information about contracts, click [**here**](None/docs/billing-and-payment/contracts).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.get_customer_contracts_list_response_model import GetCustomerContractsListResponseModel
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
    api_instance = hyperstack.CustomerContractApi(api_client)
    page = 56 # int |  (optional)
    per_page = 56 # int |  (optional)

    try:
        # List Contracts
        api_response = api_instance.get_customer_contract(page=page, per_page=per_page)
        print("The response of CustomerContractApi->get_customer_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerContractApi->get_customer_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**GetCustomerContractsListResponseModel**](GetCustomerContractsListResponseModel.md)

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
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_contract_details**
> CustomerContractDetailResponseModel get_customer_contract_details(contract_id)

Retrieve Contract Details

Retrieve details of a specific contract by providing the contract ID in the path. The endpoint returns the contract object along with its associated discount plans. For more information, [**click here**](None/docs/api-reference/pricebook-resources/retrieve-contract-details).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.customer_contract_detail_response_model import CustomerContractDetailResponseModel
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
    api_instance = hyperstack.CustomerContractApi(api_client)
    contract_id = 56 # int | 

    try:
        # Retrieve Contract Details
        api_response = api_instance.get_customer_contract_details(contract_id)
        print("The response of CustomerContractApi->get_customer_contract_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerContractApi->get_customer_contract_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**|  | 

### Return type

[**CustomerContractDetailResponseModel**](CustomerContractDetailResponseModel.md)

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
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_contract_gpu_allocation_graph**
> ContractGPUAllocationGraphResponse get_customer_contract_gpu_allocation_graph(contract_id, start_date=start_date, end_date=end_date)

Retrieve GPU Allocation Graph for Contract

Retrieve GPU allocation count graph for a specific contract by providing the contract ID in the path. The endpoint returns the GPU allocation count graph for the contract within the specified date range.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.contract_gpu_allocation_graph_response import ContractGPUAllocationGraphResponse
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
    api_instance = hyperstack.CustomerContractApi(api_client)
    contract_id = 56 # int | 
    start_date = 'start_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)
    end_date = 'end_date_example' # str | Date should be formatted in YYYY-MM-DDTHH:MM:SS (optional)

    try:
        # Retrieve GPU Allocation Graph for Contract
        api_response = api_instance.get_customer_contract_gpu_allocation_graph(contract_id, start_date=start_date, end_date=end_date)
        print("The response of CustomerContractApi->get_customer_contract_gpu_allocation_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerContractApi->get_customer_contract_gpu_allocation_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**|  | 
 **start_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 
 **end_date** | **str**| Date should be formatted in YYYY-MM-DDTHH:MM:SS | [optional] 

### Return type

[**ContractGPUAllocationGraphResponse**](ContractGPUAllocationGraphResponse.md)

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
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

