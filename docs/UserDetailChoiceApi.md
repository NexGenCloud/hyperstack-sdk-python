# hyperstack.UserDetailChoiceApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_default_flavors_and_images**](UserDetailChoiceApi.md#retrieve_default_flavors_and_images) | **GET** /core/user/resources/defaults | Retrieve Default Flavors and Images


# **retrieve_default_flavors_and_images**
> UserDefaultChoicesForUserResponse retrieve_default_flavors_and_images()

Retrieve Default Flavors and Images

Retrieve the default choices for virtual machine deployment, including the default region, flavor, and image.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.user_default_choices_for_user_response import UserDefaultChoicesForUserResponse
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
    api_instance = hyperstack.UserDetailChoiceApi(api_client)

    try:
        # Retrieve Default Flavors and Images
        api_response = api_instance.retrieve_default_flavors_and_images()
        print("The response of UserDetailChoiceApi->retrieve_default_flavors_and_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDetailChoiceApi->retrieve_default_flavors_and_images: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserDefaultChoicesForUserResponse**](UserDefaultChoicesForUserResponse.md)

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

