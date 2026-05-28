# UserLDAPSourceConnectionRequest

User source connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | 
**source** | **str** |  | 
**identifier** | **str** |  | 

## Example

```python
from authentik_client.models.user_ldap_source_connection_request import UserLDAPSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserLDAPSourceConnectionRequest from a JSON string
user_ldap_source_connection_request_instance = UserLDAPSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(UserLDAPSourceConnectionRequest.to_json())

# convert the object into a dict
user_ldap_source_connection_request_dict = user_ldap_source_connection_request_instance.to_dict()
# create an instance of UserLDAPSourceConnectionRequest from a dict
user_ldap_source_connection_request_from_dict = UserLDAPSourceConnectionRequest.from_dict(user_ldap_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


