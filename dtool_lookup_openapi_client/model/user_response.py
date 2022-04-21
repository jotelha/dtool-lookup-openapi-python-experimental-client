# coding: utf-8

"""
    dtool-lookup-server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from dtool_lookup_openapi_client.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class UserResponse(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    
    class register_permissions_on_base_uris(
        ListSchema
    ):
        _items = StrSchema
    
    
    class search_permissions_on_base_uris(
        ListSchema
    ):
        _items = StrSchema
    username = StrSchema
    is_admin = BoolSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        register_permissions_on_base_uris: typing.Union[register_permissions_on_base_uris, Unset] = unset,
        search_permissions_on_base_uris: typing.Union[search_permissions_on_base_uris, Unset] = unset,
        username: typing.Union[username, Unset] = unset,
        is_admin: typing.Union[is_admin, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'UserResponse':
        return super().__new__(
            cls,
            *args,
            register_permissions_on_base_uris=register_permissions_on_base_uris,
            search_permissions_on_base_uris=search_permissions_on_base_uris,
            username=username,
            is_admin=is_admin,
            _configuration=_configuration,
            **kwargs,
        )
