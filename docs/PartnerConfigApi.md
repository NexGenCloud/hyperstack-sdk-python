# hyperstack.PartnerConfigApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_partner_config**](PartnerConfigApi.md#get_partner_config) | **GET** /auth/partner-config | Get partner config
[**get_partner_config_by_domain**](PartnerConfigApi.md#get_partner_config_by_domain) | **GET** /auth/partner-config/docs | 


# **get_partner_config**
> PartnerConfig get_partner_config()

Get partner config

Fetch the customised customer configuration for Hyperstack.

### Example


```python
import hyperstack
from hyperstack.models.partner_config import PartnerConfig
from hyperstack.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://infrahub-api.nexgencloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperstack.Configuration(
    host = "https://infrahub-api.nexgencloud.com/v1"
)


# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.PartnerConfigApi(api_client)

    try:
        # Get partner config
        api_response = api_instance.get_partner_config()
        print("The response of PartnerConfigApi->get_partner_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerConfigApi->get_partner_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PartnerConfig**](PartnerConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partner_config_by_domain**
> PartnerConfig get_partner_config_by_domain(domain=domain)



Fetch the partner config for a given domain.

### Example


```python
import hyperstack
from hyperstack.models.partner_config import PartnerConfig
from hyperstack.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://infrahub-api.nexgencloud.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperstack.Configuration(
    host = "https://infrahub-api.nexgencloud.com/v1"
)


# Enter a context with an instance of the API client
with hyperstack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperstack.PartnerConfigApi(api_client)
    domain = 'domain_example' # str | The domain to look up the partner config for. (optional)

    try:
        api_response = api_instance.get_partner_config_by_domain(domain=domain)
        print("The response of PartnerConfigApi->get_partner_config_by_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerConfigApi->get_partner_config_by_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain to look up the partner config for. | [optional] 

### Return type

[**PartnerConfig**](PartnerConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

