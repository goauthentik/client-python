# authentik_client.RacApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rac_connection_tokens_destroy**](RacApi.md#rac_connection_tokens_destroy) | **DELETE** /rac/connection_tokens/{connection_token_uuid}/ | 
[**rac_connection_tokens_list**](RacApi.md#rac_connection_tokens_list) | **GET** /rac/connection_tokens/ | 
[**rac_connection_tokens_partial_update**](RacApi.md#rac_connection_tokens_partial_update) | **PATCH** /rac/connection_tokens/{connection_token_uuid}/ | 
[**rac_connection_tokens_retrieve**](RacApi.md#rac_connection_tokens_retrieve) | **GET** /rac/connection_tokens/{connection_token_uuid}/ | 
[**rac_connection_tokens_update**](RacApi.md#rac_connection_tokens_update) | **PUT** /rac/connection_tokens/{connection_token_uuid}/ | 
[**rac_connection_tokens_used_by_list**](RacApi.md#rac_connection_tokens_used_by_list) | **GET** /rac/connection_tokens/{connection_token_uuid}/used_by/ | 
[**rac_devices_list**](RacApi.md#rac_devices_list) | **GET** /rac/devices/ | 


# **rac_connection_tokens_destroy**
> rac_connection_tokens_destroy(connection_token_uuid)

ConnectionToken Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.RacApi(api_client)
    connection_token_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this RAC Connection token.

    try:
        api_instance.rac_connection_tokens_destroy(connection_token_uuid)
    except Exception as e:
        print("Exception when calling RacApi->rac_connection_tokens_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_token_uuid** | **UUID**| A UUID string identifying this RAC Connection token. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rac_connection_tokens_list**
> PaginatedConnectionTokenList rac_connection_tokens_list(device=device, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, session__user=session__user)

ConnectionToken Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_connection_token_list import PaginatedConnectionTokenList
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.RacApi(api_client)
    device = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)
    session__user = 56 # int |  (optional)

    try:
        api_response = api_instance.rac_connection_tokens_list(device=device, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, session__user=session__user)
        print("The response of RacApi->rac_connection_tokens_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_connection_tokens_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **UUID**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **session__user** | **int**|  | [optional] 

### Return type

[**PaginatedConnectionTokenList**](PaginatedConnectionTokenList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rac_connection_tokens_partial_update**
> ConnectionToken rac_connection_tokens_partial_update(connection_token_uuid, patched_connection_token_request=patched_connection_token_request)

ConnectionToken Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.connection_token import ConnectionToken
from authentik_client.models.patched_connection_token_request import PatchedConnectionTokenRequest
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.RacApi(api_client)
    connection_token_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this RAC Connection token.
    patched_connection_token_request = authentik_client.PatchedConnectionTokenRequest() # PatchedConnectionTokenRequest |  (optional)

    try:
        api_response = api_instance.rac_connection_tokens_partial_update(connection_token_uuid, patched_connection_token_request=patched_connection_token_request)
        print("The response of RacApi->rac_connection_tokens_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_connection_tokens_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_token_uuid** | **UUID**| A UUID string identifying this RAC Connection token. | 
 **patched_connection_token_request** | [**PatchedConnectionTokenRequest**](PatchedConnectionTokenRequest.md)|  | [optional] 

### Return type

[**ConnectionToken**](ConnectionToken.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rac_connection_tokens_retrieve**
> ConnectionToken rac_connection_tokens_retrieve(connection_token_uuid)

ConnectionToken Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.connection_token import ConnectionToken
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.RacApi(api_client)
    connection_token_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this RAC Connection token.

    try:
        api_response = api_instance.rac_connection_tokens_retrieve(connection_token_uuid)
        print("The response of RacApi->rac_connection_tokens_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_connection_tokens_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_token_uuid** | **UUID**| A UUID string identifying this RAC Connection token. | 

### Return type

[**ConnectionToken**](ConnectionToken.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rac_connection_tokens_update**
> ConnectionToken rac_connection_tokens_update(connection_token_uuid, connection_token_request)

ConnectionToken Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.connection_token import ConnectionToken
from authentik_client.models.connection_token_request import ConnectionTokenRequest
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.RacApi(api_client)
    connection_token_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this RAC Connection token.
    connection_token_request = authentik_client.ConnectionTokenRequest() # ConnectionTokenRequest | 

    try:
        api_response = api_instance.rac_connection_tokens_update(connection_token_uuid, connection_token_request)
        print("The response of RacApi->rac_connection_tokens_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_connection_tokens_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_token_uuid** | **UUID**| A UUID string identifying this RAC Connection token. | 
 **connection_token_request** | [**ConnectionTokenRequest**](ConnectionTokenRequest.md)|  | 

### Return type

[**ConnectionToken**](ConnectionToken.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rac_connection_tokens_used_by_list**
> List[UsedBy] rac_connection_tokens_used_by_list(connection_token_uuid)

Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.used_by import UsedBy
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.RacApi(api_client)
    connection_token_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this RAC Connection token.

    try:
        api_response = api_instance.rac_connection_tokens_used_by_list(connection_token_uuid)
        print("The response of RacApi->rac_connection_tokens_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_connection_tokens_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_token_uuid** | **UUID**| A UUID string identifying this RAC Connection token. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rac_devices_list**
> PaginatedRACDeviceList rac_devices_list(provider, ordering=ordering, page=page, page_size=page_size, search=search)

List devices accessible through a RAC provider

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_rac_device_list import PaginatedRACDeviceList
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.RacApi(api_client)
    provider = 56 # int | 
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.rac_devices_list(provider, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of RacApi->rac_devices_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_devices_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **int**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedRACDeviceList**](PaginatedRACDeviceList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

