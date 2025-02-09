# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.dashboard_info_response import DashboardInfoResponse

class TestDashboardInfoResponse(unittest.TestCase):
    """DashboardInfoResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DashboardInfoResponse:
        """Test DashboardInfoResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DashboardInfoResponse`
        """
        model = DashboardInfoResponse()
        if include_optional:
            return DashboardInfoResponse(
                message = '',
                overview = hyperstack.models.overview_info.OverviewInfo(
                    container = hyperstack.models.container_overview_fields.ContainerOverviewFields(
                        cost_per_hour = 1.337, 
                        count = 56, 
                        gpus = 56, 
                        ram = 1.337, 
                        vcpus = 56, ), 
                    instance = hyperstack.models.instance_overview_fields.InstanceOverviewFields(
                        cost_per_hour = 1.337, 
                        count = 56, 
                        gpus = 56, 
                        ram = 1.337, 
                        vcpus = 56, ), 
                    volume = hyperstack.models.volume_overview_fields.VolumeOverviewFields(
                        cost_per_hour = 1.337, 
                        count = 56, 
                        using = 56, ), ),
                status = True
            )
        else:
            return DashboardInfoResponse(
        )
        """

    def testDashboardInfoResponse(self):
        """Test DashboardInfoResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
