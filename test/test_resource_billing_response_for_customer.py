# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.resource_billing_response_for_customer import ResourceBillingResponseForCustomer

class TestResourceBillingResponseForCustomer(unittest.TestCase):
    """ResourceBillingResponseForCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceBillingResponseForCustomer:
        """Test ResourceBillingResponseForCustomer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceBillingResponseForCustomer`
        """
        model = ResourceBillingResponseForCustomer()
        if include_optional:
            return ResourceBillingResponseForCustomer(
                calculated_resource_bills = hyperstack.models.resource_object_response_for_customer.ResourceObjectResponseForCustomer(
                    org_id = 56, 
                    resource = hyperstack.models.infrahub_resource_object_response_for_customer.InfrahubResourceObjectResponseForCustomer(
                        actual_price = 1.337, 
                        host = '', 
                        infrahub_id = 56, 
                        name = '', 
                        price = 1.337, 
                        resources = [
                            hyperstack.models.pricebook_resource_object_response_for_customer.PricebookResourceObjectResponseForCustomer(
                                actual_price = 1.337, 
                                amount = 56, 
                                discounted_rate = 1.337, 
                                name = '', 
                                price = 1.337, 
                                rate = 1.337, 
                                type = '', )
                            ], 
                        status = '', 
                        type = '', ), ),
                message = '',
                status = True
            )
        else:
            return ResourceBillingResponseForCustomer(
        )
        """

    def testResourceBillingResponseForCustomer(self):
        """Test ResourceBillingResponseForCustomer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()