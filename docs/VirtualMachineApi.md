# hyperstack.VirtualMachineApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_firewall_rule_to_virtual_machine**](VirtualMachineApi.md#add_firewall_rule_to_virtual_machine) | **POST** /core/virtual-machines/{id}/sg-rules | Add firewall rule to virtual machine
[**attach_firewalls_to_a_virtual_machine**](VirtualMachineApi.md#attach_firewalls_to_a_virtual_machine) | **POST** /core/virtual-machines/{vm_id}/attach-firewalls | Attach firewalls to a virtual machine
[**create_snapshot_from_a_virtual_machine**](VirtualMachineApi.md#create_snapshot_from_a_virtual_machine) | **POST** /core/virtual-machines/{vm_id}/snapshots | Create snapshot from a virtual machine
[**create_virtual_machines**](VirtualMachineApi.md#create_virtual_machines) | **POST** /core/virtual-machines | Create virtual machines
[**delete_firewall_rule_from_virtual_machine**](VirtualMachineApi.md#delete_firewall_rule_from_virtual_machine) | **DELETE** /core/virtual-machines/{virtual_machine_id}/sg-rules/{sg_rule_id} | Delete firewall rule from virtual machine
[**delete_virtual_machine**](VirtualMachineApi.md#delete_virtual_machine) | **DELETE** /core/virtual-machines/{id} | Delete virtual machine
[**edit_virtual_machine_labels**](VirtualMachineApi.md#edit_virtual_machine_labels) | **PUT** /core/virtual-machines/{virtual_machine_id}/label | Edit virtual machine labels
[**fetch_virtual_machine_name_availability**](VirtualMachineApi.md#fetch_virtual_machine_name_availability) | **GET** /core/virtual-machines/name-availability/{name} | Fetch virtual machine name availability
[**hard_reboot_virtual_machine**](VirtualMachineApi.md#hard_reboot_virtual_machine) | **GET** /core/virtual-machines/{id}/hard-reboot | Hard reboot virtual machine
[**hibernate_virtual_machine**](VirtualMachineApi.md#hibernate_virtual_machine) | **GET** /core/virtual-machines/{virtual_machine_id}/hibernate | Hibernate virtual machine
[**list_virtual_machines**](VirtualMachineApi.md#list_virtual_machines) | **GET** /core/virtual-machines | List virtual machines
[**resize_virtual_machine**](VirtualMachineApi.md#resize_virtual_machine) | **POST** /core/virtual-machines/{virtual_machine_id}/resize | Resize virtual machine
[**restore_virtual_machine_from_hibernation**](VirtualMachineApi.md#restore_virtual_machine_from_hibernation) | **GET** /core/virtual-machines/{virtual_machine_id}/hibernate-restore | Restore virtual machine from hibernation
[**retrieve_virtual_machine_details**](VirtualMachineApi.md#retrieve_virtual_machine_details) | **GET** /core/virtual-machines/{id} | Retrieve virtual machine details
[**retrieve_virtual_machine_performance_metrics**](VirtualMachineApi.md#retrieve_virtual_machine_performance_metrics) | **GET** /core/virtual-machines/{virtual_machine_id}/metrics | Retrieve virtual machine performance metrics
[**retrieve_virtual_machines_associated_with_a_contract**](VirtualMachineApi.md#retrieve_virtual_machines_associated_with_a_contract) | **GET** /core/virtual-machines/contract/{contract_id}/virtual-machines | Retrieve virtual machines associated with a contract
[**start_virtual_machine**](VirtualMachineApi.md#start_virtual_machine) | **GET** /core/virtual-machines/{id}/start | Start virtual machine
[**stop_virtual_machine**](VirtualMachineApi.md#stop_virtual_machine) | **GET** /core/virtual-machines/{id}/stop | Stop virtual machine


# **add_firewall_rule_to_virtual_machine**
> SecurityGroupRule add_firewall_rule_to_virtual_machine(id, payload)

Add firewall rule to virtual machine

Creates a firewall rule for a virtual machine. Include the virtual machine ID in the path, and provide the firewall rule configuration in the request body, as detailed below. For additional information on firewall rules, [**click here**](https://infrahub-doc.nexgencloud.com/docs/api-reference/core-resources/virtual-machines/vm-firewall-rules/add-firewall-rule-to-vm).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    id = 56 # int | 
    payload = hyperstack.CreateSecurityRulePayload() # CreateSecurityRulePayload | 

    try:
        # Add firewall rule to virtual machine
        api_response = api_instance.add_firewall_rule_to_virtual_machine(id, payload)
        print("The response of VirtualMachineApi->add_firewall_rule_to_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->add_firewall_rule_to_virtual_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **payload** | [**CreateSecurityRulePayload**](CreateSecurityRulePayload.md)|  | 

### Return type

[**SecurityGroupRule**](SecurityGroupRule.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **attach_firewalls_to_a_virtual_machine**
> ResponseModel attach_firewalls_to_a_virtual_machine(vm_id, payload)

Attach firewalls to a virtual machine

Attach firewalls to a virtual machine by providing the virtual machine ID in the path and the IDs of the firewalls in the request body; any firewalls not included will be detached.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 
    payload = hyperstack.AttachFirewallsToVMPayload() # AttachFirewallsToVMPayload | 

    try:
        # Attach firewalls to a virtual machine
        api_response = api_instance.attach_firewalls_to_a_virtual_machine(vm_id, payload)
        print("The response of VirtualMachineApi->attach_firewalls_to_a_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->attach_firewalls_to_a_virtual_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **payload** | [**AttachFirewallsToVMPayload**](AttachFirewallsToVMPayload.md)|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot_from_a_virtual_machine**
> CreateSnapshotResponse create_snapshot_from_a_virtual_machine(vm_id, payload)

Create snapshot from a virtual machine

Create snapshots of a virtual machine by providing the virtual machine ID in the path

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    vm_id = 56 # int | 
    payload = hyperstack.CreateSnapshotPayload() # CreateSnapshotPayload | 

    try:
        # Create snapshot from a virtual machine
        api_response = api_instance.create_snapshot_from_a_virtual_machine(vm_id, payload)
        print("The response of VirtualMachineApi->create_snapshot_from_a_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->create_snapshot_from_a_virtual_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **int**|  | 
 **payload** | [**CreateSnapshotPayload**](CreateSnapshotPayload.md)|  | 

### Return type

[**CreateSnapshotResponse**](CreateSnapshotResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **create_virtual_machines**
> CreateInstancesResponse create_virtual_machines(payload)

Create virtual machines

Creates one or more virtual machines with the specified custom configuration and features provided in the request body. For more information about the virtual machine features offered by Infrahub, [**click here**](https://infrahub-doc.nexgencloud.com/docs/virtual-machines/virtual-machine-features#create-a-virtual-machine-with-custom-features).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    payload = hyperstack.CreateInstancesPayload() # CreateInstancesPayload | 

    try:
        # Create virtual machines
        api_response = api_instance.create_virtual_machines(payload)
        print("The response of VirtualMachineApi->create_virtual_machines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->create_virtual_machines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateInstancesPayload**](CreateInstancesPayload.md)|  | 

### Return type

[**CreateInstancesResponse**](CreateInstancesResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **delete_firewall_rule_from_virtual_machine**
> ResponseModel delete_firewall_rule_from_virtual_machine(virtual_machine_id, sg_rule_id)

Delete firewall rule from virtual machine

Deletes a firewall rule associated with a virtual machine. Provide the virtual machine ID and the firewall rule ID in the path to remove the specified rule from the specified virtual machine.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    virtual_machine_id = 56 # int | 
    sg_rule_id = 56 # int | 

    try:
        # Delete firewall rule from virtual machine
        api_response = api_instance.delete_firewall_rule_from_virtual_machine(virtual_machine_id, sg_rule_id)
        print("The response of VirtualMachineApi->delete_firewall_rule_from_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->delete_firewall_rule_from_virtual_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**|  | 
 **sg_rule_id** | **int**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **delete_virtual_machine**
> ResponseModel delete_virtual_machine(id)

Delete virtual machine

Permanently deletes a virtual machine. Provide the virtual machine ID in the path to delete the specified virtual machine.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    id = 56 # int | 

    try:
        # Delete virtual machine
        api_response = api_instance.delete_virtual_machine(id)
        print("The response of VirtualMachineApi->delete_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->delete_virtual_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **edit_virtual_machine_labels**
> ResponseModel edit_virtual_machine_labels(virtual_machine_id, payload)

Edit virtual machine labels

Adds one or more labels to an existing virtual machine. Provide the virtual machine ID in the path to add labels to the specified VM. For multiple labels, add a space between each label in the request body.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

```python
import hyperstack
from hyperstack.models.editlabelofanexisting_vm_payload import EditlabelofanexistingVMPayload
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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    virtual_machine_id = 56 # int | 
    payload = hyperstack.EditlabelofanexistingVMPayload() # EditlabelofanexistingVMPayload | 

    try:
        # Edit virtual machine labels
        api_response = api_instance.edit_virtual_machine_labels(virtual_machine_id, payload)
        print("The response of VirtualMachineApi->edit_virtual_machine_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->edit_virtual_machine_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**|  | 
 **payload** | [**EditlabelofanexistingVMPayload**](EditlabelofanexistingVMPayload.md)|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **fetch_virtual_machine_name_availability**
> NameAvailableModel fetch_virtual_machine_name_availability(name)

Fetch virtual machine name availability

Check if a Virtual Machine name is available

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hard_reboot_virtual_machine**
> ResponseModel hard_reboot_virtual_machine(id)

Hard reboot virtual machine

Initiates a hard reboot for a virtual machine, simulating the process of unplugging and rebooting a physical machine. Provide the virtual machine ID in the path to execute a hard reboot for the specified virtual machine.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    id = 56 # int | 

    try:
        # Hard reboot virtual machine
        api_response = api_instance.hard_reboot_virtual_machine(id)
        print("The response of VirtualMachineApi->hard_reboot_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->hard_reboot_virtual_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **hibernate_virtual_machine**
> ResponseModel hibernate_virtual_machine(virtual_machine_id)

Hibernate virtual machine

Initiates the hibernation of a virtual machine, saving its current state to disk before powering off. Provide the virtual machine ID in the path to specify the virtual machine to be hibernated.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    virtual_machine_id = 56 # int | 

    try:
        # Hibernate virtual machine
        api_response = api_instance.hibernate_virtual_machine(virtual_machine_id)
        print("The response of VirtualMachineApi->hibernate_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->hibernate_virtual_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **list_virtual_machines**
> Instances list_virtual_machines(page=page, page_size=page_size, search=search, environment=environment)

List virtual machines

Returns a list of your existing virtual machines, providing configuration details for each. The list is sorted by creation date, with the oldest virtual machines displayed first.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    page = 'page_example' # str | Page Number (optional)
    page_size = 'page_size_example' # str | Data Per Page (optional)
    search = 'search_example' # str |  (optional)
    environment = 'environment_example' # str | Filter Environment ID or Name (optional)

    try:
        # List virtual machines
        api_response = api_instance.list_virtual_machines(page=page, page_size=page_size, search=search, environment=environment)
        print("The response of VirtualMachineApi->list_virtual_machines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->list_virtual_machines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Page Number | [optional] 
 **page_size** | **str**| Data Per Page | [optional] 
 **search** | **str**|  | [optional] 
 **environment** | **str**| Filter Environment ID or Name | [optional] 

### Return type

[**Instances**](Instances.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resize_virtual_machine**
> ResponseModel resize_virtual_machine(virtual_machine_id, payload)

Resize virtual machine

Updates the hardware configuration for an existing virtual machine. Include the virtual machine ID in the path and provide the new configuration, referred to as a `flavor`, in the body of the request. For additional information resizing, [**click here**](https://infrahub-doc.nexgencloud.com/docs/hardware/flavors#modify-the-flavor-of-an-existing-virtual-machine).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    virtual_machine_id = 56 # int | 
    payload = hyperstack.InstanceResizePayload() # InstanceResizePayload | 

    try:
        # Resize virtual machine
        api_response = api_instance.resize_virtual_machine(virtual_machine_id, payload)
        print("The response of VirtualMachineApi->resize_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->resize_virtual_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**|  | 
 **payload** | [**InstanceResizePayload**](InstanceResizePayload.md)|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **restore_virtual_machine_from_hibernation**
> ResponseModel restore_virtual_machine_from_hibernation(virtual_machine_id)

Restore virtual machine from hibernation

Resumes a virtual machine from hibernation, bringing it back to an active state. Provide the virtual machine ID in the path to specify the virtual machine to be restored from hibernation.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    virtual_machine_id = 56 # int | 

    try:
        # Restore virtual machine from hibernation
        api_response = api_instance.restore_virtual_machine_from_hibernation(virtual_machine_id)
        print("The response of VirtualMachineApi->restore_virtual_machine_from_hibernation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->restore_virtual_machine_from_hibernation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **retrieve_virtual_machine_details**
> Instance retrieve_virtual_machine_details(id)

Retrieve virtual machine details

Retrieves the details of an existing virtual machine. Provide the virtual machine ID in the path, and Infrahub will return information about the corresponding VM.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve virtual machine details
        api_response = api_instance.retrieve_virtual_machine_details(id)
        print("The response of VirtualMachineApi->retrieve_virtual_machine_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->retrieve_virtual_machine_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Instance**](Instance.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **retrieve_virtual_machine_performance_metrics**
> MetricsFields retrieve_virtual_machine_performance_metrics(virtual_machine_id, duration=duration)

Retrieve virtual machine performance metrics

Retrieves performance metrics data for a virtual machine. Provide the virtual machine ID in the path to retrieve the following data for the specified virtual machine: CPU usage, memory usage (RAM), `network.in`, `network.out`, `disk.read`, and `disk.write`. The optional `duration` parameter can be used to specify the period for retrieving performance metrics; the default value will retrieve all available data. To learn more about virtual machine performance metrics, [**click here**](https://infrahub-doc.nexgencloud.com/docs/virtual-machines/vm-performance-metrics-and-events-history#performance-metrics).

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    virtual_machine_id = 56 # int | 
    duration = 'duration_example' # str |  (optional)

    try:
        # Retrieve virtual machine performance metrics
        api_response = api_instance.retrieve_virtual_machine_performance_metrics(virtual_machine_id, duration=duration)
        print("The response of VirtualMachineApi->retrieve_virtual_machine_performance_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->retrieve_virtual_machine_performance_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**|  | 
 **duration** | **str**|  | [optional] 

### Return type

[**MetricsFields**](MetricsFields.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **retrieve_virtual_machines_associated_with_a_contract**
> ContractInstancesResponse retrieve_virtual_machines_associated_with_a_contract(contract_id, page=page, page_size=page_size, search=search)

Retrieve virtual machines associated with a contract

Retrieves a list of virtual machines associated with a contract, providing details such as virtual machine name, timestamp, flavor name, and other relevant information. Please provide the ID of the relevant contract in the path.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

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
        api_response = api_instance.retrieve_virtual_machines_associated_with_a_contract(contract_id, page=page, page_size=page_size, search=search)
        print("The response of VirtualMachineApi->retrieve_virtual_machines_associated_with_a_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->retrieve_virtual_machines_associated_with_a_contract: %s\n" % e)
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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_virtual_machine**
> ResponseModel start_virtual_machine(id)

Start virtual machine

Initiates the startup of a virtual machine. Provide the virtual machine ID in the path to initiate the starting of the specified virtual machine.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    id = 56 # int | 

    try:
        # Start virtual machine
        api_response = api_instance.start_virtual_machine(id)
        print("The response of VirtualMachineApi->start_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->start_virtual_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

# **stop_virtual_machine**
> ResponseModel stop_virtual_machine(id)

Stop virtual machine

Shuts down a virtual machine. Provide the virtual machine ID in the path to initiate the shutdown process for the specified virtual machine.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (accessToken):

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

# Configure API key authorization: accessToken
configuration.api_key['accessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessToken'] = 'Bearer'

# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.VirtualMachineApi(api_client)
    id = 56 # int | 

    try:
        # Stop virtual machine
        api_response = api_instance.stop_virtual_machine(id)
        print("The response of VirtualMachineApi->stop_virtual_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->stop_virtual_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey), [accessToken](../README.md#accessToken)

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

