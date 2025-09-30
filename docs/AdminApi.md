# hyperstack.AdminApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_password_change_notification_email**](AdminApi.md#send_password_change_notification_email) | **POST** /auth/admin/password-change-mail | Send Password Change Notification Email


# **send_password_change_notification_email**
> CommonResponseModel send_password_change_notification_email()

Send Password Change Notification Email

Send a password change notification email to a user

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.common_response_model import CommonResponseModel
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
    api_instance = hyperstack.AdminApi(api_client)

    try:
        # Send Password Change Notification Email
        api_response = api_instance.send_password_change_notification_email()
        print("The response of AdminApi->send_password_change_notification_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->send_password_change_notification_email: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CommonResponseModel**](CommonResponseModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Email Sent Successfully. |  -  |
**400** | Unable to send email |  -  |
**401** | Unauthorized |  -  |
**404** | User Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

