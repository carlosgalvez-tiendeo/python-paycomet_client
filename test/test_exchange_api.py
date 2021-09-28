# coding: utf-8

"""
    PAYCOMET REST API

    PAYCOMET API REST for customers.  # noqa: E501

    OpenAPI spec version: 2.34.0
    Contact: tecnico@paycomet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.exchange_api import ExchangeApi  # noqa: E501
from swagger_client.rest import ApiException


class TestExchangeApi(unittest.TestCase):
    """ExchangeApi unit test stubs"""

    def setUp(self):
        self.api = ExchangeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_exchange(self):
        """Test case for exchange

        Converts a certain amount from a currency to another.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
