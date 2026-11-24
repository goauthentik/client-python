# PaginatedCustomPermissionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[CustomPermission]**](CustomPermission.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_custom_permission_list import PaginatedCustomPermissionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCustomPermissionList from a JSON string
paginated_custom_permission_list_instance = PaginatedCustomPermissionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCustomPermissionList.to_json())

# convert the object into a dict
paginated_custom_permission_list_dict = paginated_custom_permission_list_instance.to_dict()
# create an instance of PaginatedCustomPermissionList from a dict
paginated_custom_permission_list_from_dict = PaginatedCustomPermissionList.from_dict(paginated_custom_permission_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


