# paycomet-client
PAYCOMET API REST for customers.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.28.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://www.paycomet.com](https://www.paycomet.com)

## Requirements.

Python 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import paycomet_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import paycomet_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.IVRApi(paycomet_client.ApiClient(configuration))
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet_client.IvrSessionstateBody() # IvrSessionstateBody |  (optional)

try:
    # Checks an IVR session
    api_response = api_instance.check_session(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IVRApi->check_session: %s\n" % e)

# create an instance of the API class
api_instance = paycomet_client.IVRApi(paycomet_client.ApiClient(configuration))
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet_client.IvrGetsessionBody() # IvrGetsessionBody |  (optional)

try:
    # Creates an IVR session
    api_response = api_instance.get_session(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IVRApi->get_session: %s\n" % e)

# create an instance of the API class
api_instance = paycomet_client.IVRApi(paycomet_client.ApiClient(configuration))
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet_client.IvrSessioncancelBody() # IvrSessioncancelBody |  (optional)

try:
    # Cancel an IVR session
    api_response = api_instance.session_cancel(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IVRApi->session_cancel: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://rest.paycomet.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IVRApi* | [**check_session**](docs/IVRApi.md#check_session) | **POST** /v1/ivr/session-state | Checks an IVR session
*IVRApi* | [**get_session**](docs/IVRApi.md#get_session) | **POST** /v1/ivr/get-session | Creates an IVR session
*IVRApi* | [**session_cancel**](docs/IVRApi.md#session_cancel) | **POST** /v1/ivr/session-cancel | Cancel an IVR session
*BalanceApi* | [**product_balance**](docs/BalanceApi.md#product_balance) | **POST** /v1/balance | Get balance info
*CardsApi* | [**add_user**](docs/CardsApi.md#add_user) | **POST** /v1/cards | Tokenizes a card. Either card number and CVC2 or jetToken are required. For you to send directly the card data you should be PCI certified or the accepting the requirement to submit quarterly SAQ-AEP and get ASV scans. For most users is strongly recommended getting the jetToken with JETIFRAME or using GET integration to register the cards instead of REST.
*CardsApi* | [**edit_user**](docs/CardsApi.md#edit_user) | **POST** /v1/cards/edit | Changes the expiry date, cvc2 or both
*CardsApi* | [**info_user**](docs/CardsApi.md#info_user) | **POST** /v1/cards/info | Get card info
*CardsApi* | [**physical_add_card**](docs/CardsApi.md#physical_add_card) | **POST** /v1/cards/physical | Tokenize a card by physical encrypted data
*CardsApi* | [**remove_user**](docs/CardsApi.md#remove_user) | **POST** /v1/cards/delete | Removes a card
*DccApi* | [**dcc_purchase_confirm**](docs/DccApi.md#dcc_purchase_confirm) | **POST** /v1/payments/dcc/{order}/confirm | Confirm previous DCC payment
*DccApi* | [**dcc_purchase_create**](docs/DccApi.md#dcc_purchase_create) | **POST** /v1/payments/dcc | Create an DCC payment
*ErrorApi* | [**info_error**](docs/ErrorApi.md#info_error) | **POST** /v1/errors | Gets an error description
*ExchangeApi* | [**exchange**](docs/ExchangeApi.md#exchange) | **POST** /v1/exchange | Converts a certain amount from a currency to another.
*FormApi* | [**form**](docs/FormApi.md#form) | **POST** /v1/form | Create form view for user capture
*HeartbeatApi* | [**heartbeat**](docs/HeartbeatApi.md#heartbeat) | **POST** /v1/heartbeat | Check the system
*IpApi* | [**get_countryby_ip**](docs/IpApi.md#get_countryby_ip) | **POST** /v1/ip | Retrieves country info by IP
*LaunchpadApi* | [**launch_authorization**](docs/LaunchpadApi.md#launch_authorization) | **POST** /v1/launchpad/authorization | Creates a payment link and sends it to customer
*LaunchpadApi* | [**launch_preauthorization**](docs/LaunchpadApi.md#launch_preauthorization) | **POST** /v1/launchpad/preauthorization | Executes a preauthorization link and sends it to customer
*LaunchpadApi* | [**launch_subscription**](docs/LaunchpadApi.md#launch_subscription) | **POST** /v1/launchpad/subscription | Creates a subscription link and sends it to customer
*MarketplaceApi* | [**split_transfer**](docs/MarketplaceApi.md#split_transfer) | **POST** /v1/marketplace/split-transfer | Make a transfer to other accounts on PAYCOMET
*MarketplaceApi* | [**split_transfer_reversal**](docs/MarketplaceApi.md#split_transfer_reversal) | **POST** /v1/marketplace/split-transfer-reversal | Run a split transfer reversal based on a previous split transfer
*MarketplaceApi* | [**transfer**](docs/MarketplaceApi.md#transfer) | **POST** /v1/marketplace/transfer | Run a transfer
*MarketplaceApi* | [**transfer_reversal**](docs/MarketplaceApi.md#transfer_reversal) | **POST** /v1/marketplace/transfer-reversal | Make a transfer reversal based on a previous transfer
*MethodsApi* | [**get_user_payment_methods**](docs/MethodsApi.md#get_user_payment_methods) | **POST** /v1/methods | Retrieves product methods
*MiraklApi* | [**mirakl_invoices_search**](docs/MiraklApi.md#mirakl_invoices_search) | **POST** /v1/invoices | Search Mirakl invoices
*PaymentsApi* | [**execute_purchase**](docs/PaymentsApi.md#execute_purchase) | **POST** /v1/payments | Executes a payment
*PaymentsApi* | [**execute_purchase_rtoken**](docs/PaymentsApi.md#execute_purchase_rtoken) | **POST** /v1/payments/rtoken | Executes a payment by refence
*PaymentsApi* | [**operation_info**](docs/PaymentsApi.md#operation_info) | **POST** /v1/payments/{order}/info | Get info of a order
*PaymentsApi* | [**operation_search**](docs/PaymentsApi.md#operation_search) | **POST** /v1/payments/search | Search orders
*PreauthorizationsApi* | [**cancel_preauthorization**](docs/PreauthorizationsApi.md#cancel_preauthorization) | **POST** /v1/payments/{order}/preauth/cancel | Cancel previous preauthorization
*PreauthorizationsApi* | [**confirm_preauthorization**](docs/PreauthorizationsApi.md#confirm_preauthorization) | **POST** /v1/payments/{order}/preauth/confirm | Confirm previous preauthorization
*PreauthorizationsApi* | [**create_preauthoritation**](docs/PreauthorizationsApi.md#create_preauthoritation) | **POST** /v1/payments/preauth | Create preauthorization
*PreauthorizationsApi* | [**create_preauthorization_rtoken**](docs/PreauthorizationsApi.md#create_preauthorization_rtoken) | **POST** /v1/payments/preauthrtoken | Creates a preauthorization by reference
*RefundApi* | [**execute_refund**](docs/RefundApi.md#execute_refund) | **POST** /v1/payments/{order}/refund | Perform a refund
*SepaApi* | [**add_document**](docs/SepaApi.md#add_document) | **POST** /v1/sepa/add-document | Adds a SEPA document
*SepaApi* | [**check_customer**](docs/SepaApi.md#check_customer) | **POST** /v1/sepa/check-customer | Check a customers SEPA documentation
*SepaApi* | [**check_document**](docs/SepaApi.md#check_document) | **POST** /v1/sepa/check-document | Check a SEPA document
*SepaApi* | [**sepa_operations**](docs/SepaApi.md#sepa_operations) | **POST** /v1/sepa/operations | Send SEPA operations
*SusbcriptionsApi* | [**create_subscription**](docs/SusbcriptionsApi.md#create_subscription) | **POST** /v1/subscription | Create susbcription payment
*SusbcriptionsApi* | [**edit_subscription**](docs/SusbcriptionsApi.md#edit_subscription) | **POST** /v1/subscription/edit | Edit susbcription payment
*SusbcriptionsApi* | [**remove_subscription**](docs/SusbcriptionsApi.md#remove_subscription) | **POST** /v1/subscription/remove | Remove susbcription payment

## Documentation For Models

 - [CardsDeleteBody](docs/CardsDeleteBody.md)
 - [CardsEditBody](docs/CardsEditBody.md)
 - [CardsInfoBody](docs/CardsInfoBody.md)
 - [CardsPhysicalBody](docs/CardsPhysicalBody.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20014Payment](docs/InlineResponse20014Payment.md)
 - [InlineResponse20014PaymentHistory](docs/InlineResponse20014PaymentHistory.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20015Payment](docs/InlineResponse20015Payment.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse20019Subscription](docs/InlineResponse20019Subscription.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse20021](docs/InlineResponse20021.md)
 - [InlineResponse20022](docs/InlineResponse20022.md)
 - [InlineResponse20022Dcc](docs/InlineResponse20022Dcc.md)
 - [InlineResponse20023](docs/InlineResponse20023.md)
 - [InlineResponse20024](docs/InlineResponse20024.md)
 - [InlineResponse20024Submerchant](docs/InlineResponse20024Submerchant.md)
 - [InlineResponse20025](docs/InlineResponse20025.md)
 - [InlineResponse20025Submerchant](docs/InlineResponse20025Submerchant.md)
 - [InlineResponse20026](docs/InlineResponse20026.md)
 - [InlineResponse20027](docs/InlineResponse20027.md)
 - [InlineResponse20028](docs/InlineResponse20028.md)
 - [InlineResponse20028Operations](docs/InlineResponse20028Operations.md)
 - [InlineResponse20029](docs/InlineResponse20029.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse20030](docs/InlineResponse20030.md)
 - [InlineResponse20031](docs/InlineResponse20031.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2008Invoices](docs/InlineResponse2008Invoices.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse403](docs/InlineResponse403.md)
 - [InlineResponse422](docs/InlineResponse422.md)
 - [InlineResponse4221](docs/InlineResponse4221.md)
 - [InlineResponse4222](docs/InlineResponse4222.md)
 - [InlineResponse4222Error](docs/InlineResponse4222Error.md)
 - [InlineResponse4223](docs/InlineResponse4223.md)
 - [InlineResponse4223Error](docs/InlineResponse4223Error.md)
 - [InlineResponse4224](docs/InlineResponse4224.md)
 - [InlineResponse4224Error](docs/InlineResponse4224Error.md)
 - [InlineResponse4225](docs/InlineResponse4225.md)
 - [InlineResponse4225Error](docs/InlineResponse4225Error.md)
 - [InlineResponse4226](docs/InlineResponse4226.md)
 - [InlineResponse4226Error](docs/InlineResponse4226Error.md)
 - [InlineResponse422Error](docs/InlineResponse422Error.md)
 - [IvrGetsessionBody](docs/IvrGetsessionBody.md)
 - [IvrSessioncancelBody](docs/IvrSessioncancelBody.md)
 - [IvrSessionstateBody](docs/IvrSessionstateBody.md)
 - [LaunchpadAuthorizationBody](docs/LaunchpadAuthorizationBody.md)
 - [LaunchpadPreauthorizationBody](docs/LaunchpadPreauthorizationBody.md)
 - [LaunchpadSubscriptionBody](docs/LaunchpadSubscriptionBody.md)
 - [MarketplaceSplittransferBody](docs/MarketplaceSplittransferBody.md)
 - [MarketplaceSplittransferreversalBody](docs/MarketplaceSplittransferreversalBody.md)
 - [MarketplaceTransferBody](docs/MarketplaceTransferBody.md)
 - [MarketplaceTransferreversalBody](docs/MarketplaceTransferreversalBody.md)
 - [OrderConfirmBody](docs/OrderConfirmBody.md)
 - [OrderInfoBody](docs/OrderInfoBody.md)
 - [OrderRefundBody](docs/OrderRefundBody.md)
 - [PaymentsDccBody](docs/PaymentsDccBody.md)
 - [PaymentsPreauthBody](docs/PaymentsPreauthBody.md)
 - [PaymentsPreauthrtokenBody](docs/PaymentsPreauthrtokenBody.md)
 - [PaymentsRtokenBody](docs/PaymentsRtokenBody.md)
 - [PaymentsSearchBody](docs/PaymentsSearchBody.md)
 - [PreauthCancelBody](docs/PreauthCancelBody.md)
 - [PreauthConfirmBody](docs/PreauthConfirmBody.md)
 - [SepaAdddocumentBody](docs/SepaAdddocumentBody.md)
 - [SepaCheckcustomerBody](docs/SepaCheckcustomerBody.md)
 - [SepaCheckdocumentBody](docs/SepaCheckdocumentBody.md)
 - [SepaOperationsBody](docs/SepaOperationsBody.md)
 - [SubscriptionEditBody](docs/SubscriptionEditBody.md)
 - [SubscriptionRemoveBody](docs/SubscriptionRemoveBody.md)
 - [V1BalanceBody](docs/V1BalanceBody.md)
 - [V1CardsBody](docs/V1CardsBody.md)
 - [V1ErrorsBody](docs/V1ErrorsBody.md)
 - [V1ExchangeBody](docs/V1ExchangeBody.md)
 - [V1FormBody](docs/V1FormBody.md)
 - [V1HeartbeatBody](docs/V1HeartbeatBody.md)
 - [V1InvoicesBody](docs/V1InvoicesBody.md)
 - [V1IpBody](docs/V1IpBody.md)
 - [V1MethodsBody](docs/V1MethodsBody.md)
 - [V1PaymentsBody](docs/V1PaymentsBody.md)
 - [V1SubscriptionBody](docs/V1SubscriptionBody.md)
 - [V1formPayment](docs/V1formPayment.md)
 - [V1formPaymentEscrowTargets](docs/V1formPaymentEscrowTargets.md)
 - [V1formPaymentMerchantData](docs/V1formPaymentMerchantData.md)
 - [V1formPaymentMerchantDataAcctInfo](docs/V1formPaymentMerchantDataAcctInfo.md)
 - [V1formPaymentMerchantDataBilling](docs/V1formPaymentMerchantDataBilling.md)
 - [V1formPaymentMerchantDataCustomer](docs/V1formPaymentMerchantDataCustomer.md)
 - [V1formPaymentMerchantDataCustomerHomePhone](docs/V1formPaymentMerchantDataCustomerHomePhone.md)
 - [V1formPaymentMerchantDataCustomerMobilePhone](docs/V1formPaymentMerchantDataCustomerMobilePhone.md)
 - [V1formPaymentMerchantDataCustomerWorkPhone](docs/V1formPaymentMerchantDataCustomerWorkPhone.md)
 - [V1formPaymentMerchantDataMerchantRiskIndicator](docs/V1formPaymentMerchantDataMerchantRiskIndicator.md)
 - [V1formPaymentMerchantDataShipping](docs/V1formPaymentMerchantDataShipping.md)
 - [V1formPaymentMerchantDataShoppingCart](docs/V1formPaymentMerchantDataShoppingCart.md)
 - [V1formPaymentMerchantDataThreeDSRequestorAuthenticationInfo](docs/V1formPaymentMerchantDataThreeDSRequestorAuthenticationInfo.md)
 - [V1formSubscription](docs/V1formSubscription.md)
 - [V1invoicesPayment](docs/V1invoicesPayment.md)
 - [V1launchpadauthorizationMerchantData](docs/V1launchpadauthorizationMerchantData.md)
 - [V1launchpadauthorizationMerchantDataCustomer](docs/V1launchpadauthorizationMerchantDataCustomer.md)
 - [V1launchpadsubscriptionMerchantData](docs/V1launchpadsubscriptionMerchantData.md)
 - [V1launchpadsubscriptionMerchantDataShipping](docs/V1launchpadsubscriptionMerchantDataShipping.md)
 - [V1marketplacesplittransferPayment](docs/V1marketplacesplittransferPayment.md)
 - [V1marketplacesplittransferSubmerchant](docs/V1marketplacesplittransferSubmerchant.md)
 - [V1marketplacesplittransferreversalPayment](docs/V1marketplacesplittransferreversalPayment.md)
 - [V1marketplacesplittransferreversalSubmerchant](docs/V1marketplacesplittransferreversalSubmerchant.md)
 - [V1marketplacetransferPayment](docs/V1marketplacetransferPayment.md)
 - [V1marketplacetransferreversalSubmerchant](docs/V1marketplacetransferreversalSubmerchant.md)
 - [V1paymentsPayment](docs/V1paymentsPayment.md)
 - [V1paymentsdccPayment](docs/V1paymentsdccPayment.md)
 - [V1paymentsdccorderconfirmDcc](docs/V1paymentsdccorderconfirmDcc.md)
 - [V1paymentsorderinfoPayment](docs/V1paymentsorderinfoPayment.md)
 - [V1paymentsorderpreauthcancelPayment](docs/V1paymentsorderpreauthcancelPayment.md)
 - [V1paymentsorderpreauthconfirmPayment](docs/V1paymentsorderpreauthconfirmPayment.md)
 - [V1paymentsorderrefundPayment](docs/V1paymentsorderrefundPayment.md)
 - [V1paymentspreauthPayment](docs/V1paymentspreauthPayment.md)
 - [V1paymentsrtokenPayment](docs/V1paymentsrtokenPayment.md)
 - [V1sepaoperationsOperations](docs/V1sepaoperationsOperations.md)
 - [V1subscriptionPayment](docs/V1subscriptionPayment.md)
 - [V1subscriptionSubscription](docs/V1subscriptionSubscription.md)
 - [V1subscriptioneditPayment](docs/V1subscriptioneditPayment.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

tecnico@paycomet.com
