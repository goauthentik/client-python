# authentik_client.SsfApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ssf_streams_list**](SsfApi.md#ssf_streams_list) | **GET** /ssf/streams/ | 
[**ssf_streams_retrieve**](SsfApi.md#ssf_streams_retrieve) | **GET** /ssf/streams/{uuid}/ | 


# **ssf_streams_list**
> PaginatedSSFStreamList ssf_streams_list(delivery_method=delivery_method, endpoint_url=endpoint_url, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search)

SSFStream Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.paginated_ssf_stream_list import PaginatedSSFStreamList
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.SsfApi(api_client)
    delivery_method = 'delivery_method_example' # str |  (optional)
    endpoint_url = 'endpoint_url_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.ssf_streams_list(delivery_method=delivery_method, endpoint_url=endpoint_url, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search)
        print("The response of SsfApi->ssf_streams_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsfApi->ssf_streams_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_method** | **str**|  | [optional] 
 **endpoint_url** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedSSFStreamList**](PaginatedSSFStreamList.md)

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

# **ssf_streams_retrieve**
> SSFStream ssf_streams_retrieve(uuid)

SSFStream Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.ssf_stream import SSFStream
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_client.SsfApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this SSF Stream.

    try:
        api_response = api_instance.ssf_streams_retrieve(uuid)
        print("The response of SsfApi->ssf_streams_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsfApi->ssf_streams_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this SSF Stream. | 

### Return type

[**SSFStream**](SSFStream.md)

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

