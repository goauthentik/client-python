# PaginatedTelegramSourcePropertyMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[TelegramSourcePropertyMapping]**](TelegramSourcePropertyMapping.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_telegram_source_property_mapping_list import PaginatedTelegramSourcePropertyMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTelegramSourcePropertyMappingList from a JSON string
paginated_telegram_source_property_mapping_list_instance = PaginatedTelegramSourcePropertyMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTelegramSourcePropertyMappingList.to_json())

# convert the object into a dict
paginated_telegram_source_property_mapping_list_dict = paginated_telegram_source_property_mapping_list_instance.to_dict()
# create an instance of PaginatedTelegramSourcePropertyMappingList from a dict
paginated_telegram_source_property_mapping_list_from_dict = PaginatedTelegramSourcePropertyMappingList.from_dict(paginated_telegram_source_property_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


