# PaginatedSCIMSourcePropertyMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SCIMSourcePropertyMapping]**](SCIMSourcePropertyMapping.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_scim_source_property_mapping_list import PaginatedSCIMSourcePropertyMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSCIMSourcePropertyMappingList from a JSON string
paginated_scim_source_property_mapping_list_instance = PaginatedSCIMSourcePropertyMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSCIMSourcePropertyMappingList.to_json())

# convert the object into a dict
paginated_scim_source_property_mapping_list_dict = paginated_scim_source_property_mapping_list_instance.to_dict()
# create an instance of PaginatedSCIMSourcePropertyMappingList from a dict
paginated_scim_source_property_mapping_list_from_dict = PaginatedSCIMSourcePropertyMappingList.from_dict(paginated_scim_source_property_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


