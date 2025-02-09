# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.api.cluster_events_api import ClusterEventsApi


class TestClusterEventsApi(unittest.TestCase):
    """ClusterEventsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ClusterEventsApi()

    def tearDown(self) -> None:
        pass

    def test_fetch_all_of_a_cluster_events(self) -> None:
        """Test case for fetch_all_of_a_cluster_events

        Fetch all of a cluster events
        """
        pass


if __name__ == '__main__':
    unittest.main()
