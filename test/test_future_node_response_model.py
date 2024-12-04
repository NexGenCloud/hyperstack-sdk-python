# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.future_node_response_model import FutureNodeResponseModel

class TestFutureNodeResponseModel(unittest.TestCase):
    """FutureNodeResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FutureNodeResponseModel:
        """Test FutureNodeResponseModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FutureNodeResponseModel`
        """
        model = FutureNodeResponseModel()
        if include_optional:
            return FutureNodeResponseModel(
                nodes = [
                    hyperstack.models.future_node_model.FutureNodeModel(
                        expected_provision_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = 56, 
                        nexgen_name = '', 
                        openstack_name = '', 
                        stocks = [
                            hyperstack.models.future_node_stock_model.FutureNodeStockModel(
                                expected_amount = 56, 
                                id = 56, 
                                name = '', )
                            ], )
                    ],
                region = ''
            )
        else:
            return FutureNodeResponseModel(
        )
        """

    def testFutureNodeResponseModel(self):
        """Test FutureNodeResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
