# PaginatedPermissionCheckList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[PermissionCheck]**](PermissionCheck.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_permission_check_list import PaginatedPermissionCheckList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPermissionCheckList from a JSON string
paginated_permission_check_list_instance = PaginatedPermissionCheckList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPermissionCheckList.to_json())

# convert the object into a dict
paginated_permission_check_list_dict = paginated_permission_check_list_instance.to_dict()
# create an instance of PaginatedPermissionCheckList from a dict
paginated_permission_check_list_from_dict = PaginatedPermissionCheckList.from_dict(paginated_permission_check_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


