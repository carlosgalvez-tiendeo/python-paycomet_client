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
from swagger_client.api.marketplace_api import MarketplaceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMarketplaceApi(unittest.TestCase):
    """MarketplaceApi unit test stubs"""

    def setUp(self):
        self.api = MarketplaceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_split_transfer(self):
        """Test case for split_transfer

        Make a transfer to other accounts on PAYCOMET  # noqa: E501
        """
        pass

    def test_split_transfer_reversal(self):
        """Test case for split_transfer_reversal

        Run a split transfer reversal based on a previous split transfer  # noqa: E501
        """
        pass

    def test_transfer(self):
        """Test case for transfer

        Run a transfer  # noqa: E501
        """
        pass

    def test_transfer_reversal(self):
        """Test case for transfer_reversal

        Make a transfer reversal based on a previous transfer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
