# PaginatedUserKerberosSourceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[UserKerberosSourceConnection]**](UserKerberosSourceConnection.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_user_kerberos_source_connection_list import PaginatedUserKerberosSourceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserKerberosSourceConnectionList from a JSON string
paginated_user_kerberos_source_connection_list_instance = PaginatedUserKerberosSourceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserKerberosSourceConnectionList.to_json())

# convert the object into a dict
paginated_user_kerberos_source_connection_list_dict = paginated_user_kerberos_source_connection_list_instance.to_dict()
# create an instance of PaginatedUserKerberosSourceConnectionList from a dict
paginated_user_kerberos_source_connection_list_from_dict = PaginatedUserKerberosSourceConnectionList.from_dict(paginated_user_kerberos_source_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


