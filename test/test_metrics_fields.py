# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.metrics_fields import MetricsFields

class TestMetricsFields(unittest.TestCase):
    """MetricsFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetricsFields:
        """Test MetricsFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetricsFields`
        """
        model = MetricsFields()
        if include_optional:
            return MetricsFields(
                cpu = hyperstack.models.metric_item_fields.MetricItemFields(
                    columns = ["time","granularity","value"], 
                    data = [["2023-09-01T01:19:00+00:00",60,1041433070000000],["2023-09-01T01:24:00+00:00",60,1041441320000000]], 
                    unit = '', ),
                disk_read = hyperstack.models.metric_item_fields.MetricItemFields(
                    columns = ["time","granularity","value"], 
                    data = [["2023-09-01T01:19:00+00:00",60,1041433070000000],["2023-09-01T01:24:00+00:00",60,1041441320000000]], 
                    unit = '', ),
                disk_write = hyperstack.models.metric_item_fields.MetricItemFields(
                    columns = ["time","granularity","value"], 
                    data = [["2023-09-01T01:19:00+00:00",60,1041433070000000],["2023-09-01T01:24:00+00:00",60,1041441320000000]], 
                    unit = '', ),
                memory_usages = hyperstack.models.metric_item_fields.MetricItemFields(
                    columns = ["time","granularity","value"], 
                    data = [["2023-09-01T01:19:00+00:00",60,1041433070000000],["2023-09-01T01:24:00+00:00",60,1041441320000000]], 
                    unit = '', ),
                network_in = hyperstack.models.metric_item_fields.MetricItemFields(
                    columns = ["time","granularity","value"], 
                    data = [["2023-09-01T01:19:00+00:00",60,1041433070000000],["2023-09-01T01:24:00+00:00",60,1041441320000000]], 
                    unit = '', ),
                network_out = hyperstack.models.metric_item_fields.MetricItemFields(
                    columns = ["time","granularity","value"], 
                    data = [["2023-09-01T01:19:00+00:00",60,1041433070000000],["2023-09-01T01:24:00+00:00",60,1041441320000000]], 
                    unit = '', )
            )
        else:
            return MetricsFields(
        )
        """

    def testMetricsFields(self):
        """Test MetricsFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
