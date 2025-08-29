# authentik_client.RbacApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rbac_initial_permissions_create**](RbacApi.md#rbac_initial_permissions_create) | **POST** /rbac/initial_permissions/ | 
[**rbac_initial_permissions_destroy**](RbacApi.md#rbac_initial_permissions_destroy) | **DELETE** /rbac/initial_permissions/{id}/ | 
[**rbac_initial_permissions_list**](RbacApi.md#rbac_initial_permissions_list) | **GET** /rbac/initial_permissions/ | 
[**rbac_initial_permissions_partial_update**](RbacApi.md#rbac_initial_permissions_partial_update) | **PATCH** /rbac/initial_permissions/{id}/ | 
[**rbac_initial_permissions_retrieve**](RbacApi.md#rbac_initial_permissions_retrieve) | **GET** /rbac/initial_permissions/{id}/ | 
[**rbac_initial_permissions_update**](RbacApi.md#rbac_initial_permissions_update) | **PUT** /rbac/initial_permissions/{id}/ | 
[**rbac_initial_permissions_used_by_list**](RbacApi.md#rbac_initial_permissions_used_by_list) | **GET** /rbac/initial_permissions/{id}/used_by/ | 
[**rbac_permissions_assigned_by_roles_assign**](RbacApi.md#rbac_permissions_assigned_by_roles_assign) | **POST** /rbac/permissions/assigned_by_roles/{uuid}/assign/ | 
[**rbac_permissions_assigned_by_roles_list**](RbacApi.md#rbac_permissions_assigned_by_roles_list) | **GET** /rbac/permissions/assigned_by_roles/ | 
[**rbac_permissions_assigned_by_roles_unassign_partial_update**](RbacApi.md#rbac_permissions_assigned_by_roles_unassign_partial_update) | **PATCH** /rbac/permissions/assigned_by_roles/{uuid}/unassign/ | 
[**rbac_permissions_assigned_by_users_assign**](RbacApi.md#rbac_permissions_assigned_by_users_assign) | **POST** /rbac/permissions/assigned_by_users/{id}/assign/ | 
[**rbac_permissions_assigned_by_users_list**](RbacApi.md#rbac_permissions_assigned_by_users_list) | **GET** /rbac/permissions/assigned_by_users/ | 
[**rbac_permissions_assigned_by_users_unassign_partial_update**](RbacApi.md#rbac_permissions_assigned_by_users_unassign_partial_update) | **PATCH** /rbac/permissions/assigned_by_users/{id}/unassign/ | 
[**rbac_permissions_list**](RbacApi.md#rbac_permissions_list) | **GET** /rbac/permissions/ | 
[**rbac_permissions_retrieve**](RbacApi.md#rbac_permissions_retrieve) | **GET** /rbac/permissions/{id}/ | 
[**rbac_permissions_roles_destroy**](RbacApi.md#rbac_permissions_roles_destroy) | **DELETE** /rbac/permissions/roles/{id}/ | 
[**rbac_permissions_roles_list**](RbacApi.md#rbac_permissions_roles_list) | **GET** /rbac/permissions/roles/ | 
[**rbac_permissions_roles_partial_update**](RbacApi.md#rbac_permissions_roles_partial_update) | **PATCH** /rbac/permissions/roles/{id}/ | 
[**rbac_permissions_roles_retrieve**](RbacApi.md#rbac_permissions_roles_retrieve) | **GET** /rbac/permissions/roles/{id}/ | 
[**rbac_permissions_roles_update**](RbacApi.md#rbac_permissions_roles_update) | **PUT** /rbac/permissions/roles/{id}/ | 
[**rbac_permissions_users_destroy**](RbacApi.md#rbac_permissions_users_destroy) | **DELETE** /rbac/permissions/users/{id}/ | 
[**rbac_permissions_users_list**](RbacApi.md#rbac_permissions_users_list) | **GET** /rbac/permissions/users/ | 
[**rbac_permissions_users_partial_update**](RbacApi.md#rbac_permissions_users_partial_update) | **PATCH** /rbac/permissions/users/{id}/ | 
[**rbac_permissions_users_retrieve**](RbacApi.md#rbac_permissions_users_retrieve) | **GET** /rbac/permissions/users/{id}/ | 
[**rbac_permissions_users_update**](RbacApi.md#rbac_permissions_users_update) | **PUT** /rbac/permissions/users/{id}/ | 
[**rbac_roles_create**](RbacApi.md#rbac_roles_create) | **POST** /rbac/roles/ | 
[**rbac_roles_destroy**](RbacApi.md#rbac_roles_destroy) | **DELETE** /rbac/roles/{uuid}/ | 
[**rbac_roles_list**](RbacApi.md#rbac_roles_list) | **GET** /rbac/roles/ | 
[**rbac_roles_partial_update**](RbacApi.md#rbac_roles_partial_update) | **PATCH** /rbac/roles/{uuid}/ | 
[**rbac_roles_retrieve**](RbacApi.md#rbac_roles_retrieve) | **GET** /rbac/roles/{uuid}/ | 
[**rbac_roles_update**](RbacApi.md#rbac_roles_update) | **PUT** /rbac/roles/{uuid}/ | 
[**rbac_roles_used_by_list**](RbacApi.md#rbac_roles_used_by_list) | **GET** /rbac/roles/{uuid}/used_by/ | 


# **rbac_initial_permissions_create**
> InitialPermissions rbac_initial_permissions_create(initial_permissions_request)

InitialPermissions viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.initial_permissions import InitialPermissions
from authentik_client.models.initial_permissions_request import InitialPermissionsRequest
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
    api_instance = authentik_client.RbacApi(api_client)
    initial_permissions_request = authentik_client.InitialPermissionsRequest() # InitialPermissionsRequest | 

    try:
        api_response = api_instance.rbac_initial_permissions_create(initial_permissions_request)
        print("The response of RbacApi->rbac_initial_permissions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_initial_permissions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initial_permissions_request** | [**InitialPermissionsRequest**](InitialPermissionsRequest.md)|  | 

### Return type

[**InitialPermissions**](InitialPermissions.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rbac_initial_permissions_destroy**
> rbac_initial_permissions_destroy(id)

InitialPermissions viewset

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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this Initial Permissions.

    try:
        api_instance.rbac_initial_permissions_destroy(id)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_initial_permissions_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Initial Permissions. | 

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

# **rbac_initial_permissions_list**
> PaginatedInitialPermissionsList rbac_initial_permissions_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)

InitialPermissions viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_initial_permissions_list import PaginatedInitialPermissionsList
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
    api_instance = authentik_client.RbacApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.rbac_initial_permissions_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of RbacApi->rbac_initial_permissions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_initial_permissions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedInitialPermissionsList**](PaginatedInitialPermissionsList.md)

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

# **rbac_initial_permissions_partial_update**
> InitialPermissions rbac_initial_permissions_partial_update(id, patched_initial_permissions_request=patched_initial_permissions_request)

InitialPermissions viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.initial_permissions import InitialPermissions
from authentik_client.models.patched_initial_permissions_request import PatchedInitialPermissionsRequest
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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this Initial Permissions.
    patched_initial_permissions_request = authentik_client.PatchedInitialPermissionsRequest() # PatchedInitialPermissionsRequest |  (optional)

    try:
        api_response = api_instance.rbac_initial_permissions_partial_update(id, patched_initial_permissions_request=patched_initial_permissions_request)
        print("The response of RbacApi->rbac_initial_permissions_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_initial_permissions_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Initial Permissions. | 
 **patched_initial_permissions_request** | [**PatchedInitialPermissionsRequest**](PatchedInitialPermissionsRequest.md)|  | [optional] 

### Return type

[**InitialPermissions**](InitialPermissions.md)

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

# **rbac_initial_permissions_retrieve**
> InitialPermissions rbac_initial_permissions_retrieve(id)

InitialPermissions viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.initial_permissions import InitialPermissions
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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this Initial Permissions.

    try:
        api_response = api_instance.rbac_initial_permissions_retrieve(id)
        print("The response of RbacApi->rbac_initial_permissions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_initial_permissions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Initial Permissions. | 

### Return type

[**InitialPermissions**](InitialPermissions.md)

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

# **rbac_initial_permissions_update**
> InitialPermissions rbac_initial_permissions_update(id, initial_permissions_request)

InitialPermissions viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.initial_permissions import InitialPermissions
from authentik_client.models.initial_permissions_request import InitialPermissionsRequest
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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this Initial Permissions.
    initial_permissions_request = authentik_client.InitialPermissionsRequest() # InitialPermissionsRequest | 

    try:
        api_response = api_instance.rbac_initial_permissions_update(id, initial_permissions_request)
        print("The response of RbacApi->rbac_initial_permissions_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_initial_permissions_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Initial Permissions. | 
 **initial_permissions_request** | [**InitialPermissionsRequest**](InitialPermissionsRequest.md)|  | 

### Return type

[**InitialPermissions**](InitialPermissions.md)

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

# **rbac_initial_permissions_used_by_list**
> List[UsedBy] rbac_initial_permissions_used_by_list(id)

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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this Initial Permissions.

    try:
        api_response = api_instance.rbac_initial_permissions_used_by_list(id)
        print("The response of RbacApi->rbac_initial_permissions_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_initial_permissions_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Initial Permissions. | 

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

# **rbac_permissions_assigned_by_roles_assign**
> List[PermissionAssignResult] rbac_permissions_assigned_by_roles_assign(uuid, permission_assign_request)

Assign permission(s) to role. When `object_pk` is set, the permissions
are only assigned to the specific object, otherwise they are assigned globally.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.permission_assign_request import PermissionAssignRequest
from authentik_client.models.permission_assign_result import PermissionAssignResult
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
    api_instance = authentik_client.RbacApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Role.
    permission_assign_request = authentik_client.PermissionAssignRequest() # PermissionAssignRequest | 

    try:
        api_response = api_instance.rbac_permissions_assigned_by_roles_assign(uuid, permission_assign_request)
        print("The response of RbacApi->rbac_permissions_assigned_by_roles_assign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_assigned_by_roles_assign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Role. | 
 **permission_assign_request** | [**PermissionAssignRequest**](PermissionAssignRequest.md)|  | 

### Return type

[**List[PermissionAssignResult]**](PermissionAssignResult.md)

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

# **rbac_permissions_assigned_by_roles_list**
> PaginatedRoleAssignedObjectPermissionList rbac_permissions_assigned_by_roles_list(model, object_pk=object_pk, ordering=ordering, page=page, page_size=page_size, search=search)

Get assigned object permissions for a single object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_role_assigned_object_permission_list import PaginatedRoleAssignedObjectPermissionList
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
    api_instance = authentik_client.RbacApi(api_client)
    model = 'model_example' # str | 
    object_pk = 'object_pk_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.rbac_permissions_assigned_by_roles_list(model, object_pk=object_pk, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of RbacApi->rbac_permissions_assigned_by_roles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_assigned_by_roles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**|  | 
 **object_pk** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedRoleAssignedObjectPermissionList**](PaginatedRoleAssignedObjectPermissionList.md)

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

# **rbac_permissions_assigned_by_roles_unassign_partial_update**
> rbac_permissions_assigned_by_roles_unassign_partial_update(uuid, patched_permission_assign_request=patched_permission_assign_request)

Unassign permission(s) to role. When `object_pk` is set, the permissions
are only assigned to the specific object, otherwise they are assigned globally.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_permission_assign_request import PatchedPermissionAssignRequest
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
    api_instance = authentik_client.RbacApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Role.
    patched_permission_assign_request = authentik_client.PatchedPermissionAssignRequest() # PatchedPermissionAssignRequest |  (optional)

    try:
        api_instance.rbac_permissions_assigned_by_roles_unassign_partial_update(uuid, patched_permission_assign_request=patched_permission_assign_request)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_assigned_by_roles_unassign_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Role. | 
 **patched_permission_assign_request** | [**PatchedPermissionAssignRequest**](PatchedPermissionAssignRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully unassigned |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rbac_permissions_assigned_by_users_assign**
> List[PermissionAssignResult] rbac_permissions_assigned_by_users_assign(id, permission_assign_request)

Assign permission(s) to user

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.permission_assign_request import PermissionAssignRequest
from authentik_client.models.permission_assign_result import PermissionAssignResult
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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this User.
    permission_assign_request = authentik_client.PermissionAssignRequest() # PermissionAssignRequest | 

    try:
        api_response = api_instance.rbac_permissions_assigned_by_users_assign(id, permission_assign_request)
        print("The response of RbacApi->rbac_permissions_assigned_by_users_assign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_assigned_by_users_assign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 
 **permission_assign_request** | [**PermissionAssignRequest**](PermissionAssignRequest.md)|  | 

### Return type

[**List[PermissionAssignResult]**](PermissionAssignResult.md)

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

# **rbac_permissions_assigned_by_users_list**
> PaginatedUserAssignedObjectPermissionList rbac_permissions_assigned_by_users_list(model, object_pk=object_pk, ordering=ordering, page=page, page_size=page_size, search=search)

Get assigned object permissions for a single object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_user_assigned_object_permission_list import PaginatedUserAssignedObjectPermissionList
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
    api_instance = authentik_client.RbacApi(api_client)
    model = 'model_example' # str | 
    object_pk = 'object_pk_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.rbac_permissions_assigned_by_users_list(model, object_pk=object_pk, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of RbacApi->rbac_permissions_assigned_by_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_assigned_by_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**|  | 
 **object_pk** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedUserAssignedObjectPermissionList**](PaginatedUserAssignedObjectPermissionList.md)

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

# **rbac_permissions_assigned_by_users_unassign_partial_update**
> rbac_permissions_assigned_by_users_unassign_partial_update(id, patched_permission_assign_request=patched_permission_assign_request)

Unassign permission(s) to user. When `object_pk` is set, the permissions
are only assigned to the specific object, otherwise they are assigned globally.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_permission_assign_request import PatchedPermissionAssignRequest
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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this User.
    patched_permission_assign_request = authentik_client.PatchedPermissionAssignRequest() # PatchedPermissionAssignRequest |  (optional)

    try:
        api_instance.rbac_permissions_assigned_by_users_unassign_partial_update(id, patched_permission_assign_request=patched_permission_assign_request)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_assigned_by_users_unassign_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 
 **patched_permission_assign_request** | [**PatchedPermissionAssignRequest**](PatchedPermissionAssignRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully unassigned |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rbac_permissions_list**
> PaginatedPermissionList rbac_permissions_list(codename=codename, content_type__app_label=content_type__app_label, content_type__model=content_type__model, ordering=ordering, page=page, page_size=page_size, role=role, search=search, user=user)

Read-only list of all permissions, filterable by model and app

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_permission_list import PaginatedPermissionList
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
    api_instance = authentik_client.RbacApi(api_client)
    codename = 'codename_example' # str |  (optional)
    content_type__app_label = 'content_type__app_label_example' # str |  (optional)
    content_type__model = 'content_type__model_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    role = 'role_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    user = 56 # int |  (optional)

    try:
        api_response = api_instance.rbac_permissions_list(codename=codename, content_type__app_label=content_type__app_label, content_type__model=content_type__model, ordering=ordering, page=page, page_size=page_size, role=role, search=search, user=user)
        print("The response of RbacApi->rbac_permissions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codename** | **str**|  | [optional] 
 **content_type__app_label** | **str**|  | [optional] 
 **content_type__model** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **role** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user** | **int**|  | [optional] 

### Return type

[**PaginatedPermissionList**](PaginatedPermissionList.md)

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

# **rbac_permissions_retrieve**
> Permission rbac_permissions_retrieve(id)

Read-only list of all permissions, filterable by model and app

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.permission import Permission
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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this permission.

    try:
        api_response = api_instance.rbac_permissions_retrieve(id)
        print("The response of RbacApi->rbac_permissions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this permission. | 

### Return type

[**Permission**](Permission.md)

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

# **rbac_permissions_roles_destroy**
> rbac_permissions_roles_destroy(id)

Get a role's assigned object permissions

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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this group object permission.

    try:
        api_instance.rbac_permissions_roles_destroy(id)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_roles_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this group object permission. | 

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

# **rbac_permissions_roles_list**
> PaginatedExtraRoleObjectPermissionList rbac_permissions_roles_list(ordering=ordering, page=page, page_size=page_size, search=search, uuid=uuid)

Get a role's assigned object permissions

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_extra_role_object_permission_list import PaginatedExtraRoleObjectPermissionList
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
    api_instance = authentik_client.RbacApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    uuid = 'uuid_example' # str |  (optional)

    try:
        api_response = api_instance.rbac_permissions_roles_list(ordering=ordering, page=page, page_size=page_size, search=search, uuid=uuid)
        print("The response of RbacApi->rbac_permissions_roles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_roles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **uuid** | **str**|  | [optional] 

### Return type

[**PaginatedExtraRoleObjectPermissionList**](PaginatedExtraRoleObjectPermissionList.md)

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

# **rbac_permissions_roles_partial_update**
> ExtraRoleObjectPermission rbac_permissions_roles_partial_update(id, patched_extra_role_object_permission_request=patched_extra_role_object_permission_request)

Get a role's assigned object permissions

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.extra_role_object_permission import ExtraRoleObjectPermission
from authentik_client.models.patched_extra_role_object_permission_request import PatchedExtraRoleObjectPermissionRequest
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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this group object permission.
    patched_extra_role_object_permission_request = authentik_client.PatchedExtraRoleObjectPermissionRequest() # PatchedExtraRoleObjectPermissionRequest |  (optional)

    try:
        api_response = api_instance.rbac_permissions_roles_partial_update(id, patched_extra_role_object_permission_request=patched_extra_role_object_permission_request)
        print("The response of RbacApi->rbac_permissions_roles_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_roles_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this group object permission. | 
 **patched_extra_role_object_permission_request** | [**PatchedExtraRoleObjectPermissionRequest**](PatchedExtraRoleObjectPermissionRequest.md)|  | [optional] 

### Return type

[**ExtraRoleObjectPermission**](ExtraRoleObjectPermission.md)

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

# **rbac_permissions_roles_retrieve**
> ExtraRoleObjectPermission rbac_permissions_roles_retrieve(id)

Get a role's assigned object permissions

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.extra_role_object_permission import ExtraRoleObjectPermission
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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this group object permission.

    try:
        api_response = api_instance.rbac_permissions_roles_retrieve(id)
        print("The response of RbacApi->rbac_permissions_roles_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_roles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this group object permission. | 

### Return type

[**ExtraRoleObjectPermission**](ExtraRoleObjectPermission.md)

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

# **rbac_permissions_roles_update**
> ExtraRoleObjectPermission rbac_permissions_roles_update(id, extra_role_object_permission_request)

Get a role's assigned object permissions

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.extra_role_object_permission import ExtraRoleObjectPermission
from authentik_client.models.extra_role_object_permission_request import ExtraRoleObjectPermissionRequest
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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this group object permission.
    extra_role_object_permission_request = authentik_client.ExtraRoleObjectPermissionRequest() # ExtraRoleObjectPermissionRequest | 

    try:
        api_response = api_instance.rbac_permissions_roles_update(id, extra_role_object_permission_request)
        print("The response of RbacApi->rbac_permissions_roles_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_roles_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this group object permission. | 
 **extra_role_object_permission_request** | [**ExtraRoleObjectPermissionRequest**](ExtraRoleObjectPermissionRequest.md)|  | 

### Return type

[**ExtraRoleObjectPermission**](ExtraRoleObjectPermission.md)

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

# **rbac_permissions_users_destroy**
> rbac_permissions_users_destroy(id)

Get a users's assigned object permissions

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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this user object permission.

    try:
        api_instance.rbac_permissions_users_destroy(id)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user object permission. | 

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

# **rbac_permissions_users_list**
> PaginatedExtraUserObjectPermissionList rbac_permissions_users_list(ordering=ordering, page=page, page_size=page_size, search=search, user_id=user_id)

Get a users's assigned object permissions

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_extra_user_object_permission_list import PaginatedExtraUserObjectPermissionList
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
    api_instance = authentik_client.RbacApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    user_id = 56 # int |  (optional)

    try:
        api_response = api_instance.rbac_permissions_users_list(ordering=ordering, page=page, page_size=page_size, search=search, user_id=user_id)
        print("The response of RbacApi->rbac_permissions_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user_id** | **int**|  | [optional] 

### Return type

[**PaginatedExtraUserObjectPermissionList**](PaginatedExtraUserObjectPermissionList.md)

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

# **rbac_permissions_users_partial_update**
> ExtraUserObjectPermission rbac_permissions_users_partial_update(id, patched_extra_user_object_permission_request=patched_extra_user_object_permission_request)

Get a users's assigned object permissions

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.extra_user_object_permission import ExtraUserObjectPermission
from authentik_client.models.patched_extra_user_object_permission_request import PatchedExtraUserObjectPermissionRequest
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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this user object permission.
    patched_extra_user_object_permission_request = authentik_client.PatchedExtraUserObjectPermissionRequest() # PatchedExtraUserObjectPermissionRequest |  (optional)

    try:
        api_response = api_instance.rbac_permissions_users_partial_update(id, patched_extra_user_object_permission_request=patched_extra_user_object_permission_request)
        print("The response of RbacApi->rbac_permissions_users_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_users_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user object permission. | 
 **patched_extra_user_object_permission_request** | [**PatchedExtraUserObjectPermissionRequest**](PatchedExtraUserObjectPermissionRequest.md)|  | [optional] 

### Return type

[**ExtraUserObjectPermission**](ExtraUserObjectPermission.md)

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

# **rbac_permissions_users_retrieve**
> ExtraUserObjectPermission rbac_permissions_users_retrieve(id)

Get a users's assigned object permissions

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.extra_user_object_permission import ExtraUserObjectPermission
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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this user object permission.

    try:
        api_response = api_instance.rbac_permissions_users_retrieve(id)
        print("The response of RbacApi->rbac_permissions_users_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user object permission. | 

### Return type

[**ExtraUserObjectPermission**](ExtraUserObjectPermission.md)

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

# **rbac_permissions_users_update**
> ExtraUserObjectPermission rbac_permissions_users_update(id, extra_user_object_permission_request)

Get a users's assigned object permissions

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.extra_user_object_permission import ExtraUserObjectPermission
from authentik_client.models.extra_user_object_permission_request import ExtraUserObjectPermissionRequest
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
    api_instance = authentik_client.RbacApi(api_client)
    id = 56 # int | A unique integer value identifying this user object permission.
    extra_user_object_permission_request = authentik_client.ExtraUserObjectPermissionRequest() # ExtraUserObjectPermissionRequest | 

    try:
        api_response = api_instance.rbac_permissions_users_update(id, extra_user_object_permission_request)
        print("The response of RbacApi->rbac_permissions_users_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_permissions_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user object permission. | 
 **extra_user_object_permission_request** | [**ExtraUserObjectPermissionRequest**](ExtraUserObjectPermissionRequest.md)|  | 

### Return type

[**ExtraUserObjectPermission**](ExtraUserObjectPermission.md)

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

# **rbac_roles_create**
> Role rbac_roles_create(role_request)

Role viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.role import Role
from authentik_client.models.role_request import RoleRequest
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
    api_instance = authentik_client.RbacApi(api_client)
    role_request = authentik_client.RoleRequest() # RoleRequest | 

    try:
        api_response = api_instance.rbac_roles_create(role_request)
        print("The response of RbacApi->rbac_roles_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_roles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_request** | [**RoleRequest**](RoleRequest.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rbac_roles_destroy**
> rbac_roles_destroy(uuid)

Role viewset

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
    api_instance = authentik_client.RbacApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Role.

    try:
        api_instance.rbac_roles_destroy(uuid)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_roles_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Role. | 

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

# **rbac_roles_list**
> PaginatedRoleList rbac_roles_list(group__name=group__name, ordering=ordering, page=page, page_size=page_size, search=search)

Role viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_role_list import PaginatedRoleList
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
    api_instance = authentik_client.RbacApi(api_client)
    group__name = 'group__name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.rbac_roles_list(group__name=group__name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of RbacApi->rbac_roles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_roles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group__name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedRoleList**](PaginatedRoleList.md)

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

# **rbac_roles_partial_update**
> Role rbac_roles_partial_update(uuid, patched_role_request=patched_role_request)

Role viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_role_request import PatchedRoleRequest
from authentik_client.models.role import Role
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
    api_instance = authentik_client.RbacApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Role.
    patched_role_request = authentik_client.PatchedRoleRequest() # PatchedRoleRequest |  (optional)

    try:
        api_response = api_instance.rbac_roles_partial_update(uuid, patched_role_request=patched_role_request)
        print("The response of RbacApi->rbac_roles_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_roles_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Role. | 
 **patched_role_request** | [**PatchedRoleRequest**](PatchedRoleRequest.md)|  | [optional] 

### Return type

[**Role**](Role.md)

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

# **rbac_roles_retrieve**
> Role rbac_roles_retrieve(uuid)

Role viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.role import Role
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
    api_instance = authentik_client.RbacApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Role.

    try:
        api_response = api_instance.rbac_roles_retrieve(uuid)
        print("The response of RbacApi->rbac_roles_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_roles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Role. | 

### Return type

[**Role**](Role.md)

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

# **rbac_roles_update**
> Role rbac_roles_update(uuid, role_request)

Role viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.role import Role
from authentik_client.models.role_request import RoleRequest
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
    api_instance = authentik_client.RbacApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Role.
    role_request = authentik_client.RoleRequest() # RoleRequest | 

    try:
        api_response = api_instance.rbac_roles_update(uuid, role_request)
        print("The response of RbacApi->rbac_roles_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_roles_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Role. | 
 **role_request** | [**RoleRequest**](RoleRequest.md)|  | 

### Return type

[**Role**](Role.md)

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

# **rbac_roles_used_by_list**
> List[UsedBy] rbac_roles_used_by_list(uuid)

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
    api_instance = authentik_client.RbacApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Role.

    try:
        api_response = api_instance.rbac_roles_used_by_list(uuid)
        print("The response of RbacApi->rbac_roles_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RbacApi->rbac_roles_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Role. | 

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

