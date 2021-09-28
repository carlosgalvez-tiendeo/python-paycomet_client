# swagger_client.SepaApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document**](SepaApi.md#add_document) | **POST** /v1/sepa/add-document | Adds a SEPA document
[**check_customer**](SepaApi.md#check_customer) | **POST** /v1/sepa/check-customer | Check a customers SEPA documentation
[**check_document**](SepaApi.md#check_document) | **POST** /v1/sepa/check-document | Check a SEPA document
[**sepa_operations**](SepaApi.md#sepa_operations) | **POST** /v1/sepa/operations | Send SEPA operations

# **add_document**
> InlineResponse20027 add_document(paycomet_api_token, body=body)

Adds a SEPA document

add_document

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SepaApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = swagger_client.SepaAdddocumentBody() # SepaAdddocumentBody |  (optional)

try:
    # Adds a SEPA document
    api_response = api_instance.add_document(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SepaApi->add_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**SepaAdddocumentBody**](SepaAdddocumentBody.md)|  | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_customer**
> InlineResponse20028 check_customer(paycomet_api_token, body=body)

Check a customers SEPA documentation

check_customer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SepaApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = swagger_client.SepaCheckcustomerBody() # SepaCheckcustomerBody |  (optional)

try:
    # Check a customers SEPA documentation
    api_response = api_instance.check_customer(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SepaApi->check_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**SepaCheckcustomerBody**](SepaCheckcustomerBody.md)|  | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_document**
> InlineResponse20027 check_document(paycomet_api_token, body=body)

Check a SEPA document

check_document

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SepaApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = swagger_client.SepaCheckdocumentBody() # SepaCheckdocumentBody |  (optional)

try:
    # Check a SEPA document
    api_response = api_instance.check_document(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SepaApi->check_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**SepaCheckdocumentBody**](SepaCheckdocumentBody.md)|  | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sepa_operations**
> InlineResponse20029 sepa_operations(paycomet_api_token, body=body)

Send SEPA operations

sepa_operations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SepaApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = swagger_client.SepaOperationsBody() # SepaOperationsBody |  (optional)

try:
    # Send SEPA operations
    api_response = api_instance.sepa_operations(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SepaApi->sepa_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**SepaOperationsBody**](SepaOperationsBody.md)|  | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

