# swagger_client.SusbcriptionsApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](SusbcriptionsApi.md#create_subscription) | **POST** /v1/subscription | Create susbcription payment
[**edit_subscription**](SusbcriptionsApi.md#edit_subscription) | **POST** /v1/subscription/{order}/edit | Edit susbcription payment.
[**execute_subscription**](SusbcriptionsApi.md#execute_subscription) | **POST** /v1/subscription/{order}/execute | Excute a susbcription payment.
[**remove_subscription**](SusbcriptionsApi.md#remove_subscription) | **POST** /v1/subscription/{order}/remove | Remove susbcription payment. If the susbscription is not a card subscription only the idUser is need. TokenUser is just for card subscriptions.

# **create_subscription**
> InlineResponse20019 create_subscription(paycomet_api_token, body=body)

Create susbcription payment

Create subscription, create subscription token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SusbcriptionsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = swagger_client.V1SubscriptionBody() # V1SubscriptionBody |  (optional)

try:
    # Create susbcription payment
    api_response = api_instance.create_subscription(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SusbcriptionsApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**V1SubscriptionBody**](V1SubscriptionBody.md)|  | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_subscription**
> InlineResponse20020 edit_subscription(paycomet_api_token, order, body=body)

Edit susbcription payment.

Edit a subscription. The subscription is identified by the terminal, the payment method, the iduser and the original reference. The rest of the fields can be changed. Please note that changing an amount in a subscription may result in the bank rejecting the payment as the initial payment will not match the new one. To change the amount it is recommended to use the execute parameter. Even if the amount and currency are not changed they should be indicated with the original values.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SusbcriptionsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
order = 'order_example' # str | 
body = swagger_client.OrderEditBody() # OrderEditBody |  (optional)

try:
    # Edit susbcription payment.
    api_response = api_instance.edit_subscription(paycomet_api_token, order, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SusbcriptionsApi->edit_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **order** | **str**|  | 
 **body** | [**OrderEditBody**](OrderEditBody.md)|  | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_subscription**
> InlineResponse20021 execute_subscription(paycomet_api_token, order, body=body)

Excute a susbcription payment.

This command excecutes a payment of the subscription. This payment does not affect the rest of the subscription payments. However, as it doesn´t belongs to the recurrency it may be denied if the amount is different or even just because of the date of execution as it is not the expected by the bank.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SusbcriptionsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
order = 'order_example' # str | 
body = swagger_client.OrderExecuteBody() # OrderExecuteBody |  (optional)

try:
    # Excute a susbcription payment.
    api_response = api_instance.execute_subscription(paycomet_api_token, order, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SusbcriptionsApi->execute_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **order** | **str**|  | 
 **body** | [**OrderExecuteBody**](OrderExecuteBody.md)|  | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_subscription**
> InlineResponse20022 remove_subscription(paycomet_api_token, order, body=body)

Remove susbcription payment. If the susbscription is not a card subscription only the idUser is need. TokenUser is just for card subscriptions.

Delete a subscription. The subscription is identified by the terminal, the payment method, the iduser and the original reference.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SusbcriptionsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
order = 'order_example' # str | 
body = swagger_client.OrderRemoveBody() # OrderRemoveBody |  (optional)

try:
    # Remove susbcription payment. If the susbscription is not a card subscription only the idUser is need. TokenUser is just for card subscriptions.
    api_response = api_instance.remove_subscription(paycomet_api_token, order, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SusbcriptionsApi->remove_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **order** | **str**|  | 
 **body** | [**OrderRemoveBody**](OrderRemoveBody.md)|  | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

