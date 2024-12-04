# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.sub_resource_graph_billing_details_metrics import SubResourceGraphBillingDetailsMetrics

class TestSubResourceGraphBillingDetailsMetrics(unittest.TestCase):
    """SubResourceGraphBillingDetailsMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubResourceGraphBillingDetailsMetrics:
        """Test SubResourceGraphBillingDetailsMetrics
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubResourceGraphBillingDetailsMetrics`
        """
        model = SubResourceGraphBillingDetailsMetrics()
        if include_optional:
            return SubResourceGraphBillingDetailsMetrics(
                cpu_incurred_bill = 1.337,
                cpu_incurred_bill_graph = [
                    hyperstack.models.graph_datetime_value_model.GraphDatetimeValueModel(
                        datetime = '', 
                        value = 1.337, )
                    ],
                disk_incurred_bill = 1.337,
                disk_incurred_bill_graph = [
                    hyperstack.models.graph_datetime_value_model.GraphDatetimeValueModel(
                        datetime = '', 
                        value = 1.337, )
                    ],
                ephemeral_incurred_bill = 1.337,
                ephemeral_incurred_bill_graph = [
                    hyperstack.models.graph_datetime_value_model.GraphDatetimeValueModel(
                        datetime = '', 
                        value = 1.337, )
                    ],
                gpu_incurred_bill = 1.337,
                gpu_incurred_bill_graph = [
                    hyperstack.models.graph_datetime_value_model.GraphDatetimeValueModel(
                        datetime = '', 
                        value = 1.337, )
                    ],
                publicip_incurred_bill = 1.337,
                publicip_incurred_bill_graph = [
                    hyperstack.models.graph_datetime_value_model.GraphDatetimeValueModel(
                        datetime = '', 
                        value = 1.337, )
                    ],
                ram_incurred_bill = 1.337,
                ram_incurred_bill_graph = [
                    hyperstack.models.graph_datetime_value_model.GraphDatetimeValueModel(
                        datetime = '', 
                        value = 1.337, )
                    ]
            )
        else:
            return SubResourceGraphBillingDetailsMetrics(
        )
        """

    def testSubResourceGraphBillingDetailsMetrics(self):
        """Test SubResourceGraphBillingDetailsMetrics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
