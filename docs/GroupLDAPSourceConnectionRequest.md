# GroupLDAPSourceConnectionRequest

Group Source Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **UUID** |  | 
**source** | **UUID** |  | 
**identifier** | **str** |  | 

## Example

```python
from authentik_client.models.group_ldap_source_connection_request import GroupLDAPSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupLDAPSourceConnectionRequest from a JSON string
group_ldap_source_connection_request_instance = GroupLDAPSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(GroupLDAPSourceConnectionRequest.to_json())

# convert the object into a dict
group_ldap_source_connection_request_dict = group_ldap_source_connection_request_instance.to_dict()
# create an instance of GroupLDAPSourceConnectionRequest from a dict
group_ldap_source_connection_request_from_dict = GroupLDAPSourceConnectionRequest.from_dict(group_ldap_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


