# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.organization_fields import OrganizationFields

class TestOrganizationFields(unittest.TestCase):
    """OrganizationFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationFields:
        """Test OrganizationFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationFields`
        """
        model = OrganizationFields()
        if include_optional:
            return OrganizationFields(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                credit = 56,
                id = 56,
                name = '',
                threshold = 56,
                total_clusters = 56,
                total_containers = 56,
                total_instances = 56,
                total_volumes = 56,
                users = [
                    hyperstack.models.organization_user_response_model.OrganizationUserResponseModel(
                        email = '', 
                        id = 56, 
                        joined_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        rbac_roles = [
                            hyperstack.models.rbac_role_field.RbacRoleField(
                                name = '', )
                            ], 
                        role = '', 
                        sub = '', 
                        username = '', )
                    ]
            )
        else:
            return OrganizationFields(
                id = 56,
                name = '',
        )
        """

    def testOrganizationFields(self):
        """Test OrganizationFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
