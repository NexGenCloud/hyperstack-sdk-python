# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.create_update_compliance_response import CreateUpdateComplianceResponse

class TestCreateUpdateComplianceResponse(unittest.TestCase):
    """CreateUpdateComplianceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateUpdateComplianceResponse:
        """Test CreateUpdateComplianceResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateUpdateComplianceResponse`
        """
        model = CreateUpdateComplianceResponse()
        if include_optional:
            return CreateUpdateComplianceResponse(
                compliance = hyperstack.models.compliance_model_fields.ComplianceModelFields(
                    base_value = 56, 
                    gpu_model = '', 
                    id = 56, 
                    resource_type = '', 
                    variation_max = 56, 
                    variation_min = 56, 
                    variation_unit = 56, ),
                message = '',
                status = True
            )
        else:
            return CreateUpdateComplianceResponse(
        )
        """

    def testCreateUpdateComplianceResponse(self):
        """Test CreateUpdateComplianceResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
