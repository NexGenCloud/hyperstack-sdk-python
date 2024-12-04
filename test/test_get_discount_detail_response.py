# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.get_discount_detail_response import GetDiscountDetailResponse

class TestGetDiscountDetailResponse(unittest.TestCase):
    """GetDiscountDetailResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDiscountDetailResponse:
        """Test GetDiscountDetailResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDiscountDetailResponse`
        """
        model = GetDiscountDetailResponse()
        if include_optional:
            return GetDiscountDetailResponse(
                discounts_entity = hyperstack.models.discount_entity_model.DiscountEntityModel(
                    data = [
                        hyperstack.models.discount_plan_fields.DiscountPlanFields(
                            discount_amount = 1.337, 
                            discount_code = '', 
                            discount_percent = 1.337, 
                            discount_status = '', 
                            discount_type = '', 
                            end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = 56, 
                            resource = '', 
                            start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            validity_days = 56, 
                            vm_id = 56, )
                        ], 
                    entity = '', ),
                message = '',
                status = True
            )
        else:
            return GetDiscountDetailResponse(
        )
        """

    def testGetDiscountDetailResponse(self):
        """Test GetDiscountDetailResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
