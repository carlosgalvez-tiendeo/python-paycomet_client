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
from swagger_client.api.dcc_api import DccApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDccApi(unittest.TestCase):
    """DccApi unit test stubs"""

    def setUp(self):
        self.api = DccApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dcc_purchase_confirm(self):
        """Test case for dcc_purchase_confirm

        Confirm previous DCC payment  # noqa: E501
        """
        pass

    def test_dcc_purchase_create(self):
        """Test case for dcc_purchase_create

        Create an DCC payment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
