# PaginatedOAuthSourcePropertyMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[OAuthSourcePropertyMapping]**](OAuthSourcePropertyMapping.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_o_auth_source_property_mapping_list import PaginatedOAuthSourcePropertyMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOAuthSourcePropertyMappingList from a JSON string
paginated_o_auth_source_property_mapping_list_instance = PaginatedOAuthSourcePropertyMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOAuthSourcePropertyMappingList.to_json())

# convert the object into a dict
paginated_o_auth_source_property_mapping_list_dict = paginated_o_auth_source_property_mapping_list_instance.to_dict()
# create an instance of PaginatedOAuthSourcePropertyMappingList from a dict
paginated_o_auth_source_property_mapping_list_from_dict = PaginatedOAuthSourcePropertyMappingList.from_dict(paginated_o_auth_source_property_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


