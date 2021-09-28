# swagger_client.DccApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dcc_purchase_confirm**](DccApi.md#dcc_purchase_confirm) | **POST** /v1/payments/dcc/{order}/confirm | Confirm previous DCC payment
[**dcc_purchase_create**](DccApi.md#dcc_purchase_create) | **POST** /v1/payments/dcc | Create an DCC payment

# **dcc_purchase_confirm**
> InlineResponse20024 dcc_purchase_confirm(paycomet_api_token, order, body=body)

Confirm previous DCC payment

confirm_purchase_dcc

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DccApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
order = 'order_example' # str | 
body = swagger_client.OrderConfirmBody() # OrderConfirmBody |  (optional)

try:
    # Confirm previous DCC payment
    api_response = api_instance.dcc_purchase_confirm(paycomet_api_token, order, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DccApi->dcc_purchase_confirm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **order** | **str**|  | 
 **body** | [**OrderConfirmBody**](OrderConfirmBody.md)|  | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dcc_purchase_create**
> InlineResponse20023 dcc_purchase_create(paycomet_api_token, body=body)

Create an DCC payment

execute_purchase_dcc

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DccApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = swagger_client.PaymentsDccBody() # PaymentsDccBody |  (optional)

try:
    # Create an DCC payment
    api_response = api_instance.dcc_purchase_create(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DccApi->dcc_purchase_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**PaymentsDccBody**](PaymentsDccBody.md)|  | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

