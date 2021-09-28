# coding: utf-8

"""
    PAYCOMET REST API

    PAYCOMET API REST for customers.  # noqa: E501

    OpenAPI spec version: 2.34.0
    Contact: tecnico@paycomet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V1ExchangeBody(object):
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
        'amount': 'str',
        'original_currency': 'str',
        'final_currency': 'str'
    }

    attribute_map = {
        'terminal': 'terminal',
        'amount': 'amount',
        'original_currency': 'originalCurrency',
        'final_currency': 'finalCurrency'
    }

    def __init__(self, terminal=None, amount=None, original_currency=None, final_currency=None):  # noqa: E501
        """V1ExchangeBody - a model defined in Swagger"""  # noqa: E501
        self._terminal = None
        self._amount = None
        self._original_currency = None
        self._final_currency = None
        self.discriminator = None
        self.terminal = terminal
        self.amount = amount
        self.original_currency = original_currency
        self.final_currency = final_currency

    @property
    def terminal(self):
        """Gets the terminal of this V1ExchangeBody.  # noqa: E501

        Product or terminal Id.  # noqa: E501

        :return: The terminal of this V1ExchangeBody.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this V1ExchangeBody.

        Product or terminal Id.  # noqa: E501

        :param terminal: The terminal of this V1ExchangeBody.  # noqa: E501
        :type: int
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def amount(self):
        """Gets the amount of this V1ExchangeBody.  # noqa: E501

        Amount to convert  # noqa: E501

        :return: The amount of this V1ExchangeBody.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this V1ExchangeBody.

        Amount to convert  # noqa: E501

        :param amount: The amount of this V1ExchangeBody.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def original_currency(self):
        """Gets the original_currency of this V1ExchangeBody.  # noqa: E501

        Currency to convert from  # noqa: E501

        :return: The original_currency of this V1ExchangeBody.  # noqa: E501
        :rtype: str
        """
        return self._original_currency

    @original_currency.setter
    def original_currency(self, original_currency):
        """Sets the original_currency of this V1ExchangeBody.

        Currency to convert from  # noqa: E501

        :param original_currency: The original_currency of this V1ExchangeBody.  # noqa: E501
        :type: str
        """
        if original_currency is None:
            raise ValueError("Invalid value for `original_currency`, must not be `None`")  # noqa: E501

        self._original_currency = original_currency

    @property
    def final_currency(self):
        """Gets the final_currency of this V1ExchangeBody.  # noqa: E501

        Currency to convert to  # noqa: E501

        :return: The final_currency of this V1ExchangeBody.  # noqa: E501
        :rtype: str
        """
        return self._final_currency

    @final_currency.setter
    def final_currency(self, final_currency):
        """Sets the final_currency of this V1ExchangeBody.

        Currency to convert to  # noqa: E501

        :param final_currency: The final_currency of this V1ExchangeBody.  # noqa: E501
        :type: str
        """
        if final_currency is None:
            raise ValueError("Invalid value for `final_currency`, must not be `None`")  # noqa: E501

        self._final_currency = final_currency

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
        if issubclass(V1ExchangeBody, dict):
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
        if not isinstance(other, V1ExchangeBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other