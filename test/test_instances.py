# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.instances import Instances

class TestInstances(unittest.TestCase):
    """Instances unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Instances:
        """Test Instances
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Instances`
        """
        model = Instances()
        if include_optional:
            return Instances(
                count = 56,
                instances = [
                    hyperstack.models.instance_fields.InstanceFields(
                        contract_id = 56, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        environment = hyperstack.models.instance_environment_fields.InstanceEnvironmentFields(
                            features = hyperstack.models.environment_features.EnvironmentFeatures(
                                network_optimised = True, ), 
                            id = 56, 
                            name = '', 
                            org_id = 56, 
                            region = '', ), 
                        fixed_ip = '', 
                        flavor = hyperstack.models.instance_flavor_fields.InstanceFlavorFields(
                            cpu = 56, 
                            disk = 56, 
                            ephemeral = 56, 
                            gpu = '', 
                            gpu_count = 56, 
                            id = 56, 
                            name = '', 
                            ram = 1.337, ), 
                        floating_ip = '', 
                        floating_ip_status = '', 
                        id = 56, 
                        image = hyperstack.models.instance_image_fields.InstanceImageFields(
                            name = '', ), 
                        keypair = hyperstack.models.instance_keypair_fields.InstanceKeypairFields(
                            name = '', ), 
                        labels = [
                            ''
                            ], 
                        locked = True, 
                        name = '', 
                        os = '', 
                        power_state = '', 
                        security_rules = [
                            hyperstack.models.security_rules_fieldsfor_instance.SecurityRulesFieldsforInstance(
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                direction = '', 
                                ethertype = '', 
                                id = 56, 
                                port_range_max = 56, 
                                port_range_min = 56, 
                                protocol = '', 
                                remote_ip_prefix = '', 
                                status = '', )
                            ], 
                        status = '', 
                        vm_state = '', 
                        volume_attachments = [
                            hyperstack.models.volume_attachment_fields.VolumeAttachmentFields(
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                device = '', 
                                status = '', 
                                volume = hyperstack.models.volume_fieldsfor_instance.VolumeFieldsforInstance(
                                    bootable = True, 
                                    description = '', 
                                    id = 56, 
                                    name = '', 
                                    size = 56, 
                                    volume_type = '', ), )
                            ], )
                    ],
                message = '',
                page = 56,
                page_size = 56,
                status = True
            )
        else:
            return Instances(
        )
        """

    def testInstances(self):
        """Test Instances"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()