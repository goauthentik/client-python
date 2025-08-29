# PaginatedGroupLDAPSourceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[GroupLDAPSourceConnection]**](GroupLDAPSourceConnection.md) |  | 

## Example

```python
from authentik_client.models.paginated_group_ldap_source_connection_list import PaginatedGroupLDAPSourceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGroupLDAPSourceConnectionList from a JSON string
paginated_group_ldap_source_connection_list_instance = PaginatedGroupLDAPSourceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGroupLDAPSourceConnectionList.to_json())

# convert the object into a dict
paginated_group_ldap_source_connection_list_dict = paginated_group_ldap_source_connection_list_instance.to_dict()
# create an instance of PaginatedGroupLDAPSourceConnectionList from a dict
paginated_group_ldap_source_connection_list_from_dict = PaginatedGroupLDAPSourceConnectionList.from_dict(paginated_group_ldap_source_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


