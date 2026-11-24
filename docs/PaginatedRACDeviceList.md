# PaginatedRACDeviceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[RACDevice]**](RACDevice.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_rac_device_list import PaginatedRACDeviceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRACDeviceList from a JSON string
paginated_rac_device_list_instance = PaginatedRACDeviceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRACDeviceList.to_json())

# convert the object into a dict
paginated_rac_device_list_dict = paginated_rac_device_list_instance.to_dict()
# create an instance of PaginatedRACDeviceList from a dict
paginated_rac_device_list_from_dict = PaginatedRACDeviceList.from_dict(paginated_rac_device_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


