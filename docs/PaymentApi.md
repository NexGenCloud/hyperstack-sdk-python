# hyperstack.PaymentApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_receipt**](PaymentApi.md#get_payment_receipt) | **GET** /billing/payment/receipt/{payment_id} | Retrieve Payment Receipt
[**initiate_payment**](PaymentApi.md#initiate_payment) | **POST** /billing/payment/payment-initiate | POST: Initiate payment
[**list_payment_details**](PaymentApi.md#list_payment_details) | **GET** /billing/payment/payment-details | GET: View payment details


# **get_payment_receipt**
> get_payment_receipt(payment_id)

Retrieve Payment Receipt

Retrieve the payment receipt from Stripe for a specific payment

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
    api_instance = hyperstack.PaymentApi(api_client)
    payment_id = 'payment_id_example' # str | 

    try:
        # Retrieve Payment Receipt
        api_instance.get_payment_receipt(payment_id)
    except Exception as e:
        print("Exception when calling PaymentApi->get_payment_receipt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 

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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_payment**
> PaymentInitiateResponse initiate_payment(payload)

POST: Initiate payment

Creates a payment for a specified amount, adding credit to the balance of your [**organization**](/docs/rbac/organization). Include the `amount` in the body of the request to make a payment for the specified value in dollars. View a history of past payments by calling the [**Retrieve Payment History**](/docs/api-reference/billing-resources/retrieve-payment-history) API. For additional information [**click here**](None/docs/api-reference/billing-resources/create-payment).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.payment_initiate_payload import PaymentInitiatePayload
from hyperstack.models.payment_initiate_response import PaymentInitiateResponse
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
    api_instance = hyperstack.PaymentApi(api_client)
    payload = hyperstack.PaymentInitiatePayload() # PaymentInitiatePayload | 

    try:
        # POST: Initiate payment
        api_response = api_instance.initiate_payment(payload)
        print("The response of PaymentApi->initiate_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->initiate_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**PaymentInitiatePayload**](PaymentInitiatePayload.md)|  | 

### Return type

[**PaymentInitiateResponse**](PaymentInitiateResponse.md)

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

# **list_payment_details**
> PaymentDetailsResponse list_payment_details()

GET: View payment details

Retrieves a list of all payments made within your [**organization**](/docs/rbac/organization) and their details, including the amount, payment status, and more. For additional information [**click here**](None/docs/api-reference/billing-resources/retrieve-payment-history/).

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.payment_details_response import PaymentDetailsResponse
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
    api_instance = hyperstack.PaymentApi(api_client)

    try:
        # GET: View payment details
        api_response = api_instance.list_payment_details()
        print("The response of PaymentApi->list_payment_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_payment_details: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PaymentDetailsResponse**](PaymentDetailsResponse.md)

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

