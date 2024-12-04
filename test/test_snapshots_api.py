# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.api.snapshots_api import SnapshotsApi


class TestSnapshotsApi(unittest.TestCase):
    """SnapshotsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SnapshotsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_snapshot(self) -> None:
        """Test case for delete_snapshot

        Delete snapshot
        """
        pass

    def test_fetch_snapshot_name_availability(self) -> None:
        """Test case for fetch_snapshot_name_availability

        Fetch snapshot name availability
        """
        pass

    def test_restore_a_snapshot(self) -> None:
        """Test case for restore_a_snapshot

        Restore a snapshot
        """
        pass

    def test_retrieve_a_snapshot(self) -> None:
        """Test case for retrieve_a_snapshot

        Retrieve a snapshot
        """
        pass

    def test_retrieve_list_of_snapshots_with_pagination(self) -> None:
        """Test case for retrieve_list_of_snapshots_with_pagination

        Retrieve list of snapshots with pagination
        """
        pass


if __name__ == '__main__':
    unittest.main()