# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.get_all_discounts_fields import GetAllDiscountsFields

class TestGetAllDiscountsFields(unittest.TestCase):
    """GetAllDiscountsFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAllDiscountsFields:
        """Test GetAllDiscountsFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAllDiscountsFields`
        """
        model = GetAllDiscountsFields()
        if include_optional:
            return GetAllDiscountsFields(
                discount_resources = [
                    hyperstack.models.discount_resource_fields.DiscountResourceFields(
                        discount_amount = 1.337, 
                        discount_percent = 1.337, 
                        discount_type = '', 
                        resource_id = 56, )
                    ],
                discount_status = '',
                end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                org_id = 56,
                org_name = '',
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GetAllDiscountsFields(
        )
        """

    def testGetAllDiscountsFields(self):
        """Test GetAllDiscountsFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
