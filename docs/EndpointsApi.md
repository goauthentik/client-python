# authentik_client.EndpointsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoints_agents_connectors_agent_config_retrieve**](EndpointsApi.md#endpoints_agents_connectors_agent_config_retrieve) | **GET** /endpoints/agents/connectors/agent_config/ | 
[**endpoints_agents_connectors_auth_fed_create**](EndpointsApi.md#endpoints_agents_connectors_auth_fed_create) | **POST** /endpoints/agents/connectors/auth_fed/ | 
[**endpoints_agents_connectors_auth_ia_create**](EndpointsApi.md#endpoints_agents_connectors_auth_ia_create) | **POST** /endpoints/agents/connectors/auth_ia/ | 
[**endpoints_agents_connectors_check_in_create**](EndpointsApi.md#endpoints_agents_connectors_check_in_create) | **POST** /endpoints/agents/connectors/check_in/ | 
[**endpoints_agents_connectors_create**](EndpointsApi.md#endpoints_agents_connectors_create) | **POST** /endpoints/agents/connectors/ | 
[**endpoints_agents_connectors_destroy**](EndpointsApi.md#endpoints_agents_connectors_destroy) | **DELETE** /endpoints/agents/connectors/{connector_uuid}/ | 
[**endpoints_agents_connectors_enroll_create**](EndpointsApi.md#endpoints_agents_connectors_enroll_create) | **POST** /endpoints/agents/connectors/enroll/ | 
[**endpoints_agents_connectors_list**](EndpointsApi.md#endpoints_agents_connectors_list) | **GET** /endpoints/agents/connectors/ | 
[**endpoints_agents_connectors_mdm_config_create**](EndpointsApi.md#endpoints_agents_connectors_mdm_config_create) | **POST** /endpoints/agents/connectors/{connector_uuid}/mdm_config/ | 
[**endpoints_agents_connectors_partial_update**](EndpointsApi.md#endpoints_agents_connectors_partial_update) | **PATCH** /endpoints/agents/connectors/{connector_uuid}/ | 
[**endpoints_agents_connectors_retrieve**](EndpointsApi.md#endpoints_agents_connectors_retrieve) | **GET** /endpoints/agents/connectors/{connector_uuid}/ | 
[**endpoints_agents_connectors_update**](EndpointsApi.md#endpoints_agents_connectors_update) | **PUT** /endpoints/agents/connectors/{connector_uuid}/ | 
[**endpoints_agents_connectors_used_by_list**](EndpointsApi.md#endpoints_agents_connectors_used_by_list) | **GET** /endpoints/agents/connectors/{connector_uuid}/used_by/ | 
[**endpoints_agents_enrollment_tokens_create**](EndpointsApi.md#endpoints_agents_enrollment_tokens_create) | **POST** /endpoints/agents/enrollment_tokens/ | 
[**endpoints_agents_enrollment_tokens_destroy**](EndpointsApi.md#endpoints_agents_enrollment_tokens_destroy) | **DELETE** /endpoints/agents/enrollment_tokens/{token_uuid}/ | 
[**endpoints_agents_enrollment_tokens_list**](EndpointsApi.md#endpoints_agents_enrollment_tokens_list) | **GET** /endpoints/agents/enrollment_tokens/ | 
[**endpoints_agents_enrollment_tokens_partial_update**](EndpointsApi.md#endpoints_agents_enrollment_tokens_partial_update) | **PATCH** /endpoints/agents/enrollment_tokens/{token_uuid}/ | 
[**endpoints_agents_enrollment_tokens_retrieve**](EndpointsApi.md#endpoints_agents_enrollment_tokens_retrieve) | **GET** /endpoints/agents/enrollment_tokens/{token_uuid}/ | 
[**endpoints_agents_enrollment_tokens_update**](EndpointsApi.md#endpoints_agents_enrollment_tokens_update) | **PUT** /endpoints/agents/enrollment_tokens/{token_uuid}/ | 
[**endpoints_agents_enrollment_tokens_used_by_list**](EndpointsApi.md#endpoints_agents_enrollment_tokens_used_by_list) | **GET** /endpoints/agents/enrollment_tokens/{token_uuid}/used_by/ | 
[**endpoints_agents_enrollment_tokens_view_key_retrieve**](EndpointsApi.md#endpoints_agents_enrollment_tokens_view_key_retrieve) | **GET** /endpoints/agents/enrollment_tokens/{token_uuid}/view_key/ | 
[**endpoints_agents_psso_register_device_create**](EndpointsApi.md#endpoints_agents_psso_register_device_create) | **POST** /endpoints/agents/psso/register/device/ | 
[**endpoints_agents_psso_register_user_create**](EndpointsApi.md#endpoints_agents_psso_register_user_create) | **POST** /endpoints/agents/psso/register/user/ | 
[**endpoints_connectors_destroy**](EndpointsApi.md#endpoints_connectors_destroy) | **DELETE** /endpoints/connectors/{connector_uuid}/ | 
[**endpoints_connectors_list**](EndpointsApi.md#endpoints_connectors_list) | **GET** /endpoints/connectors/ | 
[**endpoints_connectors_retrieve**](EndpointsApi.md#endpoints_connectors_retrieve) | **GET** /endpoints/connectors/{connector_uuid}/ | 
[**endpoints_connectors_types_list**](EndpointsApi.md#endpoints_connectors_types_list) | **GET** /endpoints/connectors/types/ | 
[**endpoints_connectors_used_by_list**](EndpointsApi.md#endpoints_connectors_used_by_list) | **GET** /endpoints/connectors/{connector_uuid}/used_by/ | 
[**endpoints_device_access_groups_create**](EndpointsApi.md#endpoints_device_access_groups_create) | **POST** /endpoints/device_access_groups/ | 
[**endpoints_device_access_groups_destroy**](EndpointsApi.md#endpoints_device_access_groups_destroy) | **DELETE** /endpoints/device_access_groups/{pbm_uuid}/ | 
[**endpoints_device_access_groups_list**](EndpointsApi.md#endpoints_device_access_groups_list) | **GET** /endpoints/device_access_groups/ | 
[**endpoints_device_access_groups_partial_update**](EndpointsApi.md#endpoints_device_access_groups_partial_update) | **PATCH** /endpoints/device_access_groups/{pbm_uuid}/ | 
[**endpoints_device_access_groups_retrieve**](EndpointsApi.md#endpoints_device_access_groups_retrieve) | **GET** /endpoints/device_access_groups/{pbm_uuid}/ | 
[**endpoints_device_access_groups_update**](EndpointsApi.md#endpoints_device_access_groups_update) | **PUT** /endpoints/device_access_groups/{pbm_uuid}/ | 
[**endpoints_device_access_groups_used_by_list**](EndpointsApi.md#endpoints_device_access_groups_used_by_list) | **GET** /endpoints/device_access_groups/{pbm_uuid}/used_by/ | 
[**endpoints_device_bindings_create**](EndpointsApi.md#endpoints_device_bindings_create) | **POST** /endpoints/device_bindings/ | 
[**endpoints_device_bindings_destroy**](EndpointsApi.md#endpoints_device_bindings_destroy) | **DELETE** /endpoints/device_bindings/{policy_binding_uuid}/ | 
[**endpoints_device_bindings_list**](EndpointsApi.md#endpoints_device_bindings_list) | **GET** /endpoints/device_bindings/ | 
[**endpoints_device_bindings_partial_update**](EndpointsApi.md#endpoints_device_bindings_partial_update) | **PATCH** /endpoints/device_bindings/{policy_binding_uuid}/ | 
[**endpoints_device_bindings_retrieve**](EndpointsApi.md#endpoints_device_bindings_retrieve) | **GET** /endpoints/device_bindings/{policy_binding_uuid}/ | 
[**endpoints_device_bindings_update**](EndpointsApi.md#endpoints_device_bindings_update) | **PUT** /endpoints/device_bindings/{policy_binding_uuid}/ | 
[**endpoints_device_bindings_used_by_list**](EndpointsApi.md#endpoints_device_bindings_used_by_list) | **GET** /endpoints/device_bindings/{policy_binding_uuid}/used_by/ | 
[**endpoints_devices_destroy**](EndpointsApi.md#endpoints_devices_destroy) | **DELETE** /endpoints/devices/{device_uuid}/ | 
[**endpoints_devices_list**](EndpointsApi.md#endpoints_devices_list) | **GET** /endpoints/devices/ | 
[**endpoints_devices_partial_update**](EndpointsApi.md#endpoints_devices_partial_update) | **PATCH** /endpoints/devices/{device_uuid}/ | 
[**endpoints_devices_retrieve**](EndpointsApi.md#endpoints_devices_retrieve) | **GET** /endpoints/devices/{device_uuid}/ | 
[**endpoints_devices_summary_retrieve**](EndpointsApi.md#endpoints_devices_summary_retrieve) | **GET** /endpoints/devices/summary/ | 
[**endpoints_devices_update**](EndpointsApi.md#endpoints_devices_update) | **PUT** /endpoints/devices/{device_uuid}/ | 
[**endpoints_devices_used_by_list**](EndpointsApi.md#endpoints_devices_used_by_list) | **GET** /endpoints/devices/{device_uuid}/used_by/ | 
[**endpoints_fleet_connectors_create**](EndpointsApi.md#endpoints_fleet_connectors_create) | **POST** /endpoints/fleet/connectors/ | 
[**endpoints_fleet_connectors_destroy**](EndpointsApi.md#endpoints_fleet_connectors_destroy) | **DELETE** /endpoints/fleet/connectors/{connector_uuid}/ | 
[**endpoints_fleet_connectors_list**](EndpointsApi.md#endpoints_fleet_connectors_list) | **GET** /endpoints/fleet/connectors/ | 
[**endpoints_fleet_connectors_partial_update**](EndpointsApi.md#endpoints_fleet_connectors_partial_update) | **PATCH** /endpoints/fleet/connectors/{connector_uuid}/ | 
[**endpoints_fleet_connectors_retrieve**](EndpointsApi.md#endpoints_fleet_connectors_retrieve) | **GET** /endpoints/fleet/connectors/{connector_uuid}/ | 
[**endpoints_fleet_connectors_update**](EndpointsApi.md#endpoints_fleet_connectors_update) | **PUT** /endpoints/fleet/connectors/{connector_uuid}/ | 
[**endpoints_fleet_connectors_used_by_list**](EndpointsApi.md#endpoints_fleet_connectors_used_by_list) | **GET** /endpoints/fleet/connectors/{connector_uuid}/used_by/ | 


# **endpoints_agents_connectors_agent_config_retrieve**
> AgentConfig endpoints_agents_connectors_agent_config_retrieve()

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example


```python
import authentik_client
from authentik_client.models.agent_config import AgentConfig
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
    api_instance = authentik_client.EndpointsApi(api_client)

    try:
        api_response = api_instance.endpoints_agents_connectors_agent_config_retrieve()
        print("The response of EndpointsApi->endpoints_agents_connectors_agent_config_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_connectors_agent_config_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AgentConfig**](AgentConfig.md)

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

# **endpoints_agents_connectors_auth_fed_create**
> AgentTokenResponse endpoints_agents_connectors_auth_fed_create(device)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example


```python
import authentik_client
from authentik_client.models.agent_token_response import AgentTokenResponse
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
    api_instance = authentik_client.EndpointsApi(api_client)
    device = 'device_example' # str | 

    try:
        api_response = api_instance.endpoints_agents_connectors_auth_fed_create(device)
        print("The response of EndpointsApi->endpoints_agents_connectors_auth_fed_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_connectors_auth_fed_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**|  | 

### Return type

[**AgentTokenResponse**](AgentTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Device not found |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_agents_connectors_auth_ia_create**
> AgentAuthenticationResponse endpoints_agents_connectors_auth_ia_create()

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example


```python
import authentik_client
from authentik_client.models.agent_authentication_response import AgentAuthenticationResponse
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
    api_instance = authentik_client.EndpointsApi(api_client)

    try:
        api_response = api_instance.endpoints_agents_connectors_auth_ia_create()
        print("The response of EndpointsApi->endpoints_agents_connectors_auth_ia_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_connectors_auth_ia_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AgentAuthenticationResponse**](AgentAuthenticationResponse.md)

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

# **endpoints_agents_connectors_check_in_create**
> endpoints_agents_connectors_check_in_create(device_facts_request=device_facts_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example


```python
import authentik_client
from authentik_client.models.device_facts_request import DeviceFactsRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    device_facts_request = authentik_client.DeviceFactsRequest() # DeviceFactsRequest |  (optional)

    try:
        api_instance.endpoints_agents_connectors_check_in_create(device_facts_request=device_facts_request)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_connectors_check_in_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_facts_request** | [**DeviceFactsRequest**](DeviceFactsRequest.md)|  | [optional] 

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
**204** | Successfully checked in |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_agents_connectors_create**
> AgentConnector endpoints_agents_connectors_create(agent_connector_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.agent_connector import AgentConnector
from authentik_client.models.agent_connector_request import AgentConnectorRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    agent_connector_request = authentik_client.AgentConnectorRequest() # AgentConnectorRequest | 

    try:
        api_response = api_instance.endpoints_agents_connectors_create(agent_connector_request)
        print("The response of EndpointsApi->endpoints_agents_connectors_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_connectors_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_connector_request** | [**AgentConnectorRequest**](AgentConnectorRequest.md)|  | 

### Return type

[**AgentConnector**](AgentConnector.md)

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

# **endpoints_agents_connectors_destroy**
> endpoints_agents_connectors_destroy(connector_uuid)

Mixin to add a used_by endpoint to return a list of all objects using this object

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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Agent Connector.

    try:
        api_instance.endpoints_agents_connectors_destroy(connector_uuid)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_connectors_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this Agent Connector. | 

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

# **endpoints_agents_connectors_enroll_create**
> AgentTokenResponse endpoints_agents_connectors_enroll_create(enroll_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example


```python
import authentik_client
from authentik_client.models.agent_token_response import AgentTokenResponse
from authentik_client.models.enroll_request import EnrollRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    enroll_request = authentik_client.EnrollRequest() # EnrollRequest | 

    try:
        api_response = api_instance.endpoints_agents_connectors_enroll_create(enroll_request)
        print("The response of EndpointsApi->endpoints_agents_connectors_enroll_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_connectors_enroll_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enroll_request** | [**EnrollRequest**](EnrollRequest.md)|  | 

### Return type

[**AgentTokenResponse**](AgentTokenResponse.md)

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

# **endpoints_agents_connectors_list**
> PaginatedAgentConnectorList endpoints_agents_connectors_list(enabled=enabled, name=name, ordering=ordering, page=page, page_size=page_size, search=search)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_agent_connector_list import PaginatedAgentConnectorList
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
    api_instance = authentik_client.EndpointsApi(api_client)
    enabled = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.endpoints_agents_connectors_list(enabled=enabled, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of EndpointsApi->endpoints_agents_connectors_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_connectors_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedAgentConnectorList**](PaginatedAgentConnectorList.md)

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

# **endpoints_agents_connectors_mdm_config_create**
> MDMConfigResponse endpoints_agents_connectors_mdm_config_create(connector_uuid, mdm_config_request)

Generate configuration for MDM systems to deploy authentik Agent

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.mdm_config_request import MDMConfigRequest
from authentik_client.models.mdm_config_response import MDMConfigResponse
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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Agent Connector.
    mdm_config_request = authentik_client.MDMConfigRequest() # MDMConfigRequest | 

    try:
        api_response = api_instance.endpoints_agents_connectors_mdm_config_create(connector_uuid, mdm_config_request)
        print("The response of EndpointsApi->endpoints_agents_connectors_mdm_config_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_connectors_mdm_config_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this Agent Connector. | 
 **mdm_config_request** | [**MDMConfigRequest**](MDMConfigRequest.md)|  | 

### Return type

[**MDMConfigResponse**](MDMConfigResponse.md)

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

# **endpoints_agents_connectors_partial_update**
> AgentConnector endpoints_agents_connectors_partial_update(connector_uuid, patched_agent_connector_request=patched_agent_connector_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.agent_connector import AgentConnector
from authentik_client.models.patched_agent_connector_request import PatchedAgentConnectorRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Agent Connector.
    patched_agent_connector_request = authentik_client.PatchedAgentConnectorRequest() # PatchedAgentConnectorRequest |  (optional)

    try:
        api_response = api_instance.endpoints_agents_connectors_partial_update(connector_uuid, patched_agent_connector_request=patched_agent_connector_request)
        print("The response of EndpointsApi->endpoints_agents_connectors_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_connectors_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this Agent Connector. | 
 **patched_agent_connector_request** | [**PatchedAgentConnectorRequest**](PatchedAgentConnectorRequest.md)|  | [optional] 

### Return type

[**AgentConnector**](AgentConnector.md)

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

# **endpoints_agents_connectors_retrieve**
> AgentConnector endpoints_agents_connectors_retrieve(connector_uuid)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.agent_connector import AgentConnector
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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Agent Connector.

    try:
        api_response = api_instance.endpoints_agents_connectors_retrieve(connector_uuid)
        print("The response of EndpointsApi->endpoints_agents_connectors_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_connectors_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this Agent Connector. | 

### Return type

[**AgentConnector**](AgentConnector.md)

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

# **endpoints_agents_connectors_update**
> AgentConnector endpoints_agents_connectors_update(connector_uuid, agent_connector_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.agent_connector import AgentConnector
from authentik_client.models.agent_connector_request import AgentConnectorRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Agent Connector.
    agent_connector_request = authentik_client.AgentConnectorRequest() # AgentConnectorRequest | 

    try:
        api_response = api_instance.endpoints_agents_connectors_update(connector_uuid, agent_connector_request)
        print("The response of EndpointsApi->endpoints_agents_connectors_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_connectors_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this Agent Connector. | 
 **agent_connector_request** | [**AgentConnectorRequest**](AgentConnectorRequest.md)|  | 

### Return type

[**AgentConnector**](AgentConnector.md)

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

# **endpoints_agents_connectors_used_by_list**
> List[UsedBy] endpoints_agents_connectors_used_by_list(connector_uuid)

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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Agent Connector.

    try:
        api_response = api_instance.endpoints_agents_connectors_used_by_list(connector_uuid)
        print("The response of EndpointsApi->endpoints_agents_connectors_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_connectors_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this Agent Connector. | 

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

# **endpoints_agents_enrollment_tokens_create**
> EnrollmentToken endpoints_agents_enrollment_tokens_create(enrollment_token_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.enrollment_token import EnrollmentToken
from authentik_client.models.enrollment_token_request import EnrollmentTokenRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    enrollment_token_request = authentik_client.EnrollmentTokenRequest() # EnrollmentTokenRequest | 

    try:
        api_response = api_instance.endpoints_agents_enrollment_tokens_create(enrollment_token_request)
        print("The response of EndpointsApi->endpoints_agents_enrollment_tokens_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_enrollment_tokens_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_token_request** | [**EnrollmentTokenRequest**](EnrollmentTokenRequest.md)|  | 

### Return type

[**EnrollmentToken**](EnrollmentToken.md)

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

# **endpoints_agents_enrollment_tokens_destroy**
> endpoints_agents_enrollment_tokens_destroy(token_uuid)

Mixin to add a used_by endpoint to return a list of all objects using this object

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
    api_instance = authentik_client.EndpointsApi(api_client)
    token_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Enrollment Token.

    try:
        api_instance.endpoints_agents_enrollment_tokens_destroy(token_uuid)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_enrollment_tokens_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_uuid** | **UUID**| A UUID string identifying this Enrollment Token. | 

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

# **endpoints_agents_enrollment_tokens_list**
> PaginatedEnrollmentTokenList endpoints_agents_enrollment_tokens_list(connector=connector, ordering=ordering, page=page, page_size=page_size, search=search, token_uuid=token_uuid)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_enrollment_token_list import PaginatedEnrollmentTokenList
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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    token_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)

    try:
        api_response = api_instance.endpoints_agents_enrollment_tokens_list(connector=connector, ordering=ordering, page=page, page_size=page_size, search=search, token_uuid=token_uuid)
        print("The response of EndpointsApi->endpoints_agents_enrollment_tokens_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_enrollment_tokens_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector** | **UUID**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **token_uuid** | **UUID**|  | [optional] 

### Return type

[**PaginatedEnrollmentTokenList**](PaginatedEnrollmentTokenList.md)

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

# **endpoints_agents_enrollment_tokens_partial_update**
> EnrollmentToken endpoints_agents_enrollment_tokens_partial_update(token_uuid, patched_enrollment_token_request=patched_enrollment_token_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.enrollment_token import EnrollmentToken
from authentik_client.models.patched_enrollment_token_request import PatchedEnrollmentTokenRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    token_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Enrollment Token.
    patched_enrollment_token_request = authentik_client.PatchedEnrollmentTokenRequest() # PatchedEnrollmentTokenRequest |  (optional)

    try:
        api_response = api_instance.endpoints_agents_enrollment_tokens_partial_update(token_uuid, patched_enrollment_token_request=patched_enrollment_token_request)
        print("The response of EndpointsApi->endpoints_agents_enrollment_tokens_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_enrollment_tokens_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_uuid** | **UUID**| A UUID string identifying this Enrollment Token. | 
 **patched_enrollment_token_request** | [**PatchedEnrollmentTokenRequest**](PatchedEnrollmentTokenRequest.md)|  | [optional] 

### Return type

[**EnrollmentToken**](EnrollmentToken.md)

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

# **endpoints_agents_enrollment_tokens_retrieve**
> EnrollmentToken endpoints_agents_enrollment_tokens_retrieve(token_uuid)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.enrollment_token import EnrollmentToken
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
    api_instance = authentik_client.EndpointsApi(api_client)
    token_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Enrollment Token.

    try:
        api_response = api_instance.endpoints_agents_enrollment_tokens_retrieve(token_uuid)
        print("The response of EndpointsApi->endpoints_agents_enrollment_tokens_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_enrollment_tokens_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_uuid** | **UUID**| A UUID string identifying this Enrollment Token. | 

### Return type

[**EnrollmentToken**](EnrollmentToken.md)

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

# **endpoints_agents_enrollment_tokens_update**
> EnrollmentToken endpoints_agents_enrollment_tokens_update(token_uuid, enrollment_token_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.enrollment_token import EnrollmentToken
from authentik_client.models.enrollment_token_request import EnrollmentTokenRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    token_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Enrollment Token.
    enrollment_token_request = authentik_client.EnrollmentTokenRequest() # EnrollmentTokenRequest | 

    try:
        api_response = api_instance.endpoints_agents_enrollment_tokens_update(token_uuid, enrollment_token_request)
        print("The response of EndpointsApi->endpoints_agents_enrollment_tokens_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_enrollment_tokens_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_uuid** | **UUID**| A UUID string identifying this Enrollment Token. | 
 **enrollment_token_request** | [**EnrollmentTokenRequest**](EnrollmentTokenRequest.md)|  | 

### Return type

[**EnrollmentToken**](EnrollmentToken.md)

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

# **endpoints_agents_enrollment_tokens_used_by_list**
> List[UsedBy] endpoints_agents_enrollment_tokens_used_by_list(token_uuid)

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
    api_instance = authentik_client.EndpointsApi(api_client)
    token_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Enrollment Token.

    try:
        api_response = api_instance.endpoints_agents_enrollment_tokens_used_by_list(token_uuid)
        print("The response of EndpointsApi->endpoints_agents_enrollment_tokens_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_enrollment_tokens_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_uuid** | **UUID**| A UUID string identifying this Enrollment Token. | 

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

# **endpoints_agents_enrollment_tokens_view_key_retrieve**
> TokenView endpoints_agents_enrollment_tokens_view_key_retrieve(token_uuid)

Return token key and log access

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.token_view import TokenView
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
    api_instance = authentik_client.EndpointsApi(api_client)
    token_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Enrollment Token.

    try:
        api_response = api_instance.endpoints_agents_enrollment_tokens_view_key_retrieve(token_uuid)
        print("The response of EndpointsApi->endpoints_agents_enrollment_tokens_view_key_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_enrollment_tokens_view_key_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_uuid** | **UUID**| A UUID string identifying this Enrollment Token. | 

### Return type

[**TokenView**](TokenView.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Token not found or expired |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_agents_psso_register_device_create**
> AgentPSSODeviceRegistrationResponse endpoints_agents_psso_register_device_create(agent_psso_device_registration_request)

### Example


```python
import authentik_client
from authentik_client.models.agent_psso_device_registration_request import AgentPSSODeviceRegistrationRequest
from authentik_client.models.agent_psso_device_registration_response import AgentPSSODeviceRegistrationResponse
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
    api_instance = authentik_client.EndpointsApi(api_client)
    agent_psso_device_registration_request = authentik_client.AgentPSSODeviceRegistrationRequest() # AgentPSSODeviceRegistrationRequest | 

    try:
        api_response = api_instance.endpoints_agents_psso_register_device_create(agent_psso_device_registration_request)
        print("The response of EndpointsApi->endpoints_agents_psso_register_device_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_psso_register_device_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_psso_device_registration_request** | [**AgentPSSODeviceRegistrationRequest**](AgentPSSODeviceRegistrationRequest.md)|  | 

### Return type

[**AgentPSSODeviceRegistrationResponse**](AgentPSSODeviceRegistrationResponse.md)

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

# **endpoints_agents_psso_register_user_create**
> UserSelf endpoints_agents_psso_register_user_create(agent_psso_user_registration_request)

### Example


```python
import authentik_client
from authentik_client.models.agent_psso_user_registration_request import AgentPSSOUserRegistrationRequest
from authentik_client.models.user_self import UserSelf
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
    api_instance = authentik_client.EndpointsApi(api_client)
    agent_psso_user_registration_request = authentik_client.AgentPSSOUserRegistrationRequest() # AgentPSSOUserRegistrationRequest | 

    try:
        api_response = api_instance.endpoints_agents_psso_register_user_create(agent_psso_user_registration_request)
        print("The response of EndpointsApi->endpoints_agents_psso_register_user_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_agents_psso_register_user_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_psso_user_registration_request** | [**AgentPSSOUserRegistrationRequest**](AgentPSSOUserRegistrationRequest.md)|  | 

### Return type

[**UserSelf**](UserSelf.md)

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

# **endpoints_connectors_destroy**
> endpoints_connectors_destroy(connector_uuid)

Connector Viewset

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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this connector.

    try:
        api_instance.endpoints_connectors_destroy(connector_uuid)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_connectors_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this connector. | 

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

# **endpoints_connectors_list**
> PaginatedConnectorList endpoints_connectors_list(ordering=ordering, page=page, page_size=page_size, search=search)

Connector Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_connector_list import PaginatedConnectorList
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
    api_instance = authentik_client.EndpointsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.endpoints_connectors_list(ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of EndpointsApi->endpoints_connectors_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_connectors_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedConnectorList**](PaginatedConnectorList.md)

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

# **endpoints_connectors_retrieve**
> Connector endpoints_connectors_retrieve(connector_uuid)

Connector Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.connector import Connector
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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this connector.

    try:
        api_response = api_instance.endpoints_connectors_retrieve(connector_uuid)
        print("The response of EndpointsApi->endpoints_connectors_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_connectors_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this connector. | 

### Return type

[**Connector**](Connector.md)

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

# **endpoints_connectors_types_list**
> List[TypeCreate] endpoints_connectors_types_list()

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
    api_instance = authentik_client.EndpointsApi(api_client)

    try:
        api_response = api_instance.endpoints_connectors_types_list()
        print("The response of EndpointsApi->endpoints_connectors_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_connectors_types_list: %s\n" % e)
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

# **endpoints_connectors_used_by_list**
> List[UsedBy] endpoints_connectors_used_by_list(connector_uuid)

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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this connector.

    try:
        api_response = api_instance.endpoints_connectors_used_by_list(connector_uuid)
        print("The response of EndpointsApi->endpoints_connectors_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_connectors_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this connector. | 

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

# **endpoints_device_access_groups_create**
> DeviceAccessGroup endpoints_device_access_groups_create(device_access_group_request)

DeviceAccessGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.device_access_group import DeviceAccessGroup
from authentik_client.models.device_access_group_request import DeviceAccessGroupRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    device_access_group_request = authentik_client.DeviceAccessGroupRequest() # DeviceAccessGroupRequest | 

    try:
        api_response = api_instance.endpoints_device_access_groups_create(device_access_group_request)
        print("The response of EndpointsApi->endpoints_device_access_groups_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_access_groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_access_group_request** | [**DeviceAccessGroupRequest**](DeviceAccessGroupRequest.md)|  | 

### Return type

[**DeviceAccessGroup**](DeviceAccessGroup.md)

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

# **endpoints_device_access_groups_destroy**
> endpoints_device_access_groups_destroy(pbm_uuid)

DeviceAccessGroup Viewset

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
    api_instance = authentik_client.EndpointsApi(api_client)
    pbm_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device access group.

    try:
        api_instance.endpoints_device_access_groups_destroy(pbm_uuid)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_access_groups_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **UUID**| A UUID string identifying this Device access group. | 

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

# **endpoints_device_access_groups_list**
> PaginatedDeviceAccessGroupList endpoints_device_access_groups_list(name=name, ordering=ordering, page=page, page_size=page_size, pbm_uuid=pbm_uuid, search=search)

DeviceAccessGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_device_access_group_list import PaginatedDeviceAccessGroupList
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
    api_instance = authentik_client.EndpointsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    pbm_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.endpoints_device_access_groups_list(name=name, ordering=ordering, page=page, page_size=page_size, pbm_uuid=pbm_uuid, search=search)
        print("The response of EndpointsApi->endpoints_device_access_groups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_access_groups_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **pbm_uuid** | **UUID**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedDeviceAccessGroupList**](PaginatedDeviceAccessGroupList.md)

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

# **endpoints_device_access_groups_partial_update**
> DeviceAccessGroup endpoints_device_access_groups_partial_update(pbm_uuid, patched_device_access_group_request=patched_device_access_group_request)

DeviceAccessGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.device_access_group import DeviceAccessGroup
from authentik_client.models.patched_device_access_group_request import PatchedDeviceAccessGroupRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    pbm_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device access group.
    patched_device_access_group_request = authentik_client.PatchedDeviceAccessGroupRequest() # PatchedDeviceAccessGroupRequest |  (optional)

    try:
        api_response = api_instance.endpoints_device_access_groups_partial_update(pbm_uuid, patched_device_access_group_request=patched_device_access_group_request)
        print("The response of EndpointsApi->endpoints_device_access_groups_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_access_groups_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **UUID**| A UUID string identifying this Device access group. | 
 **patched_device_access_group_request** | [**PatchedDeviceAccessGroupRequest**](PatchedDeviceAccessGroupRequest.md)|  | [optional] 

### Return type

[**DeviceAccessGroup**](DeviceAccessGroup.md)

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

# **endpoints_device_access_groups_retrieve**
> DeviceAccessGroup endpoints_device_access_groups_retrieve(pbm_uuid)

DeviceAccessGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.device_access_group import DeviceAccessGroup
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
    api_instance = authentik_client.EndpointsApi(api_client)
    pbm_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device access group.

    try:
        api_response = api_instance.endpoints_device_access_groups_retrieve(pbm_uuid)
        print("The response of EndpointsApi->endpoints_device_access_groups_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_access_groups_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **UUID**| A UUID string identifying this Device access group. | 

### Return type

[**DeviceAccessGroup**](DeviceAccessGroup.md)

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

# **endpoints_device_access_groups_update**
> DeviceAccessGroup endpoints_device_access_groups_update(pbm_uuid, device_access_group_request)

DeviceAccessGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.device_access_group import DeviceAccessGroup
from authentik_client.models.device_access_group_request import DeviceAccessGroupRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    pbm_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device access group.
    device_access_group_request = authentik_client.DeviceAccessGroupRequest() # DeviceAccessGroupRequest | 

    try:
        api_response = api_instance.endpoints_device_access_groups_update(pbm_uuid, device_access_group_request)
        print("The response of EndpointsApi->endpoints_device_access_groups_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_access_groups_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **UUID**| A UUID string identifying this Device access group. | 
 **device_access_group_request** | [**DeviceAccessGroupRequest**](DeviceAccessGroupRequest.md)|  | 

### Return type

[**DeviceAccessGroup**](DeviceAccessGroup.md)

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

# **endpoints_device_access_groups_used_by_list**
> List[UsedBy] endpoints_device_access_groups_used_by_list(pbm_uuid)

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
    api_instance = authentik_client.EndpointsApi(api_client)
    pbm_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device access group.

    try:
        api_response = api_instance.endpoints_device_access_groups_used_by_list(pbm_uuid)
        print("The response of EndpointsApi->endpoints_device_access_groups_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_access_groups_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **UUID**| A UUID string identifying this Device access group. | 

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

# **endpoints_device_bindings_create**
> DeviceUserBinding endpoints_device_bindings_create(device_user_binding_request)

PolicyBinding Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.device_user_binding import DeviceUserBinding
from authentik_client.models.device_user_binding_request import DeviceUserBindingRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    device_user_binding_request = authentik_client.DeviceUserBindingRequest() # DeviceUserBindingRequest | 

    try:
        api_response = api_instance.endpoints_device_bindings_create(device_user_binding_request)
        print("The response of EndpointsApi->endpoints_device_bindings_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_bindings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_user_binding_request** | [**DeviceUserBindingRequest**](DeviceUserBindingRequest.md)|  | 

### Return type

[**DeviceUserBinding**](DeviceUserBinding.md)

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

# **endpoints_device_bindings_destroy**
> endpoints_device_bindings_destroy(policy_binding_uuid)

PolicyBinding Viewset

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
    api_instance = authentik_client.EndpointsApi(api_client)
    policy_binding_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device User binding.

    try:
        api_instance.endpoints_device_bindings_destroy(policy_binding_uuid)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_bindings_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_binding_uuid** | **UUID**| A UUID string identifying this Device User binding. | 

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

# **endpoints_device_bindings_list**
> PaginatedDeviceUserBindingList endpoints_device_bindings_list(enabled=enabled, order=order, ordering=ordering, page=page, page_size=page_size, policy=policy, policy__isnull=policy__isnull, search=search, target=target, target_in=target_in, timeout=timeout)

PolicyBinding Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_device_user_binding_list import PaginatedDeviceUserBindingList
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
    api_instance = authentik_client.EndpointsApi(api_client)
    enabled = True # bool |  (optional)
    order = 56 # int |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    policy = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    policy__isnull = True # bool |  (optional)
    search = 'search_example' # str | A search term. (optional)
    target = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    target_in = None # List[UUID] |  (optional)
    timeout = 56 # int |  (optional)

    try:
        api_response = api_instance.endpoints_device_bindings_list(enabled=enabled, order=order, ordering=ordering, page=page, page_size=page_size, policy=policy, policy__isnull=policy__isnull, search=search, target=target, target_in=target_in, timeout=timeout)
        print("The response of EndpointsApi->endpoints_device_bindings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_bindings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **bool**|  | [optional] 
 **order** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **policy** | **UUID**|  | [optional] 
 **policy__isnull** | **bool**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **target** | **UUID**|  | [optional] 
 **target_in** | [**List[UUID]**](UUID.md)|  | [optional] 
 **timeout** | **int**|  | [optional] 

### Return type

[**PaginatedDeviceUserBindingList**](PaginatedDeviceUserBindingList.md)

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

# **endpoints_device_bindings_partial_update**
> DeviceUserBinding endpoints_device_bindings_partial_update(policy_binding_uuid, patched_device_user_binding_request=patched_device_user_binding_request)

PolicyBinding Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.device_user_binding import DeviceUserBinding
from authentik_client.models.patched_device_user_binding_request import PatchedDeviceUserBindingRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    policy_binding_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device User binding.
    patched_device_user_binding_request = authentik_client.PatchedDeviceUserBindingRequest() # PatchedDeviceUserBindingRequest |  (optional)

    try:
        api_response = api_instance.endpoints_device_bindings_partial_update(policy_binding_uuid, patched_device_user_binding_request=patched_device_user_binding_request)
        print("The response of EndpointsApi->endpoints_device_bindings_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_bindings_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_binding_uuid** | **UUID**| A UUID string identifying this Device User binding. | 
 **patched_device_user_binding_request** | [**PatchedDeviceUserBindingRequest**](PatchedDeviceUserBindingRequest.md)|  | [optional] 

### Return type

[**DeviceUserBinding**](DeviceUserBinding.md)

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

# **endpoints_device_bindings_retrieve**
> DeviceUserBinding endpoints_device_bindings_retrieve(policy_binding_uuid)

PolicyBinding Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.device_user_binding import DeviceUserBinding
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
    api_instance = authentik_client.EndpointsApi(api_client)
    policy_binding_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device User binding.

    try:
        api_response = api_instance.endpoints_device_bindings_retrieve(policy_binding_uuid)
        print("The response of EndpointsApi->endpoints_device_bindings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_bindings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_binding_uuid** | **UUID**| A UUID string identifying this Device User binding. | 

### Return type

[**DeviceUserBinding**](DeviceUserBinding.md)

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

# **endpoints_device_bindings_update**
> DeviceUserBinding endpoints_device_bindings_update(policy_binding_uuid, device_user_binding_request)

PolicyBinding Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.device_user_binding import DeviceUserBinding
from authentik_client.models.device_user_binding_request import DeviceUserBindingRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    policy_binding_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device User binding.
    device_user_binding_request = authentik_client.DeviceUserBindingRequest() # DeviceUserBindingRequest | 

    try:
        api_response = api_instance.endpoints_device_bindings_update(policy_binding_uuid, device_user_binding_request)
        print("The response of EndpointsApi->endpoints_device_bindings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_bindings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_binding_uuid** | **UUID**| A UUID string identifying this Device User binding. | 
 **device_user_binding_request** | [**DeviceUserBindingRequest**](DeviceUserBindingRequest.md)|  | 

### Return type

[**DeviceUserBinding**](DeviceUserBinding.md)

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

# **endpoints_device_bindings_used_by_list**
> List[UsedBy] endpoints_device_bindings_used_by_list(policy_binding_uuid)

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
    api_instance = authentik_client.EndpointsApi(api_client)
    policy_binding_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device User binding.

    try:
        api_response = api_instance.endpoints_device_bindings_used_by_list(policy_binding_uuid)
        print("The response of EndpointsApi->endpoints_device_bindings_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_device_bindings_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_binding_uuid** | **UUID**| A UUID string identifying this Device User binding. | 

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

# **endpoints_devices_destroy**
> endpoints_devices_destroy(device_uuid)

Mixin to add a used_by endpoint to return a list of all objects using this object

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
    api_instance = authentik_client.EndpointsApi(api_client)
    device_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device.

    try:
        api_instance.endpoints_devices_destroy(device_uuid)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_devices_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **UUID**| A UUID string identifying this Device. | 

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

# **endpoints_devices_list**
> PaginatedEndpointDeviceList endpoints_devices_list(identifier=identifier, name=name, ordering=ordering, page=page, page_size=page_size, search=search)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_endpoint_device_list import PaginatedEndpointDeviceList
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
    api_instance = authentik_client.EndpointsApi(api_client)
    identifier = 'identifier_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.endpoints_devices_list(identifier=identifier, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of EndpointsApi->endpoints_devices_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_devices_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedEndpointDeviceList**](PaginatedEndpointDeviceList.md)

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

# **endpoints_devices_partial_update**
> EndpointDevice endpoints_devices_partial_update(device_uuid, patched_endpoint_device_request=patched_endpoint_device_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.endpoint_device import EndpointDevice
from authentik_client.models.patched_endpoint_device_request import PatchedEndpointDeviceRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    device_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device.
    patched_endpoint_device_request = authentik_client.PatchedEndpointDeviceRequest() # PatchedEndpointDeviceRequest |  (optional)

    try:
        api_response = api_instance.endpoints_devices_partial_update(device_uuid, patched_endpoint_device_request=patched_endpoint_device_request)
        print("The response of EndpointsApi->endpoints_devices_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_devices_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **UUID**| A UUID string identifying this Device. | 
 **patched_endpoint_device_request** | [**PatchedEndpointDeviceRequest**](PatchedEndpointDeviceRequest.md)|  | [optional] 

### Return type

[**EndpointDevice**](EndpointDevice.md)

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

# **endpoints_devices_retrieve**
> EndpointDeviceDetails endpoints_devices_retrieve(device_uuid)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.endpoint_device_details import EndpointDeviceDetails
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
    api_instance = authentik_client.EndpointsApi(api_client)
    device_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device.

    try:
        api_response = api_instance.endpoints_devices_retrieve(device_uuid)
        print("The response of EndpointsApi->endpoints_devices_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_devices_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **UUID**| A UUID string identifying this Device. | 

### Return type

[**EndpointDeviceDetails**](EndpointDeviceDetails.md)

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

# **endpoints_devices_summary_retrieve**
> DeviceSummary endpoints_devices_summary_retrieve()

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.device_summary import DeviceSummary
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
    api_instance = authentik_client.EndpointsApi(api_client)

    try:
        api_response = api_instance.endpoints_devices_summary_retrieve()
        print("The response of EndpointsApi->endpoints_devices_summary_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_devices_summary_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DeviceSummary**](DeviceSummary.md)

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

# **endpoints_devices_update**
> EndpointDevice endpoints_devices_update(device_uuid, endpoint_device_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.endpoint_device import EndpointDevice
from authentik_client.models.endpoint_device_request import EndpointDeviceRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    device_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device.
    endpoint_device_request = authentik_client.EndpointDeviceRequest() # EndpointDeviceRequest | 

    try:
        api_response = api_instance.endpoints_devices_update(device_uuid, endpoint_device_request)
        print("The response of EndpointsApi->endpoints_devices_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_devices_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **UUID**| A UUID string identifying this Device. | 
 **endpoint_device_request** | [**EndpointDeviceRequest**](EndpointDeviceRequest.md)|  | 

### Return type

[**EndpointDevice**](EndpointDevice.md)

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

# **endpoints_devices_used_by_list**
> List[UsedBy] endpoints_devices_used_by_list(device_uuid)

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
    api_instance = authentik_client.EndpointsApi(api_client)
    device_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Device.

    try:
        api_response = api_instance.endpoints_devices_used_by_list(device_uuid)
        print("The response of EndpointsApi->endpoints_devices_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_devices_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **UUID**| A UUID string identifying this Device. | 

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

# **endpoints_fleet_connectors_create**
> FleetConnector endpoints_fleet_connectors_create(fleet_connector_request)

FleetConnector Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.fleet_connector import FleetConnector
from authentik_client.models.fleet_connector_request import FleetConnectorRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    fleet_connector_request = authentik_client.FleetConnectorRequest() # FleetConnectorRequest | 

    try:
        api_response = api_instance.endpoints_fleet_connectors_create(fleet_connector_request)
        print("The response of EndpointsApi->endpoints_fleet_connectors_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_fleet_connectors_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet_connector_request** | [**FleetConnectorRequest**](FleetConnectorRequest.md)|  | 

### Return type

[**FleetConnector**](FleetConnector.md)

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

# **endpoints_fleet_connectors_destroy**
> endpoints_fleet_connectors_destroy(connector_uuid)

FleetConnector Viewset

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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Fleet Connector.

    try:
        api_instance.endpoints_fleet_connectors_destroy(connector_uuid)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_fleet_connectors_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this Fleet Connector. | 

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

# **endpoints_fleet_connectors_list**
> PaginatedFleetConnectorList endpoints_fleet_connectors_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)

FleetConnector Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_fleet_connector_list import PaginatedFleetConnectorList
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
    api_instance = authentik_client.EndpointsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.endpoints_fleet_connectors_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of EndpointsApi->endpoints_fleet_connectors_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_fleet_connectors_list: %s\n" % e)
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

[**PaginatedFleetConnectorList**](PaginatedFleetConnectorList.md)

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

# **endpoints_fleet_connectors_partial_update**
> FleetConnector endpoints_fleet_connectors_partial_update(connector_uuid, patched_fleet_connector_request=patched_fleet_connector_request)

FleetConnector Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.fleet_connector import FleetConnector
from authentik_client.models.patched_fleet_connector_request import PatchedFleetConnectorRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Fleet Connector.
    patched_fleet_connector_request = authentik_client.PatchedFleetConnectorRequest() # PatchedFleetConnectorRequest |  (optional)

    try:
        api_response = api_instance.endpoints_fleet_connectors_partial_update(connector_uuid, patched_fleet_connector_request=patched_fleet_connector_request)
        print("The response of EndpointsApi->endpoints_fleet_connectors_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_fleet_connectors_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this Fleet Connector. | 
 **patched_fleet_connector_request** | [**PatchedFleetConnectorRequest**](PatchedFleetConnectorRequest.md)|  | [optional] 

### Return type

[**FleetConnector**](FleetConnector.md)

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

# **endpoints_fleet_connectors_retrieve**
> FleetConnector endpoints_fleet_connectors_retrieve(connector_uuid)

FleetConnector Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.fleet_connector import FleetConnector
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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Fleet Connector.

    try:
        api_response = api_instance.endpoints_fleet_connectors_retrieve(connector_uuid)
        print("The response of EndpointsApi->endpoints_fleet_connectors_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_fleet_connectors_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this Fleet Connector. | 

### Return type

[**FleetConnector**](FleetConnector.md)

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

# **endpoints_fleet_connectors_update**
> FleetConnector endpoints_fleet_connectors_update(connector_uuid, fleet_connector_request)

FleetConnector Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.fleet_connector import FleetConnector
from authentik_client.models.fleet_connector_request import FleetConnectorRequest
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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Fleet Connector.
    fleet_connector_request = authentik_client.FleetConnectorRequest() # FleetConnectorRequest | 

    try:
        api_response = api_instance.endpoints_fleet_connectors_update(connector_uuid, fleet_connector_request)
        print("The response of EndpointsApi->endpoints_fleet_connectors_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_fleet_connectors_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this Fleet Connector. | 
 **fleet_connector_request** | [**FleetConnectorRequest**](FleetConnectorRequest.md)|  | 

### Return type

[**FleetConnector**](FleetConnector.md)

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

# **endpoints_fleet_connectors_used_by_list**
> List[UsedBy] endpoints_fleet_connectors_used_by_list(connector_uuid)

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
    api_instance = authentik_client.EndpointsApi(api_client)
    connector_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Fleet Connector.

    try:
        api_response = api_instance.endpoints_fleet_connectors_used_by_list(connector_uuid)
        print("The response of EndpointsApi->endpoints_fleet_connectors_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_fleet_connectors_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **UUID**| A UUID string identifying this Fleet Connector. | 

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

