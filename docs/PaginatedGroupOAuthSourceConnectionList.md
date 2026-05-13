# PaginatedGroupOAuthSourceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[GroupOAuthSourceConnection]**](GroupOAuthSourceConnection.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_group_o_auth_source_connection_list import PaginatedGroupOAuthSourceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGroupOAuthSourceConnectionList from a JSON string
paginated_group_o_auth_source_connection_list_instance = PaginatedGroupOAuthSourceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGroupOAuthSourceConnectionList.to_json())

# convert the object into a dict
paginated_group_o_auth_source_connection_list_dict = paginated_group_o_auth_source_connection_list_instance.to_dict()
# create an instance of PaginatedGroupOAuthSourceConnectionList from a dict
paginated_group_o_auth_source_connection_list_from_dict = PaginatedGroupOAuthSourceConnectionList.from_dict(paginated_group_o_auth_source_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


