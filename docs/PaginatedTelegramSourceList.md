# PaginatedTelegramSourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[TelegramSource]**](TelegramSource.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_telegram_source_list import PaginatedTelegramSourceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTelegramSourceList from a JSON string
paginated_telegram_source_list_instance = PaginatedTelegramSourceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTelegramSourceList.to_json())

# convert the object into a dict
paginated_telegram_source_list_dict = paginated_telegram_source_list_instance.to_dict()
# create an instance of PaginatedTelegramSourceList from a dict
paginated_telegram_source_list_from_dict = PaginatedTelegramSourceList.from_dict(paginated_telegram_source_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


