# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.flavor_fields import FlavorFields

class TestFlavorFields(unittest.TestCase):
    """FlavorFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlavorFields:
        """Test FlavorFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlavorFields`
        """
        model = FlavorFields()
        if include_optional:
            return FlavorFields(
                cpu = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                disk = 56,
                display_name = '',
                ephemeral = 56,
                gpu = '',
                gpu_count = 56,
                id = 56,
                labels = [
                    hyperstack.models.lable_resonse.LableResonse(
                        id = 56, 
                        label = '', )
                    ],
                name = '',
                ram = 1.337,
                region_name = '',
                stock_available = True
            )
        else:
            return FlavorFields(
        )
        """

    def testFlavorFields(self):
        """Test FlavorFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
