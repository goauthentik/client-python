# authentik_client.LifecycleApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lifecycle_iterations_create**](LifecycleApi.md#lifecycle_iterations_create) | **POST** /lifecycle/iterations/ | 
[**lifecycle_iterations_list_latest**](LifecycleApi.md#lifecycle_iterations_list_latest) | **GET** /lifecycle/iterations/latest/{content_type}/{object_id}/ | 
[**lifecycle_iterations_list_open**](LifecycleApi.md#lifecycle_iterations_list_open) | **GET** /lifecycle/iterations/open/ | 
[**lifecycle_reviews_create**](LifecycleApi.md#lifecycle_reviews_create) | **POST** /lifecycle/reviews/ | 
[**lifecycle_rules_create**](LifecycleApi.md#lifecycle_rules_create) | **POST** /lifecycle/rules/ | 
[**lifecycle_rules_destroy**](LifecycleApi.md#lifecycle_rules_destroy) | **DELETE** /lifecycle/rules/{id}/ | 
[**lifecycle_rules_list**](LifecycleApi.md#lifecycle_rules_list) | **GET** /lifecycle/rules/ | 
[**lifecycle_rules_partial_update**](LifecycleApi.md#lifecycle_rules_partial_update) | **PATCH** /lifecycle/rules/{id}/ | 
[**lifecycle_rules_retrieve**](LifecycleApi.md#lifecycle_rules_retrieve) | **GET** /lifecycle/rules/{id}/ | 
[**lifecycle_rules_update**](LifecycleApi.md#lifecycle_rules_update) | **PUT** /lifecycle/rules/{id}/ | 
[**lifecycle_user_expiration_rules_create**](LifecycleApi.md#lifecycle_user_expiration_rules_create) | **POST** /lifecycle/user_expiration_rules/ | 
[**lifecycle_user_expiration_rules_destroy**](LifecycleApi.md#lifecycle_user_expiration_rules_destroy) | **DELETE** /lifecycle/user_expiration_rules/{id}/ | 
[**lifecycle_user_expiration_rules_list**](LifecycleApi.md#lifecycle_user_expiration_rules_list) | **GET** /lifecycle/user_expiration_rules/ | 
[**lifecycle_user_expiration_rules_partial_update**](LifecycleApi.md#lifecycle_user_expiration_rules_partial_update) | **PATCH** /lifecycle/user_expiration_rules/{id}/ | 
[**lifecycle_user_expiration_rules_preview_create**](LifecycleApi.md#lifecycle_user_expiration_rules_preview_create) | **POST** /lifecycle/user_expiration_rules/{id}/preview/ | 
[**lifecycle_user_expiration_rules_preview_retrieve**](LifecycleApi.md#lifecycle_user_expiration_rules_preview_retrieve) | **GET** /lifecycle/user_expiration_rules/{id}/preview/ | 
[**lifecycle_user_expiration_rules_retrieve**](LifecycleApi.md#lifecycle_user_expiration_rules_retrieve) | **GET** /lifecycle/user_expiration_rules/{id}/ | 
[**lifecycle_user_expiration_rules_update**](LifecycleApi.md#lifecycle_user_expiration_rules_update) | **PUT** /lifecycle/user_expiration_rules/{id}/ | 
[**lifecycle_user_expiration_rules_used_by_list**](LifecycleApi.md#lifecycle_user_expiration_rules_used_by_list) | **GET** /lifecycle/user_expiration_rules/{id}/used_by/ | 
[**lifecycle_user_offboarding_create**](LifecycleApi.md#lifecycle_user_offboarding_create) | **POST** /lifecycle/user_offboarding/ | 
[**lifecycle_user_offboarding_destroy**](LifecycleApi.md#lifecycle_user_offboarding_destroy) | **DELETE** /lifecycle/user_offboarding/{id}/ | 
[**lifecycle_user_offboarding_list**](LifecycleApi.md#lifecycle_user_offboarding_list) | **GET** /lifecycle/user_offboarding/ | 
[**lifecycle_user_offboarding_retrieve**](LifecycleApi.md#lifecycle_user_offboarding_retrieve) | **GET** /lifecycle/user_offboarding/{id}/ | 


# **lifecycle_iterations_create**
> LifecycleIteration lifecycle_iterations_create(lifecycle_iteration_request)

Mixin to validate that a valid enterprise license
exists before allowing to save the object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.lifecycle_iteration import LifecycleIteration
from authentik_client.models.lifecycle_iteration_request import LifecycleIterationRequest
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
    api_instance = authentik_client.LifecycleApi(api_client)
    lifecycle_iteration_request = authentik_client.LifecycleIterationRequest() # LifecycleIterationRequest | 

    try:
        api_response = api_instance.lifecycle_iterations_create(lifecycle_iteration_request)
        print("The response of LifecycleApi->lifecycle_iterations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_iterations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lifecycle_iteration_request** | [**LifecycleIterationRequest**](LifecycleIterationRequest.md)|  | 

### Return type

[**LifecycleIteration**](LifecycleIteration.md)

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

# **lifecycle_iterations_list_latest**
> List[LifecycleIteration] lifecycle_iterations_list_latest(content_type, object_id, ordering=ordering, search=search, user_is_reviewer=user_is_reviewer)

Mixin to validate that a valid enterprise license
exists before allowing to save the object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.lifecycle_iteration import LifecycleIteration
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
    api_instance = authentik_client.LifecycleApi(api_client)
    content_type = 'content_type_example' # str | 
    object_id = 'object_id_example' # str | 
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    search = 'search_example' # str | A search term. (optional)
    user_is_reviewer = True # bool |  (optional)

    try:
        api_response = api_instance.lifecycle_iterations_list_latest(content_type, object_id, ordering=ordering, search=search, user_is_reviewer=user_is_reviewer)
        print("The response of LifecycleApi->lifecycle_iterations_list_latest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_iterations_list_latest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | 
 **object_id** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user_is_reviewer** | **bool**|  | [optional] 

### Return type

[**List[LifecycleIteration]**](LifecycleIteration.md)

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

# **lifecycle_iterations_list_open**
> PaginatedLifecycleIterationList lifecycle_iterations_list_open(ordering=ordering, page=page, page_size=page_size, search=search, user_is_reviewer=user_is_reviewer)

Mixin to validate that a valid enterprise license
exists before allowing to save the object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_lifecycle_iteration_list import PaginatedLifecycleIterationList
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
    api_instance = authentik_client.LifecycleApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    user_is_reviewer = True # bool |  (optional)

    try:
        api_response = api_instance.lifecycle_iterations_list_open(ordering=ordering, page=page, page_size=page_size, search=search, user_is_reviewer=user_is_reviewer)
        print("The response of LifecycleApi->lifecycle_iterations_list_open:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_iterations_list_open: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user_is_reviewer** | **bool**|  | [optional] 

### Return type

[**PaginatedLifecycleIterationList**](PaginatedLifecycleIterationList.md)

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

# **lifecycle_reviews_create**
> Review lifecycle_reviews_create(review_request)

Mixin to validate that a valid enterprise license
exists before allowing to save the object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.review import Review
from authentik_client.models.review_request import ReviewRequest
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
    api_instance = authentik_client.LifecycleApi(api_client)
    review_request = authentik_client.ReviewRequest() # ReviewRequest | 

    try:
        api_response = api_instance.lifecycle_reviews_create(review_request)
        print("The response of LifecycleApi->lifecycle_reviews_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_reviews_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_request** | [**ReviewRequest**](ReviewRequest.md)|  | 

### Return type

[**Review**](Review.md)

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

# **lifecycle_rules_create**
> LifecycleRule lifecycle_rules_create(lifecycle_rule_request)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.lifecycle_rule import LifecycleRule
from authentik_client.models.lifecycle_rule_request import LifecycleRuleRequest
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
    api_instance = authentik_client.LifecycleApi(api_client)
    lifecycle_rule_request = authentik_client.LifecycleRuleRequest() # LifecycleRuleRequest | 

    try:
        api_response = api_instance.lifecycle_rules_create(lifecycle_rule_request)
        print("The response of LifecycleApi->lifecycle_rules_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_rules_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lifecycle_rule_request** | [**LifecycleRuleRequest**](LifecycleRuleRequest.md)|  | 

### Return type

[**LifecycleRule**](LifecycleRule.md)

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

# **lifecycle_rules_destroy**
> lifecycle_rules_destroy(id)

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
    api_instance = authentik_client.LifecycleApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this lifecycle rule.

    try:
        api_instance.lifecycle_rules_destroy(id)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_rules_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this lifecycle rule. | 

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

# **lifecycle_rules_list**
> PaginatedLifecycleRuleList lifecycle_rules_list(content_type__model=content_type__model, ordering=ordering, page=page, page_size=page_size, search=search)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_lifecycle_rule_list import PaginatedLifecycleRuleList
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
    api_instance = authentik_client.LifecycleApi(api_client)
    content_type__model = 'content_type__model_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.lifecycle_rules_list(content_type__model=content_type__model, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of LifecycleApi->lifecycle_rules_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_rules_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type__model** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedLifecycleRuleList**](PaginatedLifecycleRuleList.md)

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

# **lifecycle_rules_partial_update**
> LifecycleRule lifecycle_rules_partial_update(id, patched_lifecycle_rule_request=patched_lifecycle_rule_request)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.lifecycle_rule import LifecycleRule
from authentik_client.models.patched_lifecycle_rule_request import PatchedLifecycleRuleRequest
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
    api_instance = authentik_client.LifecycleApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this lifecycle rule.
    patched_lifecycle_rule_request = authentik_client.PatchedLifecycleRuleRequest() # PatchedLifecycleRuleRequest |  (optional)

    try:
        api_response = api_instance.lifecycle_rules_partial_update(id, patched_lifecycle_rule_request=patched_lifecycle_rule_request)
        print("The response of LifecycleApi->lifecycle_rules_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_rules_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this lifecycle rule. | 
 **patched_lifecycle_rule_request** | [**PatchedLifecycleRuleRequest**](PatchedLifecycleRuleRequest.md)|  | [optional] 

### Return type

[**LifecycleRule**](LifecycleRule.md)

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

# **lifecycle_rules_retrieve**
> LifecycleRule lifecycle_rules_retrieve(id)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.lifecycle_rule import LifecycleRule
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
    api_instance = authentik_client.LifecycleApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this lifecycle rule.

    try:
        api_response = api_instance.lifecycle_rules_retrieve(id)
        print("The response of LifecycleApi->lifecycle_rules_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_rules_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this lifecycle rule. | 

### Return type

[**LifecycleRule**](LifecycleRule.md)

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

# **lifecycle_rules_update**
> LifecycleRule lifecycle_rules_update(id, lifecycle_rule_request)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.lifecycle_rule import LifecycleRule
from authentik_client.models.lifecycle_rule_request import LifecycleRuleRequest
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
    api_instance = authentik_client.LifecycleApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this lifecycle rule.
    lifecycle_rule_request = authentik_client.LifecycleRuleRequest() # LifecycleRuleRequest | 

    try:
        api_response = api_instance.lifecycle_rules_update(id, lifecycle_rule_request)
        print("The response of LifecycleApi->lifecycle_rules_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_rules_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this lifecycle rule. | 
 **lifecycle_rule_request** | [**LifecycleRuleRequest**](LifecycleRuleRequest.md)|  | 

### Return type

[**LifecycleRule**](LifecycleRule.md)

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

# **lifecycle_user_expiration_rules_create**
> UserExpirationRule lifecycle_user_expiration_rules_create(user_expiration_rule_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.user_expiration_rule import UserExpirationRule
from authentik_client.models.user_expiration_rule_request import UserExpirationRuleRequest
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
    api_instance = authentik_client.LifecycleApi(api_client)
    user_expiration_rule_request = authentik_client.UserExpirationRuleRequest() # UserExpirationRuleRequest | 

    try:
        api_response = api_instance.lifecycle_user_expiration_rules_create(user_expiration_rule_request)
        print("The response of LifecycleApi->lifecycle_user_expiration_rules_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_user_expiration_rules_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_expiration_rule_request** | [**UserExpirationRuleRequest**](UserExpirationRuleRequest.md)|  | 

### Return type

[**UserExpirationRule**](UserExpirationRule.md)

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

# **lifecycle_user_expiration_rules_destroy**
> lifecycle_user_expiration_rules_destroy(id)

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
    api_instance = authentik_client.LifecycleApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this User Expiration Rule.

    try:
        api_instance.lifecycle_user_expiration_rules_destroy(id)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_user_expiration_rules_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this User Expiration Rule. | 

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

# **lifecycle_user_expiration_rules_list**
> PaginatedUserExpirationRuleList lifecycle_user_expiration_rules_list(action=action, enabled=enabled, group=group, ordering=ordering, page=page, page_size=page_size, pbm_uuid=pbm_uuid, search=search)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.offboarding_action_enum import OffboardingActionEnum
from authentik_client.models.paginated_user_expiration_rule_list import PaginatedUserExpirationRuleList
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
    api_instance = authentik_client.LifecycleApi(api_client)
    action = authentik_client.OffboardingActionEnum() # OffboardingActionEnum |  (optional)
    enabled = True # bool |  (optional)
    group = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    pbm_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.lifecycle_user_expiration_rules_list(action=action, enabled=enabled, group=group, ordering=ordering, page=page, page_size=page_size, pbm_uuid=pbm_uuid, search=search)
        print("The response of LifecycleApi->lifecycle_user_expiration_rules_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_user_expiration_rules_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | [**OffboardingActionEnum**](.md)|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **group** | **UUID**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **pbm_uuid** | **UUID**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedUserExpirationRuleList**](PaginatedUserExpirationRuleList.md)

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

# **lifecycle_user_expiration_rules_partial_update**
> UserExpirationRule lifecycle_user_expiration_rules_partial_update(id, patched_user_expiration_rule_request=patched_user_expiration_rule_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_user_expiration_rule_request import PatchedUserExpirationRuleRequest
from authentik_client.models.user_expiration_rule import UserExpirationRule
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
    api_instance = authentik_client.LifecycleApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this User Expiration Rule.
    patched_user_expiration_rule_request = authentik_client.PatchedUserExpirationRuleRequest() # PatchedUserExpirationRuleRequest |  (optional)

    try:
        api_response = api_instance.lifecycle_user_expiration_rules_partial_update(id, patched_user_expiration_rule_request=patched_user_expiration_rule_request)
        print("The response of LifecycleApi->lifecycle_user_expiration_rules_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_user_expiration_rules_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this User Expiration Rule. | 
 **patched_user_expiration_rule_request** | [**PatchedUserExpirationRuleRequest**](PatchedUserExpirationRuleRequest.md)|  | [optional] 

### Return type

[**UserExpirationRule**](UserExpirationRule.md)

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

# **lifecycle_user_expiration_rules_preview_create**
> UserExpirationRulePreview lifecycle_user_expiration_rules_preview_create(id, user_expiration_rule_request)

Preview new offboardings and changes to pending rows if this rule is enabled.

POST accepts unsaved edits to the rule. Neither method saves the rule, changes
offboardings, or sends warnings. Existing policy bindings still apply.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.user_expiration_rule_preview import UserExpirationRulePreview
from authentik_client.models.user_expiration_rule_request import UserExpirationRuleRequest
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
    api_instance = authentik_client.LifecycleApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this User Expiration Rule.
    user_expiration_rule_request = authentik_client.UserExpirationRuleRequest() # UserExpirationRuleRequest | 

    try:
        api_response = api_instance.lifecycle_user_expiration_rules_preview_create(id, user_expiration_rule_request)
        print("The response of LifecycleApi->lifecycle_user_expiration_rules_preview_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_user_expiration_rules_preview_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this User Expiration Rule. | 
 **user_expiration_rule_request** | [**UserExpirationRuleRequest**](UserExpirationRuleRequest.md)|  | 

### Return type

[**UserExpirationRulePreview**](UserExpirationRulePreview.md)

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

# **lifecycle_user_expiration_rules_preview_retrieve**
> UserExpirationRulePreview lifecycle_user_expiration_rules_preview_retrieve(id)

Preview new offboardings and changes to pending rows if this rule is enabled.

POST accepts unsaved edits to the rule. Neither method saves the rule, changes
offboardings, or sends warnings. Existing policy bindings still apply.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.user_expiration_rule_preview import UserExpirationRulePreview
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
    api_instance = authentik_client.LifecycleApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this User Expiration Rule.

    try:
        api_response = api_instance.lifecycle_user_expiration_rules_preview_retrieve(id)
        print("The response of LifecycleApi->lifecycle_user_expiration_rules_preview_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_user_expiration_rules_preview_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this User Expiration Rule. | 

### Return type

[**UserExpirationRulePreview**](UserExpirationRulePreview.md)

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

# **lifecycle_user_expiration_rules_retrieve**
> UserExpirationRule lifecycle_user_expiration_rules_retrieve(id)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.user_expiration_rule import UserExpirationRule
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
    api_instance = authentik_client.LifecycleApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this User Expiration Rule.

    try:
        api_response = api_instance.lifecycle_user_expiration_rules_retrieve(id)
        print("The response of LifecycleApi->lifecycle_user_expiration_rules_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_user_expiration_rules_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this User Expiration Rule. | 

### Return type

[**UserExpirationRule**](UserExpirationRule.md)

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

# **lifecycle_user_expiration_rules_update**
> UserExpirationRule lifecycle_user_expiration_rules_update(id, user_expiration_rule_request)

Mixin to add a used_by endpoint to return a list of all objects using this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.user_expiration_rule import UserExpirationRule
from authentik_client.models.user_expiration_rule_request import UserExpirationRuleRequest
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
    api_instance = authentik_client.LifecycleApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this User Expiration Rule.
    user_expiration_rule_request = authentik_client.UserExpirationRuleRequest() # UserExpirationRuleRequest | 

    try:
        api_response = api_instance.lifecycle_user_expiration_rules_update(id, user_expiration_rule_request)
        print("The response of LifecycleApi->lifecycle_user_expiration_rules_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_user_expiration_rules_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this User Expiration Rule. | 
 **user_expiration_rule_request** | [**UserExpirationRuleRequest**](UserExpirationRuleRequest.md)|  | 

### Return type

[**UserExpirationRule**](UserExpirationRule.md)

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

# **lifecycle_user_expiration_rules_used_by_list**
> List[UsedBy] lifecycle_user_expiration_rules_used_by_list(id)

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
    api_instance = authentik_client.LifecycleApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this User Expiration Rule.

    try:
        api_response = api_instance.lifecycle_user_expiration_rules_used_by_list(id)
        print("The response of LifecycleApi->lifecycle_user_expiration_rules_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_user_expiration_rules_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this User Expiration Rule. | 

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

# **lifecycle_user_offboarding_create**
> UserOffboarding lifecycle_user_offboarding_create(user_offboarding_request)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.user_offboarding import UserOffboarding
from authentik_client.models.user_offboarding_request import UserOffboardingRequest
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
    api_instance = authentik_client.LifecycleApi(api_client)
    user_offboarding_request = authentik_client.UserOffboardingRequest() # UserOffboardingRequest | 

    try:
        api_response = api_instance.lifecycle_user_offboarding_create(user_offboarding_request)
        print("The response of LifecycleApi->lifecycle_user_offboarding_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_user_offboarding_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_offboarding_request** | [**UserOffboardingRequest**](UserOffboardingRequest.md)|  | 

### Return type

[**UserOffboarding**](UserOffboarding.md)

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

# **lifecycle_user_offboarding_destroy**
> lifecycle_user_offboarding_destroy(id)

Cancel a pending offboarding instead of deleting the record.

The row is retained (as `CANCELED`) so the offboarding stays visible in
the audit history; deletion would erase who scheduled and cancelled it.
You cannot cancel an offboarding that targets you.

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
    api_instance = authentik_client.LifecycleApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this User Offboarding.

    try:
        api_instance.lifecycle_user_offboarding_destroy(id)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_user_offboarding_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this User Offboarding. | 

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

# **lifecycle_user_offboarding_list**
> PaginatedUserOffboardingList lifecycle_user_offboarding_list(action=action, generated=generated, ordering=ordering, page=page, page_size=page_size, rule=rule, rule__isnull=rule__isnull, search=search, status=status, user__uuid=user__uuid)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.offboarding_action_enum import OffboardingActionEnum
from authentik_client.models.offboarding_status_enum import OffboardingStatusEnum
from authentik_client.models.paginated_user_offboarding_list import PaginatedUserOffboardingList
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
    api_instance = authentik_client.LifecycleApi(api_client)
    action = authentik_client.OffboardingActionEnum() # OffboardingActionEnum |  (optional)
    generated = True # bool |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    rule = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    rule__isnull = True # bool |  (optional)
    search = 'search_example' # str | A search term. (optional)
    status = authentik_client.OffboardingStatusEnum() # OffboardingStatusEnum |  (optional)
    user__uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)

    try:
        api_response = api_instance.lifecycle_user_offboarding_list(action=action, generated=generated, ordering=ordering, page=page, page_size=page_size, rule=rule, rule__isnull=rule__isnull, search=search, status=status, user__uuid=user__uuid)
        print("The response of LifecycleApi->lifecycle_user_offboarding_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_user_offboarding_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | [**OffboardingActionEnum**](.md)|  | [optional] 
 **generated** | **bool**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **rule** | **UUID**|  | [optional] 
 **rule__isnull** | **bool**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **status** | [**OffboardingStatusEnum**](.md)|  | [optional] 
 **user__uuid** | **UUID**|  | [optional] 

### Return type

[**PaginatedUserOffboardingList**](PaginatedUserOffboardingList.md)

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

# **lifecycle_user_offboarding_retrieve**
> UserOffboarding lifecycle_user_offboarding_retrieve(id)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.user_offboarding import UserOffboarding
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
    api_instance = authentik_client.LifecycleApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this User Offboarding.

    try:
        api_response = api_instance.lifecycle_user_offboarding_retrieve(id)
        print("The response of LifecycleApi->lifecycle_user_offboarding_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleApi->lifecycle_user_offboarding_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this User Offboarding. | 

### Return type

[**UserOffboarding**](UserOffboarding.md)

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

