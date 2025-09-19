# hyperstack.FirewallsApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_security_group_details**](FirewallsApi.md#delete_security_group_details) | **DELETE** /core/firewalls/{id} | Delete firewall
[**delete_security_group_rule_delete**](FirewallsApi.md#delete_security_group_rule_delete) | **DELETE** /core/firewalls/{firewall_id}/firewall-rules/{firewall_rule_id} | Delete firewall rules from firewall
[**get_security_group**](FirewallsApi.md#get_security_group) | **GET** /core/firewalls | List firewalls
[**get_security_group_details**](FirewallsApi.md#get_security_group_details) | **GET** /core/firewalls/{id} | Retrieve firewall details
[**post_security_group**](FirewallsApi.md#post_security_group) | **POST** /core/firewalls | Create firewall
[**post_security_group_rules**](FirewallsApi.md#post_security_group_rules) | **POST** /core/firewalls/{firewall_id}/firewall-rules | Add firewall rule to firewall


# **delete_security_group_details**
> ResponseModel delete_security_group_details(id)

Delete firewall

Deletes a firewall by specifying the firewall ID in the path. If the firewall is currently attached to a virtual machine, it must be detached before deletion. For more information, [**click here**](https://docs.hyperstack.cloud/docs/api-reference/core-resources/firewalls/delete-firewall).

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
    api_instance = hyperstack.FirewallsApi(api_client)
    id = 56 # int | 

    try:
        # Delete firewall
        api_response = api_instance.delete_security_group_details(id)
        print("The response of FirewallsApi->delete_security_group_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallsApi->delete_security_group_details: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_security_group_rule_delete**
> ResponseModel delete_security_group_rule_delete(firewall_id, firewall_rule_id)

Delete firewall rules from firewall

Removes a firewall rule from firewall by providing the firewall ID and firewall rule ID in the path. For more information, [**click here**](https://docs.hyperstack.cloud/docs/api-reference/core-resources/firewalls/remove-firewall-rule-from-firewall).

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
    api_instance = hyperstack.FirewallsApi(api_client)
    firewall_id = 56 # int | 
    firewall_rule_id = 56 # int | 

    try:
        # Delete firewall rules from firewall
        api_response = api_instance.delete_security_group_rule_delete(firewall_id, firewall_rule_id)
        print("The response of FirewallsApi->delete_security_group_rule_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallsApi->delete_security_group_rule_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **int**|  | 
 **firewall_rule_id** | **int**|  | 

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
**403** | Forbidden |  -  |
**404** | Not Exists |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_group**
> FirewallsListResponse get_security_group(page=page, page_size=page_size, search=search, environment=environment)

List firewalls

Retrieves a list of existing firewalls and their details, including the security rules they contain and information about the virtual machines to which they are attached. For more information about the firewalls features offered by Infrahub, [**click here**](https://docs.hyperstack.cloud/docs/network-security/security-groups).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.firewalls_list_response import FirewallsListResponse
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
    api_instance = hyperstack.FirewallsApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    environment = 'environment_example' # str | Filter Environment ID or Name (optional)

    try:
        # List firewalls
        api_response = api_instance.get_security_group(page=page, page_size=page_size, search=search, environment=environment)
        print("The response of FirewallsApi->get_security_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallsApi->get_security_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **environment** | **str**| Filter Environment ID or Name | [optional] 

### Return type

[**FirewallsListResponse**](FirewallsListResponse.md)

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

# **get_security_group_details**
> FirewallDetailResponse get_security_group_details(id)

Retrieve firewall details

Retrieves the details of an existing firewall, including the security rules it contains and information about the virtual machines to which it is attached.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.firewall_detail_response import FirewallDetailResponse
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
    api_instance = hyperstack.FirewallsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve firewall details
        api_response = api_instance.get_security_group_details(id)
        print("The response of FirewallsApi->get_security_group_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallsApi->get_security_group_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**FirewallDetailResponse**](FirewallDetailResponse.md)

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

# **post_security_group**
> FirewallResponse post_security_group(payload)

Create firewall

Creates a firewall to which firewall rules can be added. A firewall can be attached to one or more virtual machines to control inbound and outbound traffic. In the body of the request, include the name of the firewall, the ID of the environment within which the firewall will be created, and an optional description. To obtain the ID of the environment, make a request to the [**list environments**](https://docs.hyperstack.cloud/docs/api-reference/core-resources/environments/list-environments) endpoint.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.create_firewall_payload import CreateFirewallPayload
from hyperstack.models.firewall_response import FirewallResponse
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
    api_instance = hyperstack.FirewallsApi(api_client)
    payload = hyperstack.CreateFirewallPayload() # CreateFirewallPayload | 

    try:
        # Create firewall
        api_response = api_instance.post_security_group(payload)
        print("The response of FirewallsApi->post_security_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallsApi->post_security_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreateFirewallPayload**](CreateFirewallPayload.md)|  | 

### Return type

[**FirewallResponse**](FirewallResponse.md)

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
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_security_group_rules**
> FirewallRule post_security_group_rules(firewall_id, payload)

Add firewall rule to firewall

Creates a [**firewall rule**](https://docs.hyperstack.cloud/docs/network-security/security-rules) and adds it to an existing firewall. Include the firewall ID in the path, and provide the firewall rule configuration in the request body.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.create_firewall_rule_payload import CreateFirewallRulePayload
from hyperstack.models.firewall_rule import FirewallRule
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
    api_instance = hyperstack.FirewallsApi(api_client)
    firewall_id = 56 # int | 
    payload = hyperstack.CreateFirewallRulePayload() # CreateFirewallRulePayload | 

    try:
        # Add firewall rule to firewall
        api_response = api_instance.post_security_group_rules(firewall_id, payload)
        print("The response of FirewallsApi->post_security_group_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallsApi->post_security_group_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **int**|  | 
 **payload** | [**CreateFirewallRulePayload**](CreateFirewallRulePayload.md)|  | 

### Return type

[**FirewallRule**](FirewallRule.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

