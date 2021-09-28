# swagger_client.PreauthorizationsApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_preauthorization**](PreauthorizationsApi.md#cancel_preauthorization) | **POST** /v1/payments/{order}/preauth/cancel | Cancel previous preauthorization
[**confirm_preauthorization**](PreauthorizationsApi.md#confirm_preauthorization) | **POST** /v1/payments/{order}/preauth/confirm | Confirm previous preauthorization
[**create_preauthoritation**](PreauthorizationsApi.md#create_preauthoritation) | **POST** /v1/payments/preauth | Create preauthorization
[**create_preauthorization_rtoken**](PreauthorizationsApi.md#create_preauthorization_rtoken) | **POST** /v1/payments/preauthrtoken | Creates a preauthorization by reference

# **cancel_preauthorization**
> InlineResponse20016 cancel_preauthorization(paycomet_api_token, order, body=body)

Cancel previous preauthorization

cancel_preauthorization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreauthorizationsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Preauthorization privilege required)
order = 'order_example' # str | 
body = swagger_client.PreauthCancelBody() # PreauthCancelBody |  (optional)

try:
    # Cancel previous preauthorization
    api_response = api_instance.cancel_preauthorization(paycomet_api_token, order, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreauthorizationsApi->cancel_preauthorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Preauthorization privilege required) | 
 **order** | **str**|  | 
 **body** | [**PreauthCancelBody**](PreauthCancelBody.md)|  | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_preauthorization**
> InlineResponse20017 confirm_preauthorization(paycomet_api_token, order, body=body)

Confirm previous preauthorization

confirm_preauthorization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreauthorizationsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Preauthorization privilege required)
order = 'order_example' # str | 
body = swagger_client.PreauthConfirmBody() # PreauthConfirmBody |  (optional)

try:
    # Confirm previous preauthorization
    api_response = api_instance.confirm_preauthorization(paycomet_api_token, order, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreauthorizationsApi->confirm_preauthorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Preauthorization privilege required) | 
 **order** | **str**|  | 
 **body** | [**PreauthConfirmBody**](PreauthConfirmBody.md)|  | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_preauthoritation**
> InlineResponse20012 create_preauthoritation(paycomet_api_token, body=body)

Create preauthorization

create_preauthorization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreauthorizationsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Preauthorization privilege required)
body = swagger_client.PaymentsPreauthBody() # PaymentsPreauthBody |  (optional)

try:
    # Create preauthorization
    api_response = api_instance.create_preauthoritation(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreauthorizationsApi->create_preauthoritation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Preauthorization privilege required) | 
 **body** | [**PaymentsPreauthBody**](PaymentsPreauthBody.md)|  | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_preauthorization_rtoken**
> InlineResponse20018 create_preauthorization_rtoken(body=body, paycomet_api_token=paycomet_api_token)

Creates a preauthorization by reference

Creates a preauthorization with reference.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreauthorizationsApi()
body = swagger_client.PaymentsPreauthrtokenBody() # PaymentsPreauthrtokenBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required) (optional)

try:
    # Creates a preauthorization by reference
    api_response = api_instance.create_preauthorization_rtoken(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreauthorizationsApi->create_preauthorization_rtoken: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentsPreauthrtokenBody**](PaymentsPreauthrtokenBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

