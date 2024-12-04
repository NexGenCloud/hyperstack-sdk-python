# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.api.credit_api import CreditApi


class TestCreditApi(unittest.TestCase):
    """CreditApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CreditApi()

    def tearDown(self) -> None:
        pass

    def test_get_view_credit_and_threshold(self) -> None:
        """Test case for get_view_credit_and_threshold

        GET: View credit and threshold
        """
        pass


if __name__ == '__main__':
    unittest.main()
