# PaginatedDeviceAccessGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[DeviceAccessGroup]**](DeviceAccessGroup.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_device_access_group_list import PaginatedDeviceAccessGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDeviceAccessGroupList from a JSON string
paginated_device_access_group_list_instance = PaginatedDeviceAccessGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDeviceAccessGroupList.to_json())

# convert the object into a dict
paginated_device_access_group_list_dict = paginated_device_access_group_list_instance.to_dict()
# create an instance of PaginatedDeviceAccessGroupList from a dict
paginated_device_access_group_list_from_dict = PaginatedDeviceAccessGroupList.from_dict(paginated_device_access_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


