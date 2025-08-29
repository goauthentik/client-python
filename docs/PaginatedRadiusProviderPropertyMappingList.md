# PaginatedRadiusProviderPropertyMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[RadiusProviderPropertyMapping]**](RadiusProviderPropertyMapping.md) |  | 

## Example

```python
from authentik_client.models.paginated_radius_provider_property_mapping_list import PaginatedRadiusProviderPropertyMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRadiusProviderPropertyMappingList from a JSON string
paginated_radius_provider_property_mapping_list_instance = PaginatedRadiusProviderPropertyMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRadiusProviderPropertyMappingList.to_json())

# convert the object into a dict
paginated_radius_provider_property_mapping_list_dict = paginated_radius_provider_property_mapping_list_instance.to_dict()
# create an instance of PaginatedRadiusProviderPropertyMappingList from a dict
paginated_radius_provider_property_mapping_list_from_dict = PaginatedRadiusProviderPropertyMappingList.from_dict(paginated_radius_provider_property_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


