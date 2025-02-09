# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.users_info_fields import UsersInfoFields

class TestUsersInfoFields(unittest.TestCase):
    """UsersInfoFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsersInfoFields:
        """Test UsersInfoFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsersInfoFields`
        """
        model = UsersInfoFields()
        if include_optional:
            return UsersInfoFields(
                billing_address1 = '',
                billing_address2 = '',
                business = True,
                company_name = '',
                country = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                email = '',
                id = 56,
                name = '',
                organization_id = 56,
                phone = '',
                state = '',
                vat_number = '',
                zip_code = ''
            )
        else:
            return UsersInfoFields(
        )
        """

    def testUsersInfoFields(self):
        """Test UsersInfoFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
