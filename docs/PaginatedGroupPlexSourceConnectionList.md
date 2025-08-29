# PaginatedGroupPlexSourceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[GroupPlexSourceConnection]**](GroupPlexSourceConnection.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_group_plex_source_connection_list import PaginatedGroupPlexSourceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGroupPlexSourceConnectionList from a JSON string
paginated_group_plex_source_connection_list_instance = PaginatedGroupPlexSourceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGroupPlexSourceConnectionList.to_json())

# convert the object into a dict
paginated_group_plex_source_connection_list_dict = paginated_group_plex_source_connection_list_instance.to_dict()
# create an instance of PaginatedGroupPlexSourceConnectionList from a dict
paginated_group_plex_source_connection_list_from_dict = PaginatedGroupPlexSourceConnectionList.from_dict(paginated_group_plex_source_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


