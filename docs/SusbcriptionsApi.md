# paycomet_client.SusbcriptionsApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](SusbcriptionsApi.md#create_subscription) | **POST** /v1/subscription | Create susbcription payment
[**edit_subscription**](SusbcriptionsApi.md#edit_subscription) | **POST** /v1/subscription/edit | Edit susbcription payment
[**remove_subscription**](SusbcriptionsApi.md#remove_subscription) | **POST** /v1/subscription/remove | Remove susbcription payment

# **create_subscription**
> InlineResponse20019 create_subscription(paycomet_api_token, body=body)

Create susbcription payment

Create subscription, create subscription token

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.SusbcriptionsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet_client.V1SubscriptionBody() # V1SubscriptionBody |  (optional)

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
> InlineResponse20020 edit_subscription(paycomet_api_token, body=body)

Edit susbcription payment

Edit subscription, modify subscription token

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.SusbcriptionsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet_client.SubscriptionEditBody() # SubscriptionEditBody |  (optional)

try:
    # Edit susbcription payment
    api_response = api_instance.edit_subscription(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SusbcriptionsApi->edit_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) |
 **body** | [**SubscriptionEditBody**](SubscriptionEditBody.md)|  | [optional]

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_subscription**
> InlineResponse20021 remove_subscription(paycomet_api_token, body=body)

Remove susbcription payment

Delete subscription, remove subscription token

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.SusbcriptionsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet_client.SubscriptionRemoveBody() # SubscriptionRemoveBody |  (optional)

try:
    # Remove susbcription payment
    api_response = api_instance.remove_subscription(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SusbcriptionsApi->remove_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) |
 **body** | [**SubscriptionRemoveBody**](SubscriptionRemoveBody.md)|  | [optional]

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

