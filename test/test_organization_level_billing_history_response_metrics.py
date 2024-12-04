# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.organization_level_billing_history_response_metrics import OrganizationLevelBillingHistoryResponseMetrics

class TestOrganizationLevelBillingHistoryResponseMetrics(unittest.TestCase):
    """OrganizationLevelBillingHistoryResponseMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationLevelBillingHistoryResponseMetrics:
        """Test OrganizationLevelBillingHistoryResponseMetrics
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationLevelBillingHistoryResponseMetrics`
        """
        model = OrganizationLevelBillingHistoryResponseMetrics()
        if include_optional:
            return OrganizationLevelBillingHistoryResponseMetrics(
                contract_cost = 1.337,
                incurred_bill = 1.337,
                non_discounted_bill = 1.337,
                snapshot_cost = 1.337,
                vm_cost = 1.337,
                volume_cost = 1.337
            )
        else:
            return OrganizationLevelBillingHistoryResponseMetrics(
        )
        """

    def testOrganizationLevelBillingHistoryResponseMetrics(self):
        """Test OrganizationLevelBillingHistoryResponseMetrics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
