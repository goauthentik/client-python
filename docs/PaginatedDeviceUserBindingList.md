# PaginatedDeviceUserBindingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[DeviceUserBinding]**](DeviceUserBinding.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_device_user_binding_list import PaginatedDeviceUserBindingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDeviceUserBindingList from a JSON string
paginated_device_user_binding_list_instance = PaginatedDeviceUserBindingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDeviceUserBindingList.to_json())

# convert the object into a dict
paginated_device_user_binding_list_dict = paginated_device_user_binding_list_instance.to_dict()
# create an instance of PaginatedDeviceUserBindingList from a dict
paginated_device_user_binding_list_from_dict = PaginatedDeviceUserBindingList.from_dict(paginated_device_user_binding_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


