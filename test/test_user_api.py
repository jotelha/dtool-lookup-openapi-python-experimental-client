# coding: utf-8

"""
    dtool-lookup-server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

import unittest

import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api.user_api import UserApi  # noqa: E501


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_info_username_get(self):
        """Test case for user_info_username_get

        Return a user's information.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
