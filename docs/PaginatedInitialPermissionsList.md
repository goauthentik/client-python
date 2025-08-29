# PaginatedInitialPermissionsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[InitialPermissions]**](InitialPermissions.md) |  | 

## Example

```python
from authentik_client.models.paginated_initial_permissions_list import PaginatedInitialPermissionsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInitialPermissionsList from a JSON string
paginated_initial_permissions_list_instance = PaginatedInitialPermissionsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedInitialPermissionsList.to_json())

# convert the object into a dict
paginated_initial_permissions_list_dict = paginated_initial_permissions_list_instance.to_dict()
# create an instance of PaginatedInitialPermissionsList from a dict
paginated_initial_permissions_list_from_dict = PaginatedInitialPermissionsList.from_dict(paginated_initial_permissions_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


