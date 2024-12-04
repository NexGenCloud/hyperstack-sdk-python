# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.create_security_rule_payload import CreateSecurityRulePayload

class TestCreateSecurityRulePayload(unittest.TestCase):
    """CreateSecurityRulePayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSecurityRulePayload:
        """Test CreateSecurityRulePayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSecurityRulePayload`
        """
        model = CreateSecurityRulePayload()
        if include_optional:
            return CreateSecurityRulePayload(
                direction = '',
                ethertype = '',
                protocol = 'any',
                remote_ip_prefix = '',
                port_range_min = 56,
                port_range_max = 56
            )
        else:
            return CreateSecurityRulePayload(
                direction = '',
                ethertype = '',
                protocol = 'any',
                remote_ip_prefix = '',
        )
        """

    def testCreateSecurityRulePayload(self):
        """Test CreateSecurityRulePayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
