# authentik_client.AgentsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agents_agents_create**](AgentsApi.md#agents_agents_create) | **POST** /agents/agents/ | 
[**agents_agents_destroy**](AgentsApi.md#agents_agents_destroy) | **DELETE** /agents/agents/{id}/ | 
[**agents_agents_list**](AgentsApi.md#agents_agents_list) | **GET** /agents/agents/ | 
[**agents_agents_partial_update**](AgentsApi.md#agents_agents_partial_update) | **PATCH** /agents/agents/{id}/ | 
[**agents_agents_retrieve**](AgentsApi.md#agents_agents_retrieve) | **GET** /agents/agents/{id}/ | 
[**agents_agents_update**](AgentsApi.md#agents_agents_update) | **PUT** /agents/agents/{id}/ | 


# **agents_agents_create**
> AgentCreated agents_agents_create(agent_create_request=agent_create_request)

Admin-provisioned delegate identities. An admin creates a Agent for a given
parent user, then grants it access the same way as any other User -- ordinary
PolicyBindings pointed at whatever it needs.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.agent_create_request import AgentCreateRequest
from authentik_client.models.agent_created import AgentCreated
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
    api_instance = authentik_client.AgentsApi(api_client)
    agent_create_request = authentik_client.AgentCreateRequest() # AgentCreateRequest |  (optional)

    try:
        api_response = api_instance.agents_agents_create(agent_create_request=agent_create_request)
        print("The response of AgentsApi->agents_agents_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->agents_agents_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_create_request** | [**AgentCreateRequest**](AgentCreateRequest.md)|  | [optional] 

### Return type

[**AgentCreated**](AgentCreated.md)

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

# **agents_agents_destroy**
> agents_agents_destroy(id)

Admin-provisioned delegate identities. An admin creates a Agent for a given
parent user, then grants it access the same way as any other User -- ordinary
PolicyBindings pointed at whatever it needs.

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
    api_instance = authentik_client.AgentsApi(api_client)
    id = 56 # int | A unique integer value identifying this Agent.

    try:
        api_instance.agents_agents_destroy(id)
    except Exception as e:
        print("Exception when calling AgentsApi->agents_agents_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Agent. | 

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

# **agents_agents_list**
> PaginatedAgentList agents_agents_list(ordering=ordering, page=page, page_size=page_size, parent=parent, search=search)

Admin-provisioned delegate identities. An admin creates a Agent for a given
parent user, then grants it access the same way as any other User -- ordinary
PolicyBindings pointed at whatever it needs.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_agent_list import PaginatedAgentList
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
    api_instance = authentik_client.AgentsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    parent = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.agents_agents_list(ordering=ordering, page=page, page_size=page_size, parent=parent, search=search)
        print("The response of AgentsApi->agents_agents_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->agents_agents_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **parent** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedAgentList**](PaginatedAgentList.md)

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

# **agents_agents_partial_update**
> Agent agents_agents_partial_update(id, patched_agent_request=patched_agent_request)

Admin-provisioned delegate identities. An admin creates a Agent for a given
parent user, then grants it access the same way as any other User -- ordinary
PolicyBindings pointed at whatever it needs.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.agent import Agent
from authentik_client.models.patched_agent_request import PatchedAgentRequest
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
    api_instance = authentik_client.AgentsApi(api_client)
    id = 56 # int | A unique integer value identifying this Agent.
    patched_agent_request = authentik_client.PatchedAgentRequest() # PatchedAgentRequest |  (optional)

    try:
        api_response = api_instance.agents_agents_partial_update(id, patched_agent_request=patched_agent_request)
        print("The response of AgentsApi->agents_agents_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->agents_agents_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Agent. | 
 **patched_agent_request** | [**PatchedAgentRequest**](PatchedAgentRequest.md)|  | [optional] 

### Return type

[**Agent**](Agent.md)

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

# **agents_agents_retrieve**
> Agent agents_agents_retrieve(id)

Admin-provisioned delegate identities. An admin creates a Agent for a given
parent user, then grants it access the same way as any other User -- ordinary
PolicyBindings pointed at whatever it needs.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.agent import Agent
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
    api_instance = authentik_client.AgentsApi(api_client)
    id = 56 # int | A unique integer value identifying this Agent.

    try:
        api_response = api_instance.agents_agents_retrieve(id)
        print("The response of AgentsApi->agents_agents_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->agents_agents_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Agent. | 

### Return type

[**Agent**](Agent.md)

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

# **agents_agents_update**
> Agent agents_agents_update(id, agent_request)

Admin-provisioned delegate identities. An admin creates a Agent for a given
parent user, then grants it access the same way as any other User -- ordinary
PolicyBindings pointed at whatever it needs.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.agent import Agent
from authentik_client.models.agent_request import AgentRequest
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
    api_instance = authentik_client.AgentsApi(api_client)
    id = 56 # int | A unique integer value identifying this Agent.
    agent_request = authentik_client.AgentRequest() # AgentRequest | 

    try:
        api_response = api_instance.agents_agents_update(id, agent_request)
        print("The response of AgentsApi->agents_agents_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->agents_agents_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Agent. | 
 **agent_request** | [**AgentRequest**](AgentRequest.md)|  | 

### Return type

[**Agent**](Agent.md)

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

