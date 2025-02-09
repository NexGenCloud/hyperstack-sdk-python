# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.api.volume_api import VolumeApi


class TestVolumeApi(unittest.TestCase):
    """VolumeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VolumeApi()

    def tearDown(self) -> None:
        pass

    def test_create_volume(self) -> None:
        """Test case for create_volume

        Create volume
        """
        pass

    def test_delete_volume(self) -> None:
        """Test case for delete_volume

        Delete volume
        """
        pass

    def test_fetch_volume_details(self) -> None:
        """Test case for fetch_volume_details

        Fetch Volume Details
        """
        pass

    def test_fetch_volume_name_availability(self) -> None:
        """Test case for fetch_volume_name_availability

        Fetch volume name availability
        """
        pass

    def test_list_volume_types(self) -> None:
        """Test case for list_volume_types

        List volume types
        """
        pass

    def test_list_volumes(self) -> None:
        """Test case for list_volumes

        List volumes
        """
        pass


if __name__ == '__main__':
    unittest.main()
