# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.snapshot_fields import SnapshotFields

class TestSnapshotFields(unittest.TestCase):
    """SnapshotFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnapshotFields:
        """Test SnapshotFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnapshotFields`
        """
        model = SnapshotFields()
        if include_optional:
            return SnapshotFields(
                description = '',
                has_floating_ip = True,
                id = 56,
                is_image = True,
                labels = [
                    ''
                    ],
                name = '',
                region_id = 56,
                size = 56,
                status = '',
                vm_id = 56
            )
        else:
            return SnapshotFields(
                description = '',
                id = 56,
                is_image = True,
                name = '',
                region_id = 56,
                size = 56,
                status = '',
                vm_id = 56,
        )
        """

    def testSnapshotFields(self):
        """Test SnapshotFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()