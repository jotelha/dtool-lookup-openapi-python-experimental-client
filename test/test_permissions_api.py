# coding: utf-8

"""
    dtool-lookup-server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

import unittest

import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api.permissions_api import PermissionsApi  # noqa: E501


class TestPermissionsApi(unittest.TestCase):
    """PermissionsApi unit test stubs"""

    def setUp(self):
        self.api = PermissionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_permission_info_post(self):
        """Test case for admin_permission_info_post

        Get information about the permissions on a base URI.  # noqa: E501
        """
        pass

    def test_admin_permission_update_on_base_uri_post(self):
        """Test case for admin_permission_update_on_base_uri_post

        Update the permissions on a base URI.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()