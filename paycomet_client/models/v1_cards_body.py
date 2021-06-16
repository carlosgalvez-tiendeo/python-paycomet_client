# coding: utf-8

"""
    PAYCOMET REST API

    PAYCOMET API REST for customers.  # noqa: E501

    OpenAPI spec version: 2.28.0
    Contact: tecnico@paycomet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V1CardsBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'terminal': 'int',
        'cvc2': 'str',
        'jet_token': 'str',
        'expiry_year': 'str',
        'expiry_month': 'str',
        'pan': 'str',
        'order': 'str',
        'product_description': 'str',
        'language': 'str',
        'notify': 'int'
    }

    attribute_map = {
        'terminal': 'terminal',
        'cvc2': 'cvc2',
        'jet_token': 'jetToken',
        'expiry_year': 'expiryYear',
        'expiry_month': 'expiryMonth',
        'pan': 'pan',
        'order': 'order',
        'product_description': 'productDescription',
        'language': 'language',
        'notify': 'notify'
    }

    def __init__(self, terminal=None, cvc2=None, jet_token=None, expiry_year=None, expiry_month=None, pan=None, order=None, product_description=None, language='es', notify=None):  # noqa: E501
        """V1CardsBody - a model defined in Swagger"""  # noqa: E501
        self._terminal = None
        self._cvc2 = None
        self._jet_token = None
        self._expiry_year = None
        self._expiry_month = None
        self._pan = None
        self._order = None
        self._product_description = None
        self._language = None
        self._notify = None
        self.discriminator = None
        self.terminal = terminal
        if cvc2 is not None:
            self.cvc2 = cvc2
        if jet_token is not None:
            self.jet_token = jet_token
        if expiry_year is not None:
            self.expiry_year = expiry_year
        if expiry_month is not None:
            self.expiry_month = expiry_month
        if pan is not None:
            self.pan = pan
        if order is not None:
            self.order = order
        if product_description is not None:
            self.product_description = product_description
        if language is not None:
            self.language = language
        if notify is not None:
            self.notify = notify

    @property
    def terminal(self):
        """Gets the terminal of this V1CardsBody.  # noqa: E501

        Product or terminal Id.  # noqa: E501

        :return: The terminal of this V1CardsBody.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this V1CardsBody.

        Product or terminal Id.  # noqa: E501

        :param terminal: The terminal of this V1CardsBody.  # noqa: E501
        :type: int
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def cvc2(self):
        """Gets the cvc2 of this V1CardsBody.  # noqa: E501

        cvc2. Mandatory if no JetToken provided  # noqa: E501

        :return: The cvc2 of this V1CardsBody.  # noqa: E501
        :rtype: str
        """
        return self._cvc2

    @cvc2.setter
    def cvc2(self, cvc2):
        """Sets the cvc2 of this V1CardsBody.

        cvc2. Mandatory if no JetToken provided  # noqa: E501

        :param cvc2: The cvc2 of this V1CardsBody.  # noqa: E501
        :type: str
        """

        self._cvc2 = cvc2

    @property
    def jet_token(self):
        """Gets the jet_token of this V1CardsBody.  # noqa: E501

        Temporary token provided from PAYCOMET. Mandatory if no card provided.  # noqa: E501

        :return: The jet_token of this V1CardsBody.  # noqa: E501
        :rtype: str
        """
        return self._jet_token

    @jet_token.setter
    def jet_token(self, jet_token):
        """Sets the jet_token of this V1CardsBody.

        Temporary token provided from PAYCOMET. Mandatory if no card provided.  # noqa: E501

        :param jet_token: The jet_token of this V1CardsBody.  # noqa: E501
        :type: str
        """

        self._jet_token = jet_token

    @property
    def expiry_year(self):
        """Gets the expiry_year of this V1CardsBody.  # noqa: E501

        Expiry year.  Mandatory if no JetToken provided  # noqa: E501

        :return: The expiry_year of this V1CardsBody.  # noqa: E501
        :rtype: str
        """
        return self._expiry_year

    @expiry_year.setter
    def expiry_year(self, expiry_year):
        """Sets the expiry_year of this V1CardsBody.

        Expiry year.  Mandatory if no JetToken provided  # noqa: E501

        :param expiry_year: The expiry_year of this V1CardsBody.  # noqa: E501
        :type: str
        """

        self._expiry_year = expiry_year

    @property
    def expiry_month(self):
        """Gets the expiry_month of this V1CardsBody.  # noqa: E501

        Expiry month.  Mandatory if no JetToken provided.  # noqa: E501

        :return: The expiry_month of this V1CardsBody.  # noqa: E501
        :rtype: str
        """
        return self._expiry_month

    @expiry_month.setter
    def expiry_month(self, expiry_month):
        """Sets the expiry_month of this V1CardsBody.

        Expiry month.  Mandatory if no JetToken provided.  # noqa: E501

        :param expiry_month: The expiry_month of this V1CardsBody.  # noqa: E501
        :type: str
        """

        self._expiry_month = expiry_month

    @property
    def pan(self):
        """Gets the pan of this V1CardsBody.  # noqa: E501

        Card number. Mandatory if no JetToken provided  # noqa: E501

        :return: The pan of this V1CardsBody.  # noqa: E501
        :rtype: str
        """
        return self._pan

    @pan.setter
    def pan(self, pan):
        """Sets the pan of this V1CardsBody.

        Card number. Mandatory if no JetToken provided  # noqa: E501

        :param pan: The pan of this V1CardsBody.  # noqa: E501
        :type: str
        """

        self._pan = pan

    @property
    def order(self):
        """Gets the order of this V1CardsBody.  # noqa: E501

        Reference, will be included in callback.  # noqa: E501

        :return: The order of this V1CardsBody.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this V1CardsBody.

        Reference, will be included in callback.  # noqa: E501

        :param order: The order of this V1CardsBody.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def product_description(self):
        """Gets the product_description of this V1CardsBody.  # noqa: E501

        Concept, will be included in callback.  # noqa: E501

        :return: The product_description of this V1CardsBody.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this V1CardsBody.

        Concept, will be included in callback.  # noqa: E501

        :param product_description: The product_description of this V1CardsBody.  # noqa: E501
        :type: str
        """

        self._product_description = product_description

    @property
    def language(self):
        """Gets the language of this V1CardsBody.  # noqa: E501

        Language for callback translation.  # noqa: E501

        :return: The language of this V1CardsBody.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this V1CardsBody.

        Language for callback translation.  # noqa: E501

        :param language: The language of this V1CardsBody.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def notify(self):
        """Gets the notify of this V1CardsBody.  # noqa: E501

        Configure POST notification of the card tokenization result (possible values: 1 - force notify, 2 - not notify). Default product value will be used if notify is not informed  # noqa: E501

        :return: The notify of this V1CardsBody.  # noqa: E501
        :rtype: int
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """Sets the notify of this V1CardsBody.

        Configure POST notification of the card tokenization result (possible values: 1 - force notify, 2 - not notify). Default product value will be used if notify is not informed  # noqa: E501

        :param notify: The notify of this V1CardsBody.  # noqa: E501
        :type: int
        """

        self._notify = notify

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1CardsBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1CardsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other