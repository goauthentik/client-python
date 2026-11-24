# PaginatedGoogleEndpointDeviceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[GoogleEndpointDevice]**](GoogleEndpointDevice.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_google_endpoint_device_list import PaginatedGoogleEndpointDeviceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGoogleEndpointDeviceList from a JSON string
paginated_google_endpoint_device_list_instance = PaginatedGoogleEndpointDeviceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGoogleEndpointDeviceList.to_json())

# convert the object into a dict
paginated_google_endpoint_device_list_dict = paginated_google_endpoint_device_list_instance.to_dict()
# create an instance of PaginatedGoogleEndpointDeviceList from a dict
paginated_google_endpoint_device_list_from_dict = PaginatedGoogleEndpointDeviceList.from_dict(paginated_google_endpoint_device_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


