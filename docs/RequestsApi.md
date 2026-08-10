# authentik_client.RequestsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**requests_grant_requests_agent_create**](RequestsApi.md#requests_grant_requests_agent_create) | **POST** /requests/grant-requests/agent/ | 
[**requests_grant_requests_create**](RequestsApi.md#requests_grant_requests_create) | **POST** /requests/grant-requests/ | 
[**requests_grant_requests_destroy**](RequestsApi.md#requests_grant_requests_destroy) | **DELETE** /requests/grant-requests/{uuid}/ | 
[**requests_grant_requests_fulfill_partial_update**](RequestsApi.md#requests_grant_requests_fulfill_partial_update) | **PATCH** /requests/grant-requests/{uuid}/fulfill/ | 
[**requests_grant_requests_list**](RequestsApi.md#requests_grant_requests_list) | **GET** /requests/grant-requests/ | 
[**requests_grant_requests_pending_review_list**](RequestsApi.md#requests_grant_requests_pending_review_list) | **GET** /requests/grant-requests/pending_review/ | 
[**requests_grant_requests_retrieve**](RequestsApi.md#requests_grant_requests_retrieve) | **GET** /requests/grant-requests/{uuid}/ | 
[**requests_grant_requests_revoke_destroy**](RequestsApi.md#requests_grant_requests_revoke_destroy) | **DELETE** /requests/grant-requests/{uuid}/revoke/ | 
[**requests_rule_bindings_create**](RequestsApi.md#requests_rule_bindings_create) | **POST** /requests/rule-bindings/ | 
[**requests_rule_bindings_destroy**](RequestsApi.md#requests_rule_bindings_destroy) | **DELETE** /requests/rule-bindings/{uuid}/ | 
[**requests_rule_bindings_list**](RequestsApi.md#requests_rule_bindings_list) | **GET** /requests/rule-bindings/ | 
[**requests_rule_bindings_partial_update**](RequestsApi.md#requests_rule_bindings_partial_update) | **PATCH** /requests/rule-bindings/{uuid}/ | 
[**requests_rule_bindings_retrieve**](RequestsApi.md#requests_rule_bindings_retrieve) | **GET** /requests/rule-bindings/{uuid}/ | 
[**requests_rule_bindings_update**](RequestsApi.md#requests_rule_bindings_update) | **PUT** /requests/rule-bindings/{uuid}/ | 
[**requests_rule_bindings_used_by_list**](RequestsApi.md#requests_rule_bindings_used_by_list) | **GET** /requests/rule-bindings/{uuid}/used_by/ | 
[**requests_rule_child_bindings_create**](RequestsApi.md#requests_rule_child_bindings_create) | **POST** /requests/rule-child-bindings/ | 
[**requests_rule_child_bindings_destroy**](RequestsApi.md#requests_rule_child_bindings_destroy) | **DELETE** /requests/rule-child-bindings/{uuid}/ | 
[**requests_rule_child_bindings_list**](RequestsApi.md#requests_rule_child_bindings_list) | **GET** /requests/rule-child-bindings/ | 
[**requests_rule_child_bindings_partial_update**](RequestsApi.md#requests_rule_child_bindings_partial_update) | **PATCH** /requests/rule-child-bindings/{uuid}/ | 
[**requests_rule_child_bindings_retrieve**](RequestsApi.md#requests_rule_child_bindings_retrieve) | **GET** /requests/rule-child-bindings/{uuid}/ | 
[**requests_rule_child_bindings_update**](RequestsApi.md#requests_rule_child_bindings_update) | **PUT** /requests/rule-child-bindings/{uuid}/ | 
[**requests_rule_child_bindings_used_by_list**](RequestsApi.md#requests_rule_child_bindings_used_by_list) | **GET** /requests/rule-child-bindings/{uuid}/used_by/ | 
[**requests_rules_create**](RequestsApi.md#requests_rules_create) | **POST** /requests/rules/ | 
[**requests_rules_destroy**](RequestsApi.md#requests_rules_destroy) | **DELETE** /requests/rules/{uuid}/ | 
[**requests_rules_list**](RequestsApi.md#requests_rules_list) | **GET** /requests/rules/ | 
[**requests_rules_partial_update**](RequestsApi.md#requests_rules_partial_update) | **PATCH** /requests/rules/{uuid}/ | 
[**requests_rules_retrieve**](RequestsApi.md#requests_rules_retrieve) | **GET** /requests/rules/{uuid}/ | 
[**requests_rules_update**](RequestsApi.md#requests_rules_update) | **PUT** /requests/rules/{uuid}/ | 
[**requests_rules_used_by_list**](RequestsApi.md#requests_rules_used_by_list) | **GET** /requests/rules/{uuid}/used_by/ | 


# **requests_grant_requests_agent_create**
> AgentGrantRequestCreated requests_grant_requests_agent_create(agent_grant_request_create_request)

Delegate access an agent's owner already holds to the agent, time-boxed. Unlike
`create` this persists the request directly instead of returning a flow link -- an agent
authenticates with an API token and has no browser to run a flow in, so no justification
is ever collected. That is why the agent may only ask for what its owner already has:
the owner's approval is then the whole decision, and no reviewer is asked to judge a
request with nothing in it. The returned `fulfill_url` is what the agent hands to its
owner so they can act on it.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.agent_grant_request_create_request import AgentGrantRequestCreateRequest
from authentik_client.models.agent_grant_request_created import AgentGrantRequestCreated
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
    api_instance = authentik_client.RequestsApi(api_client)
    agent_grant_request_create_request = authentik_client.AgentGrantRequestCreateRequest() # AgentGrantRequestCreateRequest | 

    try:
        api_response = api_instance.requests_grant_requests_agent_create(agent_grant_request_create_request)
        print("The response of RequestsApi->requests_grant_requests_agent_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_grant_requests_agent_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_grant_request_create_request** | [**AgentGrantRequestCreateRequest**](AgentGrantRequestCreateRequest.md)|  | 

### Return type

[**AgentGrantRequestCreated**](AgentGrantRequestCreated.md)

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

# **requests_grant_requests_create**
> Link requests_grant_requests_create(grant_request_create_request)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.grant_request_create_request import GrantRequestCreateRequest
from authentik_client.models.link import Link
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
    api_instance = authentik_client.RequestsApi(api_client)
    grant_request_create_request = authentik_client.GrantRequestCreateRequest() # GrantRequestCreateRequest | 

    try:
        api_response = api_instance.requests_grant_requests_create(grant_request_create_request)
        print("The response of RequestsApi->requests_grant_requests_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_grant_requests_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_request_create_request** | [**GrantRequestCreateRequest**](GrantRequestCreateRequest.md)|  | 

### Return type

[**Link**](Link.md)

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

# **requests_grant_requests_destroy**
> requests_grant_requests_destroy(uuid)

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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Grant Request.

    try:
        api_instance.requests_grant_requests_destroy(uuid)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_grant_requests_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Grant Request. | 

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

# **requests_grant_requests_fulfill_partial_update**
> requests_grant_requests_fulfill_partial_update(uuid, patched_grant_request_fulfill_request=patched_grant_request_fulfill_request)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_grant_request_fulfill_request import PatchedGrantRequestFulfillRequest
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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Grant Request.
    patched_grant_request_fulfill_request = authentik_client.PatchedGrantRequestFulfillRequest() # PatchedGrantRequestFulfillRequest |  (optional)

    try:
        api_instance.requests_grant_requests_fulfill_partial_update(uuid, patched_grant_request_fulfill_request=patched_grant_request_fulfill_request)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_grant_requests_fulfill_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Grant Request. | 
 **patched_grant_request_fulfill_request** | [**PatchedGrantRequestFulfillRequest**](PatchedGrantRequestFulfillRequest.md)|  | [optional] 

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
**204** | Request fulfilled |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requests_grant_requests_list**
> PaginatedGrantRequestList requests_grant_requests_list(agent_owner=agent_owner, created_by=created_by, ordering=ordering, page=page, page_size=page_size, search=search, status=status)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_grant_request_list import PaginatedGrantRequestList
from authentik_client.models.request_status import RequestStatus
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
    api_instance = authentik_client.RequestsApi(api_client)
    agent_owner = 56 # int |  (optional)
    created_by = 56 # int |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    status = authentik_client.RequestStatus() # RequestStatus |  (optional)

    try:
        api_response = api_instance.requests_grant_requests_list(agent_owner=agent_owner, created_by=created_by, ordering=ordering, page=page, page_size=page_size, search=search, status=status)
        print("The response of RequestsApi->requests_grant_requests_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_grant_requests_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_owner** | **int**|  | [optional] 
 **created_by** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **status** | [**RequestStatus**](.md)|  | [optional] 

### Return type

[**PaginatedGrantRequestList**](PaginatedGrantRequestList.md)

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

# **requests_grant_requests_pending_review_list**
> PaginatedGrantRequestList requests_grant_requests_pending_review_list(agent_owner=agent_owner, created_by=created_by, ordering=ordering, page=page, page_size=page_size, search=search, status=status)

List pending grant requests the current user is eligible to review.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_grant_request_list import PaginatedGrantRequestList
from authentik_client.models.request_status import RequestStatus
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
    api_instance = authentik_client.RequestsApi(api_client)
    agent_owner = 56 # int |  (optional)
    created_by = 56 # int |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    status = authentik_client.RequestStatus() # RequestStatus |  (optional)

    try:
        api_response = api_instance.requests_grant_requests_pending_review_list(agent_owner=agent_owner, created_by=created_by, ordering=ordering, page=page, page_size=page_size, search=search, status=status)
        print("The response of RequestsApi->requests_grant_requests_pending_review_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_grant_requests_pending_review_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_owner** | **int**|  | [optional] 
 **created_by** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **status** | [**RequestStatus**](.md)|  | [optional] 

### Return type

[**PaginatedGrantRequestList**](PaginatedGrantRequestList.md)

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

# **requests_grant_requests_retrieve**
> GrantRequest requests_grant_requests_retrieve(uuid)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.grant_request import GrantRequest
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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Grant Request.

    try:
        api_response = api_instance.requests_grant_requests_retrieve(uuid)
        print("The response of RequestsApi->requests_grant_requests_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_grant_requests_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Grant Request. | 

### Return type

[**GrantRequest**](GrantRequest.md)

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

# **requests_grant_requests_revoke_destroy**
> requests_grant_requests_revoke_destroy(uuid)

Immediately end an active grant. Available to the same reviewers who could
approve it in the first place.

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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Grant Request.

    try:
        api_instance.requests_grant_requests_revoke_destroy(uuid)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_grant_requests_revoke_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Grant Request. | 

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
**204** | Grant revoked |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requests_rule_bindings_create**
> RequestRuleBinding requests_rule_bindings_create(request_rule_binding_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.request_rule_binding import RequestRuleBinding
from authentik_client.models.request_rule_binding_request import RequestRuleBindingRequest
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
    api_instance = authentik_client.RequestsApi(api_client)
    request_rule_binding_request = authentik_client.RequestRuleBindingRequest() # RequestRuleBindingRequest | 

    try:
        api_response = api_instance.requests_rule_bindings_create(request_rule_binding_request)
        print("The response of RequestsApi->requests_rule_bindings_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_bindings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_rule_binding_request** | [**RequestRuleBindingRequest**](RequestRuleBindingRequest.md)|  | 

### Return type

[**RequestRuleBinding**](RequestRuleBinding.md)

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

# **requests_rule_bindings_destroy**
> requests_rule_bindings_destroy(uuid)

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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule Binding.

    try:
        api_instance.requests_rule_bindings_destroy(uuid)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_bindings_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule Binding. | 

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

# **requests_rule_bindings_list**
> PaginatedRequestRuleBindingList requests_rule_bindings_list(ordering=ordering, page=page, page_size=page_size, rule=rule, search=search, target=target)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_request_rule_binding_list import PaginatedRequestRuleBindingList
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
    api_instance = authentik_client.RequestsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    rule = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    search = 'search_example' # str | A search term. (optional)
    target = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)

    try:
        api_response = api_instance.requests_rule_bindings_list(ordering=ordering, page=page, page_size=page_size, rule=rule, search=search, target=target)
        print("The response of RequestsApi->requests_rule_bindings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_bindings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **rule** | **UUID**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **target** | **UUID**|  | [optional] 

### Return type

[**PaginatedRequestRuleBindingList**](PaginatedRequestRuleBindingList.md)

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

# **requests_rule_bindings_partial_update**
> RequestRuleBinding requests_rule_bindings_partial_update(uuid, patched_request_rule_binding_request=patched_request_rule_binding_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_request_rule_binding_request import PatchedRequestRuleBindingRequest
from authentik_client.models.request_rule_binding import RequestRuleBinding
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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule Binding.
    patched_request_rule_binding_request = authentik_client.PatchedRequestRuleBindingRequest() # PatchedRequestRuleBindingRequest |  (optional)

    try:
        api_response = api_instance.requests_rule_bindings_partial_update(uuid, patched_request_rule_binding_request=patched_request_rule_binding_request)
        print("The response of RequestsApi->requests_rule_bindings_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_bindings_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule Binding. | 
 **patched_request_rule_binding_request** | [**PatchedRequestRuleBindingRequest**](PatchedRequestRuleBindingRequest.md)|  | [optional] 

### Return type

[**RequestRuleBinding**](RequestRuleBinding.md)

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

# **requests_rule_bindings_retrieve**
> RequestRuleBinding requests_rule_bindings_retrieve(uuid)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.request_rule_binding import RequestRuleBinding
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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule Binding.

    try:
        api_response = api_instance.requests_rule_bindings_retrieve(uuid)
        print("The response of RequestsApi->requests_rule_bindings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_bindings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule Binding. | 

### Return type

[**RequestRuleBinding**](RequestRuleBinding.md)

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

# **requests_rule_bindings_update**
> RequestRuleBinding requests_rule_bindings_update(uuid, request_rule_binding_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.request_rule_binding import RequestRuleBinding
from authentik_client.models.request_rule_binding_request import RequestRuleBindingRequest
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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule Binding.
    request_rule_binding_request = authentik_client.RequestRuleBindingRequest() # RequestRuleBindingRequest | 

    try:
        api_response = api_instance.requests_rule_bindings_update(uuid, request_rule_binding_request)
        print("The response of RequestsApi->requests_rule_bindings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_bindings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule Binding. | 
 **request_rule_binding_request** | [**RequestRuleBindingRequest**](RequestRuleBindingRequest.md)|  | 

### Return type

[**RequestRuleBinding**](RequestRuleBinding.md)

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

# **requests_rule_bindings_used_by_list**
> List[UsedBy] requests_rule_bindings_used_by_list(uuid)

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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule Binding.

    try:
        api_response = api_instance.requests_rule_bindings_used_by_list(uuid)
        print("The response of RequestsApi->requests_rule_bindings_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_bindings_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule Binding. | 

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

# **requests_rule_child_bindings_create**
> RequestRuleChildBinding requests_rule_child_bindings_create(request_rule_child_binding_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.request_rule_child_binding import RequestRuleChildBinding
from authentik_client.models.request_rule_child_binding_request import RequestRuleChildBindingRequest
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
    api_instance = authentik_client.RequestsApi(api_client)
    request_rule_child_binding_request = authentik_client.RequestRuleChildBindingRequest() # RequestRuleChildBindingRequest | 

    try:
        api_response = api_instance.requests_rule_child_bindings_create(request_rule_child_binding_request)
        print("The response of RequestsApi->requests_rule_child_bindings_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_child_bindings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_rule_child_binding_request** | [**RequestRuleChildBindingRequest**](RequestRuleChildBindingRequest.md)|  | 

### Return type

[**RequestRuleChildBinding**](RequestRuleChildBinding.md)

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

# **requests_rule_child_bindings_destroy**
> requests_rule_child_bindings_destroy(uuid)

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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule Child Binding.

    try:
        api_instance.requests_rule_child_bindings_destroy(uuid)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_child_bindings_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule Child Binding. | 

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

# **requests_rule_child_bindings_list**
> PaginatedRequestRuleChildBindingList requests_rule_child_bindings_list(binding=binding, ordering=ordering, page=page, page_size=page_size, search=search, target=target)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_request_rule_child_binding_list import PaginatedRequestRuleChildBindingList
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
    api_instance = authentik_client.RequestsApi(api_client)
    binding = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    target = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)

    try:
        api_response = api_instance.requests_rule_child_bindings_list(binding=binding, ordering=ordering, page=page, page_size=page_size, search=search, target=target)
        print("The response of RequestsApi->requests_rule_child_bindings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_child_bindings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binding** | **UUID**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **target** | **UUID**|  | [optional] 

### Return type

[**PaginatedRequestRuleChildBindingList**](PaginatedRequestRuleChildBindingList.md)

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

# **requests_rule_child_bindings_partial_update**
> RequestRuleChildBinding requests_rule_child_bindings_partial_update(uuid, patched_request_rule_child_binding_request=patched_request_rule_child_binding_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_request_rule_child_binding_request import PatchedRequestRuleChildBindingRequest
from authentik_client.models.request_rule_child_binding import RequestRuleChildBinding
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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule Child Binding.
    patched_request_rule_child_binding_request = authentik_client.PatchedRequestRuleChildBindingRequest() # PatchedRequestRuleChildBindingRequest |  (optional)

    try:
        api_response = api_instance.requests_rule_child_bindings_partial_update(uuid, patched_request_rule_child_binding_request=patched_request_rule_child_binding_request)
        print("The response of RequestsApi->requests_rule_child_bindings_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_child_bindings_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule Child Binding. | 
 **patched_request_rule_child_binding_request** | [**PatchedRequestRuleChildBindingRequest**](PatchedRequestRuleChildBindingRequest.md)|  | [optional] 

### Return type

[**RequestRuleChildBinding**](RequestRuleChildBinding.md)

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

# **requests_rule_child_bindings_retrieve**
> RequestRuleChildBinding requests_rule_child_bindings_retrieve(uuid)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.request_rule_child_binding import RequestRuleChildBinding
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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule Child Binding.

    try:
        api_response = api_instance.requests_rule_child_bindings_retrieve(uuid)
        print("The response of RequestsApi->requests_rule_child_bindings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_child_bindings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule Child Binding. | 

### Return type

[**RequestRuleChildBinding**](RequestRuleChildBinding.md)

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

# **requests_rule_child_bindings_update**
> RequestRuleChildBinding requests_rule_child_bindings_update(uuid, request_rule_child_binding_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.request_rule_child_binding import RequestRuleChildBinding
from authentik_client.models.request_rule_child_binding_request import RequestRuleChildBindingRequest
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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule Child Binding.
    request_rule_child_binding_request = authentik_client.RequestRuleChildBindingRequest() # RequestRuleChildBindingRequest | 

    try:
        api_response = api_instance.requests_rule_child_bindings_update(uuid, request_rule_child_binding_request)
        print("The response of RequestsApi->requests_rule_child_bindings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_child_bindings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule Child Binding. | 
 **request_rule_child_binding_request** | [**RequestRuleChildBindingRequest**](RequestRuleChildBindingRequest.md)|  | 

### Return type

[**RequestRuleChildBinding**](RequestRuleChildBinding.md)

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

# **requests_rule_child_bindings_used_by_list**
> List[UsedBy] requests_rule_child_bindings_used_by_list(uuid)

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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule Child Binding.

    try:
        api_response = api_instance.requests_rule_child_bindings_used_by_list(uuid)
        print("The response of RequestsApi->requests_rule_child_bindings_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rule_child_bindings_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule Child Binding. | 

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

# **requests_rules_create**
> RequestRule requests_rules_create(request_rule_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.request_rule import RequestRule
from authentik_client.models.request_rule_request import RequestRuleRequest
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
    api_instance = authentik_client.RequestsApi(api_client)
    request_rule_request = authentik_client.RequestRuleRequest() # RequestRuleRequest | 

    try:
        api_response = api_instance.requests_rules_create(request_rule_request)
        print("The response of RequestsApi->requests_rules_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rules_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_rule_request** | [**RequestRuleRequest**](RequestRuleRequest.md)|  | 

### Return type

[**RequestRule**](RequestRule.md)

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

# **requests_rules_destroy**
> requests_rules_destroy(uuid)

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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule.

    try:
        api_instance.requests_rules_destroy(uuid)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rules_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule. | 

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

# **requests_rules_list**
> PaginatedRequestRuleList requests_rules_list(name=name, ordering=ordering, page=page, page_size=page_size, pbm_uuid=pbm_uuid, request_flow__slug=request_flow__slug, search=search)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_request_rule_list import PaginatedRequestRuleList
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
    api_instance = authentik_client.RequestsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    pbm_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    request_flow__slug = 'request_flow__slug_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.requests_rules_list(name=name, ordering=ordering, page=page, page_size=page_size, pbm_uuid=pbm_uuid, request_flow__slug=request_flow__slug, search=search)
        print("The response of RequestsApi->requests_rules_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rules_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **pbm_uuid** | **UUID**|  | [optional] 
 **request_flow__slug** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedRequestRuleList**](PaginatedRequestRuleList.md)

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

# **requests_rules_partial_update**
> RequestRule requests_rules_partial_update(uuid, patched_request_rule_request=patched_request_rule_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_request_rule_request import PatchedRequestRuleRequest
from authentik_client.models.request_rule import RequestRule
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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule.
    patched_request_rule_request = authentik_client.PatchedRequestRuleRequest() # PatchedRequestRuleRequest |  (optional)

    try:
        api_response = api_instance.requests_rules_partial_update(uuid, patched_request_rule_request=patched_request_rule_request)
        print("The response of RequestsApi->requests_rules_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rules_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule. | 
 **patched_request_rule_request** | [**PatchedRequestRuleRequest**](PatchedRequestRuleRequest.md)|  | [optional] 

### Return type

[**RequestRule**](RequestRule.md)

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

# **requests_rules_retrieve**
> RequestRule requests_rules_retrieve(uuid)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.request_rule import RequestRule
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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule.

    try:
        api_response = api_instance.requests_rules_retrieve(uuid)
        print("The response of RequestsApi->requests_rules_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rules_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule. | 

### Return type

[**RequestRule**](RequestRule.md)

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

# **requests_rules_update**
> RequestRule requests_rules_update(uuid, request_rule_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.request_rule import RequestRule
from authentik_client.models.request_rule_request import RequestRuleRequest
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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule.
    request_rule_request = authentik_client.RequestRuleRequest() # RequestRuleRequest | 

    try:
        api_response = api_instance.requests_rules_update(uuid, request_rule_request)
        print("The response of RequestsApi->requests_rules_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rules_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule. | 
 **request_rule_request** | [**RequestRuleRequest**](RequestRuleRequest.md)|  | 

### Return type

[**RequestRule**](RequestRule.md)

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

# **requests_rules_used_by_list**
> List[UsedBy] requests_rules_used_by_list(uuid)

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
    api_instance = authentik_client.RequestsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Request Rule.

    try:
        api_response = api_instance.requests_rules_used_by_list(uuid)
        print("The response of RequestsApi->requests_rules_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->requests_rules_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**| A UUID string identifying this Request Rule. | 

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

