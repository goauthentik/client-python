# PaginatedEndpointDeviceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[EndpointDevice]**](EndpointDevice.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_endpoint_device_list import PaginatedEndpointDeviceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEndpointDeviceList from a JSON string
paginated_endpoint_device_list_instance = PaginatedEndpointDeviceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEndpointDeviceList.to_json())

# convert the object into a dict
paginated_endpoint_device_list_dict = paginated_endpoint_device_list_instance.to_dict()
# create an instance of PaginatedEndpointDeviceList from a dict
paginated_endpoint_device_list_from_dict = PaginatedEndpointDeviceList.from_dict(paginated_endpoint_device_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


