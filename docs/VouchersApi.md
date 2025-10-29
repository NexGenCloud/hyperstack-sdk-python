# hyperstack.VouchersApi

All URIs are relative to *https://infrahub-api.nexgencloud.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redeem_a_voucher**](VouchersApi.md#redeem_a_voucher) | **POST** /billing/billing/vouchers/redeem | Redeem a voucher with a voucher_code


# **redeem_a_voucher**
> VoucherRedeemResponseSchema redeem_a_voucher(payload)

Redeem a voucher with a voucher_code

Request to redeem a voucher with a voucher code.

### Example

* Api Key Authentication (apiKey):

```python
import hyperstack
from hyperstack.models.redeem_voucher_payload import RedeemVoucherPayload
from hyperstack.models.voucher_redeem_response_schema import VoucherRedeemResponseSchema
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
    api_instance = hyperstack.VouchersApi(api_client)
    payload = hyperstack.RedeemVoucherPayload() # RedeemVoucherPayload | 

    try:
        # Redeem a voucher with a voucher_code
        api_response = api_instance.redeem_a_voucher(payload)
        print("The response of VouchersApi->redeem_a_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->redeem_a_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**RedeemVoucherPayload**](RedeemVoucherPayload.md)|  | 

### Return type

[**VoucherRedeemResponseSchema**](VoucherRedeemResponseSchema.md)

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

