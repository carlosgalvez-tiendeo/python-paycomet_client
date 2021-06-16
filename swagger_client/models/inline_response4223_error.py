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

class InlineResponse4223Error(object):
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
        'message': 'str',
        'detail': 'list[Object]'
    }

    attribute_map = {
        'message': 'message',
        'detail': 'detail'
    }

    def __init__(self, message=None, detail=None):  # noqa: E501
        """InlineResponse4223Error - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._detail = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if detail is not None:
            self.detail = detail

    @property
    def message(self):
        """Gets the message of this InlineResponse4223Error.  # noqa: E501


        :return: The message of this InlineResponse4223Error.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse4223Error.


        :param message: The message of this InlineResponse4223Error.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def detail(self):
        """Gets the detail of this InlineResponse4223Error.  # noqa: E501


        :return: The detail of this InlineResponse4223Error.  # noqa: E501
        :rtype: list[Object]
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this InlineResponse4223Error.


        :param detail: The detail of this InlineResponse4223Error.  # noqa: E501
        :type: list[Object]
        """

        self._detail = detail

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
        if issubclass(InlineResponse4223Error, dict):
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
        if not isinstance(other, InlineResponse4223Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
