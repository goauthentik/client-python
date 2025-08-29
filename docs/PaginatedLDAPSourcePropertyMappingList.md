# PaginatedLDAPSourcePropertyMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[LDAPSourcePropertyMapping]**](LDAPSourcePropertyMapping.md) |  | 

## Example

```python
from authentik_client.models.paginated_ldap_source_property_mapping_list import PaginatedLDAPSourcePropertyMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLDAPSourcePropertyMappingList from a JSON string
paginated_ldap_source_property_mapping_list_instance = PaginatedLDAPSourcePropertyMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLDAPSourcePropertyMappingList.to_json())

# convert the object into a dict
paginated_ldap_source_property_mapping_list_dict = paginated_ldap_source_property_mapping_list_instance.to_dict()
# create an instance of PaginatedLDAPSourcePropertyMappingList from a dict
paginated_ldap_source_property_mapping_list_from_dict = PaginatedLDAPSourcePropertyMappingList.from_dict(paginated_ldap_source_property_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


