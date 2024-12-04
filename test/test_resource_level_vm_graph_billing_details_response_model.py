# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.resource_level_vm_graph_billing_details_response_model import ResourceLevelVmGraphBillingDetailsResponseModel

class TestResourceLevelVmGraphBillingDetailsResponseModel(unittest.TestCase):
    """ResourceLevelVmGraphBillingDetailsResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceLevelVmGraphBillingDetailsResponseModel:
        """Test ResourceLevelVmGraphBillingDetailsResponseModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceLevelVmGraphBillingDetailsResponseModel`
        """
        model = ResourceLevelVmGraphBillingDetailsResponseModel()
        if include_optional:
            return ResourceLevelVmGraphBillingDetailsResponseModel(
                billing_history_vm_details = hyperstack.models.resource_level_graph_billing_details_vm.ResourceLevelGraphBillingDetailsVM(
                    billing_history = [
                        hyperstack.models.resource_level_graph_billing_vm_details_resources.ResourceLevelGraphBillingVMDetailsResources(
                            attributes = hyperstack.models.resource_level_graph_billing_details_attributes.ResourceLevelGraphBillingDetailsAttributes(
                                id = '', 
                                infrahub_id = 56, 
                                resource_name = '', ), 
                            metrics = hyperstack.models.resource_level_graph_billing_details_metrics.ResourceLevelGraphBillingDetailsMetrics(
                                incurred_bill = 1.337, 
                                incurred_bill_graph = [
                                    hyperstack.models.graph_datetime_value_model.GraphDatetimeValueModel(
                                        datetime = '', 
                                        value = 1.337, )
                                    ], ), )
                        ], 
                    granularity = 56, 
                    org_id = 56, 
                    total_count = 56, ),
                message = '',
                status = True
            )
        else:
            return ResourceLevelVmGraphBillingDetailsResponseModel(
        )
        """

    def testResourceLevelVmGraphBillingDetailsResponseModel(self):
        """Test ResourceLevelVmGraphBillingDetailsResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
