# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.node_stock_response_model import NodeStockResponseModel

class TestNodeStockResponseModel(unittest.TestCase):
    """NodeStockResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeStockResponseModel:
        """Test NodeStockResponseModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeStockResponseModel`
        """
        model = NodeStockResponseModel()
        if include_optional:
            return NodeStockResponseModel(
                stocks = [
                    hyperstack.models.node_response_model.NodeResponseModel(
                        nodes = [
                            hyperstack.models.node_model.NodeModel(
                                flavors = [
                                    ''
                                    ], 
                                nexgen_name = '', 
                                openstack_id = '', 
                                openstack_name = '', 
                                organizations = [
                                    56
                                    ], 
                                projects = [
                                    ''
                                    ], 
                                provision_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                status = '', 
                                stocks = [
                                    hyperstack.models.node_stocks_payload.NodeStocksPayload(
                                        in_use = 56, 
                                        name = '', 
                                        total = 56, 
                                        type = '', )
                                    ], 
                                sunset_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        region = '', )
                    ]
            )
        else:
            return NodeStockResponseModel(
        )
        """

    def testNodeStockResponseModel(self):
        """Test NodeStockResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()