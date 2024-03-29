# coding: utf-8

"""
    dtool-lookup-server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

import unittest

import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api.mongo_api import MongoApi  # noqa: E501


class TestMongoApi(unittest.TestCase):
    """MongoApi unit test stubs"""

    def setUp(self):
        self.api = MongoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_mongo_aggregate_post(self):
        """Test case for mongo_aggregate_post

        Aggregate the datasets a user has access to.  # noqa: E501
        """
        pass

    def test_mongo_config_get(self):
        """Test case for mongo_config_get

        Return the JSON-serialized plugin configuration.  # noqa: E501
        """
        pass

    def test_mongo_query_post(self):
        """Test case for mongo_query_post

        Query datasets a user has access to.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
