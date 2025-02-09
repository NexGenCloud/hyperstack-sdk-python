# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.volume_attachment_fields import VolumeAttachmentFields

class TestVolumeAttachmentFields(unittest.TestCase):
    """VolumeAttachmentFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VolumeAttachmentFields:
        """Test VolumeAttachmentFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VolumeAttachmentFields`
        """
        model = VolumeAttachmentFields()
        if include_optional:
            return VolumeAttachmentFields(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                device = '',
                status = '',
                volume = hyperstack.models.volume_fieldsfor_instance.VolumeFieldsforInstance(
                    bootable = True, 
                    description = '', 
                    id = 56, 
                    name = '', 
                    size = 56, 
                    volume_type = '', )
            )
        else:
            return VolumeAttachmentFields(
        )
        """

    def testVolumeAttachmentFields(self):
        """Test VolumeAttachmentFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
