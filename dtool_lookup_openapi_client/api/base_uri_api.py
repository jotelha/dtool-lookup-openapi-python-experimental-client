# coding: utf-8

"""
    dtool-lookup-server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

from dtool_lookup_openapi_client.api_client import ApiClient
from dtool_lookup_openapi_client.api.base_uri_api_endpoints.admin_base_uri_list_get import AdminBaseUriListGet
from dtool_lookup_openapi_client.api.base_uri_api_endpoints.admin_base_uri_register_post import AdminBaseUriRegisterPost


class BaseUriApi(
    AdminBaseUriListGet,
    AdminBaseUriRegisterPost,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass