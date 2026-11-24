# authentik_client.DebugApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**debug_log_create**](DebugApi.md#debug_log_create) | **POST** /debug/log/ | 


# **debug_log_create**
> debug_log_create(server_log_request)

Debug-only endpoint to allow frontend to log messages, usable
when browser develooper-tools aren't available.

Never available in production.

### Example

* Bearer Authentication (authentik):

```python
import authentik_client
from authentik_client.models.server_log_request import ServerLogRequest
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
    api_instance = authentik_client.DebugApi(api_client)
    server_log_request = authentik_client.ServerLogRequest() # ServerLogRequest | 

    try:
        api_instance.debug_log_create(server_log_request)
    except Exception as e:
        print("Exception when calling DebugApi->debug_log_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_log_request** | [**ServerLogRequest**](ServerLogRequest.md)|  | 

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
**201** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

