# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.api.billing_api import BillingApi


class TestBillingApi(unittest.TestCase):
    """BillingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BillingApi()

    def tearDown(self) -> None:
        pass

    def test_get_all_thresholds_for_organization(self) -> None:
        """Test case for get_all_thresholds_for_organization

        GET: All Thresholds for Organization
        """
        pass

    def test_get_billing_usage(self) -> None:
        """Test case for get_billing_usage

        GET: Billing usage
        """
        pass

    def test_get_last_day_cost(self) -> None:
        """Test case for get_last_day_cost

        GET: Last Day Cost
        """
        pass

    def test_retrieve_billing_history_for_a_specific_billing_cycle(self) -> None:
        """Test case for retrieve_billing_history_for_a_specific_billing_cycle

        Retrieve Billing History for a specific Billing Cycle
        """
        pass

    def test_retrieve_billing_history_of_a_specific_snapshot_for_a_specific_billing_cycle(self) -> None:
        """Test case for retrieve_billing_history_of_a_specific_snapshot_for_a_specific_billing_cycle

        Retrieve Billing History of a Specific Snapshot for a specific Billing Cycle
        """
        pass

    def test_retrieve_billing_history_of_a_specific_virtual_machine_for_a_specific_billing_cycle(self) -> None:
        """Test case for retrieve_billing_history_of_a_specific_virtual_machine_for_a_specific_billing_cycle

        Retrieve Billing History of a Specific Virtual Machine for a specific Billing Cycle
        """
        pass

    def test_retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle(self) -> None:
        """Test case for retrieve_billing_history_of_a_specific_volume_for_a_specific_billing_cycle

        Retrieve Billing History of a Specific Volume for a specific Billing Cycle
        """
        pass

    def test_retrieve_billing_history_of_contract_for_a_specific_billing_cycle(self) -> None:
        """Test case for retrieve_billing_history_of_contract_for_a_specific_billing_cycle

        Retrieve Billing History of Contract for a specific Billing Cycle
        """
        pass

    def test_retrieve_billing_history_of_snapshot_for_a_specific_billing_cycle(self) -> None:
        """Test case for retrieve_billing_history_of_snapshot_for_a_specific_billing_cycle

        Retrieve Billing History of Snapshot for a specific Billing Cycle
        """
        pass

    def test_retrieve_billing_history_of_virtual_machine_for_a_specific_billing_cycle(self) -> None:
        """Test case for retrieve_billing_history_of_virtual_machine_for_a_specific_billing_cycle

        Retrieve Billing History of Virtual Machine for a specific Billing Cycle
        """
        pass

    def test_retrieve_billing_history_of_volume_for_a_specific_billing_cycle(self) -> None:
        """Test case for retrieve_billing_history_of_volume_for_a_specific_billing_cycle

        Retrieve Billing History of Volume for a specific Billing Cycle
        """
        pass

    def test_retrieve_hourly_cost_datapoints_of_a_specific_snapshot_for_a_specific_billing_cycle(self) -> None:
        """Test case for retrieve_hourly_cost_datapoints_of_a_specific_snapshot_for_a_specific_billing_cycle

        Retrieve hourly cost datapoints of a Specific Snapshot for a specific billing cycle
        """
        pass

    def test_retrieve_hourly_cost_datapoints_of_a_specific_virtual_machine_for_a_specific_billing_cycle(self) -> None:
        """Test case for retrieve_hourly_cost_datapoints_of_a_specific_virtual_machine_for_a_specific_billing_cycle

        Retrieve hourly cost datapoints of a Specific Virtual Machine for a specific billing cycle
        """
        pass

    def test_retrieve_hourly_cost_datapoints_of_a_specific_volume_for_a_specific_billing_cycle(self) -> None:
        """Test case for retrieve_hourly_cost_datapoints_of_a_specific_volume_for_a_specific_billing_cycle

        Retrieve hourly cost datapoints of a Specific Volume for a specific billing cycle
        """
        pass

    def test_retrieve_sub_resources_historical_cost_datapoints_of_a_virtual(self) -> None:
        """Test case for retrieve_sub_resources_historical_cost_datapoints_of_a_virtual

        Retrieve Sub-Resources Historical Cost datapoints of a Virtual
        """
        pass

    def test_retrieve_total_costs_and_non_discount_costs_for_sub_resources(self) -> None:
        """Test case for retrieve_total_costs_and_non_discount_costs_for_sub_resources

        Retrieve Total Costs and Non Discount Costs for Sub Resources
        """
        pass

    def test_retrieve_vm_billing_events_history(self) -> None:
        """Test case for retrieve_vm_billing_events_history

        Retrieve VM billing events history
        """
        pass

    def test_retrieve_volume_billing_events_history(self) -> None:
        """Test case for retrieve_volume_billing_events_history

        Retrieve Volume billing events history
        """
        pass

    def test_update_subscribe_or_unsubscribe_notification_threshold(self) -> None:
        """Test case for update_subscribe_or_unsubscribe_notification_threshold

        Update: Subscribe or Unsubscribe Notification Threshold
        """
        pass


if __name__ == '__main__':
    unittest.main()
