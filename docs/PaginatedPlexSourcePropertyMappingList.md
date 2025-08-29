# PaginatedPlexSourcePropertyMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[PlexSourcePropertyMapping]**](PlexSourcePropertyMapping.md) |  | 

## Example

```python
from authentik_client.models.paginated_plex_source_property_mapping_list import PaginatedPlexSourcePropertyMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPlexSourcePropertyMappingList from a JSON string
paginated_plex_source_property_mapping_list_instance = PaginatedPlexSourcePropertyMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPlexSourcePropertyMappingList.to_json())

# convert the object into a dict
paginated_plex_source_property_mapping_list_dict = paginated_plex_source_property_mapping_list_instance.to_dict()
# create an instance of PaginatedPlexSourcePropertyMappingList from a dict
paginated_plex_source_property_mapping_list_from_dict = PaginatedPlexSourcePropertyMappingList.from_dict(paginated_plex_source_property_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


