# paycomet_client.IpApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countryby_ip**](IpApi.md#get_countryby_ip) | **POST** /v1/ip | Retrieves country info by IP

# **get_countryby_ip**
> InlineResponse2009 get_countryby_ip(body=body, paycomet_api_token=paycomet_api_token)

Retrieves country info by IP

Country by IP

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.IpApi()
body = paycomet_client.V1IpBody() # V1IpBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Query privilege required) (optional)

try:
    # Retrieves country info by IP
    api_response = api_instance.get_countryby_ip(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpApi->get_countryby_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1IpBody**](V1IpBody.md)|  | [optional]
 **paycomet_api_token** | **str**| PAYCOMET API key (Query privilege required) | [optional]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

