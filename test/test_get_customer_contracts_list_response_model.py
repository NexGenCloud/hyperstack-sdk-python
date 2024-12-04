# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.get_customer_contracts_list_response_model import GetCustomerContractsListResponseModel

class TestGetCustomerContractsListResponseModel(unittest.TestCase):
    """GetCustomerContractsListResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCustomerContractsListResponseModel:
        """Test GetCustomerContractsListResponseModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCustomerContractsListResponseModel`
        """
        model = GetCustomerContractsListResponseModel()
        if include_optional:
            return GetCustomerContractsListResponseModel(
                contracts = [
                    hyperstack.models.customer_contract_fields.CustomerContractFields(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        discounts = [
                            hyperstack.models.contract_discount_plan_fields.ContractDiscountPlanFields(
                                discount_amount = 1.337, 
                                discount_code = '', 
                                discount_percent = 1.337, 
                                discount_status = '', 
                                discount_type = '', 
                                id = 56, 
                                resource_count = 56, 
                                resource_id = 56, 
                                resource_name = '', )
                            ], 
                        end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiration_policy = 56, 
                        id = 56, 
                        org_id = 56, 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = '', )
                    ],
                count = 56,
                message = '',
                status = True
            )
        else:
            return GetCustomerContractsListResponseModel(
        )
        """

    def testGetCustomerContractsListResponseModel(self):
        """Test GetCustomerContractsListResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
