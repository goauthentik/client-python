# authentik_client.ReportsApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_exports_destroy**](ReportsApi.md#reports_exports_destroy) | **DELETE** /reports/exports/{id}/ | 
[**reports_exports_list**](ReportsApi.md#reports_exports_list) | **GET** /reports/exports/ | 
[**reports_exports_retrieve**](ReportsApi.md#reports_exports_retrieve) | **GET** /reports/exports/{id}/ | 


# **reports_exports_destroy**
> reports_exports_destroy(id)

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
    api_instance = authentik_client.ReportsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Data Export.

    try:
        api_instance.reports_exports_destroy(id)
    except Exception as e:
        print("Exception when calling ReportsApi->reports_exports_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this Data Export. | 

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

# **reports_exports_list**
> PaginatedDataExportList reports_exports_list(ordering=ordering, page=page, page_size=page_size, search=search)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_data_export_list import PaginatedDataExportList
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.ReportsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.reports_exports_list(ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of ReportsApi->reports_exports_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->reports_exports_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedDataExportList**](PaginatedDataExportList.md)

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

# **reports_exports_retrieve**
> DataExport reports_exports_retrieve(id)

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.data_export import DataExport
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.ReportsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A UUID string identifying this Data Export.

    try:
        api_response = api_instance.reports_exports_retrieve(id)
        print("The response of ReportsApi->reports_exports_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->reports_exports_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| A UUID string identifying this Data Export. | 

### Return type

[**DataExport**](DataExport.md)

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

