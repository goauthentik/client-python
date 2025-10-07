# authentik_client.TasksApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_schedules_list**](TasksApi.md#tasks_schedules_list) | **GET** /tasks/schedules/ | 
[**tasks_schedules_partial_update**](TasksApi.md#tasks_schedules_partial_update) | **PATCH** /tasks/schedules/{id}/ | 
[**tasks_schedules_retrieve**](TasksApi.md#tasks_schedules_retrieve) | **GET** /tasks/schedules/{id}/ | 
[**tasks_schedules_send_create**](TasksApi.md#tasks_schedules_send_create) | **POST** /tasks/schedules/{id}/send/ | 
[**tasks_schedules_update**](TasksApi.md#tasks_schedules_update) | **PUT** /tasks/schedules/{id}/ | 
[**tasks_tasks_list**](TasksApi.md#tasks_tasks_list) | **GET** /tasks/tasks/ | 
[**tasks_tasks_retrieve**](TasksApi.md#tasks_tasks_retrieve) | **GET** /tasks/tasks/{message_id}/ | 
[**tasks_tasks_retry_create**](TasksApi.md#tasks_tasks_retry_create) | **POST** /tasks/tasks/{message_id}/retry/ | 
[**tasks_tasks_status_retrieve**](TasksApi.md#tasks_tasks_status_retrieve) | **GET** /tasks/tasks/status/ | 
[**tasks_workers_list**](TasksApi.md#tasks_workers_list) | **GET** /tasks/workers | 


# **tasks_schedules_list**
> PaginatedScheduleList tasks_schedules_list(actor_name=actor_name, ordering=ordering, page=page, page_size=page_size, paused=paused, rel_obj_content_type__app_label=rel_obj_content_type__app_label, rel_obj_content_type__model=rel_obj_content_type__model, rel_obj_id=rel_obj_id, rel_obj_id__isnull=rel_obj_id__isnull, search=search)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_schedule_list import PaginatedScheduleList
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TasksApi(api_client)
    actor_name = 'actor_name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    paused = True # bool |  (optional)
    rel_obj_content_type__app_label = 'rel_obj_content_type__app_label_example' # str |  (optional)
    rel_obj_content_type__model = 'rel_obj_content_type__model_example' # str |  (optional)
    rel_obj_id = 'rel_obj_id_example' # str |  (optional)
    rel_obj_id__isnull = True # bool |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.tasks_schedules_list(actor_name=actor_name, ordering=ordering, page=page, page_size=page_size, paused=paused, rel_obj_content_type__app_label=rel_obj_content_type__app_label, rel_obj_content_type__model=rel_obj_content_type__model, rel_obj_id=rel_obj_id, rel_obj_id__isnull=rel_obj_id__isnull, search=search)
        print("The response of TasksApi->tasks_schedules_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_schedules_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **paused** | **bool**|  | [optional] 
 **rel_obj_content_type__app_label** | **str**|  | [optional] 
 **rel_obj_content_type__model** | **str**|  | [optional] 
 **rel_obj_id** | **str**|  | [optional] 
 **rel_obj_id__isnull** | **bool**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedScheduleList**](PaginatedScheduleList.md)

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

# **tasks_schedules_partial_update**
> Schedule tasks_schedules_partial_update(id, patched_schedule_request=patched_schedule_request)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.patched_schedule_request import PatchedScheduleRequest
from authentik_client.models.schedule import Schedule
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TasksApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Schedule.
    patched_schedule_request = authentik_client.PatchedScheduleRequest() # PatchedScheduleRequest |  (optional)

    try:
        api_response = api_instance.tasks_schedules_partial_update(id, patched_schedule_request=patched_schedule_request)
        print("The response of TasksApi->tasks_schedules_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_schedules_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Schedule. | 
 **patched_schedule_request** | [**PatchedScheduleRequest**](PatchedScheduleRequest.md)|  | [optional] 

### Return type

[**Schedule**](Schedule.md)

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

# **tasks_schedules_retrieve**
> Schedule tasks_schedules_retrieve(id)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.schedule import Schedule
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TasksApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Schedule.

    try:
        api_response = api_instance.tasks_schedules_retrieve(id)
        print("The response of TasksApi->tasks_schedules_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_schedules_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Schedule. | 

### Return type

[**Schedule**](Schedule.md)

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

# **tasks_schedules_send_create**
> tasks_schedules_send_create(id)

Trigger this schedule now

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
    api_instance = authentik_client.TasksApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Schedule.

    try:
        api_instance.tasks_schedules_send_create(id)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_schedules_send_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Schedule. | 

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
**204** | Schedule sent successfully |  -  |
**404** | Schedule not found |  -  |
**500** | Failed to send schedule |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_schedules_update**
> Schedule tasks_schedules_update(id, schedule_request)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.schedule import Schedule
from authentik_client.models.schedule_request import ScheduleRequest
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TasksApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Schedule.
    schedule_request = authentik_client.ScheduleRequest() # ScheduleRequest | 

    try:
        api_response = api_instance.tasks_schedules_update(id, schedule_request)
        print("The response of TasksApi->tasks_schedules_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_schedules_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Schedule. | 
 **schedule_request** | [**ScheduleRequest**](ScheduleRequest.md)|  | 

### Return type

[**Schedule**](Schedule.md)

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

# **tasks_tasks_list**
> PaginatedTaskList tasks_tasks_list(actor_name=actor_name, aggregated_status=aggregated_status, ordering=ordering, page=page, page_size=page_size, queue_name=queue_name, rel_obj_content_type__app_label=rel_obj_content_type__app_label, rel_obj_content_type__model=rel_obj_content_type__model, rel_obj_id=rel_obj_id, rel_obj_id__isnull=rel_obj_id__isnull, search=search, state=state)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_task_list import PaginatedTaskList
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TasksApi(api_client)
    actor_name = 'actor_name_example' # str |  (optional)
    aggregated_status = ['aggregated_status_example'] # List[str] |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    queue_name = 'queue_name_example' # str |  (optional)
    rel_obj_content_type__app_label = 'rel_obj_content_type__app_label_example' # str |  (optional)
    rel_obj_content_type__model = 'rel_obj_content_type__model_example' # str |  (optional)
    rel_obj_id = 'rel_obj_id_example' # str |  (optional)
    rel_obj_id__isnull = True # bool |  (optional)
    search = 'search_example' # str | A search term. (optional)
    state = 'state_example' # str | Task status   (optional)

    try:
        api_response = api_instance.tasks_tasks_list(actor_name=actor_name, aggregated_status=aggregated_status, ordering=ordering, page=page, page_size=page_size, queue_name=queue_name, rel_obj_content_type__app_label=rel_obj_content_type__app_label, rel_obj_content_type__model=rel_obj_content_type__model, rel_obj_id=rel_obj_id, rel_obj_id__isnull=rel_obj_id__isnull, search=search, state=state)
        print("The response of TasksApi->tasks_tasks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_tasks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_name** | **str**|  | [optional] 
 **aggregated_status** | [**List[str]**](str.md)|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **queue_name** | **str**|  | [optional] 
 **rel_obj_content_type__app_label** | **str**|  | [optional] 
 **rel_obj_content_type__model** | **str**|  | [optional] 
 **rel_obj_id** | **str**|  | [optional] 
 **rel_obj_id__isnull** | **bool**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **state** | **str**| Task status   | [optional] 

### Return type

[**PaginatedTaskList**](PaginatedTaskList.md)

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

# **tasks_tasks_retrieve**
> Task tasks_tasks_retrieve(message_id)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.task import Task
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TasksApi(api_client)
    message_id = 'message_id_example' # str | A UUID string identifying this Task.

    try:
        api_response = api_instance.tasks_tasks_retrieve(message_id)
        print("The response of TasksApi->tasks_tasks_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_tasks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| A UUID string identifying this Task. | 

### Return type

[**Task**](Task.md)

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

# **tasks_tasks_retry_create**
> tasks_tasks_retry_create(message_id)

Retry task

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
    api_instance = authentik_client.TasksApi(api_client)
    message_id = 'message_id_example' # str | A UUID string identifying this Task.

    try:
        api_instance.tasks_tasks_retry_create(message_id)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_tasks_retry_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| A UUID string identifying this Task. | 

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
**204** | Task retried successfully |  -  |
**400** | Task is not in a retryable state |  -  |
**404** | Task not found |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_tasks_status_retrieve**
> GlobalTaskStatus tasks_tasks_status_retrieve()

Global status summary for all tasks

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.global_task_status import GlobalTaskStatus
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TasksApi(api_client)

    try:
        api_response = api_instance.tasks_tasks_status_retrieve()
        print("The response of TasksApi->tasks_tasks_status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_tasks_status_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GlobalTaskStatus**](GlobalTaskStatus.md)

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

# **tasks_workers_list**
> List[Worker] tasks_workers_list()

Get currently connected worker count.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.worker import Worker
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.TasksApi(api_client)

    try:
        api_response = api_instance.tasks_workers_list()
        print("The response of TasksApi->tasks_workers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_workers_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Worker]**](Worker.md)

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

