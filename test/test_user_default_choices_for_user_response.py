# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.user_default_choices_for_user_response import UserDefaultChoicesForUserResponse

class TestUserDefaultChoicesForUserResponse(unittest.TestCase):
    """UserDefaultChoicesForUserResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserDefaultChoicesForUserResponse:
        """Test UserDefaultChoicesForUserResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserDefaultChoicesForUserResponse`
        """
        model = UserDefaultChoicesForUserResponse()
        if include_optional:
            return UserDefaultChoicesForUserResponse(
                message = '',
                status = True,
                user_default_choices = [
                    hyperstack.models.user_default_choice_for_user_fields.UserDefaultChoiceForUserFields(
                        flavor_id = 56, 
                        image_id = 56, 
                        keypair_id = 56, )
                    ]
            )
        else:
            return UserDefaultChoicesForUserResponse(
        )
        """

    def testUserDefaultChoicesForUserResponse(self):
        """Test UserDefaultChoicesForUserResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
