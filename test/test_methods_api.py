# coding: utf-8

"""
    PAYCOMET REST API

    PAYCOMET API REST for customers.  # noqa: E501

    OpenAPI spec version: 2.28.0
    Contact: tecnico@paycomet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import paycomet_client
from paycomet_client.api.methods_api import MethodsApi  # noqa: E501
from paycomet_client.rest import ApiException


class TestMethodsApi(unittest.TestCase):
    """MethodsApi unit test stubs"""

    def setUp(self):
        self.api = MethodsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_user_payment_methods(self):
        """Test case for get_user_payment_methods

        Retrieves product methods  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
