# coding: utf-8

"""
    dtool-lookup-server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

from dtool_lookup_openapi_client.api_client import ApiClient
from dtool_lookup_openapi_client.api.user_admin_api_endpoints.admin_user_list_get import AdminUserListGet
from dtool_lookup_openapi_client.api.user_admin_api_endpoints.admin_user_register_post import AdminUserRegisterPost


class UserAdminApi(
    AdminUserListGet,
    AdminUserRegisterPost,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass