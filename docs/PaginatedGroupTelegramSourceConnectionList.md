# PaginatedGroupTelegramSourceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[GroupTelegramSourceConnection]**](GroupTelegramSourceConnection.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_group_telegram_source_connection_list import PaginatedGroupTelegramSourceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGroupTelegramSourceConnectionList from a JSON string
paginated_group_telegram_source_connection_list_instance = PaginatedGroupTelegramSourceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGroupTelegramSourceConnectionList.to_json())

# convert the object into a dict
paginated_group_telegram_source_connection_list_dict = paginated_group_telegram_source_connection_list_instance.to_dict()
# create an instance of PaginatedGroupTelegramSourceConnectionList from a dict
paginated_group_telegram_source_connection_list_from_dict = PaginatedGroupTelegramSourceConnectionList.from_dict(paginated_group_telegram_source_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


