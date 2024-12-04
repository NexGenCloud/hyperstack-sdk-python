# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.instances_summary_fields import InstancesSummaryFields

class TestInstancesSummaryFields(unittest.TestCase):
    """InstancesSummaryFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstancesSummaryFields:
        """Test InstancesSummaryFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstancesSummaryFields`
        """
        model = InstancesSummaryFields()
        if include_optional:
            return InstancesSummaryFields(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                environment = '',
                environment_id = 56,
                fixed_ip = '',
                flavor = '',
                flavor_id = 56,
                floating_ip = '',
                floating_ip_status = '',
                id = 56,
                image = '',
                image_id = 56,
                keypair = '',
                keypair_id = 56,
                name = '',
                org_id = 56,
                status = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return InstancesSummaryFields(
        )
        """

    def testInstancesSummaryFields(self):
        """Test InstancesSummaryFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
