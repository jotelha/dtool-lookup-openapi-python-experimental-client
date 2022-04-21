# coding: utf-8

"""
    dtool-lookup-server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

from dtool_lookup_openapi_client.api_client import ApiClient
from dtool_lookup_openapi_client.api.graph_api_endpoints.graph_config_get import GraphConfigGet
from dtool_lookup_openapi_client.api.graph_api_endpoints.graph_lookup_uuid_get import GraphLookupUuidGet
from dtool_lookup_openapi_client.api.graph_api_endpoints.graph_lookup_uuid_post import GraphLookupUuidPost


class GraphApi(
    GraphConfigGet,
    GraphLookupUuidGet,
    GraphLookupUuidPost,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass