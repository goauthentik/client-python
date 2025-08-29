# authentik_client.PropertymappingsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**propertymappings_all_destroy**](PropertymappingsApi.md#propertymappings_all_destroy) | **DELETE** /propertymappings/all/{pm_uuid}/ | 
[**propertymappings_all_list**](PropertymappingsApi.md#propertymappings_all_list) | **GET** /propertymappings/all/ | 
[**propertymappings_all_retrieve**](PropertymappingsApi.md#propertymappings_all_retrieve) | **GET** /propertymappings/all/{pm_uuid}/ | 
[**propertymappings_all_test_create**](PropertymappingsApi.md#propertymappings_all_test_create) | **POST** /propertymappings/all/{pm_uuid}/test/ | 
[**propertymappings_all_types_list**](PropertymappingsApi.md#propertymappings_all_types_list) | **GET** /propertymappings/all/types/ | 
[**propertymappings_all_used_by_list**](PropertymappingsApi.md#propertymappings_all_used_by_list) | **GET** /propertymappings/all/{pm_uuid}/used_by/ | 
[**propertymappings_notification_create**](PropertymappingsApi.md#propertymappings_notification_create) | **POST** /propertymappings/notification/ | 
[**propertymappings_notification_destroy**](PropertymappingsApi.md#propertymappings_notification_destroy) | **DELETE** /propertymappings/notification/{pm_uuid}/ | 
[**propertymappings_notification_list**](PropertymappingsApi.md#propertymappings_notification_list) | **GET** /propertymappings/notification/ | 
[**propertymappings_notification_partial_update**](PropertymappingsApi.md#propertymappings_notification_partial_update) | **PATCH** /propertymappings/notification/{pm_uuid}/ | 
[**propertymappings_notification_retrieve**](PropertymappingsApi.md#propertymappings_notification_retrieve) | **GET** /propertymappings/notification/{pm_uuid}/ | 
[**propertymappings_notification_update**](PropertymappingsApi.md#propertymappings_notification_update) | **PUT** /propertymappings/notification/{pm_uuid}/ | 
[**propertymappings_notification_used_by_list**](PropertymappingsApi.md#propertymappings_notification_used_by_list) | **GET** /propertymappings/notification/{pm_uuid}/used_by/ | 
[**propertymappings_provider_google_workspace_create**](PropertymappingsApi.md#propertymappings_provider_google_workspace_create) | **POST** /propertymappings/provider/google_workspace/ | 
[**propertymappings_provider_google_workspace_destroy**](PropertymappingsApi.md#propertymappings_provider_google_workspace_destroy) | **DELETE** /propertymappings/provider/google_workspace/{pm_uuid}/ | 
[**propertymappings_provider_google_workspace_list**](PropertymappingsApi.md#propertymappings_provider_google_workspace_list) | **GET** /propertymappings/provider/google_workspace/ | 
[**propertymappings_provider_google_workspace_partial_update**](PropertymappingsApi.md#propertymappings_provider_google_workspace_partial_update) | **PATCH** /propertymappings/provider/google_workspace/{pm_uuid}/ | 
[**propertymappings_provider_google_workspace_retrieve**](PropertymappingsApi.md#propertymappings_provider_google_workspace_retrieve) | **GET** /propertymappings/provider/google_workspace/{pm_uuid}/ | 
[**propertymappings_provider_google_workspace_update**](PropertymappingsApi.md#propertymappings_provider_google_workspace_update) | **PUT** /propertymappings/provider/google_workspace/{pm_uuid}/ | 
[**propertymappings_provider_google_workspace_used_by_list**](PropertymappingsApi.md#propertymappings_provider_google_workspace_used_by_list) | **GET** /propertymappings/provider/google_workspace/{pm_uuid}/used_by/ | 
[**propertymappings_provider_microsoft_entra_create**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_create) | **POST** /propertymappings/provider/microsoft_entra/ | 
[**propertymappings_provider_microsoft_entra_destroy**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_destroy) | **DELETE** /propertymappings/provider/microsoft_entra/{pm_uuid}/ | 
[**propertymappings_provider_microsoft_entra_list**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_list) | **GET** /propertymappings/provider/microsoft_entra/ | 
[**propertymappings_provider_microsoft_entra_partial_update**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_partial_update) | **PATCH** /propertymappings/provider/microsoft_entra/{pm_uuid}/ | 
[**propertymappings_provider_microsoft_entra_retrieve**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_retrieve) | **GET** /propertymappings/provider/microsoft_entra/{pm_uuid}/ | 
[**propertymappings_provider_microsoft_entra_update**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_update) | **PUT** /propertymappings/provider/microsoft_entra/{pm_uuid}/ | 
[**propertymappings_provider_microsoft_entra_used_by_list**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_used_by_list) | **GET** /propertymappings/provider/microsoft_entra/{pm_uuid}/used_by/ | 
[**propertymappings_provider_rac_create**](PropertymappingsApi.md#propertymappings_provider_rac_create) | **POST** /propertymappings/provider/rac/ | 
[**propertymappings_provider_rac_destroy**](PropertymappingsApi.md#propertymappings_provider_rac_destroy) | **DELETE** /propertymappings/provider/rac/{pm_uuid}/ | 
[**propertymappings_provider_rac_list**](PropertymappingsApi.md#propertymappings_provider_rac_list) | **GET** /propertymappings/provider/rac/ | 
[**propertymappings_provider_rac_partial_update**](PropertymappingsApi.md#propertymappings_provider_rac_partial_update) | **PATCH** /propertymappings/provider/rac/{pm_uuid}/ | 
[**propertymappings_provider_rac_retrieve**](PropertymappingsApi.md#propertymappings_provider_rac_retrieve) | **GET** /propertymappings/provider/rac/{pm_uuid}/ | 
[**propertymappings_provider_rac_update**](PropertymappingsApi.md#propertymappings_provider_rac_update) | **PUT** /propertymappings/provider/rac/{pm_uuid}/ | 
[**propertymappings_provider_rac_used_by_list**](PropertymappingsApi.md#propertymappings_provider_rac_used_by_list) | **GET** /propertymappings/provider/rac/{pm_uuid}/used_by/ | 
[**propertymappings_provider_radius_create**](PropertymappingsApi.md#propertymappings_provider_radius_create) | **POST** /propertymappings/provider/radius/ | 
[**propertymappings_provider_radius_destroy**](PropertymappingsApi.md#propertymappings_provider_radius_destroy) | **DELETE** /propertymappings/provider/radius/{pm_uuid}/ | 
[**propertymappings_provider_radius_list**](PropertymappingsApi.md#propertymappings_provider_radius_list) | **GET** /propertymappings/provider/radius/ | 
[**propertymappings_provider_radius_partial_update**](PropertymappingsApi.md#propertymappings_provider_radius_partial_update) | **PATCH** /propertymappings/provider/radius/{pm_uuid}/ | 
[**propertymappings_provider_radius_retrieve**](PropertymappingsApi.md#propertymappings_provider_radius_retrieve) | **GET** /propertymappings/provider/radius/{pm_uuid}/ | 
[**propertymappings_provider_radius_update**](PropertymappingsApi.md#propertymappings_provider_radius_update) | **PUT** /propertymappings/provider/radius/{pm_uuid}/ | 
[**propertymappings_provider_radius_used_by_list**](PropertymappingsApi.md#propertymappings_provider_radius_used_by_list) | **GET** /propertymappings/provider/radius/{pm_uuid}/used_by/ | 
[**propertymappings_provider_saml_create**](PropertymappingsApi.md#propertymappings_provider_saml_create) | **POST** /propertymappings/provider/saml/ | 
[**propertymappings_provider_saml_destroy**](PropertymappingsApi.md#propertymappings_provider_saml_destroy) | **DELETE** /propertymappings/provider/saml/{pm_uuid}/ | 
[**propertymappings_provider_saml_list**](PropertymappingsApi.md#propertymappings_provider_saml_list) | **GET** /propertymappings/provider/saml/ | 
[**propertymappings_provider_saml_partial_update**](PropertymappingsApi.md#propertymappings_provider_saml_partial_update) | **PATCH** /propertymappings/provider/saml/{pm_uuid}/ | 
[**propertymappings_provider_saml_retrieve**](PropertymappingsApi.md#propertymappings_provider_saml_retrieve) | **GET** /propertymappings/provider/saml/{pm_uuid}/ | 
[**propertymappings_provider_saml_update**](PropertymappingsApi.md#propertymappings_provider_saml_update) | **PUT** /propertymappings/provider/saml/{pm_uuid}/ | 
[**propertymappings_provider_saml_used_by_list**](PropertymappingsApi.md#propertymappings_provider_saml_used_by_list) | **GET** /propertymappings/provider/saml/{pm_uuid}/used_by/ | 
[**propertymappings_provider_scim_create**](PropertymappingsApi.md#propertymappings_provider_scim_create) | **POST** /propertymappings/provider/scim/ | 
[**propertymappings_provider_scim_destroy**](PropertymappingsApi.md#propertymappings_provider_scim_destroy) | **DELETE** /propertymappings/provider/scim/{pm_uuid}/ | 
[**propertymappings_provider_scim_list**](PropertymappingsApi.md#propertymappings_provider_scim_list) | **GET** /propertymappings/provider/scim/ | 
[**propertymappings_provider_scim_partial_update**](PropertymappingsApi.md#propertymappings_provider_scim_partial_update) | **PATCH** /propertymappings/provider/scim/{pm_uuid}/ | 
[**propertymappings_provider_scim_retrieve**](PropertymappingsApi.md#propertymappings_provider_scim_retrieve) | **GET** /propertymappings/provider/scim/{pm_uuid}/ | 
[**propertymappings_provider_scim_update**](PropertymappingsApi.md#propertymappings_provider_scim_update) | **PUT** /propertymappings/provider/scim/{pm_uuid}/ | 
[**propertymappings_provider_scim_used_by_list**](PropertymappingsApi.md#propertymappings_provider_scim_used_by_list) | **GET** /propertymappings/provider/scim/{pm_uuid}/used_by/ | 
[**propertymappings_provider_scope_create**](PropertymappingsApi.md#propertymappings_provider_scope_create) | **POST** /propertymappings/provider/scope/ | 
[**propertymappings_provider_scope_destroy**](PropertymappingsApi.md#propertymappings_provider_scope_destroy) | **DELETE** /propertymappings/provider/scope/{pm_uuid}/ | 
[**propertymappings_provider_scope_list**](PropertymappingsApi.md#propertymappings_provider_scope_list) | **GET** /propertymappings/provider/scope/ | 
[**propertymappings_provider_scope_partial_update**](PropertymappingsApi.md#propertymappings_provider_scope_partial_update) | **PATCH** /propertymappings/provider/scope/{pm_uuid}/ | 
[**propertymappings_provider_scope_retrieve**](PropertymappingsApi.md#propertymappings_provider_scope_retrieve) | **GET** /propertymappings/provider/scope/{pm_uuid}/ | 
[**propertymappings_provider_scope_update**](PropertymappingsApi.md#propertymappings_provider_scope_update) | **PUT** /propertymappings/provider/scope/{pm_uuid}/ | 
[**propertymappings_provider_scope_used_by_list**](PropertymappingsApi.md#propertymappings_provider_scope_used_by_list) | **GET** /propertymappings/provider/scope/{pm_uuid}/used_by/ | 
[**propertymappings_source_kerberos_create**](PropertymappingsApi.md#propertymappings_source_kerberos_create) | **POST** /propertymappings/source/kerberos/ | 
[**propertymappings_source_kerberos_destroy**](PropertymappingsApi.md#propertymappings_source_kerberos_destroy) | **DELETE** /propertymappings/source/kerberos/{pm_uuid}/ | 
[**propertymappings_source_kerberos_list**](PropertymappingsApi.md#propertymappings_source_kerberos_list) | **GET** /propertymappings/source/kerberos/ | 
[**propertymappings_source_kerberos_partial_update**](PropertymappingsApi.md#propertymappings_source_kerberos_partial_update) | **PATCH** /propertymappings/source/kerberos/{pm_uuid}/ | 
[**propertymappings_source_kerberos_retrieve**](PropertymappingsApi.md#propertymappings_source_kerberos_retrieve) | **GET** /propertymappings/source/kerberos/{pm_uuid}/ | 
[**propertymappings_source_kerberos_update**](PropertymappingsApi.md#propertymappings_source_kerberos_update) | **PUT** /propertymappings/source/kerberos/{pm_uuid}/ | 
[**propertymappings_source_kerberos_used_by_list**](PropertymappingsApi.md#propertymappings_source_kerberos_used_by_list) | **GET** /propertymappings/source/kerberos/{pm_uuid}/used_by/ | 
[**propertymappings_source_ldap_create**](PropertymappingsApi.md#propertymappings_source_ldap_create) | **POST** /propertymappings/source/ldap/ | 
[**propertymappings_source_ldap_destroy**](PropertymappingsApi.md#propertymappings_source_ldap_destroy) | **DELETE** /propertymappings/source/ldap/{pm_uuid}/ | 
[**propertymappings_source_ldap_list**](PropertymappingsApi.md#propertymappings_source_ldap_list) | **GET** /propertymappings/source/ldap/ | 
[**propertymappings_source_ldap_partial_update**](PropertymappingsApi.md#propertymappings_source_ldap_partial_update) | **PATCH** /propertymappings/source/ldap/{pm_uuid}/ | 
[**propertymappings_source_ldap_retrieve**](PropertymappingsApi.md#propertymappings_source_ldap_retrieve) | **GET** /propertymappings/source/ldap/{pm_uuid}/ | 
[**propertymappings_source_ldap_update**](PropertymappingsApi.md#propertymappings_source_ldap_update) | **PUT** /propertymappings/source/ldap/{pm_uuid}/ | 
[**propertymappings_source_ldap_used_by_list**](PropertymappingsApi.md#propertymappings_source_ldap_used_by_list) | **GET** /propertymappings/source/ldap/{pm_uuid}/used_by/ | 
[**propertymappings_source_oauth_create**](PropertymappingsApi.md#propertymappings_source_oauth_create) | **POST** /propertymappings/source/oauth/ | 
[**propertymappings_source_oauth_destroy**](PropertymappingsApi.md#propertymappings_source_oauth_destroy) | **DELETE** /propertymappings/source/oauth/{pm_uuid}/ | 
[**propertymappings_source_oauth_list**](PropertymappingsApi.md#propertymappings_source_oauth_list) | **GET** /propertymappings/source/oauth/ | 
[**propertymappings_source_oauth_partial_update**](PropertymappingsApi.md#propertymappings_source_oauth_partial_update) | **PATCH** /propertymappings/source/oauth/{pm_uuid}/ | 
[**propertymappings_source_oauth_retrieve**](PropertymappingsApi.md#propertymappings_source_oauth_retrieve) | **GET** /propertymappings/source/oauth/{pm_uuid}/ | 
[**propertymappings_source_oauth_update**](PropertymappingsApi.md#propertymappings_source_oauth_update) | **PUT** /propertymappings/source/oauth/{pm_uuid}/ | 
[**propertymappings_source_oauth_used_by_list**](PropertymappingsApi.md#propertymappings_source_oauth_used_by_list) | **GET** /propertymappings/source/oauth/{pm_uuid}/used_by/ | 
[**propertymappings_source_plex_create**](PropertymappingsApi.md#propertymappings_source_plex_create) | **POST** /propertymappings/source/plex/ | 
[**propertymappings_source_plex_destroy**](PropertymappingsApi.md#propertymappings_source_plex_destroy) | **DELETE** /propertymappings/source/plex/{pm_uuid}/ | 
[**propertymappings_source_plex_list**](PropertymappingsApi.md#propertymappings_source_plex_list) | **GET** /propertymappings/source/plex/ | 
[**propertymappings_source_plex_partial_update**](PropertymappingsApi.md#propertymappings_source_plex_partial_update) | **PATCH** /propertymappings/source/plex/{pm_uuid}/ | 
[**propertymappings_source_plex_retrieve**](PropertymappingsApi.md#propertymappings_source_plex_retrieve) | **GET** /propertymappings/source/plex/{pm_uuid}/ | 
[**propertymappings_source_plex_update**](PropertymappingsApi.md#propertymappings_source_plex_update) | **PUT** /propertymappings/source/plex/{pm_uuid}/ | 
[**propertymappings_source_plex_used_by_list**](PropertymappingsApi.md#propertymappings_source_plex_used_by_list) | **GET** /propertymappings/source/plex/{pm_uuid}/used_by/ | 
[**propertymappings_source_saml_create**](PropertymappingsApi.md#propertymappings_source_saml_create) | **POST** /propertymappings/source/saml/ | 
[**propertymappings_source_saml_destroy**](PropertymappingsApi.md#propertymappings_source_saml_destroy) | **DELETE** /propertymappings/source/saml/{pm_uuid}/ | 
[**propertymappings_source_saml_list**](PropertymappingsApi.md#propertymappings_source_saml_list) | **GET** /propertymappings/source/saml/ | 
[**propertymappings_source_saml_partial_update**](PropertymappingsApi.md#propertymappings_source_saml_partial_update) | **PATCH** /propertymappings/source/saml/{pm_uuid}/ | 
[**propertymappings_source_saml_retrieve**](PropertymappingsApi.md#propertymappings_source_saml_retrieve) | **GET** /propertymappings/source/saml/{pm_uuid}/ | 
[**propertymappings_source_saml_update**](PropertymappingsApi.md#propertymappings_source_saml_update) | **PUT** /propertymappings/source/saml/{pm_uuid}/ | 
[**propertymappings_source_saml_used_by_list**](PropertymappingsApi.md#propertymappings_source_saml_used_by_list) | **GET** /propertymappings/source/saml/{pm_uuid}/used_by/ | 
[**propertymappings_source_scim_create**](PropertymappingsApi.md#propertymappings_source_scim_create) | **POST** /propertymappings/source/scim/ | 
[**propertymappings_source_scim_destroy**](PropertymappingsApi.md#propertymappings_source_scim_destroy) | **DELETE** /propertymappings/source/scim/{pm_uuid}/ | 
[**propertymappings_source_scim_list**](PropertymappingsApi.md#propertymappings_source_scim_list) | **GET** /propertymappings/source/scim/ | 
[**propertymappings_source_scim_partial_update**](PropertymappingsApi.md#propertymappings_source_scim_partial_update) | **PATCH** /propertymappings/source/scim/{pm_uuid}/ | 
[**propertymappings_source_scim_retrieve**](PropertymappingsApi.md#propertymappings_source_scim_retrieve) | **GET** /propertymappings/source/scim/{pm_uuid}/ | 
[**propertymappings_source_scim_update**](PropertymappingsApi.md#propertymappings_source_scim_update) | **PUT** /propertymappings/source/scim/{pm_uuid}/ | 
[**propertymappings_source_scim_used_by_list**](PropertymappingsApi.md#propertymappings_source_scim_used_by_list) | **GET** /propertymappings/source/scim/{pm_uuid}/used_by/ | 


# **propertymappings_all_destroy**
> propertymappings_all_destroy(pm_uuid)

PropertyMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Property Mapping.

    try:
        api_instance.propertymappings_all_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_all_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Property Mapping. | 

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

# **propertymappings_all_list**
> PaginatedPropertyMappingList propertymappings_all_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)

PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_property_mapping_list import PaginatedPropertyMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    managed = ['managed_example'] # List[str] |  (optional)
    managed__isnull = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_all_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_all_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_all_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **managed__isnull** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedPropertyMappingList**](PaginatedPropertyMappingList.md)

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

# **propertymappings_all_retrieve**
> PropertyMapping propertymappings_all_retrieve(pm_uuid)

PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.property_mapping import PropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Property Mapping.

    try:
        api_response = api_instance.propertymappings_all_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_all_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_all_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Property Mapping. | 

### Return type

[**PropertyMapping**](PropertyMapping.md)

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

# **propertymappings_all_test_create**
> PropertyMappingTestResult propertymappings_all_test_create(pm_uuid, format_result=format_result, property_mapping_test_request=property_mapping_test_request)

Test Property Mapping

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.property_mapping_test_request import PropertyMappingTestRequest
from authentik_client.models.property_mapping_test_result import PropertyMappingTestResult
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Property Mapping.
    format_result = True # bool |  (optional)
    property_mapping_test_request = authentik_client.PropertyMappingTestRequest() # PropertyMappingTestRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_all_test_create(pm_uuid, format_result=format_result, property_mapping_test_request=property_mapping_test_request)
        print("The response of PropertymappingsApi->propertymappings_all_test_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_all_test_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Property Mapping. | 
 **format_result** | **bool**|  | [optional] 
 **property_mapping_test_request** | [**PropertyMappingTestRequest**](PropertyMappingTestRequest.md)|  | [optional] 

### Return type

[**PropertyMappingTestResult**](PropertyMappingTestResult.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid parameters |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **propertymappings_all_types_list**
> List[TypeCreate] propertymappings_all_types_list()

Get all creatable types

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.type_create import TypeCreate
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
    api_instance = authentik_client.PropertymappingsApi(api_client)

    try:
        api_response = api_instance.propertymappings_all_types_list()
        print("The response of PropertymappingsApi->propertymappings_all_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_all_types_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TypeCreate]**](TypeCreate.md)

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

# **propertymappings_all_used_by_list**
> List[UsedBy] propertymappings_all_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Property Mapping.

    try:
        api_response = api_instance.propertymappings_all_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_all_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_all_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Property Mapping. | 

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

# **propertymappings_notification_create**
> NotificationWebhookMapping propertymappings_notification_create(notification_webhook_mapping_request)

NotificationWebhookMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.notification_webhook_mapping import NotificationWebhookMapping
from authentik_client.models.notification_webhook_mapping_request import NotificationWebhookMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    notification_webhook_mapping_request = authentik_client.NotificationWebhookMappingRequest() # NotificationWebhookMappingRequest | 

    try:
        api_response = api_instance.propertymappings_notification_create(notification_webhook_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_notification_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_webhook_mapping_request** | [**NotificationWebhookMappingRequest**](NotificationWebhookMappingRequest.md)|  | 

### Return type

[**NotificationWebhookMapping**](NotificationWebhookMapping.md)

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

# **propertymappings_notification_destroy**
> propertymappings_notification_destroy(pm_uuid)

NotificationWebhookMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Webhook Mapping.

    try:
        api_instance.propertymappings_notification_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Webhook Mapping. | 

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

# **propertymappings_notification_list**
> PaginatedNotificationWebhookMappingList propertymappings_notification_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)

NotificationWebhookMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_notification_webhook_mapping_list import PaginatedNotificationWebhookMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_notification_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_notification_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_list: %s\n" % e)
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

[**PaginatedNotificationWebhookMappingList**](PaginatedNotificationWebhookMappingList.md)

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

# **propertymappings_notification_partial_update**
> NotificationWebhookMapping propertymappings_notification_partial_update(pm_uuid, patched_notification_webhook_mapping_request=patched_notification_webhook_mapping_request)

NotificationWebhookMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.notification_webhook_mapping import NotificationWebhookMapping
from authentik_client.models.patched_notification_webhook_mapping_request import PatchedNotificationWebhookMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Webhook Mapping.
    patched_notification_webhook_mapping_request = authentik_client.PatchedNotificationWebhookMappingRequest() # PatchedNotificationWebhookMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_notification_partial_update(pm_uuid, patched_notification_webhook_mapping_request=patched_notification_webhook_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_notification_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Webhook Mapping. | 
 **patched_notification_webhook_mapping_request** | [**PatchedNotificationWebhookMappingRequest**](PatchedNotificationWebhookMappingRequest.md)|  | [optional] 

### Return type

[**NotificationWebhookMapping**](NotificationWebhookMapping.md)

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

# **propertymappings_notification_retrieve**
> NotificationWebhookMapping propertymappings_notification_retrieve(pm_uuid)

NotificationWebhookMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.notification_webhook_mapping import NotificationWebhookMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Webhook Mapping.

    try:
        api_response = api_instance.propertymappings_notification_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_notification_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Webhook Mapping. | 

### Return type

[**NotificationWebhookMapping**](NotificationWebhookMapping.md)

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

# **propertymappings_notification_update**
> NotificationWebhookMapping propertymappings_notification_update(pm_uuid, notification_webhook_mapping_request)

NotificationWebhookMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.notification_webhook_mapping import NotificationWebhookMapping
from authentik_client.models.notification_webhook_mapping_request import NotificationWebhookMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Webhook Mapping.
    notification_webhook_mapping_request = authentik_client.NotificationWebhookMappingRequest() # NotificationWebhookMappingRequest | 

    try:
        api_response = api_instance.propertymappings_notification_update(pm_uuid, notification_webhook_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_notification_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Webhook Mapping. | 
 **notification_webhook_mapping_request** | [**NotificationWebhookMappingRequest**](NotificationWebhookMappingRequest.md)|  | 

### Return type

[**NotificationWebhookMapping**](NotificationWebhookMapping.md)

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

# **propertymappings_notification_used_by_list**
> List[UsedBy] propertymappings_notification_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Webhook Mapping.

    try:
        api_response = api_instance.propertymappings_notification_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_notification_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Webhook Mapping. | 

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

# **propertymappings_provider_google_workspace_create**
> GoogleWorkspaceProviderMapping propertymappings_provider_google_workspace_create(google_workspace_provider_mapping_request)

GoogleWorkspaceProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.google_workspace_provider_mapping import GoogleWorkspaceProviderMapping
from authentik_client.models.google_workspace_provider_mapping_request import GoogleWorkspaceProviderMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    google_workspace_provider_mapping_request = authentik_client.GoogleWorkspaceProviderMappingRequest() # GoogleWorkspaceProviderMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_google_workspace_create(google_workspace_provider_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_google_workspace_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_workspace_provider_mapping_request** | [**GoogleWorkspaceProviderMappingRequest**](GoogleWorkspaceProviderMappingRequest.md)|  | 

### Return type

[**GoogleWorkspaceProviderMapping**](GoogleWorkspaceProviderMapping.md)

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

# **propertymappings_provider_google_workspace_destroy**
> propertymappings_provider_google_workspace_destroy(pm_uuid)

GoogleWorkspaceProviderMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Google Workspace Provider Mapping.

    try:
        api_instance.propertymappings_provider_google_workspace_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Google Workspace Provider Mapping. | 

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

# **propertymappings_provider_google_workspace_list**
> PaginatedGoogleWorkspaceProviderMappingList propertymappings_provider_google_workspace_list(expression=expression, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, search=search)

GoogleWorkspaceProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_google_workspace_provider_mapping_list import PaginatedGoogleWorkspaceProviderMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    expression = 'expression_example' # str |  (optional)
    managed = ['managed_example'] # List[str] |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    pm_uuid = 'pm_uuid_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_provider_google_workspace_list(expression=expression, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, search=search)
        print("The response of PropertymappingsApi->propertymappings_provider_google_workspace_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expression** | **str**|  | [optional] 
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **pm_uuid** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedGoogleWorkspaceProviderMappingList**](PaginatedGoogleWorkspaceProviderMappingList.md)

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

# **propertymappings_provider_google_workspace_partial_update**
> GoogleWorkspaceProviderMapping propertymappings_provider_google_workspace_partial_update(pm_uuid, patched_google_workspace_provider_mapping_request=patched_google_workspace_provider_mapping_request)

GoogleWorkspaceProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.google_workspace_provider_mapping import GoogleWorkspaceProviderMapping
from authentik_client.models.patched_google_workspace_provider_mapping_request import PatchedGoogleWorkspaceProviderMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Google Workspace Provider Mapping.
    patched_google_workspace_provider_mapping_request = authentik_client.PatchedGoogleWorkspaceProviderMappingRequest() # PatchedGoogleWorkspaceProviderMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_provider_google_workspace_partial_update(pm_uuid, patched_google_workspace_provider_mapping_request=patched_google_workspace_provider_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_google_workspace_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Google Workspace Provider Mapping. | 
 **patched_google_workspace_provider_mapping_request** | [**PatchedGoogleWorkspaceProviderMappingRequest**](PatchedGoogleWorkspaceProviderMappingRequest.md)|  | [optional] 

### Return type

[**GoogleWorkspaceProviderMapping**](GoogleWorkspaceProviderMapping.md)

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

# **propertymappings_provider_google_workspace_retrieve**
> GoogleWorkspaceProviderMapping propertymappings_provider_google_workspace_retrieve(pm_uuid)

GoogleWorkspaceProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.google_workspace_provider_mapping import GoogleWorkspaceProviderMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Google Workspace Provider Mapping.

    try:
        api_response = api_instance.propertymappings_provider_google_workspace_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_google_workspace_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Google Workspace Provider Mapping. | 

### Return type

[**GoogleWorkspaceProviderMapping**](GoogleWorkspaceProviderMapping.md)

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

# **propertymappings_provider_google_workspace_update**
> GoogleWorkspaceProviderMapping propertymappings_provider_google_workspace_update(pm_uuid, google_workspace_provider_mapping_request)

GoogleWorkspaceProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.google_workspace_provider_mapping import GoogleWorkspaceProviderMapping
from authentik_client.models.google_workspace_provider_mapping_request import GoogleWorkspaceProviderMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Google Workspace Provider Mapping.
    google_workspace_provider_mapping_request = authentik_client.GoogleWorkspaceProviderMappingRequest() # GoogleWorkspaceProviderMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_google_workspace_update(pm_uuid, google_workspace_provider_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_google_workspace_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Google Workspace Provider Mapping. | 
 **google_workspace_provider_mapping_request** | [**GoogleWorkspaceProviderMappingRequest**](GoogleWorkspaceProviderMappingRequest.md)|  | 

### Return type

[**GoogleWorkspaceProviderMapping**](GoogleWorkspaceProviderMapping.md)

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

# **propertymappings_provider_google_workspace_used_by_list**
> List[UsedBy] propertymappings_provider_google_workspace_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Google Workspace Provider Mapping.

    try:
        api_response = api_instance.propertymappings_provider_google_workspace_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_google_workspace_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Google Workspace Provider Mapping. | 

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

# **propertymappings_provider_microsoft_entra_create**
> MicrosoftEntraProviderMapping propertymappings_provider_microsoft_entra_create(microsoft_entra_provider_mapping_request)

MicrosoftEntraProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.microsoft_entra_provider_mapping import MicrosoftEntraProviderMapping
from authentik_client.models.microsoft_entra_provider_mapping_request import MicrosoftEntraProviderMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    microsoft_entra_provider_mapping_request = authentik_client.MicrosoftEntraProviderMappingRequest() # MicrosoftEntraProviderMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_microsoft_entra_create(microsoft_entra_provider_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_microsoft_entra_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **microsoft_entra_provider_mapping_request** | [**MicrosoftEntraProviderMappingRequest**](MicrosoftEntraProviderMappingRequest.md)|  | 

### Return type

[**MicrosoftEntraProviderMapping**](MicrosoftEntraProviderMapping.md)

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

# **propertymappings_provider_microsoft_entra_destroy**
> propertymappings_provider_microsoft_entra_destroy(pm_uuid)

MicrosoftEntraProviderMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Microsoft Entra Provider Mapping.

    try:
        api_instance.propertymappings_provider_microsoft_entra_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Microsoft Entra Provider Mapping. | 

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

# **propertymappings_provider_microsoft_entra_list**
> PaginatedMicrosoftEntraProviderMappingList propertymappings_provider_microsoft_entra_list(expression=expression, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, search=search)

MicrosoftEntraProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_microsoft_entra_provider_mapping_list import PaginatedMicrosoftEntraProviderMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    expression = 'expression_example' # str |  (optional)
    managed = ['managed_example'] # List[str] |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    pm_uuid = 'pm_uuid_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_provider_microsoft_entra_list(expression=expression, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, search=search)
        print("The response of PropertymappingsApi->propertymappings_provider_microsoft_entra_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expression** | **str**|  | [optional] 
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **pm_uuid** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedMicrosoftEntraProviderMappingList**](PaginatedMicrosoftEntraProviderMappingList.md)

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

# **propertymappings_provider_microsoft_entra_partial_update**
> MicrosoftEntraProviderMapping propertymappings_provider_microsoft_entra_partial_update(pm_uuid, patched_microsoft_entra_provider_mapping_request=patched_microsoft_entra_provider_mapping_request)

MicrosoftEntraProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.microsoft_entra_provider_mapping import MicrosoftEntraProviderMapping
from authentik_client.models.patched_microsoft_entra_provider_mapping_request import PatchedMicrosoftEntraProviderMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Microsoft Entra Provider Mapping.
    patched_microsoft_entra_provider_mapping_request = authentik_client.PatchedMicrosoftEntraProviderMappingRequest() # PatchedMicrosoftEntraProviderMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_provider_microsoft_entra_partial_update(pm_uuid, patched_microsoft_entra_provider_mapping_request=patched_microsoft_entra_provider_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_microsoft_entra_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Microsoft Entra Provider Mapping. | 
 **patched_microsoft_entra_provider_mapping_request** | [**PatchedMicrosoftEntraProviderMappingRequest**](PatchedMicrosoftEntraProviderMappingRequest.md)|  | [optional] 

### Return type

[**MicrosoftEntraProviderMapping**](MicrosoftEntraProviderMapping.md)

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

# **propertymappings_provider_microsoft_entra_retrieve**
> MicrosoftEntraProviderMapping propertymappings_provider_microsoft_entra_retrieve(pm_uuid)

MicrosoftEntraProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.microsoft_entra_provider_mapping import MicrosoftEntraProviderMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Microsoft Entra Provider Mapping.

    try:
        api_response = api_instance.propertymappings_provider_microsoft_entra_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_microsoft_entra_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Microsoft Entra Provider Mapping. | 

### Return type

[**MicrosoftEntraProviderMapping**](MicrosoftEntraProviderMapping.md)

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

# **propertymappings_provider_microsoft_entra_update**
> MicrosoftEntraProviderMapping propertymappings_provider_microsoft_entra_update(pm_uuid, microsoft_entra_provider_mapping_request)

MicrosoftEntraProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.microsoft_entra_provider_mapping import MicrosoftEntraProviderMapping
from authentik_client.models.microsoft_entra_provider_mapping_request import MicrosoftEntraProviderMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Microsoft Entra Provider Mapping.
    microsoft_entra_provider_mapping_request = authentik_client.MicrosoftEntraProviderMappingRequest() # MicrosoftEntraProviderMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_microsoft_entra_update(pm_uuid, microsoft_entra_provider_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_microsoft_entra_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Microsoft Entra Provider Mapping. | 
 **microsoft_entra_provider_mapping_request** | [**MicrosoftEntraProviderMappingRequest**](MicrosoftEntraProviderMappingRequest.md)|  | 

### Return type

[**MicrosoftEntraProviderMapping**](MicrosoftEntraProviderMapping.md)

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

# **propertymappings_provider_microsoft_entra_used_by_list**
> List[UsedBy] propertymappings_provider_microsoft_entra_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Microsoft Entra Provider Mapping.

    try:
        api_response = api_instance.propertymappings_provider_microsoft_entra_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_microsoft_entra_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Microsoft Entra Provider Mapping. | 

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

# **propertymappings_provider_rac_create**
> RACPropertyMapping propertymappings_provider_rac_create(rac_property_mapping_request)

RACPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.rac_property_mapping import RACPropertyMapping
from authentik_client.models.rac_property_mapping_request import RACPropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    rac_property_mapping_request = authentik_client.RACPropertyMappingRequest() # RACPropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_rac_create(rac_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_rac_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_rac_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rac_property_mapping_request** | [**RACPropertyMappingRequest**](RACPropertyMappingRequest.md)|  | 

### Return type

[**RACPropertyMapping**](RACPropertyMapping.md)

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

# **propertymappings_provider_rac_destroy**
> propertymappings_provider_rac_destroy(pm_uuid)

RACPropertyMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this RAC Provider Property Mapping.

    try:
        api_instance.propertymappings_provider_rac_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_rac_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this RAC Provider Property Mapping. | 

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

# **propertymappings_provider_rac_list**
> PaginatedRACPropertyMappingList propertymappings_provider_rac_list(managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, search=search)

RACPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_rac_property_mapping_list import PaginatedRACPropertyMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    managed = ['managed_example'] # List[str] |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_provider_rac_list(managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_provider_rac_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_rac_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedRACPropertyMappingList**](PaginatedRACPropertyMappingList.md)

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

# **propertymappings_provider_rac_partial_update**
> RACPropertyMapping propertymappings_provider_rac_partial_update(pm_uuid, patched_rac_property_mapping_request=patched_rac_property_mapping_request)

RACPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_rac_property_mapping_request import PatchedRACPropertyMappingRequest
from authentik_client.models.rac_property_mapping import RACPropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this RAC Provider Property Mapping.
    patched_rac_property_mapping_request = authentik_client.PatchedRACPropertyMappingRequest() # PatchedRACPropertyMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_provider_rac_partial_update(pm_uuid, patched_rac_property_mapping_request=patched_rac_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_rac_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_rac_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this RAC Provider Property Mapping. | 
 **patched_rac_property_mapping_request** | [**PatchedRACPropertyMappingRequest**](PatchedRACPropertyMappingRequest.md)|  | [optional] 

### Return type

[**RACPropertyMapping**](RACPropertyMapping.md)

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

# **propertymappings_provider_rac_retrieve**
> RACPropertyMapping propertymappings_provider_rac_retrieve(pm_uuid)

RACPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.rac_property_mapping import RACPropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this RAC Provider Property Mapping.

    try:
        api_response = api_instance.propertymappings_provider_rac_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_rac_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_rac_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this RAC Provider Property Mapping. | 

### Return type

[**RACPropertyMapping**](RACPropertyMapping.md)

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

# **propertymappings_provider_rac_update**
> RACPropertyMapping propertymappings_provider_rac_update(pm_uuid, rac_property_mapping_request)

RACPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.rac_property_mapping import RACPropertyMapping
from authentik_client.models.rac_property_mapping_request import RACPropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this RAC Provider Property Mapping.
    rac_property_mapping_request = authentik_client.RACPropertyMappingRequest() # RACPropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_rac_update(pm_uuid, rac_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_rac_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_rac_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this RAC Provider Property Mapping. | 
 **rac_property_mapping_request** | [**RACPropertyMappingRequest**](RACPropertyMappingRequest.md)|  | 

### Return type

[**RACPropertyMapping**](RACPropertyMapping.md)

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

# **propertymappings_provider_rac_used_by_list**
> List[UsedBy] propertymappings_provider_rac_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this RAC Provider Property Mapping.

    try:
        api_response = api_instance.propertymappings_provider_rac_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_rac_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_rac_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this RAC Provider Property Mapping. | 

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

# **propertymappings_provider_radius_create**
> RadiusProviderPropertyMapping propertymappings_provider_radius_create(radius_provider_property_mapping_request)

RadiusProviderPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.radius_provider_property_mapping import RadiusProviderPropertyMapping
from authentik_client.models.radius_provider_property_mapping_request import RadiusProviderPropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    radius_provider_property_mapping_request = authentik_client.RadiusProviderPropertyMappingRequest() # RadiusProviderPropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_radius_create(radius_provider_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_radius_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_radius_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radius_provider_property_mapping_request** | [**RadiusProviderPropertyMappingRequest**](RadiusProviderPropertyMappingRequest.md)|  | 

### Return type

[**RadiusProviderPropertyMapping**](RadiusProviderPropertyMapping.md)

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

# **propertymappings_provider_radius_destroy**
> propertymappings_provider_radius_destroy(pm_uuid)

RadiusProviderPropertyMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Radius Provider Property Mapping.

    try:
        api_instance.propertymappings_provider_radius_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_radius_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Radius Provider Property Mapping. | 

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

# **propertymappings_provider_radius_list**
> PaginatedRadiusProviderPropertyMappingList propertymappings_provider_radius_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)

RadiusProviderPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_radius_provider_property_mapping_list import PaginatedRadiusProviderPropertyMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    managed = ['managed_example'] # List[str] |  (optional)
    managed__isnull = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_provider_radius_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_provider_radius_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_radius_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **managed__isnull** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedRadiusProviderPropertyMappingList**](PaginatedRadiusProviderPropertyMappingList.md)

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

# **propertymappings_provider_radius_partial_update**
> RadiusProviderPropertyMapping propertymappings_provider_radius_partial_update(pm_uuid, patched_radius_provider_property_mapping_request=patched_radius_provider_property_mapping_request)

RadiusProviderPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_radius_provider_property_mapping_request import PatchedRadiusProviderPropertyMappingRequest
from authentik_client.models.radius_provider_property_mapping import RadiusProviderPropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Radius Provider Property Mapping.
    patched_radius_provider_property_mapping_request = authentik_client.PatchedRadiusProviderPropertyMappingRequest() # PatchedRadiusProviderPropertyMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_provider_radius_partial_update(pm_uuid, patched_radius_provider_property_mapping_request=patched_radius_provider_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_radius_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_radius_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Radius Provider Property Mapping. | 
 **patched_radius_provider_property_mapping_request** | [**PatchedRadiusProviderPropertyMappingRequest**](PatchedRadiusProviderPropertyMappingRequest.md)|  | [optional] 

### Return type

[**RadiusProviderPropertyMapping**](RadiusProviderPropertyMapping.md)

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

# **propertymappings_provider_radius_retrieve**
> RadiusProviderPropertyMapping propertymappings_provider_radius_retrieve(pm_uuid)

RadiusProviderPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.radius_provider_property_mapping import RadiusProviderPropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Radius Provider Property Mapping.

    try:
        api_response = api_instance.propertymappings_provider_radius_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_radius_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_radius_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Radius Provider Property Mapping. | 

### Return type

[**RadiusProviderPropertyMapping**](RadiusProviderPropertyMapping.md)

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

# **propertymappings_provider_radius_update**
> RadiusProviderPropertyMapping propertymappings_provider_radius_update(pm_uuid, radius_provider_property_mapping_request)

RadiusProviderPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.radius_provider_property_mapping import RadiusProviderPropertyMapping
from authentik_client.models.radius_provider_property_mapping_request import RadiusProviderPropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Radius Provider Property Mapping.
    radius_provider_property_mapping_request = authentik_client.RadiusProviderPropertyMappingRequest() # RadiusProviderPropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_radius_update(pm_uuid, radius_provider_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_radius_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_radius_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Radius Provider Property Mapping. | 
 **radius_provider_property_mapping_request** | [**RadiusProviderPropertyMappingRequest**](RadiusProviderPropertyMappingRequest.md)|  | 

### Return type

[**RadiusProviderPropertyMapping**](RadiusProviderPropertyMapping.md)

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

# **propertymappings_provider_radius_used_by_list**
> List[UsedBy] propertymappings_provider_radius_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Radius Provider Property Mapping.

    try:
        api_response = api_instance.propertymappings_provider_radius_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_radius_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_radius_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Radius Provider Property Mapping. | 

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

# **propertymappings_provider_saml_create**
> SAMLPropertyMapping propertymappings_provider_saml_create(saml_property_mapping_request)

SAMLPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.saml_property_mapping import SAMLPropertyMapping
from authentik_client.models.saml_property_mapping_request import SAMLPropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    saml_property_mapping_request = authentik_client.SAMLPropertyMappingRequest() # SAMLPropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_saml_create(saml_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_saml_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_saml_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_property_mapping_request** | [**SAMLPropertyMappingRequest**](SAMLPropertyMappingRequest.md)|  | 

### Return type

[**SAMLPropertyMapping**](SAMLPropertyMapping.md)

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

# **propertymappings_provider_saml_destroy**
> propertymappings_provider_saml_destroy(pm_uuid)

SAMLPropertyMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Provider Property Mapping.

    try:
        api_instance.propertymappings_provider_saml_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_saml_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Provider Property Mapping. | 

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

# **propertymappings_provider_saml_list**
> PaginatedSAMLPropertyMappingList propertymappings_provider_saml_list(friendly_name=friendly_name, managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, saml_name=saml_name, search=search)

SAMLPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_saml_property_mapping_list import PaginatedSAMLPropertyMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    friendly_name = 'friendly_name_example' # str |  (optional)
    managed = ['managed_example'] # List[str] |  (optional)
    managed__isnull = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    saml_name = 'saml_name_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_provider_saml_list(friendly_name=friendly_name, managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, saml_name=saml_name, search=search)
        print("The response of PropertymappingsApi->propertymappings_provider_saml_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_saml_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**|  | [optional] 
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **managed__isnull** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **saml_name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedSAMLPropertyMappingList**](PaginatedSAMLPropertyMappingList.md)

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

# **propertymappings_provider_saml_partial_update**
> SAMLPropertyMapping propertymappings_provider_saml_partial_update(pm_uuid, patched_saml_property_mapping_request=patched_saml_property_mapping_request)

SAMLPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_saml_property_mapping_request import PatchedSAMLPropertyMappingRequest
from authentik_client.models.saml_property_mapping import SAMLPropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Provider Property Mapping.
    patched_saml_property_mapping_request = authentik_client.PatchedSAMLPropertyMappingRequest() # PatchedSAMLPropertyMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_provider_saml_partial_update(pm_uuid, patched_saml_property_mapping_request=patched_saml_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_saml_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_saml_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Provider Property Mapping. | 
 **patched_saml_property_mapping_request** | [**PatchedSAMLPropertyMappingRequest**](PatchedSAMLPropertyMappingRequest.md)|  | [optional] 

### Return type

[**SAMLPropertyMapping**](SAMLPropertyMapping.md)

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

# **propertymappings_provider_saml_retrieve**
> SAMLPropertyMapping propertymappings_provider_saml_retrieve(pm_uuid)

SAMLPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.saml_property_mapping import SAMLPropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Provider Property Mapping.

    try:
        api_response = api_instance.propertymappings_provider_saml_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_saml_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_saml_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Provider Property Mapping. | 

### Return type

[**SAMLPropertyMapping**](SAMLPropertyMapping.md)

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

# **propertymappings_provider_saml_update**
> SAMLPropertyMapping propertymappings_provider_saml_update(pm_uuid, saml_property_mapping_request)

SAMLPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.saml_property_mapping import SAMLPropertyMapping
from authentik_client.models.saml_property_mapping_request import SAMLPropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Provider Property Mapping.
    saml_property_mapping_request = authentik_client.SAMLPropertyMappingRequest() # SAMLPropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_saml_update(pm_uuid, saml_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_saml_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_saml_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Provider Property Mapping. | 
 **saml_property_mapping_request** | [**SAMLPropertyMappingRequest**](SAMLPropertyMappingRequest.md)|  | 

### Return type

[**SAMLPropertyMapping**](SAMLPropertyMapping.md)

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

# **propertymappings_provider_saml_used_by_list**
> List[UsedBy] propertymappings_provider_saml_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Provider Property Mapping.

    try:
        api_response = api_instance.propertymappings_provider_saml_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_saml_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_saml_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Provider Property Mapping. | 

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

# **propertymappings_provider_scim_create**
> SCIMMapping propertymappings_provider_scim_create(scim_mapping_request)

SCIMMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.scim_mapping import SCIMMapping
from authentik_client.models.scim_mapping_request import SCIMMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    scim_mapping_request = authentik_client.SCIMMappingRequest() # SCIMMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_scim_create(scim_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_scim_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scim_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scim_mapping_request** | [**SCIMMappingRequest**](SCIMMappingRequest.md)|  | 

### Return type

[**SCIMMapping**](SCIMMapping.md)

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

# **propertymappings_provider_scim_destroy**
> propertymappings_provider_scim_destroy(pm_uuid)

SCIMMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Provider Mapping.

    try:
        api_instance.propertymappings_provider_scim_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scim_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Provider Mapping. | 

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

# **propertymappings_provider_scim_list**
> PaginatedSCIMMappingList propertymappings_provider_scim_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)

SCIMMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_scim_mapping_list import PaginatedSCIMMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    managed = ['managed_example'] # List[str] |  (optional)
    managed__isnull = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_provider_scim_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_provider_scim_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scim_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **managed__isnull** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedSCIMMappingList**](PaginatedSCIMMappingList.md)

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

# **propertymappings_provider_scim_partial_update**
> SCIMMapping propertymappings_provider_scim_partial_update(pm_uuid, patched_scim_mapping_request=patched_scim_mapping_request)

SCIMMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_scim_mapping_request import PatchedSCIMMappingRequest
from authentik_client.models.scim_mapping import SCIMMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Provider Mapping.
    patched_scim_mapping_request = authentik_client.PatchedSCIMMappingRequest() # PatchedSCIMMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_provider_scim_partial_update(pm_uuid, patched_scim_mapping_request=patched_scim_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_scim_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scim_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Provider Mapping. | 
 **patched_scim_mapping_request** | [**PatchedSCIMMappingRequest**](PatchedSCIMMappingRequest.md)|  | [optional] 

### Return type

[**SCIMMapping**](SCIMMapping.md)

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

# **propertymappings_provider_scim_retrieve**
> SCIMMapping propertymappings_provider_scim_retrieve(pm_uuid)

SCIMMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.scim_mapping import SCIMMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Provider Mapping.

    try:
        api_response = api_instance.propertymappings_provider_scim_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_scim_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scim_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Provider Mapping. | 

### Return type

[**SCIMMapping**](SCIMMapping.md)

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

# **propertymappings_provider_scim_update**
> SCIMMapping propertymappings_provider_scim_update(pm_uuid, scim_mapping_request)

SCIMMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.scim_mapping import SCIMMapping
from authentik_client.models.scim_mapping_request import SCIMMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Provider Mapping.
    scim_mapping_request = authentik_client.SCIMMappingRequest() # SCIMMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_scim_update(pm_uuid, scim_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_scim_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scim_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Provider Mapping. | 
 **scim_mapping_request** | [**SCIMMappingRequest**](SCIMMappingRequest.md)|  | 

### Return type

[**SCIMMapping**](SCIMMapping.md)

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

# **propertymappings_provider_scim_used_by_list**
> List[UsedBy] propertymappings_provider_scim_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Provider Mapping.

    try:
        api_response = api_instance.propertymappings_provider_scim_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_scim_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scim_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Provider Mapping. | 

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

# **propertymappings_provider_scope_create**
> ScopeMapping propertymappings_provider_scope_create(scope_mapping_request)

ScopeMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.scope_mapping import ScopeMapping
from authentik_client.models.scope_mapping_request import ScopeMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    scope_mapping_request = authentik_client.ScopeMappingRequest() # ScopeMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_scope_create(scope_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_scope_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scope_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_mapping_request** | [**ScopeMappingRequest**](ScopeMappingRequest.md)|  | 

### Return type

[**ScopeMapping**](ScopeMapping.md)

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

# **propertymappings_provider_scope_destroy**
> propertymappings_provider_scope_destroy(pm_uuid)

ScopeMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Scope Mapping.

    try:
        api_instance.propertymappings_provider_scope_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scope_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Scope Mapping. | 

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

# **propertymappings_provider_scope_list**
> PaginatedScopeMappingList propertymappings_provider_scope_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, scope_name=scope_name, search=search)

ScopeMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_scope_mapping_list import PaginatedScopeMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    managed = ['managed_example'] # List[str] |  (optional)
    managed__isnull = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    scope_name = 'scope_name_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_provider_scope_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, scope_name=scope_name, search=search)
        print("The response of PropertymappingsApi->propertymappings_provider_scope_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scope_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **managed__isnull** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **scope_name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedScopeMappingList**](PaginatedScopeMappingList.md)

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

# **propertymappings_provider_scope_partial_update**
> ScopeMapping propertymappings_provider_scope_partial_update(pm_uuid, patched_scope_mapping_request=patched_scope_mapping_request)

ScopeMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_scope_mapping_request import PatchedScopeMappingRequest
from authentik_client.models.scope_mapping import ScopeMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Scope Mapping.
    patched_scope_mapping_request = authentik_client.PatchedScopeMappingRequest() # PatchedScopeMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_provider_scope_partial_update(pm_uuid, patched_scope_mapping_request=patched_scope_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_scope_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scope_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Scope Mapping. | 
 **patched_scope_mapping_request** | [**PatchedScopeMappingRequest**](PatchedScopeMappingRequest.md)|  | [optional] 

### Return type

[**ScopeMapping**](ScopeMapping.md)

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

# **propertymappings_provider_scope_retrieve**
> ScopeMapping propertymappings_provider_scope_retrieve(pm_uuid)

ScopeMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.scope_mapping import ScopeMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Scope Mapping.

    try:
        api_response = api_instance.propertymappings_provider_scope_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_scope_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scope_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Scope Mapping. | 

### Return type

[**ScopeMapping**](ScopeMapping.md)

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

# **propertymappings_provider_scope_update**
> ScopeMapping propertymappings_provider_scope_update(pm_uuid, scope_mapping_request)

ScopeMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.scope_mapping import ScopeMapping
from authentik_client.models.scope_mapping_request import ScopeMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Scope Mapping.
    scope_mapping_request = authentik_client.ScopeMappingRequest() # ScopeMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_scope_update(pm_uuid, scope_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_scope_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scope_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Scope Mapping. | 
 **scope_mapping_request** | [**ScopeMappingRequest**](ScopeMappingRequest.md)|  | 

### Return type

[**ScopeMapping**](ScopeMapping.md)

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

# **propertymappings_provider_scope_used_by_list**
> List[UsedBy] propertymappings_provider_scope_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Scope Mapping.

    try:
        api_response = api_instance.propertymappings_provider_scope_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_scope_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_scope_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Scope Mapping. | 

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

# **propertymappings_source_kerberos_create**
> KerberosSourcePropertyMapping propertymappings_source_kerberos_create(kerberos_source_property_mapping_request)

KerberosSource PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.kerberos_source_property_mapping import KerberosSourcePropertyMapping
from authentik_client.models.kerberos_source_property_mapping_request import KerberosSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    kerberos_source_property_mapping_request = authentik_client.KerberosSourcePropertyMappingRequest() # KerberosSourcePropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_source_kerberos_create(kerberos_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_kerberos_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_kerberos_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kerberos_source_property_mapping_request** | [**KerberosSourcePropertyMappingRequest**](KerberosSourcePropertyMappingRequest.md)|  | 

### Return type

[**KerberosSourcePropertyMapping**](KerberosSourcePropertyMapping.md)

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

# **propertymappings_source_kerberos_destroy**
> propertymappings_source_kerberos_destroy(pm_uuid)

KerberosSource PropertyMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Kerberos Source Property Mapping.

    try:
        api_instance.propertymappings_source_kerberos_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_kerberos_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Kerberos Source Property Mapping. | 

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

# **propertymappings_source_kerberos_list**
> PaginatedKerberosSourcePropertyMappingList propertymappings_source_kerberos_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)

KerberosSource PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_kerberos_source_property_mapping_list import PaginatedKerberosSourcePropertyMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    managed = ['managed_example'] # List[str] |  (optional)
    managed__isnull = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_source_kerberos_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_source_kerberos_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_kerberos_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **managed__isnull** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedKerberosSourcePropertyMappingList**](PaginatedKerberosSourcePropertyMappingList.md)

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

# **propertymappings_source_kerberos_partial_update**
> KerberosSourcePropertyMapping propertymappings_source_kerberos_partial_update(pm_uuid, patched_kerberos_source_property_mapping_request=patched_kerberos_source_property_mapping_request)

KerberosSource PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.kerberos_source_property_mapping import KerberosSourcePropertyMapping
from authentik_client.models.patched_kerberos_source_property_mapping_request import PatchedKerberosSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Kerberos Source Property Mapping.
    patched_kerberos_source_property_mapping_request = authentik_client.PatchedKerberosSourcePropertyMappingRequest() # PatchedKerberosSourcePropertyMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_source_kerberos_partial_update(pm_uuid, patched_kerberos_source_property_mapping_request=patched_kerberos_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_kerberos_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_kerberos_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Kerberos Source Property Mapping. | 
 **patched_kerberos_source_property_mapping_request** | [**PatchedKerberosSourcePropertyMappingRequest**](PatchedKerberosSourcePropertyMappingRequest.md)|  | [optional] 

### Return type

[**KerberosSourcePropertyMapping**](KerberosSourcePropertyMapping.md)

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

# **propertymappings_source_kerberos_retrieve**
> KerberosSourcePropertyMapping propertymappings_source_kerberos_retrieve(pm_uuid)

KerberosSource PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.kerberos_source_property_mapping import KerberosSourcePropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Kerberos Source Property Mapping.

    try:
        api_response = api_instance.propertymappings_source_kerberos_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_source_kerberos_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_kerberos_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Kerberos Source Property Mapping. | 

### Return type

[**KerberosSourcePropertyMapping**](KerberosSourcePropertyMapping.md)

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

# **propertymappings_source_kerberos_update**
> KerberosSourcePropertyMapping propertymappings_source_kerberos_update(pm_uuid, kerberos_source_property_mapping_request)

KerberosSource PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.kerberos_source_property_mapping import KerberosSourcePropertyMapping
from authentik_client.models.kerberos_source_property_mapping_request import KerberosSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Kerberos Source Property Mapping.
    kerberos_source_property_mapping_request = authentik_client.KerberosSourcePropertyMappingRequest() # KerberosSourcePropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_source_kerberos_update(pm_uuid, kerberos_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_kerberos_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_kerberos_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Kerberos Source Property Mapping. | 
 **kerberos_source_property_mapping_request** | [**KerberosSourcePropertyMappingRequest**](KerberosSourcePropertyMappingRequest.md)|  | 

### Return type

[**KerberosSourcePropertyMapping**](KerberosSourcePropertyMapping.md)

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

# **propertymappings_source_kerberos_used_by_list**
> List[UsedBy] propertymappings_source_kerberos_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Kerberos Source Property Mapping.

    try:
        api_response = api_instance.propertymappings_source_kerberos_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_source_kerberos_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_kerberos_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Kerberos Source Property Mapping. | 

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

# **propertymappings_source_ldap_create**
> LDAPSourcePropertyMapping propertymappings_source_ldap_create(ldap_source_property_mapping_request)

LDAP PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.ldap_source_property_mapping import LDAPSourcePropertyMapping
from authentik_client.models.ldap_source_property_mapping_request import LDAPSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    ldap_source_property_mapping_request = authentik_client.LDAPSourcePropertyMappingRequest() # LDAPSourcePropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_source_ldap_create(ldap_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_ldap_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_ldap_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_source_property_mapping_request** | [**LDAPSourcePropertyMappingRequest**](LDAPSourcePropertyMappingRequest.md)|  | 

### Return type

[**LDAPSourcePropertyMapping**](LDAPSourcePropertyMapping.md)

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

# **propertymappings_source_ldap_destroy**
> propertymappings_source_ldap_destroy(pm_uuid)

LDAP PropertyMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this LDAP Source Property Mapping.

    try:
        api_instance.propertymappings_source_ldap_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_ldap_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this LDAP Source Property Mapping. | 

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

# **propertymappings_source_ldap_list**
> PaginatedLDAPSourcePropertyMappingList propertymappings_source_ldap_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)

LDAP PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_ldap_source_property_mapping_list import PaginatedLDAPSourcePropertyMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    managed = ['managed_example'] # List[str] |  (optional)
    managed__isnull = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_source_ldap_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_source_ldap_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_ldap_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **managed__isnull** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedLDAPSourcePropertyMappingList**](PaginatedLDAPSourcePropertyMappingList.md)

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

# **propertymappings_source_ldap_partial_update**
> LDAPSourcePropertyMapping propertymappings_source_ldap_partial_update(pm_uuid, patched_ldap_source_property_mapping_request=patched_ldap_source_property_mapping_request)

LDAP PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.ldap_source_property_mapping import LDAPSourcePropertyMapping
from authentik_client.models.patched_ldap_source_property_mapping_request import PatchedLDAPSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this LDAP Source Property Mapping.
    patched_ldap_source_property_mapping_request = authentik_client.PatchedLDAPSourcePropertyMappingRequest() # PatchedLDAPSourcePropertyMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_source_ldap_partial_update(pm_uuid, patched_ldap_source_property_mapping_request=patched_ldap_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_ldap_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_ldap_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this LDAP Source Property Mapping. | 
 **patched_ldap_source_property_mapping_request** | [**PatchedLDAPSourcePropertyMappingRequest**](PatchedLDAPSourcePropertyMappingRequest.md)|  | [optional] 

### Return type

[**LDAPSourcePropertyMapping**](LDAPSourcePropertyMapping.md)

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

# **propertymappings_source_ldap_retrieve**
> LDAPSourcePropertyMapping propertymappings_source_ldap_retrieve(pm_uuid)

LDAP PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.ldap_source_property_mapping import LDAPSourcePropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this LDAP Source Property Mapping.

    try:
        api_response = api_instance.propertymappings_source_ldap_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_source_ldap_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_ldap_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this LDAP Source Property Mapping. | 

### Return type

[**LDAPSourcePropertyMapping**](LDAPSourcePropertyMapping.md)

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

# **propertymappings_source_ldap_update**
> LDAPSourcePropertyMapping propertymappings_source_ldap_update(pm_uuid, ldap_source_property_mapping_request)

LDAP PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.ldap_source_property_mapping import LDAPSourcePropertyMapping
from authentik_client.models.ldap_source_property_mapping_request import LDAPSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this LDAP Source Property Mapping.
    ldap_source_property_mapping_request = authentik_client.LDAPSourcePropertyMappingRequest() # LDAPSourcePropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_source_ldap_update(pm_uuid, ldap_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_ldap_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_ldap_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this LDAP Source Property Mapping. | 
 **ldap_source_property_mapping_request** | [**LDAPSourcePropertyMappingRequest**](LDAPSourcePropertyMappingRequest.md)|  | 

### Return type

[**LDAPSourcePropertyMapping**](LDAPSourcePropertyMapping.md)

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

# **propertymappings_source_ldap_used_by_list**
> List[UsedBy] propertymappings_source_ldap_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this LDAP Source Property Mapping.

    try:
        api_response = api_instance.propertymappings_source_ldap_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_source_ldap_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_ldap_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this LDAP Source Property Mapping. | 

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

# **propertymappings_source_oauth_create**
> OAuthSourcePropertyMapping propertymappings_source_oauth_create(o_auth_source_property_mapping_request)

OAuthSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.o_auth_source_property_mapping import OAuthSourcePropertyMapping
from authentik_client.models.o_auth_source_property_mapping_request import OAuthSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    o_auth_source_property_mapping_request = authentik_client.OAuthSourcePropertyMappingRequest() # OAuthSourcePropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_source_oauth_create(o_auth_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_oauth_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_oauth_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_source_property_mapping_request** | [**OAuthSourcePropertyMappingRequest**](OAuthSourcePropertyMappingRequest.md)|  | 

### Return type

[**OAuthSourcePropertyMapping**](OAuthSourcePropertyMapping.md)

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

# **propertymappings_source_oauth_destroy**
> propertymappings_source_oauth_destroy(pm_uuid)

OAuthSourcePropertyMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this OAuth Source Property Mapping.

    try:
        api_instance.propertymappings_source_oauth_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_oauth_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this OAuth Source Property Mapping. | 

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

# **propertymappings_source_oauth_list**
> PaginatedOAuthSourcePropertyMappingList propertymappings_source_oauth_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)

OAuthSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_o_auth_source_property_mapping_list import PaginatedOAuthSourcePropertyMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    managed = ['managed_example'] # List[str] |  (optional)
    managed__isnull = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_source_oauth_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_source_oauth_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_oauth_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **managed__isnull** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedOAuthSourcePropertyMappingList**](PaginatedOAuthSourcePropertyMappingList.md)

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

# **propertymappings_source_oauth_partial_update**
> OAuthSourcePropertyMapping propertymappings_source_oauth_partial_update(pm_uuid, patched_o_auth_source_property_mapping_request=patched_o_auth_source_property_mapping_request)

OAuthSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.o_auth_source_property_mapping import OAuthSourcePropertyMapping
from authentik_client.models.patched_o_auth_source_property_mapping_request import PatchedOAuthSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this OAuth Source Property Mapping.
    patched_o_auth_source_property_mapping_request = authentik_client.PatchedOAuthSourcePropertyMappingRequest() # PatchedOAuthSourcePropertyMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_source_oauth_partial_update(pm_uuid, patched_o_auth_source_property_mapping_request=patched_o_auth_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_oauth_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_oauth_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this OAuth Source Property Mapping. | 
 **patched_o_auth_source_property_mapping_request** | [**PatchedOAuthSourcePropertyMappingRequest**](PatchedOAuthSourcePropertyMappingRequest.md)|  | [optional] 

### Return type

[**OAuthSourcePropertyMapping**](OAuthSourcePropertyMapping.md)

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

# **propertymappings_source_oauth_retrieve**
> OAuthSourcePropertyMapping propertymappings_source_oauth_retrieve(pm_uuid)

OAuthSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.o_auth_source_property_mapping import OAuthSourcePropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this OAuth Source Property Mapping.

    try:
        api_response = api_instance.propertymappings_source_oauth_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_source_oauth_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_oauth_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this OAuth Source Property Mapping. | 

### Return type

[**OAuthSourcePropertyMapping**](OAuthSourcePropertyMapping.md)

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

# **propertymappings_source_oauth_update**
> OAuthSourcePropertyMapping propertymappings_source_oauth_update(pm_uuid, o_auth_source_property_mapping_request)

OAuthSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.o_auth_source_property_mapping import OAuthSourcePropertyMapping
from authentik_client.models.o_auth_source_property_mapping_request import OAuthSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this OAuth Source Property Mapping.
    o_auth_source_property_mapping_request = authentik_client.OAuthSourcePropertyMappingRequest() # OAuthSourcePropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_source_oauth_update(pm_uuid, o_auth_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_oauth_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_oauth_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this OAuth Source Property Mapping. | 
 **o_auth_source_property_mapping_request** | [**OAuthSourcePropertyMappingRequest**](OAuthSourcePropertyMappingRequest.md)|  | 

### Return type

[**OAuthSourcePropertyMapping**](OAuthSourcePropertyMapping.md)

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

# **propertymappings_source_oauth_used_by_list**
> List[UsedBy] propertymappings_source_oauth_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this OAuth Source Property Mapping.

    try:
        api_response = api_instance.propertymappings_source_oauth_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_source_oauth_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_oauth_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this OAuth Source Property Mapping. | 

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

# **propertymappings_source_plex_create**
> PlexSourcePropertyMapping propertymappings_source_plex_create(plex_source_property_mapping_request)

PlexSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.plex_source_property_mapping import PlexSourcePropertyMapping
from authentik_client.models.plex_source_property_mapping_request import PlexSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    plex_source_property_mapping_request = authentik_client.PlexSourcePropertyMappingRequest() # PlexSourcePropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_source_plex_create(plex_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_plex_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_plex_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plex_source_property_mapping_request** | [**PlexSourcePropertyMappingRequest**](PlexSourcePropertyMappingRequest.md)|  | 

### Return type

[**PlexSourcePropertyMapping**](PlexSourcePropertyMapping.md)

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

# **propertymappings_source_plex_destroy**
> propertymappings_source_plex_destroy(pm_uuid)

PlexSourcePropertyMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Plex Source Property Mapping.

    try:
        api_instance.propertymappings_source_plex_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_plex_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Plex Source Property Mapping. | 

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

# **propertymappings_source_plex_list**
> PaginatedPlexSourcePropertyMappingList propertymappings_source_plex_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)

PlexSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_plex_source_property_mapping_list import PaginatedPlexSourcePropertyMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    managed = ['managed_example'] # List[str] |  (optional)
    managed__isnull = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_source_plex_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_source_plex_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_plex_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **managed__isnull** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedPlexSourcePropertyMappingList**](PaginatedPlexSourcePropertyMappingList.md)

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

# **propertymappings_source_plex_partial_update**
> PlexSourcePropertyMapping propertymappings_source_plex_partial_update(pm_uuid, patched_plex_source_property_mapping_request=patched_plex_source_property_mapping_request)

PlexSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_plex_source_property_mapping_request import PatchedPlexSourcePropertyMappingRequest
from authentik_client.models.plex_source_property_mapping import PlexSourcePropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Plex Source Property Mapping.
    patched_plex_source_property_mapping_request = authentik_client.PatchedPlexSourcePropertyMappingRequest() # PatchedPlexSourcePropertyMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_source_plex_partial_update(pm_uuid, patched_plex_source_property_mapping_request=patched_plex_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_plex_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_plex_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Plex Source Property Mapping. | 
 **patched_plex_source_property_mapping_request** | [**PatchedPlexSourcePropertyMappingRequest**](PatchedPlexSourcePropertyMappingRequest.md)|  | [optional] 

### Return type

[**PlexSourcePropertyMapping**](PlexSourcePropertyMapping.md)

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

# **propertymappings_source_plex_retrieve**
> PlexSourcePropertyMapping propertymappings_source_plex_retrieve(pm_uuid)

PlexSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.plex_source_property_mapping import PlexSourcePropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Plex Source Property Mapping.

    try:
        api_response = api_instance.propertymappings_source_plex_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_source_plex_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_plex_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Plex Source Property Mapping. | 

### Return type

[**PlexSourcePropertyMapping**](PlexSourcePropertyMapping.md)

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

# **propertymappings_source_plex_update**
> PlexSourcePropertyMapping propertymappings_source_plex_update(pm_uuid, plex_source_property_mapping_request)

PlexSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.plex_source_property_mapping import PlexSourcePropertyMapping
from authentik_client.models.plex_source_property_mapping_request import PlexSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Plex Source Property Mapping.
    plex_source_property_mapping_request = authentik_client.PlexSourcePropertyMappingRequest() # PlexSourcePropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_source_plex_update(pm_uuid, plex_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_plex_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_plex_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Plex Source Property Mapping. | 
 **plex_source_property_mapping_request** | [**PlexSourcePropertyMappingRequest**](PlexSourcePropertyMappingRequest.md)|  | 

### Return type

[**PlexSourcePropertyMapping**](PlexSourcePropertyMapping.md)

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

# **propertymappings_source_plex_used_by_list**
> List[UsedBy] propertymappings_source_plex_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Plex Source Property Mapping.

    try:
        api_response = api_instance.propertymappings_source_plex_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_source_plex_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_plex_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Plex Source Property Mapping. | 

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

# **propertymappings_source_saml_create**
> SAMLSourcePropertyMapping propertymappings_source_saml_create(saml_source_property_mapping_request)

SAMLSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.saml_source_property_mapping import SAMLSourcePropertyMapping
from authentik_client.models.saml_source_property_mapping_request import SAMLSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    saml_source_property_mapping_request = authentik_client.SAMLSourcePropertyMappingRequest() # SAMLSourcePropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_source_saml_create(saml_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_saml_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_saml_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_source_property_mapping_request** | [**SAMLSourcePropertyMappingRequest**](SAMLSourcePropertyMappingRequest.md)|  | 

### Return type

[**SAMLSourcePropertyMapping**](SAMLSourcePropertyMapping.md)

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

# **propertymappings_source_saml_destroy**
> propertymappings_source_saml_destroy(pm_uuid)

SAMLSourcePropertyMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Source Property Mapping.

    try:
        api_instance.propertymappings_source_saml_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_saml_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Source Property Mapping. | 

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

# **propertymappings_source_saml_list**
> PaginatedSAMLSourcePropertyMappingList propertymappings_source_saml_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)

SAMLSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_saml_source_property_mapping_list import PaginatedSAMLSourcePropertyMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    managed = ['managed_example'] # List[str] |  (optional)
    managed__isnull = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_source_saml_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_source_saml_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_saml_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **managed__isnull** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedSAMLSourcePropertyMappingList**](PaginatedSAMLSourcePropertyMappingList.md)

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

# **propertymappings_source_saml_partial_update**
> SAMLSourcePropertyMapping propertymappings_source_saml_partial_update(pm_uuid, patched_saml_source_property_mapping_request=patched_saml_source_property_mapping_request)

SAMLSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_saml_source_property_mapping_request import PatchedSAMLSourcePropertyMappingRequest
from authentik_client.models.saml_source_property_mapping import SAMLSourcePropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Source Property Mapping.
    patched_saml_source_property_mapping_request = authentik_client.PatchedSAMLSourcePropertyMappingRequest() # PatchedSAMLSourcePropertyMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_source_saml_partial_update(pm_uuid, patched_saml_source_property_mapping_request=patched_saml_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_saml_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_saml_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Source Property Mapping. | 
 **patched_saml_source_property_mapping_request** | [**PatchedSAMLSourcePropertyMappingRequest**](PatchedSAMLSourcePropertyMappingRequest.md)|  | [optional] 

### Return type

[**SAMLSourcePropertyMapping**](SAMLSourcePropertyMapping.md)

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

# **propertymappings_source_saml_retrieve**
> SAMLSourcePropertyMapping propertymappings_source_saml_retrieve(pm_uuid)

SAMLSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.saml_source_property_mapping import SAMLSourcePropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Source Property Mapping.

    try:
        api_response = api_instance.propertymappings_source_saml_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_source_saml_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_saml_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Source Property Mapping. | 

### Return type

[**SAMLSourcePropertyMapping**](SAMLSourcePropertyMapping.md)

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

# **propertymappings_source_saml_update**
> SAMLSourcePropertyMapping propertymappings_source_saml_update(pm_uuid, saml_source_property_mapping_request)

SAMLSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.saml_source_property_mapping import SAMLSourcePropertyMapping
from authentik_client.models.saml_source_property_mapping_request import SAMLSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Source Property Mapping.
    saml_source_property_mapping_request = authentik_client.SAMLSourcePropertyMappingRequest() # SAMLSourcePropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_source_saml_update(pm_uuid, saml_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_saml_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_saml_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Source Property Mapping. | 
 **saml_source_property_mapping_request** | [**SAMLSourcePropertyMappingRequest**](SAMLSourcePropertyMappingRequest.md)|  | 

### Return type

[**SAMLSourcePropertyMapping**](SAMLSourcePropertyMapping.md)

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

# **propertymappings_source_saml_used_by_list**
> List[UsedBy] propertymappings_source_saml_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Source Property Mapping.

    try:
        api_response = api_instance.propertymappings_source_saml_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_source_saml_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_saml_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Source Property Mapping. | 

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

# **propertymappings_source_scim_create**
> SCIMSourcePropertyMapping propertymappings_source_scim_create(scim_source_property_mapping_request)

SCIMSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.scim_source_property_mapping import SCIMSourcePropertyMapping
from authentik_client.models.scim_source_property_mapping_request import SCIMSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    scim_source_property_mapping_request = authentik_client.SCIMSourcePropertyMappingRequest() # SCIMSourcePropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_source_scim_create(scim_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_scim_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_scim_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scim_source_property_mapping_request** | [**SCIMSourcePropertyMappingRequest**](SCIMSourcePropertyMappingRequest.md)|  | 

### Return type

[**SCIMSourcePropertyMapping**](SCIMSourcePropertyMapping.md)

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

# **propertymappings_source_scim_destroy**
> propertymappings_source_scim_destroy(pm_uuid)

SCIMSourcePropertyMapping Viewset

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Source Property Mapping.

    try:
        api_instance.propertymappings_source_scim_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_scim_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Source Property Mapping. | 

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

# **propertymappings_source_scim_list**
> PaginatedSCIMSourcePropertyMappingList propertymappings_source_scim_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)

SCIMSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_scim_source_property_mapping_list import PaginatedSCIMSourcePropertyMappingList
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    managed = ['managed_example'] # List[str] |  (optional)
    managed__isnull = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_source_scim_list(managed=managed, managed__isnull=managed__isnull, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_source_scim_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_scim_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **managed__isnull** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedSCIMSourcePropertyMappingList**](PaginatedSCIMSourcePropertyMappingList.md)

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

# **propertymappings_source_scim_partial_update**
> SCIMSourcePropertyMapping propertymappings_source_scim_partial_update(pm_uuid, patched_scim_source_property_mapping_request=patched_scim_source_property_mapping_request)

SCIMSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_scim_source_property_mapping_request import PatchedSCIMSourcePropertyMappingRequest
from authentik_client.models.scim_source_property_mapping import SCIMSourcePropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Source Property Mapping.
    patched_scim_source_property_mapping_request = authentik_client.PatchedSCIMSourcePropertyMappingRequest() # PatchedSCIMSourcePropertyMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_source_scim_partial_update(pm_uuid, patched_scim_source_property_mapping_request=patched_scim_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_scim_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_scim_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Source Property Mapping. | 
 **patched_scim_source_property_mapping_request** | [**PatchedSCIMSourcePropertyMappingRequest**](PatchedSCIMSourcePropertyMappingRequest.md)|  | [optional] 

### Return type

[**SCIMSourcePropertyMapping**](SCIMSourcePropertyMapping.md)

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

# **propertymappings_source_scim_retrieve**
> SCIMSourcePropertyMapping propertymappings_source_scim_retrieve(pm_uuid)

SCIMSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.scim_source_property_mapping import SCIMSourcePropertyMapping
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Source Property Mapping.

    try:
        api_response = api_instance.propertymappings_source_scim_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_source_scim_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_scim_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Source Property Mapping. | 

### Return type

[**SCIMSourcePropertyMapping**](SCIMSourcePropertyMapping.md)

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

# **propertymappings_source_scim_update**
> SCIMSourcePropertyMapping propertymappings_source_scim_update(pm_uuid, scim_source_property_mapping_request)

SCIMSourcePropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.scim_source_property_mapping import SCIMSourcePropertyMapping
from authentik_client.models.scim_source_property_mapping_request import SCIMSourcePropertyMappingRequest
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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Source Property Mapping.
    scim_source_property_mapping_request = authentik_client.SCIMSourcePropertyMappingRequest() # SCIMSourcePropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_source_scim_update(pm_uuid, scim_source_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_source_scim_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_scim_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Source Property Mapping. | 
 **scim_source_property_mapping_request** | [**SCIMSourcePropertyMappingRequest**](SCIMSourcePropertyMappingRequest.md)|  | 

### Return type

[**SCIMSourcePropertyMapping**](SCIMSourcePropertyMapping.md)

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

# **propertymappings_source_scim_used_by_list**
> List[UsedBy] propertymappings_source_scim_used_by_list(pm_uuid)

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
    api_instance = authentik_client.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Source Property Mapping.

    try:
        api_response = api_instance.propertymappings_source_scim_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_source_scim_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_source_scim_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Source Property Mapping. | 

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

