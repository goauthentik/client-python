# PaginatedGroupSAMLSourceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[GroupSAMLSourceConnection]**](GroupSAMLSourceConnection.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_client.models.paginated_group_saml_source_connection_list import PaginatedGroupSAMLSourceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGroupSAMLSourceConnectionList from a JSON string
paginated_group_saml_source_connection_list_instance = PaginatedGroupSAMLSourceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGroupSAMLSourceConnectionList.to_json())

# convert the object into a dict
paginated_group_saml_source_connection_list_dict = paginated_group_saml_source_connection_list_instance.to_dict()
# create an instance of PaginatedGroupSAMLSourceConnectionList from a dict
paginated_group_saml_source_connection_list_from_dict = PaginatedGroupSAMLSourceConnectionList.from_dict(paginated_group_saml_source_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


