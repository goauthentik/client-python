# PaginatedKerberosSourcePropertyMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[KerberosSourcePropertyMapping]**](KerberosSourcePropertyMapping.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_kerberos_source_property_mapping_list import PaginatedKerberosSourcePropertyMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedKerberosSourcePropertyMappingList from a JSON string
paginated_kerberos_source_property_mapping_list_instance = PaginatedKerberosSourcePropertyMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedKerberosSourcePropertyMappingList.to_json())

# convert the object into a dict
paginated_kerberos_source_property_mapping_list_dict = paginated_kerberos_source_property_mapping_list_instance.to_dict()
# create an instance of PaginatedKerberosSourcePropertyMappingList from a dict
paginated_kerberos_source_property_mapping_list_from_dict = PaginatedKerberosSourcePropertyMappingList.from_dict(paginated_kerberos_source_property_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


