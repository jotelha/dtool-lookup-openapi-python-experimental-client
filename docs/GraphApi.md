# dtool_lookup_openapi_client.GraphApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_config_get**](GraphApi.md#graph_config_get) | **GET** /graph/config | Return the JSON-serialized dependency graph plugin configuration.
[**graph_lookup_uuid_get**](GraphApi.md#graph_lookup_uuid_get) | **GET** /graph/lookup/{uuid} | List the datasets within the same dependency graph as &lt;uuid&gt;. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
[**graph_lookup_uuid_post**](GraphApi.md#graph_lookup_uuid_post) | **POST** /graph/lookup/{uuid} | List the datasets within the same dependency graph as &lt;uuid&gt;. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.

# **graph_config_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} graph_config_get()

Return the JSON-serialized dependency graph plugin configuration.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import graph_api
from dtool_lookup_openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dtool_lookup_openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dtool_lookup_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with dtool_lookup_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return the JSON-serialized dependency graph plugin configuration.
        api_response = api_instance.graph_config_get()
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling GraphApi->graph_config_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | OK
default | ApiResponseForDefault | Default error response

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](Error.md) |  | 



**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[bearerAuth](../README.md#bearerAuth)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_lookup_uuid_get**
> [Dataset] graph_lookup_uuid_get(uuid)

List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import graph_api
from dtool_lookup_openapi_client.model.pagination_metadata import PaginationMetadata
from dtool_lookup_openapi_client.model.dataset import Dataset
from dtool_lookup_openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dtool_lookup_openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dtool_lookup_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with dtool_lookup_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "uuid_example",
    }
    query_params = {
    }
    try:
        # List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
        api_response = api_instance.graph_lookup_uuid_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling GraphApi->graph_lookup_uuid_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'uuid': "uuid_example",
    }
    query_params = {
        'page': 1,
        'page_size': 10,
    }
    try:
        # List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
        api_response = api_instance.graph_lookup_uuid_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling GraphApi->graph_lookup_uuid_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
page_size | PageSizeSchema | | optional


#### PageSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 1

#### PageSizeSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 10

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
uuid | UuidSchema | | 

#### UuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | OK
422 | ApiResponseFor422 | Unprocessable Entity
default | ApiResponseForDefault | Default error response

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**[Dataset]** |  | 
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Pagination | XPaginationSchema | | optional

#### XPaginationSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginationMetadata**](PaginationMetadata.md) |  | 



#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](Error.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](Error.md) |  | 



[**[Dataset]**](Dataset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_lookup_uuid_post**
> [Dataset] graph_lookup_uuid_post(uuiddependency_keys)

List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.api import graph_api
from dtool_lookup_openapi_client.model.pagination_metadata import PaginationMetadata
from dtool_lookup_openapi_client.model.dataset import Dataset
from dtool_lookup_openapi_client.model.dependency_keys import DependencyKeys
from dtool_lookup_openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dtool_lookup_openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dtool_lookup_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with dtool_lookup_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "uuid_example",
    }
    query_params = {
    }
    body = DependencyKeys(
        dependency_keys=[
            "dependency_keys_example"
        ],
    )
    try:
        # List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
        api_response = api_instance.graph_lookup_uuid_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling GraphApi->graph_lookup_uuid_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'uuid': "uuid_example",
    }
    query_params = {
        'page': 1,
        'page_size': 10,
    }
    body = DependencyKeys(
        dependency_keys=[
            "dependency_keys_example"
        ],
    )
    try:
        # List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
        api_response = api_instance.graph_lookup_uuid_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except dtool_lookup_openapi_client.ApiException as e:
        print("Exception when calling GraphApi->graph_lookup_uuid_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DependencyKeys**](DependencyKeys.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
page_size | PageSizeSchema | | optional


#### PageSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 1

#### PageSizeSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 10

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
uuid | UuidSchema | | 

#### UuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
422 | ApiResponseFor422 | Unprocessable Entity
200 | ApiResponseFor200 | OK
default | ApiResponseForDefault | Default error response

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](Error.md) |  | 


#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**[Dataset]** |  | 
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Pagination | XPaginationSchema | | optional

#### XPaginationSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginationMetadata**](PaginationMetadata.md) |  | 



#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](Error.md) |  | 



[**[Dataset]**](Dataset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

