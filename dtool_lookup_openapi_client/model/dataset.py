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


class Dataset(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'creator_username',
        'name',
        'frozen_at',
        'uri',
        'uuid',
        'created_at',
    ))
    
    
    class creator_username(
        _SchemaValidator(
            max_length=255,
        ),
        StrSchema
    ):
        pass
    
    
    class name(
        _SchemaValidator(
            max_length=80,
        ),
        StrSchema
    ):
        pass
    frozen_at = DateTimeSchema
    
    
    class uri(
        _SchemaValidator(
            max_length=255,
        ),
        StrSchema
    ):
        pass
    
    
    class uuid(
        _SchemaValidator(
            max_length=36,
        ),
        StrSchema
    ):
        pass
    created_at = DateTimeSchema
    base_uri = AnyTypeSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        creator_username: creator_username,
        name: name,
        frozen_at: frozen_at,
        uri: uri,
        uuid: uuid,
        created_at: created_at,
        base_uri: typing.Union[base_uri, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'Dataset':
        return super().__new__(
            cls,
            *args,
            creator_username=creator_username,
            name=name,
            frozen_at=frozen_at,
            uri=uri,
            uuid=uuid,
            created_at=created_at,
            base_uri=base_uri,
            _configuration=_configuration,
            **kwargs,
        )