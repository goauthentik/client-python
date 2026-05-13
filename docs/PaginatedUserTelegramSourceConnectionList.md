# PaginatedUserTelegramSourceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[UserTelegramSourceConnection]**](UserTelegramSourceConnection.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_user_telegram_source_connection_list import PaginatedUserTelegramSourceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserTelegramSourceConnectionList from a JSON string
paginated_user_telegram_source_connection_list_instance = PaginatedUserTelegramSourceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserTelegramSourceConnectionList.to_json())

# convert the object into a dict
paginated_user_telegram_source_connection_list_dict = paginated_user_telegram_source_connection_list_instance.to_dict()
# create an instance of PaginatedUserTelegramSourceConnectionList from a dict
paginated_user_telegram_source_connection_list_from_dict = PaginatedUserTelegramSourceConnectionList.from_dict(paginated_user_telegram_source_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


