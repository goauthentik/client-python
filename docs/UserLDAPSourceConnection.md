# UserLDAPSourceConnection

User source connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**user** | **int** |  | 
**source** | **UUID** |  | 
**source_obj** | [**Source**](Source.md) |  | [readonly] 
**identifier** | **str** |  | 
**created** | **datetime** |  | [readonly] 
**last_updated** | **datetime** |  | [readonly] 

## Example

```python
from authentik_client.models.user_ldap_source_connection import UserLDAPSourceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of UserLDAPSourceConnection from a JSON string
user_ldap_source_connection_instance = UserLDAPSourceConnection.from_json(json)
# print the JSON string representation of the object
print(UserLDAPSourceConnection.to_json())

# convert the object into a dict
user_ldap_source_connection_dict = user_ldap_source_connection_instance.to_dict()
# create an instance of UserLDAPSourceConnection from a dict
user_ldap_source_connection_from_dict = UserLDAPSourceConnection.from_dict(user_ldap_source_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


