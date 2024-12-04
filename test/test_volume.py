# coding: utf-8

"""
    Infrahub-API

    Leverage the Infrahub API and Hyperstack platform to easily create, manage, and scale powerful GPU virtual machines and their associated resources.   Access this SDK to automate the deployment of your workloads and streamline your infrastructure management.  To contribute, please raise an issue with a bug report, feature request, feedback, or general inquiry.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.volume import Volume

class TestVolume(unittest.TestCase):
    """Volume unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Volume:
        """Test Volume
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Volume`
        """
        model = Volume()
        if include_optional:
            return Volume(
                message = '',
                status = True,
                volume = hyperstack.models.volume_fields.VolumeFields(
                    bootable = True, 
                    callback_url = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = '', 
                    environment = hyperstack.models.environment_fieldsfor_volume.EnvironmentFieldsforVolume(
                        name = '', ), 
                    id = 56, 
                    image_id = 56, 
                    name = '', 
                    os_image = '', 
                    size = 56, 
                    status = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    volume_type = '', )
            )
        else:
            return Volume(
        )
        """

    def testVolume(self):
        """Test Volume"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
