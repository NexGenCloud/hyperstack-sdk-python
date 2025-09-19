# hyperstack.FirewallAttachmentApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_attach_security_groups**](FirewallAttachmentApi.md#post_attach_security_groups) | **POST** /core/firewalls/{firewall_id}/update-attachments | Attach Firewalls to VMs


# **post_attach_security_groups**
> ResponseModel post_attach_security_groups(firewall_id, payload)

Attach Firewalls to VMs

Attach a firewall to one or more virtual machines by providing the virtual machine IDs in the request body and the firewall ID in the path. For more information, [**click here**](https://docs.hyperstack.cloud/docs/api-reference/core-resources/firewalls/attach-firewall-to-vms).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.attach_firewall_with_vm import AttachFirewallWithVM
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
    api_instance = hyperstack.FirewallAttachmentApi(api_client)
    firewall_id = 56 # int | 
    payload = hyperstack.AttachFirewallWithVM() # AttachFirewallWithVM | 

    try:
        # Attach Firewalls to VMs
        api_response = api_instance.post_attach_security_groups(firewall_id, payload)
        print("The response of FirewallAttachmentApi->post_attach_security_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallAttachmentApi->post_attach_security_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **int**|  | 
 **payload** | [**AttachFirewallWithVM**](AttachFirewallWithVM.md)|  | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

