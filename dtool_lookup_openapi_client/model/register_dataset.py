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


class RegisterDataset(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    
    class tags(
        ListSchema
    ):
        _items = StrSchema

    @classmethod
    @property
    def manifest(cls) -> typing.Type['Manifest']:
        return Manifest
    creator_username = StrSchema
    readme = DictSchema
    type = StrSchema
    name = StrSchema
    frozen_at = StrSchema
    uuid = UUIDSchema
    uri = StrSchema
    created_at = StrSchema
    base_uri = StrSchema
    annotations = DictSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        tags: typing.Union[tags, Unset] = unset,
        manifest: typing.Union['Manifest', Unset] = unset,
        creator_username: typing.Union[creator_username, Unset] = unset,
        readme: typing.Union[readme, Unset] = unset,
        type: typing.Union[type, Unset] = unset,
        name: typing.Union[name, Unset] = unset,
        frozen_at: typing.Union[frozen_at, Unset] = unset,
        uuid: typing.Union[uuid, Unset] = unset,
        uri: typing.Union[uri, Unset] = unset,
        created_at: typing.Union[created_at, Unset] = unset,
        base_uri: typing.Union[base_uri, Unset] = unset,
        annotations: typing.Union[annotations, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'RegisterDataset':
        return super().__new__(
            cls,
            *args,
            tags=tags,
            manifest=manifest,
            creator_username=creator_username,
            readme=readme,
            type=type,
            name=name,
            frozen_at=frozen_at,
            uuid=uuid,
            uri=uri,
            created_at=created_at,
            base_uri=base_uri,
            annotations=annotations,
            _configuration=_configuration,
            **kwargs,
        )

from dtool_lookup_openapi_client.model.manifest import Manifest
