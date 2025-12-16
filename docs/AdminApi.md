# authentik_client.AdminApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_apps_list**](AdminApi.md#admin_apps_list) | **GET** /admin/apps/ | 
[**admin_file_create**](AdminApi.md#admin_file_create) | **POST** /admin/file/ | 
[**admin_file_destroy**](AdminApi.md#admin_file_destroy) | **DELETE** /admin/file/ | 
[**admin_file_list**](AdminApi.md#admin_file_list) | **GET** /admin/file/ | 
[**admin_file_used_by_list**](AdminApi.md#admin_file_used_by_list) | **GET** /admin/file/used_by/ | 
[**admin_models_list**](AdminApi.md#admin_models_list) | **GET** /admin/models/ | 
[**admin_settings_partial_update**](AdminApi.md#admin_settings_partial_update) | **PATCH** /admin/settings/ | 
[**admin_settings_retrieve**](AdminApi.md#admin_settings_retrieve) | **GET** /admin/settings/ | 
[**admin_settings_update**](AdminApi.md#admin_settings_update) | **PUT** /admin/settings/ | 
[**admin_system_create**](AdminApi.md#admin_system_create) | **POST** /admin/system/ | 
[**admin_system_retrieve**](AdminApi.md#admin_system_retrieve) | **GET** /admin/system/ | 
[**admin_version_history_list**](AdminApi.md#admin_version_history_list) | **GET** /admin/version/history/ | 
[**admin_version_history_retrieve**](AdminApi.md#admin_version_history_retrieve) | **GET** /admin/version/history/{id}/ | 
[**admin_version_retrieve**](AdminApi.md#admin_version_retrieve) | **GET** /admin/version/ | 


# **admin_apps_list**
> List[App] admin_apps_list()

Read-only view list all installed apps

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.app import App
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
    api_instance = authentik_client.AdminApi(api_client)

    try:
        api_response = api_instance.admin_apps_list()
        print("The response of AdminApi->admin_apps_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_apps_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[App]**](App.md)

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

# **admin_file_create**
> admin_file_create(file, name=name, usage=usage)

Upload file to storage backend.

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
    api_instance = authentik_client.AdminApi(api_client)
    file = None # bytearray | 
    name = 'name_example' # str |  (optional)
    usage = 'media' # str |  (optional) (default to 'media')

    try:
        api_instance.admin_file_create(file, name=name, usage=usage)
    except Exception as e:
        print("Exception when calling AdminApi->admin_file_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **name** | **str**|  | [optional] 
 **usage** | **str**|  | [optional] [default to &#39;media&#39;]

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_file_destroy**
> admin_file_destroy(name=name, usage=usage)

Delete file from storage backend.

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
    api_instance = authentik_client.AdminApi(api_client)
    name = 'name_example' # str |  (optional)
    usage = media # str |  (optional) (default to media)

    try:
        api_instance.admin_file_destroy(name=name, usage=usage)
    except Exception as e:
        print("Exception when calling AdminApi->admin_file_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **usage** | **str**|  | [optional] [default to media]

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
**200** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_file_list**
> List[FileList] admin_file_list(manageable_only=manageable_only, search=search, usage=usage)

List files from storage backend.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.file_list import FileList
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
    api_instance = authentik_client.AdminApi(api_client)
    manageable_only = False # bool |  (optional) (default to False)
    search = 'search_example' # str | A search term. (optional)
    usage = media # str |  (optional) (default to media)

    try:
        api_response = api_instance.admin_file_list(manageable_only=manageable_only, search=search, usage=usage)
        print("The response of AdminApi->admin_file_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_file_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manageable_only** | **bool**|  | [optional] [default to False]
 **search** | **str**| A search term. | [optional] 
 **usage** | **str**|  | [optional] [default to media]

### Return type

[**List[FileList]**](FileList.md)

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

# **admin_file_used_by_list**
> List[UsedBy] admin_file_used_by_list(name=name)

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
    api_instance = authentik_client.AdminApi(api_client)
    name = 'name_example' # str |  (optional)

    try:
        api_response = api_instance.admin_file_used_by_list(name=name)
        print("The response of AdminApi->admin_file_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_file_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

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

# **admin_models_list**
> List[App] admin_models_list()

Read-only view list all installed models

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.app import App
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
    api_instance = authentik_client.AdminApi(api_client)

    try:
        api_response = api_instance.admin_models_list()
        print("The response of AdminApi->admin_models_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_models_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[App]**](App.md)

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

# **admin_settings_partial_update**
> Settings admin_settings_partial_update(patched_settings_request=patched_settings_request)

Settings view

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_settings_request import PatchedSettingsRequest
from authentik_client.models.settings import Settings
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
    api_instance = authentik_client.AdminApi(api_client)
    patched_settings_request = authentik_client.PatchedSettingsRequest() # PatchedSettingsRequest |  (optional)

    try:
        api_response = api_instance.admin_settings_partial_update(patched_settings_request=patched_settings_request)
        print("The response of AdminApi->admin_settings_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_settings_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_settings_request** | [**PatchedSettingsRequest**](PatchedSettingsRequest.md)|  | [optional] 

### Return type

[**Settings**](Settings.md)

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

# **admin_settings_retrieve**
> Settings admin_settings_retrieve()

Settings view

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.settings import Settings
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
    api_instance = authentik_client.AdminApi(api_client)

    try:
        api_response = api_instance.admin_settings_retrieve()
        print("The response of AdminApi->admin_settings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_settings_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Settings**](Settings.md)

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

# **admin_settings_update**
> Settings admin_settings_update(settings_request)

Settings view

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.settings import Settings
from authentik_client.models.settings_request import SettingsRequest
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
    api_instance = authentik_client.AdminApi(api_client)
    settings_request = authentik_client.SettingsRequest() # SettingsRequest | 

    try:
        api_response = api_instance.admin_settings_update(settings_request)
        print("The response of AdminApi->admin_settings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request** | [**SettingsRequest**](SettingsRequest.md)|  | 

### Return type

[**Settings**](Settings.md)

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

# **admin_system_create**
> SystemInfo admin_system_create()

Get system information.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.system_info import SystemInfo
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
    api_instance = authentik_client.AdminApi(api_client)

    try:
        api_response = api_instance.admin_system_create()
        print("The response of AdminApi->admin_system_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_system_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemInfo**](SystemInfo.md)

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

# **admin_system_retrieve**
> SystemInfo admin_system_retrieve()

Get system information.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.system_info import SystemInfo
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
    api_instance = authentik_client.AdminApi(api_client)

    try:
        api_response = api_instance.admin_system_retrieve()
        print("The response of AdminApi->admin_system_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_system_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemInfo**](SystemInfo.md)

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

# **admin_version_history_list**
> List[VersionHistory] admin_version_history_list(build=build, ordering=ordering, search=search, version=version)

VersionHistory Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.version_history import VersionHistory
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
    api_instance = authentik_client.AdminApi(api_client)
    build = 'build_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    search = 'search_example' # str | A search term. (optional)
    version = 'version_example' # str |  (optional)

    try:
        api_response = api_instance.admin_version_history_list(build=build, ordering=ordering, search=search, version=version)
        print("The response of AdminApi->admin_version_history_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_version_history_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**List[VersionHistory]**](VersionHistory.md)

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

# **admin_version_history_retrieve**
> VersionHistory admin_version_history_retrieve(id)

VersionHistory Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.version_history import VersionHistory
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
    api_instance = authentik_client.AdminApi(api_client)
    id = 56 # int | A unique integer value identifying this Version history.

    try:
        api_response = api_instance.admin_version_history_retrieve(id)
        print("The response of AdminApi->admin_version_history_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_version_history_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Version history. | 

### Return type

[**VersionHistory**](VersionHistory.md)

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

# **admin_version_retrieve**
> Version admin_version_retrieve()

Get running and latest version.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.version import Version
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
    api_instance = authentik_client.AdminApi(api_client)

    try:
        api_response = api_instance.admin_version_retrieve()
        print("The response of AdminApi->admin_version_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_version_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

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

