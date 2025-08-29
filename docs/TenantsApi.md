# authentik_client.TenantsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_domains_create**](TenantsApi.md#tenants_domains_create) | **POST** /tenants/domains/ | 
[**tenants_domains_destroy**](TenantsApi.md#tenants_domains_destroy) | **DELETE** /tenants/domains/{id}/ | 
[**tenants_domains_list**](TenantsApi.md#tenants_domains_list) | **GET** /tenants/domains/ | 
[**tenants_domains_partial_update**](TenantsApi.md#tenants_domains_partial_update) | **PATCH** /tenants/domains/{id}/ | 
[**tenants_domains_retrieve**](TenantsApi.md#tenants_domains_retrieve) | **GET** /tenants/domains/{id}/ | 
[**tenants_domains_update**](TenantsApi.md#tenants_domains_update) | **PUT** /tenants/domains/{id}/ | 
[**tenants_tenants_create**](TenantsApi.md#tenants_tenants_create) | **POST** /tenants/tenants/ | 
[**tenants_tenants_create_admin_group_create**](TenantsApi.md#tenants_tenants_create_admin_group_create) | **POST** /tenants/tenants/{tenant_uuid}/create_admin_group/ | 
[**tenants_tenants_create_recovery_key_create**](TenantsApi.md#tenants_tenants_create_recovery_key_create) | **POST** /tenants/tenants/{tenant_uuid}/create_recovery_key/ | 
[**tenants_tenants_destroy**](TenantsApi.md#tenants_tenants_destroy) | **DELETE** /tenants/tenants/{tenant_uuid}/ | 
[**tenants_tenants_list**](TenantsApi.md#tenants_tenants_list) | **GET** /tenants/tenants/ | 
[**tenants_tenants_partial_update**](TenantsApi.md#tenants_tenants_partial_update) | **PATCH** /tenants/tenants/{tenant_uuid}/ | 
[**tenants_tenants_retrieve**](TenantsApi.md#tenants_tenants_retrieve) | **GET** /tenants/tenants/{tenant_uuid}/ | 
[**tenants_tenants_update**](TenantsApi.md#tenants_tenants_update) | **PUT** /tenants/tenants/{tenant_uuid}/ | 


# **tenants_domains_create**
> Domain tenants_domains_create(domain_request)

Domain ViewSet

### Example


```python
import authentik_client
from authentik_client.models.domain import Domain
from authentik_client.models.domain_request import DomainRequest
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    domain_request = authentik_client.DomainRequest() # DomainRequest | 

    try:
        api_response = api_instance.tenants_domains_create(domain_request)
        print("The response of TenantsApi->tenants_domains_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_domains_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_request** | [**DomainRequest**](DomainRequest.md)|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

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

# **tenants_domains_destroy**
> tenants_domains_destroy(id)

Domain ViewSet

### Example


```python
import authentik_client
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    id = 56 # int | A unique integer value identifying this Domain.

    try:
        api_instance.tenants_domains_destroy(id)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_domains_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Domain. | 

### Return type

void (empty response body)

### Authorization

No authorization required

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

# **tenants_domains_list**
> PaginatedDomainList tenants_domains_list(ordering=ordering, page=page, page_size=page_size, search=search)

Domain ViewSet

### Example


```python
import authentik_client
from authentik_client.models.paginated_domain_list import PaginatedDomainList
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.tenants_domains_list(ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of TenantsApi->tenants_domains_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_domains_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedDomainList**](PaginatedDomainList.md)

### Authorization

No authorization required

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

# **tenants_domains_partial_update**
> Domain tenants_domains_partial_update(id, patched_domain_request=patched_domain_request)

Domain ViewSet

### Example


```python
import authentik_client
from authentik_client.models.domain import Domain
from authentik_client.models.patched_domain_request import PatchedDomainRequest
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    id = 56 # int | A unique integer value identifying this Domain.
    patched_domain_request = authentik_client.PatchedDomainRequest() # PatchedDomainRequest |  (optional)

    try:
        api_response = api_instance.tenants_domains_partial_update(id, patched_domain_request=patched_domain_request)
        print("The response of TenantsApi->tenants_domains_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_domains_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Domain. | 
 **patched_domain_request** | [**PatchedDomainRequest**](PatchedDomainRequest.md)|  | [optional] 

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

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

# **tenants_domains_retrieve**
> Domain tenants_domains_retrieve(id)

Domain ViewSet

### Example


```python
import authentik_client
from authentik_client.models.domain import Domain
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    id = 56 # int | A unique integer value identifying this Domain.

    try:
        api_response = api_instance.tenants_domains_retrieve(id)
        print("The response of TenantsApi->tenants_domains_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_domains_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Domain. | 

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

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

# **tenants_domains_update**
> Domain tenants_domains_update(id, domain_request)

Domain ViewSet

### Example


```python
import authentik_client
from authentik_client.models.domain import Domain
from authentik_client.models.domain_request import DomainRequest
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    id = 56 # int | A unique integer value identifying this Domain.
    domain_request = authentik_client.DomainRequest() # DomainRequest | 

    try:
        api_response = api_instance.tenants_domains_update(id, domain_request)
        print("The response of TenantsApi->tenants_domains_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_domains_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Domain. | 
 **domain_request** | [**DomainRequest**](DomainRequest.md)|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

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

# **tenants_tenants_create**
> Tenant tenants_tenants_create(tenant_request)

Tenant Viewset

### Example


```python
import authentik_client
from authentik_client.models.tenant import Tenant
from authentik_client.models.tenant_request import TenantRequest
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    tenant_request = authentik_client.TenantRequest() # TenantRequest | 

    try:
        api_response = api_instance.tenants_tenants_create(tenant_request)
        print("The response of TenantsApi->tenants_tenants_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_tenants_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_request** | [**TenantRequest**](TenantRequest.md)|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

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

# **tenants_tenants_create_admin_group_create**
> tenants_tenants_create_admin_group_create(tenant_uuid, tenant_admin_group_request_request)

Create admin group and add user to it.

### Example


```python
import authentik_client
from authentik_client.models.tenant_admin_group_request_request import TenantAdminGroupRequestRequest
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    tenant_uuid = 'tenant_uuid_example' # str | A UUID string identifying this Tenant.
    tenant_admin_group_request_request = authentik_client.TenantAdminGroupRequestRequest() # TenantAdminGroupRequestRequest | 

    try:
        api_instance.tenants_tenants_create_admin_group_create(tenant_uuid, tenant_admin_group_request_request)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_tenants_create_admin_group_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_uuid** | **str**| A UUID string identifying this Tenant. | 
 **tenant_admin_group_request_request** | [**TenantAdminGroupRequestRequest**](TenantAdminGroupRequestRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Group created successfully. |  -  |
**400** | Bad request |  -  |
**404** | User not found |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_tenants_create_recovery_key_create**
> TenantRecoveryKeyResponse tenants_tenants_create_recovery_key_create(tenant_uuid, tenant_recovery_key_request_request)

Create recovery key for user.

### Example


```python
import authentik_client
from authentik_client.models.tenant_recovery_key_request_request import TenantRecoveryKeyRequestRequest
from authentik_client.models.tenant_recovery_key_response import TenantRecoveryKeyResponse
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    tenant_uuid = 'tenant_uuid_example' # str | A UUID string identifying this Tenant.
    tenant_recovery_key_request_request = authentik_client.TenantRecoveryKeyRequestRequest() # TenantRecoveryKeyRequestRequest | 

    try:
        api_response = api_instance.tenants_tenants_create_recovery_key_create(tenant_uuid, tenant_recovery_key_request_request)
        print("The response of TenantsApi->tenants_tenants_create_recovery_key_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_tenants_create_recovery_key_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_uuid** | **str**| A UUID string identifying this Tenant. | 
 **tenant_recovery_key_request_request** | [**TenantRecoveryKeyRequestRequest**](TenantRecoveryKeyRequestRequest.md)|  | 

### Return type

[**TenantRecoveryKeyResponse**](TenantRecoveryKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**404** | User not found |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_tenants_destroy**
> tenants_tenants_destroy(tenant_uuid)

Tenant Viewset

### Example


```python
import authentik_client
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    tenant_uuid = 'tenant_uuid_example' # str | A UUID string identifying this Tenant.

    try:
        api_instance.tenants_tenants_destroy(tenant_uuid)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_tenants_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_uuid** | **str**| A UUID string identifying this Tenant. | 

### Return type

void (empty response body)

### Authorization

No authorization required

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

# **tenants_tenants_list**
> PaginatedTenantList tenants_tenants_list(ordering=ordering, page=page, page_size=page_size, search=search)

Tenant Viewset

### Example


```python
import authentik_client
from authentik_client.models.paginated_tenant_list import PaginatedTenantList
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.tenants_tenants_list(ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of TenantsApi->tenants_tenants_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_tenants_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedTenantList**](PaginatedTenantList.md)

### Authorization

No authorization required

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

# **tenants_tenants_partial_update**
> Tenant tenants_tenants_partial_update(tenant_uuid, patched_tenant_request=patched_tenant_request)

Tenant Viewset

### Example


```python
import authentik_client
from authentik_client.models.patched_tenant_request import PatchedTenantRequest
from authentik_client.models.tenant import Tenant
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    tenant_uuid = 'tenant_uuid_example' # str | A UUID string identifying this Tenant.
    patched_tenant_request = authentik_client.PatchedTenantRequest() # PatchedTenantRequest |  (optional)

    try:
        api_response = api_instance.tenants_tenants_partial_update(tenant_uuid, patched_tenant_request=patched_tenant_request)
        print("The response of TenantsApi->tenants_tenants_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_tenants_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_uuid** | **str**| A UUID string identifying this Tenant. | 
 **patched_tenant_request** | [**PatchedTenantRequest**](PatchedTenantRequest.md)|  | [optional] 

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

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

# **tenants_tenants_retrieve**
> Tenant tenants_tenants_retrieve(tenant_uuid)

Tenant Viewset

### Example


```python
import authentik_client
from authentik_client.models.tenant import Tenant
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    tenant_uuid = 'tenant_uuid_example' # str | A UUID string identifying this Tenant.

    try:
        api_response = api_instance.tenants_tenants_retrieve(tenant_uuid)
        print("The response of TenantsApi->tenants_tenants_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_tenants_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_uuid** | **str**| A UUID string identifying this Tenant. | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

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

# **tenants_tenants_update**
> Tenant tenants_tenants_update(tenant_uuid, tenant_request)

Tenant Viewset

### Example


```python
import authentik_client
from authentik_client.models.tenant import Tenant
from authentik_client.models.tenant_request import TenantRequest
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)


# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TenantsApi(api_client)
    tenant_uuid = 'tenant_uuid_example' # str | A UUID string identifying this Tenant.
    tenant_request = authentik_client.TenantRequest() # TenantRequest | 

    try:
        api_response = api_instance.tenants_tenants_update(tenant_uuid, tenant_request)
        print("The response of TenantsApi->tenants_tenants_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_tenants_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_uuid** | **str**| A UUID string identifying this Tenant. | 
 **tenant_request** | [**TenantRequest**](TenantRequest.md)|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

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

