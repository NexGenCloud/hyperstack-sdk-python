# hyperstack.VirtualMachineApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_instance**](VirtualMachineApi.md#delete_instance) | **DELETE** /core/virtual-machines/{vm_id} | Delete virtual machine
[**delete_security_rule**](VirtualMachineApi.md#delete_security_rule) | **DELETE** /core/virtual-machines/{vm_id}/sg-rules/{sg_rule_id} | Delete firewall rule from virtual machine
[**fetch_virtual_machine_name_availability**](VirtualMachineApi.md#fetch_virtual_machine_name_availability) | **GET** /core/virtual-machines/name-availability/{name} | Fetch virtual machine name availability
[**get_contract_instances**](VirtualMachineApi.md#get_contract_instances) | **GET** /core/virtual-machines/contract/{contract_id}/virtual-machines | Retrieve virtual machines associated with a contract
[**get_instance**](VirtualMachineApi.md#get_instance) | **GET** /core/virtual-machines | List virtual machines
[**get_instance2**](VirtualMachineApi.md#get_instance2) | **GET** /core/virtual-machines/{vm_id} | Retrieve virtual machine details
[**get_instance3**](VirtualMachineApi.md#get_instance3) | **GET** /core/virtual-machines/{vm_id}/hard-reboot | Hard reboot virtual machine
[**get_instance4**](VirtualMachineApi.md#get_instance4) | **GET** /core/virtual-machines/{vm_id}/start | Start virtual machine
[**get_instance5**](VirtualMachineApi.md#get_instance5) | **GET** /core/virtual-machines/{vm_id}/stop | Stop virtual machine
[**get_instance_hibernate**](VirtualMachineApi.md#get_instance_hibernate) | **GET** /core/virtual-machines/{vm_id}/hibernate | Hibernate virtual machine
[**get_instance_hibernate_restore**](VirtualMachineApi.md#get_instance_hibernate_restore) | **GET** /core/virtual-machines/{vm_id}/hibernate-restore | Restore virtual machine from hibernation
[**get_instance_logs**](VirtualMachineApi.md#get_instance_logs) | **GET** /core/virtual-machines/{vm_id}/logs | Get virtual machine logs
[**get_instance_metrics**](VirtualMachineApi.md#get_instance_metrics) | **GET** /core/virtual-machines/{vm_id}/metrics | Retrieve virtual machine performance metrics
[**post_instance**](VirtualMachineApi.md#post_instance) | **POST** /core/virtual-machines | Create virtual machines
[**post_instance_attach_firewalls**](VirtualMachineApi.md#post_instance_attach_firewalls) | **POST** /core/virtual-machines/{vm_id}/attach-firewalls | Attach firewalls to a virtual machine
[**post_instance_logs**](VirtualMachineApi.md#post_instance_logs) | **POST** /core/virtual-machines/{vm_id}/logs | Request virtual machine logs
[**post_instance_resize**](VirtualMachineApi.md#post_instance_resize) | **POST** /core/virtual-machines/{vm_id}/resize | Resize virtual machine
[**post_security_rule**](VirtualMachineApi.md#post_security_rule) | **POST** /core/virtual-machines/{vm_id}/sg-rules | Add firewall rule to virtual machine
[**post_snapshots**](VirtualMachineApi.md#post_snapshots) | **POST** /core/virtual-machines/{vm_id}/snapshots | Create snapshot from a virtual machine
[**put_labels**](VirtualMachineApi.md#put_labels) | **PUT** /core/virtual-machines/{vm_id}/label | Edit virtual machine labels


# **delete_instance**
> ResponseModel delete_instance(vm_id)

Delete virtual machine

Permanently deletes a virtual machine. Provide the virtual machine ID in the path to delete the specified virtual machine.

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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 

    try:
        # Delete virtual machine
        api_response = api_instance.delete_instance(vm_id)
        print("The response of VirtualMachineApi->delete_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->delete_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 

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
**200** | Virtual machine deleted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_security_rule**
> ResponseModel delete_security_rule(vm_id, sg_rule_id)

Delete firewall rule from virtual machine

Deletes a firewall rule associated with a virtual machine. Provide the virtual machine ID and the firewall rule ID in the path to remove the specified rule from the specified virtual machine.

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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 
    sg_rule_id = 56 # int | 

    try:
        # Delete firewall rule from virtual machine
        api_response = api_instance.delete_security_rule(vm_id, sg_rule_id)
        print("The response of VirtualMachineApi->delete_security_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->delete_security_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **sg_rule_id** | **int**|  | 

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
**200** | The firewall rule has been successfully removed from the virtual machine. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_virtual_machine_name_availability**
> NameAvailableModel fetch_virtual_machine_name_availability(name)

Fetch virtual machine name availability

Check if a Virtual Machine name is available

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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    name = 'name_example' # str | 

    try:
        # Fetch virtual machine name availability
        api_response = api_instance.fetch_virtual_machine_name_availability(name)
        print("The response of VirtualMachineApi->fetch_virtual_machine_name_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->fetch_virtual_machine_name_availability: %s\n" % e)
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

# **get_contract_instances**
> ContractInstancesResponse get_contract_instances(contract_id, page=page, page_size=page_size, search=search)

Retrieve virtual machines associated with a contract

Retrieves a list of virtual machines associated with a contract, providing details such as virtual machine name, timestamp, flavor name, and other relevant information. Please provide the ID of the relevant contract in the path.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.contract_instances_response import ContractInstancesResponse
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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    contract_id = 56 # int | 
    page = 'page_example' # str | Page Number (optional)
    page_size = 'page_size_example' # str | Data Per Page (optional)
    search = 'search_example' # str | Search By Instance ID or Name (optional)

    try:
        # Retrieve virtual machines associated with a contract
        api_response = api_instance.get_contract_instances(contract_id, page=page, page_size=page_size, search=search)
        print("The response of VirtualMachineApi->get_contract_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->get_contract_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**|  | 
 **page** | **str**| Page Number | [optional] 
 **page_size** | **str**| Data Per Page | [optional] 
 **search** | **str**| Search By Instance ID or Name | [optional] 

### Return type

[**ContractInstancesResponse**](ContractInstancesResponse.md)

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

# **get_instance**
> Instances get_instance(page=page, page_size=page_size, search=search, environment=environment, exclude_firewalls=exclude_firewalls)

List virtual machines

Returns a list of your existing virtual machines, providing configuration details for each. The list is sorted by creation date, with the oldest virtual machines displayed first.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.instances import Instances
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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    environment = 'environment_example' # str |  (optional)
    exclude_firewalls = [56] # List[int] | Comma-separated list of Security Group IDs to ignore instances attached (optional)

    try:
        # List virtual machines
        api_response = api_instance.get_instance(page=page, page_size=page_size, search=search, environment=environment, exclude_firewalls=exclude_firewalls)
        print("The response of VirtualMachineApi->get_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->get_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **environment** | **str**|  | [optional] 
 **exclude_firewalls** | [**List[int]**](int.md)| Comma-separated list of Security Group IDs to ignore instances attached | [optional] 

### Return type

[**Instances**](Instances.md)

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

# **get_instance2**
> Instance get_instance2(vm_id)

Retrieve virtual machine details

Retrieves the details of an existing virtual machine. Provide the virtual machine ID in the path, and Infrahub will return information about the corresponding VM.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.instance import Instance
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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 

    try:
        # Retrieve virtual machine details
        api_response = api_instance.get_instance2(vm_id)
        print("The response of VirtualMachineApi->get_instance2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->get_instance2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 

### Return type

[**Instance**](Instance.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Virtual machine details retrieved successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance3**
> ResponseModel get_instance3(vm_id)

Hard reboot virtual machine

Initiates a hard reboot for a virtual machine, simulating the process of unplugging and rebooting a physical machine. Provide the virtual machine ID in the path to execute a hard reboot for the specified virtual machine.

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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 

    try:
        # Hard reboot virtual machine
        api_response = api_instance.get_instance3(vm_id)
        print("The response of VirtualMachineApi->get_instance3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->get_instance3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 

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
**200** | Hard reboot process has been successfully initiated. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance4**
> ResponseModel get_instance4(vm_id)

Start virtual machine

Initiates the startup of a virtual machine. Provide the virtual machine ID in the path to initiate the starting of the specified virtual machine.

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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 

    try:
        # Start virtual machine
        api_response = api_instance.get_instance4(vm_id)
        print("The response of VirtualMachineApi->get_instance4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->get_instance4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 

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
**200** | Virtual machine started successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance5**
> ResponseModel get_instance5(vm_id)

Stop virtual machine

Shuts down a virtual machine. Provide the virtual machine ID in the path to initiate the shutdown process for the specified virtual machine.

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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 

    try:
        # Stop virtual machine
        api_response = api_instance.get_instance5(vm_id)
        print("The response of VirtualMachineApi->get_instance5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->get_instance5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 

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
**200** | Virtual machine shut down successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_hibernate**
> ResponseModel get_instance_hibernate(vm_id)

Hibernate virtual machine

Initiates the hibernation of a virtual machine, saving its current state to disk before powering off. Provide the virtual machine ID in the path to specify the virtual machine to be hibernated.

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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 

    try:
        # Hibernate virtual machine
        api_response = api_instance.get_instance_hibernate(vm_id)
        print("The response of VirtualMachineApi->get_instance_hibernate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->get_instance_hibernate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 

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
**200** | Hibernation request for the virtual machine was successful. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_hibernate_restore**
> ResponseModel get_instance_hibernate_restore(vm_id)

Restore virtual machine from hibernation

Resumes a virtual machine from hibernation, bringing it back to an active state. Provide the virtual machine ID in the path to specify the virtual machine to be restored from hibernation.

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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 

    try:
        # Restore virtual machine from hibernation
        api_response = api_instance.get_instance_hibernate_restore(vm_id)
        print("The response of VirtualMachineApi->get_instance_hibernate_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->get_instance_hibernate_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 

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
**200** | The request to restore the virtual machine from hibernation was successful. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_logs**
> GetInstanceLogsResponse get_instance_logs(vm_id, request_id)

Get virtual machine logs

Retrieve console logs for a virtual machine

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.get_instance_logs_response import GetInstanceLogsResponse
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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 
    request_id = 56 # int | 

    try:
        # Get virtual machine logs
        api_response = api_instance.get_instance_logs(vm_id, request_id)
        print("The response of VirtualMachineApi->get_instance_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->get_instance_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **request_id** | **int**|  | 

### Return type

[**GetInstanceLogsResponse**](GetInstanceLogsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logs were successfully retrieved |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_metrics**
> MetricsFields get_instance_metrics(vm_id, duration=duration)

Retrieve virtual machine performance metrics

Retrieves performance metrics data for a virtual machine. Provide the virtual machine ID in the path to retrieve the following data for the specified virtual machine: CPU usage, memory usage (RAM), `network.in`, `network.out`, `disk.read`, and `disk.write`. The optional `duration` parameter can be used to specify the period for retrieving performance metrics; the default value will retrieve all available data. To learn more about virtual machine performance metrics, [**click here**](https://docs.hyperstack.cloud/docs/virtual-machines/vm-performance-metrics-and-events-history#performance-metrics).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.metrics_fields import MetricsFields
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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 
    duration = 'duration_example' # str |  (optional)

    try:
        # Retrieve virtual machine performance metrics
        api_response = api_instance.get_instance_metrics(vm_id, duration=duration)
        print("The response of VirtualMachineApi->get_instance_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->get_instance_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **duration** | **str**|  | [optional] 

### Return type

[**MetricsFields**](MetricsFields.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Virtual machine performance metrics have been successfully retrieved. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_instance**
> CreateInstancesResponse post_instance(payload)

Create virtual machines

Creates one or more virtual machines with the specified custom configuration and features provided in the request body. For more information about the virtual machine features offered by Infrahub, [**click here**](https://docs.hyperstack.cloud/docs/virtual-machines/virtual-machine-features#create-a-virtual-machine-with-custom-features).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.create_instances_payload import CreateInstancesPayload
from hyperstack.models.create_instances_response import CreateInstancesResponse
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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    payload = hyperstack.CreateInstancesPayload() # CreateInstancesPayload | 

    try:
        # Create virtual machines
        api_response = api_instance.post_instance(payload)
        print("The response of VirtualMachineApi->post_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->post_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateInstancesPayload**](CreateInstancesPayload.md)|  | 

### Return type

[**CreateInstancesResponse**](CreateInstancesResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Virtual machine(s) created successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_instance_attach_firewalls**
> ResponseModel post_instance_attach_firewalls(vm_id, payload)

Attach firewalls to a virtual machine

Attach firewalls to a virtual machine by providing the virtual machine ID in the path and the IDs of the firewalls in the request body; any firewalls not included will be detached.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.attach_firewalls_to_vm_payload import AttachFirewallsToVMPayload
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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 
    payload = hyperstack.AttachFirewallsToVMPayload() # AttachFirewallsToVMPayload | 

    try:
        # Attach firewalls to a virtual machine
        api_response = api_instance.post_instance_attach_firewalls(vm_id, payload)
        print("The response of VirtualMachineApi->post_instance_attach_firewalls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->post_instance_attach_firewalls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **payload** | [**AttachFirewallsToVMPayload**](AttachFirewallsToVMPayload.md)|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_instance_logs**
> RequestInstanceLogsResponse post_instance_logs(vm_id, payload)

Request virtual machine logs

Request console logs for a virtual machine

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.request_instance_logs_payload import RequestInstanceLogsPayload
from hyperstack.models.request_instance_logs_response import RequestInstanceLogsResponse
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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 
    payload = hyperstack.RequestInstanceLogsPayload() # RequestInstanceLogsPayload | 

    try:
        # Request virtual machine logs
        api_response = api_instance.post_instance_logs(vm_id, payload)
        print("The response of VirtualMachineApi->post_instance_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->post_instance_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **payload** | [**RequestInstanceLogsPayload**](RequestInstanceLogsPayload.md)|  | 

### Return type

[**RequestInstanceLogsResponse**](RequestInstanceLogsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logs were successfully requested |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_instance_resize**
> ResponseModel post_instance_resize(vm_id, payload)

Resize virtual machine

Updates the hardware configuration for an existing virtual machine. Include the virtual machine ID in the path and provide the new configuration, referred to as a `flavor`, in the body of the request. For additional information resizing, [**click here**](https://docs.hyperstack.cloud/docs/hardware/flavors#modify-the-flavor-of-an-existing-virtual-machine).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.instance_resize_payload import InstanceResizePayload
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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 
    payload = hyperstack.InstanceResizePayload() # InstanceResizePayload | 

    try:
        # Resize virtual machine
        api_response = api_instance.post_instance_resize(vm_id, payload)
        print("The response of VirtualMachineApi->post_instance_resize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->post_instance_resize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **payload** | [**InstanceResizePayload**](InstanceResizePayload.md)|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resizing of the virtual machine configuration was successful. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_security_rule**
> SecurityGroupRule post_security_rule(vm_id, payload)

Add firewall rule to virtual machine

Creates a firewall rule for a virtual machine. Include the virtual machine ID in the path, and provide the firewall rule configuration in the request body, as detailed below. For additional information on firewall rules, [**click here**](https://docs.hyperstack.cloud/docs/api-reference/core-resources/virtual-machines/vm-firewall-rules/add-firewall-rule-to-vm).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.create_security_rule_payload import CreateSecurityRulePayload
from hyperstack.models.security_group_rule import SecurityGroupRule
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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 
    payload = hyperstack.CreateSecurityRulePayload() # CreateSecurityRulePayload | 

    try:
        # Add firewall rule to virtual machine
        api_response = api_instance.post_security_rule(vm_id, payload)
        print("The response of VirtualMachineApi->post_security_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->post_security_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **payload** | [**CreateSecurityRulePayload**](CreateSecurityRulePayload.md)|  | 

### Return type

[**SecurityGroupRule**](SecurityGroupRule.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The firewall rule has been successfully added to the virtual machine. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_snapshots**
> CreateSnapshotResponse post_snapshots(vm_id, payload)

Create snapshot from a virtual machine

Create snapshots of a virtual machine by providing the virtual machine ID in the path

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.create_snapshot_payload import CreateSnapshotPayload
from hyperstack.models.create_snapshot_response import CreateSnapshotResponse
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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 
    payload = hyperstack.CreateSnapshotPayload() # CreateSnapshotPayload | 

    try:
        # Create snapshot from a virtual machine
        api_response = api_instance.post_snapshots(vm_id, payload)
        print("The response of VirtualMachineApi->post_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->post_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **payload** | [**CreateSnapshotPayload**](CreateSnapshotPayload.md)|  | 

### Return type

[**CreateSnapshotResponse**](CreateSnapshotResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_labels**
> ResponseModel put_labels(vm_id, payload)

Edit virtual machine labels

Adds one or more labels to an existing virtual machine. Provide the virtual machine ID in the path to add labels to the specified VM. For multiple labels, add a space between each label in the request body.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.edit_label_of_an_existing_vm_payload import EditLabelOfAnExistingVMPayload
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
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 
    payload = hyperstack.EditLabelOfAnExistingVMPayload() # EditLabelOfAnExistingVMPayload | 

    try:
        # Edit virtual machine labels
        api_response = api_instance.put_labels(vm_id, payload)
        print("The response of VirtualMachineApi->put_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->put_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **payload** | [**EditLabelOfAnExistingVMPayload**](EditLabelOfAnExistingVMPayload.md)|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Labels edited successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

