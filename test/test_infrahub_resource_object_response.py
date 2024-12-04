# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.infrahub_resource_object_response import InfrahubResourceObjectResponse

class TestInfrahubResourceObjectResponse(unittest.TestCase):
    """InfrahubResourceObjectResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InfrahubResourceObjectResponse:
        """Test InfrahubResourceObjectResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InfrahubResourceObjectResponse`
        """
        model = InfrahubResourceObjectResponse()
        if include_optional:
            return InfrahubResourceObjectResponse(
                actual_host_price = 1.337,
                actual_price = 1.337,
                contract_id = 56,
                host = '',
                host_price = 1.337,
                infrahub_id = 56,
                name = '',
                nexgen_actual_price = 1.337,
                nexgen_price = 1.337,
                price = 1.337,
                resources = [
                    hyperstack.models.pricebook_resource_object_response.PricebookResourceObjectResponse(
                        actual_price = 1.337, 
                        amount = 56, 
                        discounted_rate = 1.337, 
                        host_original_price = 1.337, 
                        host_price = 1.337, 
                        name = '', 
                        nexgen_original_price = 1.337, 
                        nexgen_price = 1.337, 
                        price = 1.337, 
                        rate = 1.337, 
                        type = '', )
                    ],
                status = '',
                type = ''
            )
        else:
            return InfrahubResourceObjectResponse(
        )
        """

    def testInfrahubResourceObjectResponse(self):
        """Test InfrahubResourceObjectResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
