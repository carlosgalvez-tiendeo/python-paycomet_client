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

class CardsDeleteBody(object):
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
        'id_user': 'int',
        'token_user': 'str'
    }

    attribute_map = {
        'terminal': 'terminal',
        'id_user': 'idUser',
        'token_user': 'tokenUser'
    }

    def __init__(self, terminal=None, id_user=None, token_user=None):  # noqa: E501
        """CardsDeleteBody - a model defined in Swagger"""  # noqa: E501
        self._terminal = None
        self._id_user = None
        self._token_user = None
        self.discriminator = None
        self.terminal = terminal
        self.id_user = id_user
        self.token_user = token_user

    @property
    def terminal(self):
        """Gets the terminal of this CardsDeleteBody.  # noqa: E501

        Product or terminal Id.  # noqa: E501

        :return: The terminal of this CardsDeleteBody.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this CardsDeleteBody.

        Product or terminal Id.  # noqa: E501

        :param terminal: The terminal of this CardsDeleteBody.  # noqa: E501
        :type: int
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def id_user(self):
        """Gets the id_user of this CardsDeleteBody.  # noqa: E501

        Identification of user card given by PAYCOMET  # noqa: E501

        :return: The id_user of this CardsDeleteBody.  # noqa: E501
        :rtype: int
        """
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        """Sets the id_user of this CardsDeleteBody.

        Identification of user card given by PAYCOMET  # noqa: E501

        :param id_user: The id_user of this CardsDeleteBody.  # noqa: E501
        :type: int
        """
        if id_user is None:
            raise ValueError("Invalid value for `id_user`, must not be `None`")  # noqa: E501

        self._id_user = id_user

    @property
    def token_user(self):
        """Gets the token_user of this CardsDeleteBody.  # noqa: E501

        Identification of user card given by PAYCOMET  # noqa: E501

        :return: The token_user of this CardsDeleteBody.  # noqa: E501
        :rtype: str
        """
        return self._token_user

    @token_user.setter
    def token_user(self, token_user):
        """Sets the token_user of this CardsDeleteBody.

        Identification of user card given by PAYCOMET  # noqa: E501

        :param token_user: The token_user of this CardsDeleteBody.  # noqa: E501
        :type: str
        """
        if token_user is None:
            raise ValueError("Invalid value for `token_user`, must not be `None`")  # noqa: E501

        self._token_user = token_user

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
        if issubclass(CardsDeleteBody, dict):
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
        if not isinstance(other, CardsDeleteBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
